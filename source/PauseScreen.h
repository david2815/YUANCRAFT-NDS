#ifndef PAUSESCREEN_H
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
