new_cpp = """#include "AsyncSaveManager.h"
#include <stdio.h>
#include <nds/fifocommon.h>
#include <nds/fifomessages.h>

AsyncSaveManager::SaveTask AsyncSaveManager::s_queue[AsyncSaveManager::QUEUE_CAPACITY] = {};
int AsyncSaveManager::s_head = 0;
int AsyncSaveManager::s_tail = 0;
int AsyncSaveManager::s_pendingCount = 0;
bool AsyncSaveManager::s_initialized = false;
int AsyncSaveManager::s_totalTasks = 0;
int AsyncSaveManager::s_completedTasks = 0;
bool AsyncSaveManager::s_sessionActive = false;
bool AsyncSaveManager::s_sessionSuccess = false;
bool AsyncSaveManager::s_allEnqueued = false;

void AsyncSaveManager::init() {
    if (s_initialized) return;
    for (int i = 0; i < QUEUE_CAPACITY; i++) {
        s_queue[i].inUse = false;
        s_queue[i].dataSize = 0;
        s_queue[i].path[0] = '\\0';
    }
    s_head = 0;
    s_tail = 0;
    s_pendingCount = 0;
    s_totalTasks = 0;
    s_completedTasks = 0;
    s_sessionActive = false;
    s_sessionSuccess = false;
    s_allEnqueued = false;
    s_initialized = true;
}

bool AsyncSaveManager::enqueueSave(const char* path, const u8* compData, int compSize) {
    if (!s_initialized) init();
    if (!path || !compData || compSize <= 0) return false;
    if (compSize > MAX_BUFFER_SIZE) return false;

    // Si la cola está llena, procesar una tarea antes de encolar la siguiente
    if (s_pendingCount >= QUEUE_CAPACITY) {
        processQueue();
    }

    int slot = -1;
    for (int i = 0; i < QUEUE_CAPACITY; i++) {
        int idx = (s_tail + i) % QUEUE_CAPACITY;
        if (!s_queue[idx].inUse) {
            slot = idx;
            break;
        }
    }
    if (slot == -1) return false;

    SaveTask& task = s_queue[slot];
    strncpy(task.path, path, sizeof(task.path) - 1);
    task.path[sizeof(task.path) - 1] = '\\0';
    task.dataSize = compSize;
    memcpy(task.data, compData, (size_t)compSize);
    task.inUse = true;

    s_tail = (slot + 1) % QUEUE_CAPACITY;
    s_pendingCount++;

    // Notificación al coprocesador ARM7 mediante canal FIFO
    // Notifica el tamaño y registro del volcado de fondo
    fifoSendValue32(FIFO_USER_01, (u32)(0x53410000 | (compSize & 0xFFFF))); // 'SA' = Save Async

    return true;
}

void AsyncSaveManager::processQueue() {
    if (!s_initialized || s_pendingCount <= 0) {
        if (s_sessionActive && s_allEnqueued && s_pendingCount == 0) {
            s_completedTasks = s_totalTasks;
            s_sessionActive = false;
            s_sessionSuccess = true;
        }
        return;
    }

    int slot = -1;
    for (int i = 0; i < QUEUE_CAPACITY; i++) {
        int idx = (s_head + i) % QUEUE_CAPACITY;
        if (s_queue[idx].inUse) {
            slot = idx;
            break;
        }
    }
    if (slot == -1) {
        if (s_sessionActive && s_allEnqueued) {
            s_completedTasks = s_totalTasks;
            s_sessionActive = false;
            s_sessionSuccess = true;
        }
        return;
    }

    SaveTask& task = s_queue[slot];
    FILE* f = fopen(task.path, "wb");
    if (f) {
        fwrite(task.data, 1, (size_t)task.dataSize, f);
        fclose(f);
    }

    task.inUse = false;
    s_head = (slot + 1) % QUEUE_CAPACITY;
    s_pendingCount--;

    s_completedTasks++;
    if (s_sessionActive && s_allEnqueued && s_pendingCount == 0) {
        s_completedTasks = s_totalTasks;
        s_sessionActive = false;
        s_sessionSuccess = true;
    } else if (s_sessionActive && s_totalTasks > 0 && s_completedTasks >= s_totalTasks && s_pendingCount == 0) {
        s_sessionActive = false;
        s_sessionSuccess = true;
    }

    // Confirmación de escritura completada al ARM7
    fifoSendValue32(FIFO_USER_01, 0x53410000 | 0x00FF);
}

void AsyncSaveManager::flushAll() {
    if (!s_initialized) return;
    while (s_pendingCount > 0) {
        processQueue();
    }
}

int AsyncSaveManager::getPendingCount() {
    return s_pendingCount;
}

void AsyncSaveManager::startSaveSession(int totalTasks) {
    if (!s_initialized) init();
    s_totalTasks = totalTasks >= 0 ? totalTasks : 0;
    s_completedTasks = 0;
    s_sessionActive = true;
    s_sessionSuccess = false;
    s_allEnqueued = false;
}

void AsyncSaveManager::notifyAllEnqueued(int totalActual) {
    if (totalActual >= 0) {
        s_totalTasks = totalActual;
    }
    s_allEnqueued = true;
    // Si no habia tareas pendientes que escribir en SD, la sesion concluye con exito de inmediato
    if (s_sessionActive && s_pendingCount == 0) {
        s_completedTasks = s_totalTasks;
        s_sessionActive = false;
        s_sessionSuccess = true;
    }
}

int AsyncSaveManager::getTotalTasks() {
    return s_totalTasks;
}

int AsyncSaveManager::getCompletedTasks() {
    return s_completedTasks;
}

int AsyncSaveManager::getProgressPercent() {
    if (!s_sessionActive && s_sessionSuccess) return 100;
    if (s_totalTasks <= 0) {
        return (s_allEnqueued && s_pendingCount == 0) ? 100 : 0;
    }
    int p = (s_completedTasks * 100) / s_totalTasks;
    if (p > 100) p = 100;
    return p;
}

bool AsyncSaveManager::isSavingComplete() {
    if (!s_sessionActive) return true;
    if (s_allEnqueued && s_pendingCount == 0) {
        s_completedTasks = s_totalTasks;
        s_sessionActive = false;
        s_sessionSuccess = true;
        return true;
    }
    if (s_totalTasks > 0 && s_completedTasks >= s_totalTasks && s_pendingCount == 0) {
        s_sessionActive = false;
        s_sessionSuccess = true;
        return true;
    }
    return false;
}

bool AsyncSaveManager::hasSucceeded() {
    return s_sessionSuccess;
}

void AsyncSaveManager::resetSaveSession() {
    s_totalTasks = 0;
    s_completedTasks = 0;
    s_sessionActive = false;
    s_sessionSuccess = false;
    s_allEnqueued = false;
}
"""

with open("source/AsyncSaveManager.cpp", "w", encoding="utf-8", newline="\n") as f:
    f.write(new_cpp)

print("source/AsyncSaveManager.cpp rewritten successfully")

