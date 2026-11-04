#include "StartupSplash.h"
#include <nds.h>
#include "eagteklogo.h"
#include "mojanglogo.h"

namespace {
    const int LOGO_FRAMES = 60;   // 1 segundo por logo, cambio síncrono limpio

    void showLogo(const unsigned int* bitmap, const unsigned short* pal, unsigned int palLen, bool hold) {
        swiWaitForVBlank();   // Sincronizar con el inicio de cuadro

        videoSetMode(MODE_5_2D | DISPLAY_BG3_ACTIVE);
        vramSetBankB(VRAM_B_MAIN_BG_0x06000000);
        const int id = bgInit(3, BgType_Bmp8, BgSize_B8_256x256, 0, 0);

        // 1. Limpieza explícita del búfer de video en VRAM y paleta de color
        u16* gfx = (u16*)bgGetGfxPtr(id);
        dmaFillWords(0, gfx, 256 * 256);
        dmaFillHalfWords(0, BG_PALETTE, 512);

        // 2. Limpieza de registros de interrupciones pendientes
        REG_IF = REG_IF;

        dmaCopy(pal, BG_PALETTE, palLen);
        decompress(bitmap, gfx, LZ77Vram);   // Descompresión directa a VRAM

        // 3. Bucle simple con swiWaitForVBlank() sin hilos ni solicitudes IPC
        if (hold) {
            for (int f = 0; f < LOGO_FRAMES; f++) {
                swiWaitForVBlank();
            }
        }
    }
}

void StartupSplash::show() {
    // Limpieza de interrupciones y estado de cola IPC antes del despliegue del logo
    REG_IF = REG_IF;
    REG_IPC_FIFO_CR = IPC_FIFO_ENABLE | IPC_FIFO_SEND_CLEAR;

    // Pantalla inferior: sin capas activas, color neutro limpio
    videoSetModeSub(MODE_0_2D);
    setBackdropColorSub(RGB15(31, 31, 31));

    // Despliegue secuencial de logos con limpieza de buffers
    showLogo((const unsigned int*)eagteklogoBitmap, eagteklogoPal, eagteklogoPalLen, true);
    showLogo((const unsigned int*)mojanglogoBitmap, mojanglogoPal, mojanglogoPalLen, true);
}

void StartupSplash::finish() {
    setBackdropColorSub(0);
    consoleDemoInit();   // Consola inferior normal tras la pantalla de presentación
}
