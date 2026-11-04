#ifndef ASYNC_SAVE_MANAGER_H
#define ASYNC_SAVE_MANAGER_H

#include <nds.h>
#include <stdio.h>
#include <string.h>

// ============================================================================
// AsyncSaveManager: Sistema de Guardado Asíncrono Continuo (ARM7/SD)
// ============================================================================
// - Serializa bloques en búfer binario continuo para no bloquear el bucle
//   principal ARM9.
// - Notifica y coordina con el coprocesador ARM7 mediante FIFO_USER_01.
// - Procesa la escritura física a la SD en segundo plano sin pausas de frame.
// ============================================================================

class AsyncSaveManager {
public:
    static const int QUEUE_CAPACITY = 8;
    static const int MAX_BUFFER_SIZE = 4096; // Búfer continuo para datos comprimidos LZSS

    // Estructura estrictamente alineada a 32 bits para DMA y coprocesador
    struct __attribute__((aligned(4))) SaveTask {
        char path[96];
        int dataSize;
        u8 data[MAX_BUFFER_SIZE] __attribute__((aligned(4)));
        volatile bool inUse;
        u8 _pad[3];
    };

    static void init();
    static bool enqueueSave(const char* path, const u8* compData, int compSize);
    static void processQueue();
    static void flushAll();
    static int getPendingCount();

    // Estado del volcado seguro para la UI
    static void startSaveSession(int totalTasks);
    static void notifyAllEnqueued(int totalActual = -1);
    static int getTotalTasks();
    static int getCompletedTasks();
    static int getProgressPercent(); // 0..100
    static bool isSavingComplete();
    static bool hasSucceeded();
    static void resetSaveSession();

private:
    static SaveTask s_queue[QUEUE_CAPACITY] __attribute__((aligned(4)));
    static int s_head;
    static int s_tail;
    static int s_pendingCount;
    static bool s_initialized;

    static int s_totalTasks;
    static int s_completedTasks;
    static bool s_sessionActive;
    static bool s_sessionSuccess;
    static bool s_allEnqueued;
};

#endif // ASYNC_SAVE_MANAGER_H

