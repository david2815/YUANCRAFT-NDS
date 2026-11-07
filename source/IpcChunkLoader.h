#ifndef IPC_CHUNK_LOADER_H
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

// Estructura en memoria segura de intercambio (IPC Sync), alineada a línea de caché ARM9 (32 bytes)
struct __attribute__((aligned(32))) IpcChunkExchange {
    volatile u32 status;
    volatile int chunkX;
    volatile int chunkZ;
    volatile int slotIndex;
    volatile u32 requestStartTick;
    volatile u32 dataSize;
    volatile u32 frameCounter;
    char path[128];
    u8 compBuffer[12288] __attribute__((aligned(32)));  // Búfer LZSS transferido por ARM7
    u8 rawBuffer[12288] __attribute__((aligned(32)));  // Búfer descomprimido (blocks + liquidMeta)
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

    // Notificación segura sin corromper los registros de control IPC_FIFO_CR
    static inline void irqSendFIFO(u32 cmd) {
        (void)cmd;
    }

private:
    static IpcChunkExchange s_exchange;
    static bool s_initialized;
};

#endif // IPC_CHUNK_LOADER_H
