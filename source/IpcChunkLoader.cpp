#include "IpcChunkLoader.h"
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
    s_exchange.path[sizeof(s_exchange.path) - 1] = '\0';

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
