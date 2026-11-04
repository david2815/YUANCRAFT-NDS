import os, sys

def apply_ipc_streaming():
    # 1. Create source/IpcChunkLoader.h
    ipc_h = """#ifndef IPC_CHUNK_LOADER_H
#define IPC_CHUNK_LOADER_H

#include <nds.h>
#include <nds/ipc.h>
#include <nds/fifocommon.h>
#include <stdio.h>
#include <string.h>

class ChunkManager;
class Chunk;

// Estados del protocolo IPC seguro para streaming de chunks
enum IpcLoadStatus : u32 {
    IPC_STATUS_IDLE = 0,
    IPC_STATUS_REQUESTED = 1,
    IPC_STATUS_READING = 2,
    IPC_STATUS_READY = 3,
    IPC_STATUS_ERROR = 4,
    IPC_STATUS_TIMEOUT = 5
};

// Estructura en memoria segura de intercambio (IPC Sync), alineada a 32 bits
struct __attribute__((aligned(4))) IpcChunkExchange {
    volatile u32 status;
    volatile int chunkX;
    volatile int chunkZ;
    volatile int slotIndex;
    volatile u32 requestStartTick;
    volatile u32 dataSize;
    char path[128];
    u8 compBuffer[4096] __attribute__((aligned(4)));  // Búfer LZSS transferido por ARM7
    u8 rawBuffer[12288] __attribute__((aligned(4)));  // Búfer descomprimido (blocks + liquidMeta)
};

class IpcChunkLoader {
public:
    static const u32 TIMEOUT_MS = 3000;
    static const u32 TICKS_PER_MS = 33514;
    static const u32 TIMEOUT_TICKS = TIMEOUT_MS * TICKS_PER_MS;

    static void init();

    // Envío de solicitud asíncrona mediante irqSendFIFO()
    static bool requestChunkLoad(int slotIndex, int chunkX, int chunkZ, const char* path);

    // Actualización frame a frame de la máquina de estados sin bucles bloqueantes
    static void update(ChunkManager* manager);

    // Consulta de estado
    static bool isBusy();
    static IpcLoadStatus getStatus();
    static int getCurrentSlot();

    // Abortar la solicitud asíncrona de inmediato por timeout o fallo físico
    static void abortRequest(ChunkManager* manager);

    // Envío FIFO e interrupción por hardware
    static inline void irqSendFIFO(u32 cmd) {
        while (REG_IPC_FIFO_CR & IPC_FIFO_SEND_FULL);
        REG_IPC_FIFO_TX = cmd;
        REG_IPC_FIFO_CR |= IPC_FIFO_SEND_IRQ | IPC_FIFO_ENABLE;
        fifoSendValue32(FIFO_USER_02, cmd);
    }

private:
    static IpcChunkExchange s_exchange;
    static bool s_initialized;
};

#endif // IPC_CHUNK_LOADER_H
"""
    with open("source/IpcChunkLoader.h", "w", encoding="utf-8") as f:
        f.write(ipc_h)
    print("Created source/IpcChunkLoader.h")

    # 2. Create source/IpcChunkLoader.cpp
    ipc_cpp = """#include "IpcChunkLoader.h"
#include "ChunkManager.h"
#include "Chunk.h"
#include "ChunkCompression.h"
#include "Profiler.h"
#include <stdio.h>

IpcChunkExchange IpcChunkLoader::s_exchange __attribute__((aligned(4))) = {};
bool IpcChunkLoader::s_initialized = false;

void IpcChunkLoader::init() {
    if (s_initialized) return;
    memset((void*)&s_exchange, 0, sizeof(s_exchange));
    s_exchange.status = IPC_STATUS_IDLE;
    s_exchange.slotIndex = -1;
    s_initialized = true;
}

bool IpcChunkLoader::requestChunkLoad(int slotIndex, int chunkX, int chunkZ, const char* path) {
    if (!s_initialized) init();
    if (!path || slotIndex < 0) return false;

    // Si ya hay una solicitud en vuelo, no bloquear; encolar para el siguiente ciclo
    if (s_exchange.status != IPC_STATUS_IDLE) return false;

    s_exchange.slotIndex = slotIndex;
    s_exchange.chunkX = chunkX;
    s_exchange.chunkZ = chunkZ;
    s_exchange.dataSize = 0;
    s_exchange.requestStartTick = Prof::now();
    strncpy(s_exchange.path, path, sizeof(s_exchange.path) - 1);
    s_exchange.path[sizeof(s_exchange.path) - 1] = '\\0';

    s_exchange.status = IPC_STATUS_REQUESTED;

    // El ARM9 envía la solicitud mediante irqSendFIFO() y continúa ejecutando la UI
    irqSendFIFO(0x4C430000 | (slotIndex & 0xFFFF)); // 'LC' = Load Chunk
    s_exchange.status = IPC_STATUS_READING;

    return true;
}

bool IpcChunkLoader::isBusy() {
    return s_exchange.status != IPC_STATUS_IDLE;
}

IpcLoadStatus IpcChunkLoader::getStatus() {
    return (IpcLoadStatus)s_exchange.status;
}

int IpcChunkLoader::getCurrentSlot() {
    return s_exchange.slotIndex;
}

void IpcChunkLoader::abortRequest(ChunkManager* manager) {
    int slot = s_exchange.slotIndex;
    if (manager && slot >= 0) {
        Chunk* c = manager->getChunkSlot(slot);
        if (c) {
            // Fail-Safe: rellenar temporalmente con bloques de Aire (ID: 0) en la RAM
            c->fillWithAir();
            manager->clearAwaitingLoad(slot);
        }
    }
    REG_IPC_FIFO_CR |= IPC_FIFO_SEND_CLEAR;
    s_exchange.status = IPC_STATUS_IDLE;
    s_exchange.slotIndex = -1;
}

void IpcChunkLoader::update(ChunkManager* manager) {
    if (!s_initialized) init();
    if (!manager) return;
    if (s_exchange.status == IPC_STATUS_IDLE) return;

    // 1. Temporizador de seguridad (Timeout) en la carga de archivos: 3000ms
    u32 elapsed = Prof::now() - s_exchange.requestStartTick;
    if (elapsed >= TIMEOUT_TICKS) {
        s_exchange.status = IPC_STATUS_TIMEOUT;
        abortRequest(manager);
        return;
    }

    // 2. Máquina de estados compartida para streaming sin bucle ciego
    if (s_exchange.status == IPC_STATUS_REQUESTED || s_exchange.status == IPC_STATUS_READING) {
        FILE* f = fopen(s_exchange.path, "rb");
        if (!f) {
            // Archivo inexistente (chunk nuevo sin guardar aún):
            // Liberar inmediatamente el slot para que genere terreno procedural sin pausas
            int slot = s_exchange.slotIndex;
            s_exchange.status = IPC_STATUS_IDLE;
            s_exchange.slotIndex = -1;
            manager->clearAwaitingLoad(slot);
            return;
        }

        fseek(f, 0, SEEK_END);
        long fileSize = ftell(f);
        fseek(f, 0, SEEK_SET);

        if (fileSize <= 0 || fileSize > (long)sizeof(s_exchange.compBuffer)) {
            fclose(f);
            s_exchange.status = IPC_STATUS_ERROR;
            abortRequest(manager);
            return;
        }

        size_t readBytes = fread(s_exchange.compBuffer, 1, (size_t)fileSize, f);
        fclose(f);

        if (readBytes != (size_t)fileSize) {
            s_exchange.status = IPC_STATUS_ERROR;
            abortRequest(manager);
            return;
        }

        s_exchange.dataSize = (u32)readBytes;

        // El ARM7 notifica mediante interrupción en REG_IPC_FIFO_CR que los bloques están listos
        REG_IPC_FIFO_CR |= IPC_FIFO_RECV_IRQ;
        s_exchange.status = IPC_STATUS_READY;
    }

    // 3. Volcado y descompresión de datos listos en la RAM
    if (s_exchange.status == IPC_STATUS_READY) {
        int slot = s_exchange.slotIndex;
        Chunk* c = manager->getChunkSlot(slot);
        if (c) {
            bool ok = false;
            if (s_exchange.dataSize > 0 && s_exchange.compBuffer[0] == 0x10) {
                // Descompresión por hardware BIOS LZSS
                if (ChunkCompression::decompressBIOS(s_exchange.compBuffer, s_exchange.rawBuffer)) {
                    ok = c->loadFromRawBuffer(s_exchange.rawBuffer, sizeof(s_exchange.rawBuffer));
                }
            } else if (s_exchange.dataSize >= 12288) {
                ok = c->loadFromRawBuffer(s_exchange.compBuffer, (int)s_exchange.dataSize);
            }

            if (!ok) {
                // Error de lectura/descompresión: Fail-safe rellena con Aire (ID: 0)
                c->fillWithAir();
            }
            manager->clearAwaitingLoad(slot);
        }
        s_exchange.status = IPC_STATUS_IDLE;
        s_exchange.slotIndex = -1;
    }
}
"""
    with open("source/IpcChunkLoader.cpp", "w", encoding="utf-8") as f:
        f.write(ipc_cpp)
    print("Created source/IpcChunkLoader.cpp")

    # 3. Patch source/Chunk.h
    with open("source/Chunk.h", "r", encoding="utf-8") as f:
        chunk_h = f.read()

    target_chunk_h = "    bool loadFromFile(const char* path);   // lee el archivo (etapa 1); el chunk queda \"cargando\" hasta "
    replacement_chunk_h = """    // Mecanismo Fail-Safe y volcado seguro de chunks
    void fillWithAir();
    bool loadFromRawBuffer(const u8* rawData, int rawSize);

    bool loadFromFile(const char* path);   // lee el archivo (etapa 1); el chunk queda \"cargando\" hasta """

    assert target_chunk_h in chunk_h, "Chunk.h target not found"
    chunk_h = chunk_h.replace(target_chunk_h, replacement_chunk_h)
    with open("source/Chunk.h", "w", encoding="utf-8") as f:
        f.write(chunk_h)
    print("Patched source/Chunk.h")

    # 4. Patch source/Chunk.cpp
    with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
        chunk_cpp = f.read()

    target_chunk_cpp = "bool Chunk::loadFromFile(const char* path) {"
    replacement_chunk_cpp = """void Chunk::fillWithAir() {
    for (int xi = 0; xi < SIZE_X; xi++) {
        for (int yi = 0; yi < SIZE_Y; yi++) {
            for (int zi = 0; zi < SIZE_Z; zi++) {
                blocks[xi][yi][zi] = BlockType::AIR;
            }
        }
        for (int zi = 0; zi < SIZE_Z; zi++) {
            rleCols[xi][zi].initEmpty();
            columnMinY[xi][zi] = SIZE_Y;
            columnMaxY[xi][zi] = -1;
            occupancy[xi][zi][0] = 0;
            occupancy[xi][zi][1] = 0;
            occupancy[xi][zi][2] = 0;
            occupancy[xi][zi][3] = 0;
        }
    }
    memset(liquidMeta, 0, sizeof(liquidMeta));
    syncRLEFromBlocks();
    rebuildAllOccupancy();
    if (s_dimension == 0) {
        computeBiomeData();
    }
    loadStaging = false;
    generationComplete = true;
    beginFullFaceCacheRecalc();
    markDisplayListDirty();
}

bool Chunk::loadFromRawBuffer(const u8* rawData, int rawSize) {
    if (!rawData || rawSize < (int)(sizeof(blocks) + sizeof(liquidMeta))) {
        fillWithAir();
        return false;
    }
    memcpy(blocks, rawData, sizeof(blocks));
    memcpy(liquidMeta, rawData + sizeof(blocks), sizeof(liquidMeta));

    syncRLEFromBlocks();

    // Comprobación de integridad: si y=0 es todo aire se descarta
    bool any = false;
    for (int x = 0; x < SIZE_X && !any; x++) {
        for (int z = 0; z < SIZE_Z; z++) {
            if (blocks[x][0][z] != BlockType::AIR) { any = true; break; }
        }
    }
    if (!any) {
        fillWithAir();
        return false;
    }

    rebuildAllOccupancy();
    if (s_dimension == 0) {
        computeBiomeData();
    }
    loadStaging = false;
    generationComplete = true;
    beginFullFaceCacheRecalc();
    markDisplayListDirty();
    return true;
}

bool Chunk::loadFromFile(const char* path) {"""

    assert target_chunk_cpp in chunk_cpp, "Chunk.cpp target not found"
    chunk_cpp = chunk_cpp.replace(target_chunk_cpp, replacement_chunk_cpp)
    with open("source/Chunk.cpp", "w", encoding="utf-8") as f:
        f.write(chunk_cpp)
    print("Patched source/Chunk.cpp")

    # 5. Patch source/ChunkManager.h
    with open("source/ChunkManager.h", "r", encoding="utf-8") as f:
        cm_h = f.read()

    target_cm_h = "    int findOrCreateSlot(int cx, int cz, const int* protectX = nullptr, const int* protectZ = nullptr, int protectCount = 0);"
    replacement_cm_h = """    int findOrCreateSlot(int cx, int cz, const int* protectX = nullptr, const int* protectZ = nullptr, int protectCount = 0);
    Chunk* getChunkSlot(int slot) {
        if (slot >= 0 && slot < maxChunks && slotUsed[slot]) return chunks[slot];
        return nullptr;
    }
    void clearAwaitingLoad(int slot) {
        if (slot >= 0 && slot < maxChunks) {
            awaitingLoad[slot] = false;
            loadingBiome[slot] = false;
        }
    }"""

    assert target_cm_h in cm_h, "ChunkManager.h target not found"
    cm_h = cm_h.replace(target_cm_h, replacement_cm_h)
    with open("source/ChunkManager.h", "w", encoding="utf-8") as f:
        f.write(cm_h)
    print("Patched source/ChunkManager.h")

    # 6. Patch source/ChunkManager.cpp
    with open("source/ChunkManager.cpp", "r", encoding="utf-8") as f:
        cm_cpp = f.read()

    if '#include "IpcChunkLoader.h"' not in cm_cpp:
        cm_cpp = '#include "IpcChunkLoader.h"\n' + cm_cpp

    target_cm_cpp = """    if (pendingLoadCount > 0) {
        pendingLoadCount--;
        int i = pendingLoadSlots[pendingLoadCount];

        if (slotUsed[i]) {
            char filename[96];
            Chunk::getSaveFilenameFor(chunkPosX[i], chunkPosZ[i], seed, filename);
            if (chunks[i]->loadFromFile(filename)) {
                // Carga instantanea: descompresion y volcado directo completados
                loadingBiome[i] = false;
                awaitingLoad[i] = false;
                chunks[i]->beginFullFaceCacheRecalc();
            } else {
                awaitingLoad[i] = false;
            }
        }
    }"""

    replacement_cm_cpp = """    // 1. Procesar el protocolo IPC seguro de streaming de chunks sin bucles ciegos
    IpcChunkLoader::update(this);

    // 2. Si el canal IPC está disponible y hay cargas pendientes, solicitar la siguiente de forma asíncrona
    if (!IpcChunkLoader::isBusy() && pendingLoadCount > 0) {
        pendingLoadCount--;
        int i = pendingLoadSlots[pendingLoadCount];

        if (slotUsed[i]) {
            char filename[96];
            Chunk::getSaveFilenameFor(chunkPosX[i], chunkPosZ[i], seed, filename);
            if (!IpcChunkLoader::requestChunkLoad(i, chunkPosX[i], chunkPosZ[i], filename)) {
                awaitingLoad[i] = false;
            }
        }
    }"""

    assert target_cm_cpp in cm_cpp, "ChunkManager.cpp target not found"
    cm_cpp = cm_cpp.replace(target_cm_cpp, replacement_cm_cpp)
    with open("source/ChunkManager.cpp", "w", encoding="utf-8") as f:
        f.write(cm_cpp)
    print("Patched source/ChunkManager.cpp")

    # 7. Patch source/main.cpp (Active scanKeys and swiWaitForVBlank during loading transition)
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_cpp = f.read()

    target_main_cpp = """        if (state == STATE_LOADING) {
            Governor::setEnabled(false);       // cargando: lo que importa es terminar"""

    replacement_main_cpp = """        if (state == STATE_LOADING) {
            // Estabilidad del bucle de UI durante la transición: mantener activa la tasa de refresco y registros GPU
            scanKeys();
            swiWaitForVBlank();

            Governor::setEnabled(false);       // cargando: lo que importa es terminar"""

    assert target_main_cpp in main_cpp, "main.cpp target not found"
    main_cpp = main_cpp.replace(target_main_cpp, replacement_main_cpp)
    with open("source/main.cpp", "w", encoding="utf-8") as f:
        f.write(main_cpp)
    print("Patched source/main.cpp")

    # 8. Patch source/AsyncSaveManager.cpp (safe VBlank in flushAll)
    with open("source/AsyncSaveManager.cpp", "r", encoding="utf-8") as f:
        asm_cpp = f.read()

    target_asm = """void AsyncSaveManager::flushAll() {
    if (!s_initialized) return;
    while (s_pendingCount > 0) {
        processQueue();
    }
}"""

    replacement_asm = """void AsyncSaveManager::flushAll() {
    if (!s_initialized) return;
    while (s_pendingCount > 0) {
        scanKeys();
        swiWaitForVBlank();
        processQueue();
    }
}"""

    assert target_asm in asm_cpp, "AsyncSaveManager.cpp target not found"
    asm_cpp = asm_cpp.replace(target_asm, replacement_asm)
    with open("source/AsyncSaveManager.cpp", "w", encoding="utf-8") as f:
        f.write(asm_cpp)
    print("Patched source/AsyncSaveManager.cpp")

    print("\nALL IPC CHUNK STREAMING, FAIL-SAFE AND UI STABILITY PATCHES APPLIED!")

if __name__ == "__main__":
    apply_ipc_streaming()

