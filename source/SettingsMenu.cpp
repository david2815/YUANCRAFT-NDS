#include "Hardware.h"
#include "SettingsMenu.h"
#include "Options.h"
#include "PerformancePreset.h"
#include "TextKeyboard.h"
#include "Controls.h"
#include "Sound.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static int s_selected = 0;          // 0 = back, 1 = controls, 2 = auto jump, 3 = debug large chest, 4 = chunk mode, 5 = default seed (random/custom), 6 = custom default seed, 7 = clockcompassinvupdate, 8 = particles, 9 = sound, 10 = inventoryMap
static inline int getRowCount() { return 15; }
// Pop-up de confirmacion para opciones exclusivas de DSi en DS original
static bool s_showingPopUp = false;
static int s_pendingOption = -1;
static int s_pendingValue = 0;

static void drawPopUp() {
    consoleClear();
    iprintf("\x1b[31m================================\x1b[39m\n");
    iprintf("  \x1b[33;1mADVERTENCIA: EXCLUSIVO DSi\x1b[39m\n");
    iprintf("\x1b[31m================================\x1b[39m\n\n");
    iprintf(" Este ajuste requiere la CPU a\n");
    iprintf(" 133 MHz de una Nintendo DSi.\n\n");
    iprintf(" En Nintendo DS clasica (67 MHz)\n");
    iprintf(" causara caidas severas de FPS\n");
    iprintf(" y riesgo de falta de memoria.\n\n");
    iprintf(" Deseas aplicarlo de todos modos?\n\n");
    iprintf(" \x1b[32m[A] Confirmar bajo tu riesgo\x1b[39m\n");
    iprintf(" \x1b[31m[B] Cancelar\x1b[39m\n\n");
    iprintf("\x1b[31m================================\x1b[39m\n");
}

// Devuelve la longitud visual de la cadena en columnas de consola (omitiendo codigos de escape ANSI)
static int visualLength(const char* s) {
    if (!s) return 0;
    int len = 0;
    bool inEsc = false;
    for (; *s; s++) {
        if (*s == '\x1b') inEsc = true;
        else if (inEsc) {
            if (*s == 'm') inEsc = false;
        } else {
            len++;
        }
    }
    return len;
}

// "->  etiqueta                valor": flecha a la izquierda en la fila elegida, valor alineado a la derecha
static void printRow(bool selected, const char* label, const char* value) {
    const char* prefix = selected ? "-> " : "   ";
    if (!label || label[0] == '\0') {
        iprintf("%s%s\n", prefix, value ? value : "");
        return;
    }
    int labelLen = (int)strlen(label);
    int visValLen = visualLength(value ? value : "");
    int totalVis = 3 + labelLen + visValLen;
    if (totalVis < 32) {
        int spaces = 32 - 3 - labelLen - visValLen;
        if (spaces < 1) spaces = 1;
        iprintf("%s%s%*s%s\n", prefix, label, spaces, "", value ? value : "");
    } else {
        // Si no cabe en una linea de 32 columnas, se imprime la etiqueta y debajo el valor con sangria
        iprintf("%s%s:\n   %s\n", prefix, label, value ? value : "");
    }
}

// Una fila por indice: el menu se desplaza como una lista (VISIBLE filas a la vez, la ventana baja o sube cuando la seleccion llega al borde)
static const int VISIBLE = 7;
static int s_top = 0;

static void printOption(int row) {
    const bool sel = s_selected == row;
    switch (row) {
        case 0: printRow(sel, "", "back"); break;
        case 1: printRow(sel, "difficulty", (Options::get().difficulty == 0 ? "peaceful" : Options::get().difficulty == 1 ? "easy" : Options::get().difficulty == 3 ? "hard" : "normal")); break;
        case 2: printRow(sel, "controls", Options::get().controlMode == 1 ? "xyba >" : "normal >"); break;
        case 3: printRow(sel, "auto jump", Options::get().autoJump ? "on" : "off"); break;
        case 4: {
            static const char* const MODE_NAMES[3] = { "fast", "ds", "dsi" };
            const int m = Options::get().chunkMode <= 2 ? Options::get().chunkMode : 1;
            char valBuf[96];
            if (!g_isDSi && m == 2) {
                snprintf(valBuf, sizeof(valBuf), "dsi \x1b[31m[Exclusivo DSi]\x1b[39m");
            } else {
                snprintf(valBuf, sizeof(valBuf), "%s", MODE_NAMES[m]);
            }
            printRow(sel, "chunk mode", valBuf);
            break;
        }
        case 5: {
            const int q = Options::get().renderQuality;
            char valBuf[96];
            if (!g_isDSi && q == 0) {
                snprintf(valBuf, sizeof(valBuf), "high \x1b[33m[Riesgo: Caida FPS]\x1b[39m");
            } else {
                snprintf(valBuf, sizeof(valBuf), "%s", q == 2 ? "fast" : (q == 1 ? "balanced" : "high"));
            }
            printRow(sel, "render", valBuf);
            break;
        }
        case 6: printRow(sel, "default seed", Options::get().seedMode == 1 ? "custom" : "random"); break;
        case 7: {
            char seedText[16] = "";
            if (Options::get().customSeedSet) snprintf(seedText, sizeof(seedText), "%u", Options::get().customSeed);
            printRow(sel, "custom default seed", seedText);
            break;
        }
        case 8: printRow(sel, "clockcompassinvupdate", Options::get().clockCompassInvUpdate ? "true" : "false"); break;
        case 9: printRow(sel, "debug options", ">"); break;
        case 10: printRow(sel, "particles", Options::get().particles ? "on" : "off"); break;
        case 11: printRow(sel, "sound", Options::get().sound ? "on" : "off"); break;
        case 12: printRow(sel, "inventoryMap", Options::get().inventoryMap ? "true" : "false"); break;
        case 13: printRow(sel, "fps counter", Options::get().showFps ? "on" : "off"); break;
        case 14: {
            printRow(sel, "perf preset", PresetManager::getCurrentPresetName());
            break;
        }
    }
}

static void draw() {
    if (s_selected < s_top) s_top = s_selected;
    if (s_selected >= s_top + VISIBLE) s_top = s_selected - VISIBLE + 1;
    if (s_top < 0) s_top = 0;
    if (s_top > getRowCount() - VISIBLE) s_top = getRowCount() - VISIBLE;
    consoleClear();
    iprintf("Options\n\n");
    iprintf("%s\n", s_top > 0 ? "                              ^" : "");
    for (int r = s_top; r < s_top + VISIBLE && r < getRowCount(); r++) printOption(r);
    iprintf("%s\n", s_top + VISIBLE < getRowCount() ? "                              v" : "");
}

// ---- Submenu "controls": modo (perfil), reset del perfil y un boton por accion ----
static int s_view = 0;              // 0 = lista de opciones, 1 = submenu de controles, 2 = submenu debug options
static int cSel = 0, cTop = 0;
static bool cListening = false;     // esperando el boton nuevo de la accion elegida
static const int C_ROWS = 3 + Controls::COUNT;   // 0 back, 1 controls mode, 2 reset profile, 3.. acciones

static void printControlsRow(int row) {
    const bool sel = cSel == row;
    const int mode = Options::get().controlMode == 1 ? 1 : 0;
    if (row == 0) printRow(sel, "", "back");
    else if (row == 1) printRow(sel, "controls mode", mode == 1 ? "xyba" : "normal");
    else if (row == 2) printRow(sel, "reset this profile", "A");
    else {
        const Controls::Action a = (Controls::Action)(row - 3);
        printRow(sel, Controls::actionName(a), (sel && cListening) ? "press..." : Controls::keyName(Controls::getKey(mode, a)));
    }
}

static void drawControls() {
    if (cSel < cTop) cTop = cSel;
    if (cSel >= cTop + VISIBLE) cTop = cSel - VISIBLE + 1;
    if (cTop < 0) cTop = 0;
    if (cTop > C_ROWS - VISIBLE) cTop = C_ROWS - VISIBLE;
    consoleClear();
    iprintf("Controls (%s profile)\n\n", Options::get().controlMode == 1 ? "xyba" : "normal");
    iprintf("%s\n", cTop > 0 ? "                              ^" : "");
    for (int r = cTop; r < cTop + VISIBLE && r < C_ROWS; r++) printControlsRow(r);
    iprintf("%s\n", cTop + VISIBLE < C_ROWS ? "                              v" : "");
    if (cListening) iprintf("\nPress the new button\n(touch to cancel)\n");
    else if (cSel >= 3) iprintf("\nA: set  LEFT/RIGHT: cycle\n");
}

static void openControls() {
    s_view = 1; cSel = 0; cTop = 0; cListening = false;
    drawControls();
}

// true = volver a la lista de opciones
static bool updateControls(u32 keysDown) {
    const int mode = Options::get().controlMode == 1 ? 1 : 0;
    if (cListening) {
        u16 k;
        if (keysDown & KEY_TOUCH) { cListening = false; drawControls(); }
        else if (Controls::isBindable(keysDown, k)) {
            Controls::bind(mode, (Controls::Action)(cSel - 3), k);
            Controls::save();
            cListening = false;
            drawControls();
        }
        return false;
    }
    if (keysDown & KEY_B) return true;
    if (keysDown & KEY_UP)   { cSel = (cSel + C_ROWS - 1) % C_ROWS; drawControls(); }
    if (keysDown & KEY_DOWN) { cSel = (cSel + 1) % C_ROWS; drawControls(); }
    if (keysDown & (KEY_A | KEY_LEFT | KEY_RIGHT)) {
        if (cSel == 0) {
            if (keysDown & KEY_A) return true;
        } else if (cSel == 1) {
            Options::get().controlMode = mode == 1 ? 0 : 1;   // cambia el perfil activo (y el comportamiento del touch)
            Options::save();
            drawControls();
        } else if (cSel == 2) {
            if (keysDown & KEY_A) { Controls::resetProfile(mode); Controls::save(); drawControls(); }   // solo el perfil elegido
        } else {
            const Controls::Action a = (Controls::Action)(cSel - 3);
            if (keysDown & KEY_A) { cListening = true; drawControls(); }
            else { Controls::cycle(mode, a, (keysDown & KEY_LEFT) ? -1 : 1); Controls::save(); drawControls(); }
        }
    }
    return false;
}

// ---- Submenu "debug options": cofres de debug, spikes.txt, contenido de la debug screen y sus teclas ----
static int dSel = 0;
static const int D_ROWS = 6;   // 0 back, 1 debug large chest, 2 spike log, 3 debug screen info, 4 debug screen options, 5 old mob spawn limit

static void drawDebug() {
    consoleClear();
    iprintf("Debug options\n\n");
    for (int r = 0; r < D_ROWS; r++) {
        const bool sel = dSel == r;
        switch (r) {
            case 0: printRow(sel, "", "back"); break;
            case 1: printRow(sel, "debug large chest", Options::get().debugLargeChest ? "true" : "false"); break;
            case 2: printRow(sel, "spikes.txt log", Options::get().spikeLog ? "on" : "off"); break;
            case 3: printRow(sel, "debug screen info", Options::get().debugCoordsOnly ? "coords" : "full"); break;
            case 4: printRow(sel, "debug screen options", Options::get().debugScreenOptions ? "on" : "off"); break;
            case 5: printRow(sel, "oldmobspawnlimit", Options::get().oldMobSpawnLimit ? "true" : "false"); break;
        }
    }
    iprintf("\n");
    if (dSel == 3) iprintf("full: performance + coords\ncoords: only coordinates\n");
    else if (dSel == 4) iprintf("on: B = day/night, Y = rain,\nX = damage (peaceful only)\n");
    else if (dSel == 2) iprintf("slow frames (30 ms+) are saved\nto /mcdsefiles/spikes.txt\n");
    else if (dSel == 5) iprintf("true: the old mob limits (twice\nas many mobs, slower)\nfalse: half the mobs (default)\n");
}

static void openDebug() { s_view = 2; dSel = 0; drawDebug(); }

// true = volver a la lista de opciones
static bool updateDebug(u32 keysDown) {
    if (keysDown & KEY_B) return true;
    if (keysDown & KEY_UP)   { dSel = (dSel + D_ROWS - 1) % D_ROWS; drawDebug(); }
    if (keysDown & KEY_DOWN) { dSel = (dSel + 1) % D_ROWS; drawDebug(); }
    if (keysDown & (KEY_A | KEY_LEFT | KEY_RIGHT)) {
        if (dSel == 0) {
            if (keysDown & KEY_A) return true;
        } else {
            Options::Data& o = Options::get();
            if (dSel == 1) o.debugLargeChest = !o.debugLargeChest;
            else if (dSel == 2) o.spikeLog = !o.spikeLog;
            else if (dSel == 3) o.debugCoordsOnly = !o.debugCoordsOnly;
            else if (dSel == 4) o.debugScreenOptions = !o.debugScreenOptions;
            else o.oldMobSpawnLimit = !o.oldMobSpawnLimit;
            Options::save();
            drawDebug();
        }
    }
    return false;
}

void SettingsMenu::open() {
    s_selected = 0;
    s_top = 0;
    s_view = 0;
    s_showingPopUp = false;
    cListening = false;
    consoleDemoInit();   // consola de la pantalla de abajo
    draw();
}

bool SettingsMenu::update(u32 keysDown) {
    if (keysDown & KEY_TOUCH) {
        touchPosition touch;
        touchRead(&touch);
        if (s_showingPopUp) {
            if (touch.py >= 120 && touch.py <= 160) {
                // Confirmar
                Sound::uiClick();
                if (s_pendingOption == 4) Options::get().chunkMode = (unsigned char)s_pendingValue;
                else if (s_pendingOption == 5) Options::get().renderQuality = (unsigned char)s_pendingValue;
                PresetManager::notifyOptionChanged();
                Options::save();
                s_showingPopUp = false;
                consoleDemoInit();
                draw();
                return false;
            } else if (touch.py > 160) {
                // Cancelar
                Sound::uiClick();
                s_showingPopUp = false;
                consoleDemoInit();
                draw();
                return false;
            }
        } else if (s_view == 0) {
            // Tocar en la zona superior (y < 32) equivale al boton back
            if (touch.py < 32) {
                Sound::uiClick();
                return true;
            }
        }
    }

    if (s_showingPopUp) {
        if (keysDown & KEY_A) {
            Sound::uiClick();
            if (s_pendingOption == 4) Options::get().chunkMode = (unsigned char)s_pendingValue;
            else if (s_pendingOption == 5) Options::get().renderQuality = (unsigned char)s_pendingValue;
            PresetManager::notifyOptionChanged();
            Options::save();
            s_showingPopUp = false;
            consoleDemoInit();
            draw();
            return false;
        }
        if (keysDown & KEY_B) {
            Sound::uiClick();
            s_showingPopUp = false;
            consoleDemoInit();
            draw();
            return false;
        }
        return false;
    }

    if (keysDown & (KEY_A | KEY_B | KEY_LEFT | KEY_RIGHT)) Sound::uiClick();   // cada cambio de opcion, submenu o volver

    if (s_view == 1) {
        if (updateControls(keysDown)) { s_view = 0;
    s_showingPopUp = false; consoleDemoInit(); draw(); }
        return false;
    }
    if (s_view == 2) {
        if (updateDebug(keysDown)) { s_view = 0;
    s_showingPopUp = false; consoleDemoInit(); draw(); }
        return false;
    }
    if (keysDown & KEY_B) return true;

    if (keysDown & KEY_UP)   { s_selected = (s_selected + getRowCount() - 1) % getRowCount(); draw(); }
    if (keysDown & KEY_DOWN) { s_selected = (s_selected + 1) % getRowCount(); draw(); }

    if (keysDown & (KEY_A | KEY_LEFT | KEY_RIGHT)) {
        if (s_selected == 0) {
            if (keysDown & KEY_A) return true;
        } else if (s_selected == 1) {
            { int d = Options::get().difficulty; d = (keysDown & KEY_LEFT) ? (d + 3) % 4 : (d + 1) % 4; Options::get().difficulty = (unsigned char)d; }
            Options::save();
            draw();
        } else if (s_selected == 2) {
            consoleDemoInit();
            openControls();   // submenu de controles
        } else if (s_selected == 3) {
            Options::get().autoJump = !Options::get().autoJump;
            Options::save();
            draw();
        } else if (s_selected == 9) {
            consoleDemoInit();
            openDebug();   // submenu debug options
        } else if (s_selected == 10) {
            Options::get().particles = !Options::get().particles;
            PresetManager::notifyOptionChanged();
            Options::save();
            draw();
        } else if (s_selected == 5) {
            int q = Options::get().renderQuality;
            q = (keysDown & KEY_LEFT) ? (q + 2) % 3 : (q + 1) % 3;
            if (!g_isDSi && q == 0) {
                // Advertencia para 'high' en DS clasica
                s_showingPopUp = true;
                s_pendingOption = 5;
                s_pendingValue = 0;
                drawPopUp();
                return false;
            }
            Options::get().renderQuality = (unsigned char)q;
            PresetManager::notifyOptionChanged();
            Options::save();
            draw();
        } else if (s_selected == 12) {
            Options::get().inventoryMap = !Options::get().inventoryMap;
            Options::save();
            draw();
        } else if (s_selected == 13) {
            Options::get().showFps = !Options::get().showFps;
            Options::save();
            draw();
        } else if (s_selected == 11) {
            Options::get().sound = !Options::get().sound;
            Options::save();
            draw();
        } else if (s_selected == 8) {
            Options::get().clockCompassInvUpdate = !Options::get().clockCompassInvUpdate;
            Options::save();
            draw();
        } else if (s_selected == 6) {
            Options::get().seedMode = Options::get().seedMode == 1 ? 0 : 1;
            Options::save();
            draw();
        } else if (s_selected == 7) {
            if (keysDown & KEY_A) {   // A abre el teclado numerico; vacio = sin seed custom
                char buf[12] = "";
                if (Options::get().customSeedSet) snprintf(buf, sizeof(buf), "%u", Options::get().customSeed);
                if (TextKeyboard::edit("Custom default seed", buf, 9, true)) {
                    Options::get().customSeedSet = buf[0] != 0;
                    Options::get().customSeed = buf[0] ? (unsigned int)strtoul(buf, nullptr, 10) : 0;
                    Options::save();
                }
                consoleDemoInit();   // de vuelta a la lista
                draw();
            }
        } else if (s_selected == 14) {
            PresetManager::cyclePreset((keysDown & KEY_LEFT) ? -1 : 1);
            draw();
        } else if (s_selected == 4) {
            // fast (0) -> ds (1) -> dsi (2)
            int m = Options::get().chunkMode;
            m = (keysDown & KEY_LEFT) ? (m + 2) % 3 : (m + 1) % 3;
            if (!g_isDSi && m == 2) {
                // Advertencia y Pop-up en DS original
                s_showingPopUp = true;
                s_pendingOption = 4;
                s_pendingValue = 2;
                drawPopUp();
                return false;
            }
            Options::get().chunkMode = (unsigned char)m;
            PresetManager::notifyOptionChanged();
            Options::save();
            draw();
        }
    }
    return false;
}