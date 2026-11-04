#include "StartupSplash.h"
#include <nds.h>
#include "eagteklogo.h"
#include "mojanglogo.h"

namespace {
    const int LOGO_FRAMES = 60;   // 1 segundo por logo

    void showLogo(const unsigned int* bitmap, const unsigned short* pal, unsigned int palLen, bool hold) {
        swiWaitForVBlank();   // Sincronizar con el inicio de cuadro

        videoSetMode(MODE_5_2D | DISPLAY_BG3_ACTIVE);
        vramSetBankB(VRAM_B_MAIN_BG_0x06000000);
        const int id = bgInit(3, BgType_Bmp8, BgSize_B8_256x256, 0, 0);

        // Limpieza de pantalla y paleta
        u16* gfx = (u16*)bgGetGfxPtr(id);
        dmaFillWords(0, gfx, 256 * 192);
        dmaFillHalfWords(0, BG_PALETTE, 512);

        // Copiar paleta y descomprimir bitmap directamente en VRAM
        dmaCopy(pal, BG_PALETTE, palLen);
        decompress(bitmap, gfx, LZ77Vram);

        if (hold) {
            for (int f = 0; f < LOGO_FRAMES; f++) {
                swiWaitForVBlank();
            }
        }
    }
}

void StartupSplash::show() {
    // Despliegue secuencial de logos sin alterar registros de interrupción ni registros de control FIFO
    showLogo((const unsigned int*)eagteklogoBitmap, eagteklogoPal, eagteklogoPalLen, true);
    showLogo((const unsigned int*)mojanglogoBitmap, mojanglogoPal, mojanglogoPalLen, true);
}

void StartupSplash::finish() {
    // Restaurar el color de fondo neutro y la consola de depuración en pantalla inferior
    setBackdropColorSub(0);
}

