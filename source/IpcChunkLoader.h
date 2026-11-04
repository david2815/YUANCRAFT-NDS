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
