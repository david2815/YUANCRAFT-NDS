h_content = """#ifndef PAUSESCREEN_H
#define PAUSESCREEN_H

#include <nds.h>

// Menu de pausa (pantalla de abajo): imagen pauseMenu.png con 4 botones en las mismas posiciones del menu principal.
// El juego no se congela mientras esta abierto; solo se bloquean los controles.
namespace PauseScreen {
    enum Button { BTN_NONE = 0, BTN_BACK, BTN_OPTIONS, BTN_SAVE, BTN_QUIT, BTN_CONTINUE };

    void show();                                // dibuja la imagen
    void showSavingProgress(int percent, int current, int total); // dibuja barra de progreso de guardado
    void showSaveComplete();                    // dibuja opciones tras guardar (Continuar / Salir)
    Button touched(int touchX, int touchY);     // que boton esta bajo el lapiz
    Button touchedSaveComplete(int touchX, int touchY); // que boton bajo el lapiz tras guardar
}

#endif
"""
with open("source/PauseScreen.h", "w", encoding="utf-8") as f:
    f.write(h_content)
print("Updated source/PauseScreen.h")

with open("source/PauseScreen.cpp", "r", encoding="utf-8", errors="replace") as f:
    cpp_content = f.read()

extra_cpp = """
void PauseScreen::showSavingProgress(int percent, int current, int total) {
    consoleDemoInit();
    consoleClear();
    iprintf("\\x1b[36m================================\\x1b[39m\\n");
    iprintf("   \\x1b[32;1mGUARDADO SEGURO A PRUEBA\\x1b[39m\\n");
    iprintf("       \\x1b[32;1mDE FALLOS EN SD\\x1b[39m\\n");
    iprintf("\\x1b[36m================================\\x1b[39m\\n\\n");
    iprintf(" \\x1b[31;1mNO apagues la consola\\x1b[39m ni\\n");
    iprintf(" retires la tarjeta SD.\\n\\n");
    iprintf(" Volcado RLE/LZSS asincrono:\\n\\n");

    char bar[21];
    int filled = (percent * 20) / 100;
    if (filled > 20) filled = 20;
    for (int i = 0; i < 20; i++) bar[i] = (i < filled) ? '=' : ' ';
    bar[20] = '\\0';

    iprintf(" [%s] %3d%%\\n\\n", bar, percent);
    iprintf(" Chunks volcados: %d / %d\\n\\n", current, total);
    iprintf("\\x1b[33m [Entradas y botones bloqueados]\\x1b[39m\\n");
}

void PauseScreen::showSaveComplete() {
    consoleDemoInit();
    consoleClear();
    iprintf("\\x1b[32m================================\\x1b[39m\\n");
    iprintf("    \\x1b[32;1mGUARDADO EXITOSO (SUCCESS)\\x1b[39m\\n");
    iprintf("\\x1b[32m================================\\x1b[39m\\n\\n");
    iprintf(" Todos los datos del mundo se\\n");
    iprintf(" han volcado a la SD con exito.\\n\\n");
    iprintf(" Deseas continuar o salir?\\n\\n");
    iprintf(" \\x1b[36m------------------------------\\x1b[39m\\n");
    iprintf("  \\x1b[37;1m[A] Continuar Partida\\x1b[39m\\n");
    iprintf(" \\x1b[36m------------------------------\\x1b[39m\\n");
    iprintf("  \\x1b[37;1m[B] Salir al Menu Principal\\x1b[39m\\n");
    iprintf(" \\x1b[36m------------------------------\\x1b[39m\\n\\n");
    iprintf(" Toca la opcion o presiona A / B\\n");
}

PauseScreen::Button PauseScreen::touchedSaveComplete(int touchX, int touchY) {
    if (touchX < 20 || touchX > 236) return BTN_NONE;
    if (touchY >= 80 && touchY <= 120) return BTN_CONTINUE;
    if (touchY >= 125 && touchY <= 165) return BTN_QUIT;
    return BTN_NONE;
}
"""

if "showSavingProgress" not in cpp_content:
    cpp_content = cpp_content.strip() + extra_cpp

with open("source/PauseScreen.cpp", "w", encoding="utf-8") as f:
    f.write(cpp_content)
print("Updated source/PauseScreen.cpp")

