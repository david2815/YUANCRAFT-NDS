#include "DsiDebug.h"
#include <stdio.h>
#include <stdarg.h>
#include <string.h>

volatile uint32_t g_CurrentExecStep = 0;

static FILE* openLogFile(const char* mode) {
    FILE* f = fopen("sd:/mc_dsi_debug.log", mode);
    if (!f) f = fopen("/mc_dsi_debug.log", mode);
    if (!f) f = fopen("fat:/mc_dsi_debug.log", mode);
    return f;
}

void DSI_DebugInit(void) {
    FILE* f = openLogFile("w");
    if (f) {
        fputs("=== YUANCRAFT DSI HARDWARE DEBUG LOG ===\n", f);
        fflush(f);
        fclose(f);
    }
}

void DSI_Log(const char* format, ...) {
    // 1. Escritura inmediata en la tarjeta SD con flush forzado antes de cualquier posible bloqueo
    FILE* f = openLogFile("a");
    if (f) {
        va_list args;
        va_start(args, format);
        vfprintf(f, format, args);
        va_end(args);
        fflush(f);
        fclose(f);
    }

    // 2. Salida directa a la consola de texto en pantalla inferior (para visualización en consola física)
    va_list args2;
    va_start(args2, format);
    vprintf(format, args2);
    va_end(args2);
}

