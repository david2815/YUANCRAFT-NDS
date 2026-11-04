#include "StartupSplash.h"
#include <nds.h>
#include "eagteklogo.h"
#include "mojanglogo.h"

namespace {
    const int LOGO_FRAMES = 60;   // 1 segundo por logo (60 frames a 60 Hz)

    void showLogo(const unsigned int* bitmap, const unsigned short* pal, unsigned int palLen, bool hold) {
        // 1. Configurar modo gráfico 2D y banco de VRAM B en pantalla principal
        videoSetMode(MODE_5_2D | DISPLAY_BG3_ACTIVE);
        vramSetBankB(VRAM_B_MAIN_BG_0x06000000);
        const int id = bgInit(3, BgType_Bmp8, BgSize_B8_256x256, 0, 0);

        // 2. Limpieza de pantalla y paleta inicial a negro para evitar artefactos visuales
        u16* gfx = (u16*)bgGetGfxPtr(id);
        dmaFillWords(0, gfx, 256 * 192);
        dmaFillHalfWords(0, BG_PALETTE, 512);

        // 3. Descomprimir bitmap directamente en VRAM
        decompress(bitmap, gfx, LZ77Vram);

        // 4. Copiar paleta sincronizada en VBlank para despliegue instantáneo sin tearing
        swiWaitForVBlank();
        dmaCopy(pal, BG_PALETTE, palLen);

        // 5. Mantener en pantalla durante los frames requeridos
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

