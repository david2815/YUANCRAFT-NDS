#include "DebugLogger.h"
#include <string.h>
#include <sys/stat.h>

char DebugLogger::s_history[DebugLogger::MAX_HISTORY][DebugLogger::LINE_LEN] = {};
int DebugLogger::s_head = 0;
int DebugLogger::s_count = 0;
bool DebugLogger::s_initialized = false;
bool DebugLogger::s_fatAvailable = false;
FILE* DebugLogger::s_logFile = nullptr;

void DebugLogger::init(bool fatAvailable) {
    s_fatAvailable = fatAvailable;
    s_initialized = true;

    // Solo interactuar con la tarjeta SD si libfat confirmó inicialización exitosa
    if (s_fatAvailable) {
        mkdir("/mcdsefiles", 0777);
        mkdir("/mcdsefiles/worlds", 0777);

        if (!s_logFile) {
            s_logFile = fopen("/mcdsefiles/worlds/debug_load.txt", "w");
            if (s_logFile) {
                fputs("=== YUANCRAFT NDS - DEBUG LOAD LOG ===\n", s_logFile);
                fflush(s_logFile);
            }
        }
    } else {
        if (s_logFile) {
            fclose(s_logFile);
            s_logFile = nullptr;
        }
    }
}

bool DebugLogger::isFatAvailable() {
    return s_fatAvailable;
}

void DebugLogger::log(const char* fmt, ...) {
    if (!s_initialized) {
        init(false);
    }

    char buffer[LINE_LEN];
    va_list args;
    va_start(args, fmt);
    vsnprintf(buffer, sizeof(buffer), fmt, args);
    va_end(args);

    // 1. Escribir a la SD ÚNICAMENTE si libfat está disponible y confirmado
    if (s_fatAvailable) {
        FILE* f = fopen("/mcdsefiles/worlds/debug_load.txt", "a");
        if (f) {
            fputs(buffer, f);
            fputc('\n', f);
            fclose(f);
        }
    }

    // 2. Almacenar en búfer circular para la pantalla de depuración interna
    snprintf(s_history[s_head], sizeof(s_history[s_head]), "%s", buffer);
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
        iprintf("%s\n", getLine(i));
    }
}
