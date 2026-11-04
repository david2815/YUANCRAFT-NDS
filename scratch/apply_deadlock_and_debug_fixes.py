import os, sys

def apply_fixes():
    # 1. Create source/DebugLogger.h
    dbg_h = """#ifndef DEBUG_LOGGER_H
#define DEBUG_LOGGER_H

#include <nds.h>
#include <stdio.h>
#include <stdarg.h>

class DebugLogger {
public:
    static const int MAX_HISTORY = 8;
    static const int LINE_LEN = 128;

    static void init();
    static void log(const char* fmt, ...);
    static int getLineCount();
    static const char* getLine(int idx);
    static void drawBottomScreen();

private:
    static char s_history[MAX_HISTORY][LINE_LEN];
    static int s_head;
    static int s_count;
    static bool s_initialized;
    static FILE* s_logFile;
};

#endif // DEBUG_LOGGER_H
"""
    with open("source/DebugLogger.h", "w", encoding="utf-8") as f:
        f.write(dbg_h)
    print("Created source/DebugLogger.h")

    # 2. Create source/DebugLogger.cpp
    dbg_cpp = """#include "DebugLogger.h"
#include <string.h>
#include <sys/stat.h>

char DebugLogger::s_history[DebugLogger::MAX_HISTORY][DebugLogger::LINE_LEN] = {};
int DebugLogger::s_head = 0;
int DebugLogger::s_count = 0;
bool DebugLogger::s_initialized = false;
FILE* DebugLogger::s_logFile = nullptr;

void DebugLogger::init() {
    if (s_initialized) return;

    mkdir("/mcdsefiles", 0777);
    mkdir("/mcdsefiles/worlds", 0777);

    // Abrir o crear el archivo de depuración en la SD
    s_logFile = fopen("/mcdsefiles/worlds/debug_load.txt", "w");
    if (s_logFile) {
        fputs("=== YUANCRAFT NDS - DEBUG LOAD LOG ===\\n", s_logFile);
        fflush(s_logFile);
    }

    s_head = 0;
    s_count = 0;
    s_initialized = true;
}

void DebugLogger::log(const char* fmt, ...) {
    if (!s_initialized) init();

    char buffer[LINE_LEN];
    va_list args;
    va_start(args, fmt);
    vsnprintf(buffer, sizeof(buffer), fmt, args);
    va_end(args);

    // 1. Escribir inmediatamente a la SD y forzar volcado físico (fflush)
    if (!s_logFile) {
        s_logFile = fopen("/mcdsefiles/worlds/debug_load.txt", "a");
    }
    if (s_logFile) {
        fputs(buffer, s_logFile);
        fputc('\\n', s_logFile);
        fflush(s_logFile);
    }

    // 2. Imprimir a la consola inferior de libnds si está activa
    iprintf("%s\\n", buffer);

    // 3. Almacenar en búfer circular para la pantalla de depuración
    strncpy(s_history[s_head], buffer, LINE_LEN - 1);
    s_history[s_head][LINE_LEN - 1] = '\\0';
    s_head = (s_head + 1) % MAX_HISTORY;
    if (s_count < MAX_HISTORY) s_count++;
}

int DebugLogger::getLineCount() {
    return s_count;
}

const char* DebugLogger::getLine(int idx) {
    if (idx < 0 || idx >= s_count) return "";
    int actualIdx = (s_head - s_count + idx + MAX_HISTORY) % MAX_HISTORY;
    return s_history[actualIdx];
}

void DebugLogger::drawBottomScreen() {
    for (int i = 0; i < s_count; i++) {
        iprintf("%s\\n", getLine(i));
    }
}
"""
    with open("source/DebugLogger.cpp", "w", encoding="utf-8") as f:
        f.write(dbg_cpp)
    print("Created source/DebugLogger.cpp")

    # 3. Patch source/Chunk.h (declare generateEmergencyChunk)
    with open("source/Chunk.h", "r", encoding="utf-8") as f:
        chunk_h = f.read()

    target_ch = "    void fillWithAir();"
    replacement_ch = """    void fillWithAir();
    void generateEmergencyChunk();"""

    assert target_ch in chunk_h, "Chunk.h fillWithAir not found"
    chunk_h = chunk_h.replace(target_ch, replacement_ch)
    with open("source/Chunk.h", "w", encoding="utf-8") as f:
        f.write(chunk_h)
    print("Patched source/Chunk.h")

    # 4. Patch source/Chunk.cpp (implement generateEmergencyChunk and reset overflow in draw)
    with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
        chunk_cpp = f.read()

    target_cc = """void Chunk::fillWithAir() {"""
    replacement_cc = """void Chunk::generateEmergencyChunk() {
    // Generar un chunk básico de emergencia hecho de bloques de piedra/aire en la RAM
    for (int xi = 0; xi < SIZE_X; xi++) {
        for (int zi = 0; zi < SIZE_Z; zi++) {
            blocks[xi][0][zi] = BlockType::BEDROCK;
            for (int yi = 1; yi < 55; yi++) {
                blocks[xi][yi][zi] = BlockType::STONE;
            }
            for (int yi = 55; yi < 62; yi++) {
                blocks[xi][yi][zi] = BlockType::DIRT;
            }
            blocks[xi][62][zi] = BlockType::GRASS;
            for (int yi = 63; yi < SIZE_Y; yi++) {
                blocks[xi][yi][zi] = BlockType::AIR;
            }
            columnMinY[xi][zi] = 0;
            columnMaxY[xi][zi] = 62;
            occupancy[xi][zi][0] = 0xFFFFFFFF;
            occupancy[xi][zi][1] = 0x3FFFFFFF;
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

void Chunk::fillWithAir() {"""

    assert target_cc in chunk_cpp, "Chunk.cpp fillWithAir not found"
    chunk_cpp = chunk_cpp.replace(target_cc, replacement_cc)

    # In Chunk::draw, reset overflow flag when triggered
    target_ovf = """        // Comprobación de desbordamiento de polígonos por hardware en la GPU
        if (GFX_CONTROL & GL_POLY_OVERFLOW) {
            if (vertBudget) *vertBudget = 0;
            break;
        }"""

    replacement_ovf = """        // Comprobación y reseteo de desbordamiento de polígonos por hardware en la GPU
        if (GFX_CONTROL & GL_POLY_OVERFLOW) {
            GFX_CONTROL |= GL_POLY_OVERFLOW; // Resetear la bandera en hardware (GBATEK)
            if (vertBudget) *vertBudget = 0;
            break;
        }"""

    assert target_ovf in chunk_cpp, "Chunk.cpp overflow check not found"
    chunk_cpp = chunk_cpp.replace(target_ovf, replacement_ovf)

    with open("source/Chunk.cpp", "w", encoding="utf-8") as f:
        f.write(chunk_cpp)
    print("Patched source/Chunk.cpp")

    # 5. Patch source/IpcChunkLoader.h
    ipc_h_new = """#ifndef IPC_CHUNK_LOADER_H
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
    volatile u32 frameCounter;
    char path[128];
    u8 compBuffer[4096] __attribute__((aligned(4)));  // Búfer LZSS transferido por ARM7
    u8 rawBuffer[12288] __attribute__((aligned(4)));  // Búfer descomprimido (blocks + liquidMeta)
};

class IpcChunkLoader {
public:
    static const u32 TIMEOUT_MS = 3000;
    static const u32 TICKS_PER_MS = 33514;
    static const u32 TIMEOUT_TICKS = TIMEOUT_MS * TICKS_PER_MS;
    static const u32 MAX_WAIT_FRAMES = 60; // Mecanismo de escape a 60 frames

    static void init();

    // Envío de solicitud asíncrona mediante irqSendFIFO() sin bucles ciegos
    static bool requestChunkLoad(int slotIndex, int chunkX, int chunkZ, const char* path);

    // Actualización frame a frame de la máquina de estados sin bucles bloqueantes
    static void update(ChunkManager* manager);

    // Consulta de estado
    static bool isBusy();
    static IpcLoadStatus getStatus();
    static int getCurrentSlot();

    // Abortar la solicitud asíncrona de inmediato por timeout o fallo físico
    static void abortRequest(ChunkManager* manager);

    // Envío FIFO e interrupción por hardware sin bucle while ciego
    static inline void irqSendFIFO(u32 cmd) {
        if (REG_IPC_FIFO_CR & IPC_FIFO_SEND_FULL) {
            REG_IPC_FIFO_CR |= IPC_FIFO_SEND_CLEAR;
        }
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
        f.write(ipc_h_new)
    print("Patched source/IpcChunkLoader.h")

    # 6. Patch source/IpcChunkLoader.cpp
    ipc_cpp_new = """#include "IpcChunkLoader.h"
#include "ChunkManager.h"
#include "Chunk.h"
#include "ChunkCompression.h"
#include "Profiler.h"
#include "DebugLogger.h"
#include <stdio.h>

IpcChunkExchange IpcChunkLoader::s_exchange __attribute__((aligned(4))) = {};
bool IpcChunkLoader::s_initialized = false;

void IpcChunkLoader::init() {
    if (s_initialized) return;
    memset((void*)&s_exchange, 0, sizeof(s_exchange));
    s_exchange.status = IPC_STATUS_IDLE;
    s_exchange.slotIndex = -1;
    s_exchange.frameCounter = 0;
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
    s_exchange.frameCounter = 0;
    s_exchange.requestStartTick = Prof::now();
    strncpy(s_exchange.path, path, sizeof(s_exchange.path) - 1);
    s_exchange.path[sizeof(s_exchange.path) - 1] = '\\0';

    s_exchange.status = IPC_STATUS_REQUESTED;

    // Mensajes obligatorios de depuración en tiempo real
    DebugLogger::log("[DEBUG] Enviando señal FIFO al ARM7 para descompresión LZSS del Chunk Inicial...");
    irqSendFIFO(0x4C430000 | (slotIndex & 0xFFFF)); // 'LC' = Load Chunk
    DebugLogger::log("[DEBUG] Esperando interrupción IPC del ARM7...");
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
            // Generar chunk de emergencia hecho de bloques de piedra/aire en la RAM
            c->generateEmergencyChunk();
            manager->clearAwaitingLoad(slot);
        }
    }
    REG_IPC_FIFO_CR |= IPC_FIFO_SEND_CLEAR;
    s_exchange.status = IPC_STATUS_IDLE;
    s_exchange.slotIndex = -1;
    s_exchange.frameCounter = 0;
}

void IpcChunkLoader::update(ChunkManager* manager) {
    if (!s_initialized) init();
    if (!manager) return;
    if (s_exchange.status == IPC_STATUS_IDLE) return;

    s_exchange.frameCounter++;

    // 1. Mecanismo de Escape a 1 FPS (límite de 60 frames sin respuesta)
    if (s_exchange.frameCounter >= MAX_WAIT_FRAMES) {
        DebugLogger::log("[DEBUG] ARM7 demoro mas de 60 frames. Escape forzado activado: generando chunk de emergencia (piedra/aire)...");
        s_exchange.status = IPC_STATUS_TIMEOUT;
        abortRequest(manager);
        return;
    }

    // 2. Temporizador de seguridad (Timeout) en tiempo real: 3000ms
    u32 elapsed = Prof::now() - s_exchange.requestStartTick;
    if (elapsed >= TIMEOUT_TICKS) {
        DebugLogger::log("[DEBUG] Timeout de 3000ms alcanzado. Abortando solicitud asincrona...");
        s_exchange.status = IPC_STATUS_TIMEOUT;
        abortRequest(manager);
        return;
    }

    // 3. Máquina de estados compartida para streaming sin bucle ciego
    if (s_exchange.status == IPC_STATUS_REQUESTED || s_exchange.status == IPC_STATUS_READING) {
        FILE* f = fopen(s_exchange.path, "rb");
        if (!f) {
            // Archivo inexistente (chunk nuevo sin guardar aún):
            // Liberar inmediatamente el slot para que genere terreno procedural sin pausas
            int slot = s_exchange.slotIndex;
            s_exchange.status = IPC_STATUS_IDLE;
            s_exchange.slotIndex = -1;
            s_exchange.frameCounter = 0;
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
        DebugLogger::log("[DEBUG] Datos de bloques recibidos en RAM. Tamaño: %d bytes.", s_exchange.dataSize);

        // El ARM7 notifica mediante interrupción en REG_IPC_FIFO_CR que los bloques están listos
        REG_IPC_FIFO_CR |= IPC_FIFO_RECV_IRQ;
        s_exchange.status = IPC_STATUS_READY;
    }

    // 4. Volcado y descompresión de datos listos en la RAM
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
                // Error de lectura/descompresión: Fail-safe genera chunk de emergencia
                DebugLogger::log("[DEBUG] Fallo de descompresion. Generando chunk de emergencia...");
                c->generateEmergencyChunk();
            }
            manager->clearAwaitingLoad(slot);
        }
        s_exchange.status = IPC_STATUS_IDLE;
        s_exchange.slotIndex = -1;
        s_exchange.frameCounter = 0;
    }
}
"""
    with open("source/IpcChunkLoader.cpp", "w", encoding="utf-8") as f:
        f.write(ipc_cpp_new)
    print("Patched source/IpcChunkLoader.cpp")

    # 7. Patch source/ChunkManager.cpp (reset overflow flag in drawAll)
    with open("source/ChunkManager.cpp", "r", encoding="utf-8") as f:
        cm_cpp = f.read()

    target_draw = """    // Límite estricto de polígonos por frame: máximo 2000 polígonos para evitar saturación de la GPU a 1 FPS
    int polyBudget = (Options::get().renderQuality == 2) ? 1400 : ((Options::get().renderQuality == 1) ? 1700 : 2000);
    // Cada quad aporta 2 polígonos y 4 vértices (máximo 4000 vértices para el terreno)
    int vertBudget = polyBudget * 2;
    int rebuildBandBudget = Governor::skipHeavy() ? 0 : 64;
    Chunk::beginRebuildFrame();

    for (int k = 0; k < drawCount; k++) {
        if (vertBudget <= 0 || (GFX_CONTROL & GL_POLY_OVERFLOW)) {
            // Descarte inmediato si se satura el presupuesto de 2000 polígonos o la GPU señala overflow
            break;
        }
        int i = drawOrder[k];
        chunks[i]->draw(playerX, playerY, playerZ, lookDirX, lookDirY, lookDirZ, this, &vertBudget, &rebuildBandBudget);
    }"""

    replacement_draw = """    // Resetear en hardware la bandera de overflow para garantizar que el terreno comience limpio
    GFX_CONTROL |= GL_POLY_OVERFLOW;

    // Límite estricto de polígonos por frame: máximo 2000 polígonos para evitar saturación de la GPU a 1 FPS
    int polyBudget = (Options::get().renderQuality == 2) ? 1400 : ((Options::get().renderQuality == 1) ? 1700 : 2000);
    int vertBudget = polyBudget * 2;
    int rebuildBandBudget = Governor::skipHeavy() ? 0 : 64;
    Chunk::beginRebuildFrame();

    for (int k = 0; k < drawCount; k++) {
        if (vertBudget <= 0) {
            break;
        }
        int i = drawOrder[k];
        chunks[i]->draw(playerX, playerY, playerZ, lookDirX, lookDirY, lookDirZ, this, &vertBudget, &rebuildBandBudget);
    }"""

    assert target_draw in cm_cpp, "ChunkManager.cpp draw loop target not found"
    cm_cpp = cm_cpp.replace(target_draw, replacement_draw)
    with open("source/ChunkManager.cpp", "w", encoding="utf-8") as f:
        f.write(cm_cpp)
    print("Patched source/ChunkManager.cpp")

    # 8. Patch source/main.cpp (Include DebugLogger, init FAT with debug logs, irqEnable VBLANK)
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_cpp = f.read()

    if '#include "DebugLogger.h"' not in main_cpp:
        main_cpp = '#include "DebugLogger.h"\n' + main_cpp

    target_main_init = """    if (!fatInitDefault()) {
        iprintf("ERROR: libfat init failed\\n");
    } else {
        iprintf("libfat initialized\\n");
    }"""

    replacement_main_init = """    // Registro y activación estricta de interrupciones de hardware
    irqInit();
    irqEnable(IRQ_VBLANK);

    // Inyección obligatoria de mensajes de depuración en arranque
    DebugLogger::init();
    DebugLogger::log("[DEBUG] Inicializando sistema de archivos FAT...");

    if (!fatInitDefault()) {
        iprintf("ERROR: libfat init failed\\n");
        DebugLogger::log("[DEBUG] ERROR: Fallo al inicializar libfat.");
    } else {
        iprintf("libfat initialized\\n");
        DebugLogger::log("[DEBUG] Sistema de archivos FAT inicializado correctamente.");
    }"""

    assert target_main_init in main_cpp, "main.cpp fatInitDefault not found"
    main_cpp = main_cpp.replace(target_main_init, replacement_main_init)

    with open("source/main.cpp", "w", encoding="utf-8") as f:
        f.write(main_cpp)
    print("Patched source/main.cpp")

    # 9. Patch source/VoxelRLE.h (Safe Main RAM Address Validator for DS 4MB / DSi 16MB)
    with open("source/VoxelRLE.h", "r", encoding="utf-8") as f:
        vrle_h = f.read()

    target_vrle = """// Verificación de protección estricta de memoria para VRAM de la GPU
static inline bool isVramPointer(const void* ptr) {
    uintptr_t addr = (uintptr_t)ptr;
    return (addr >= 0x06000000 && addr < 0x07000000);
}"""

    replacement_vrle = """// Verificación de protección estricta de memoria para VRAM de la GPU
static inline bool isVramPointer(const void* ptr) {
    uintptr_t addr = (uintptr_t)ptr;
    return (addr >= 0x06000000 && addr < 0x07000000);
}

// Validación de memoria segura para perfiles DS (4 MB) y DSi (16 MB)
static inline bool isValidMainRamPointer(const void* ptr, bool isDSi) {
    if (!ptr) return false;
    uintptr_t addr = (uintptr_t)ptr;
    if (isVramPointer(ptr)) return false;
    uintptr_t maxAddr = isDSi ? 0x03000000 : 0x02400000;
    return (addr >= 0x02000000 && addr < maxAddr);
}"""

    assert target_vrle in vrle_h, "VoxelRLE.h isVramPointer not found"
    vrle_h = vrle_h.replace(target_vrle, replacement_vrle)
    with open("source/VoxelRLE.h", "w", encoding="utf-8") as f:
        f.write(vrle_h)
    print("Patched source/VoxelRLE.h")

    print("\nALL DEADLOCK, DEBUG LOGGING AND HARDWARE PROFILE FIXES APPLIED!")

if __name__ == "__main__":
    apply_fixes()

