#ifndef DSI_DEBUG_H
#define DSI_DEBUG_H

#include <nds.h>
#include <stdio.h>
#include <stdarg.h>

#ifdef __cplusplus
extern "C" {
#endif

// Marcador global de fase de ejecución volátil para capturar deadlocks en hardware real
extern volatile uint32_t g_CurrentExecStep;

// Inicializa y limpia el archivo de depuración en la tarjeta SD
void DSI_DebugInit(void);

// Escritura con flush físico inmediato a "sd:/mc_dsi_debug.log" y salida a consola
void DSI_Log(const char* format, ...);

#ifdef __cplusplus
}
#endif

#endif // DSI_DEBUG_H

