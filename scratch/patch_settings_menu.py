import re

with open('source/SettingsMenu.cpp', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace ROW_COUNT with dynamic getRowCount()
text = text.replace(
    'static const int ROW_COUNT = 14;',
    'static inline int getRowCount() { return isDSiMode() ? 15 : 14; }'
)

# 2. Add pop-up state
popup_state = """// Pop-up de confirmacion para opciones exclusivas de DSi en DS original
static bool s_showingPopUp = false;
static int s_pendingOption = -1;
static int s_pendingValue = 0;

static void drawPopUp() {
    consoleClear();
    iprintf("\\x1b[31m================================\\x1b[39m\\n");
    iprintf("  \\x1b[33;1mADVERTENCIA: EXCLUSIVO DSi\\x1b[39m\\n");
    iprintf("\\x1b[31m================================\\x1b[39m\\n\\n");
    iprintf(" Este ajuste requiere la CPU a\\n");
    iprintf(" 133 MHz de una Nintendo DSi.\\n\\n");
    iprintf(" En Nintendo DS clasica (67 MHz)\\n");
    iprintf(" causara caidas severas de FPS\\n");
    iprintf(" y riesgo de falta de memoria.\\n\\n");
    iprintf(" Deseas aplicarlo de todos modos?\\n\\n");
    iprintf(" \\x1b[32m[A] Confirmar bajo tu riesgo\\x1b[39m\\n");
    iprintf(" \\x1b[31m[B] Cancelar\\x1b[39m\\n\\n");
    iprintf("\\x1b[31m================================\\x1b[39m\\n");
}
"""

text = text.replace('static const int COLUMNS = 32;', popup_state + '\nstatic const int COLUMNS = 32;')

# 3. Update printOption for chunk mode, render, and dsi profile
old_chunk_opt = """        case 4: {
            static const char* const MODE_NAMES[3] = { "fast", "ds", "dsi" };
            printRow(sel, "chunk mode", MODE_NAMES[Options::get().chunkMode <= 2 ? Options::get().chunkMode : 1]);
            break;
        }
        case 5: printRow(sel, "render", Options::get().renderQuality == 2 ? "fast" : (Options::get().renderQuality == 1 ? "balanced" : "high")); break;"""

new_chunk_opt = """        case 4: {
            static const char* const MODE_NAMES[3] = { "fast", "ds", "dsi" };
            const int m = Options::get().chunkMode <= 2 ? Options::get().chunkMode : 1;
            char valBuf[40];
            if (!isDSiMode() && m == 2) {
                snprintf(valBuf, sizeof(valBuf), "dsi \\x1b[31m[Exclusivo DSi]\\x1b[39m");
            } else {
                snprintf(valBuf, sizeof(valBuf), "%s", MODE_NAMES[m]);
            }
            printRow(sel, "chunk mode", valBuf);
            break;
        }
        case 5: {
            const int q = Options::get().renderQuality;
            char valBuf[40];
            if (!isDSiMode() && q == 0) {
                snprintf(valBuf, sizeof(valBuf), "high \\x1b[33m[Riesgo: Caida FPS]\\x1b[39m");
            } else {
                snprintf(valBuf, sizeof(valBuf), "%s", q == 2 ? "fast" : (q == 1 ? "balanced" : "high"));
            }
            printRow(sel, "render", valBuf);
            break;
        }"""

text = text.replace(old_chunk_opt, new_chunk_opt)

# Add case 14 in printOption
old_case13 = '        case 13: printRow(sel, "fps counter", Options::get().showFps ? "on" : "off"); break;\n    }'
new_case13 = """        case 13: printRow(sel, "fps counter", Options::get().showFps ? "on" : "off"); break;
        case 14: {
            if (isDSiMode()) {
                const bool fluid = Options::get().dsiPerformanceProfile == 1;
                printRow(sel, "dsi perf profile", fluid ? "fluid (60fps)" : "distance (30fps)");
            }
            break;
        }
    }"""
text = text.replace(old_case13, new_case13)

# Replace all occurrences of ROW_COUNT in draw() and update()
text = text.replace('if (s_top > ROW_COUNT - VISIBLE) s_top = ROW_COUNT - VISIBLE;', 'if (s_top > getRowCount() - VISIBLE) s_top = getRowCount() - VISIBLE;')
text = text.replace('for (int r = s_top; r < s_top + VISIBLE && r < ROW_COUNT; r++) printOption(r);', 'for (int r = s_top; r < s_top + VISIBLE && r < getRowCount(); r++) printOption(r);')
text = text.replace('iprintf("%s\\n", s_top + VISIBLE < ROW_COUNT ? "                              v" : "");', 'iprintf("%s\\n", s_top + VISIBLE < getRowCount() ? "                              v" : "");')
text = text.replace('if (keysDown & KEY_UP)   { s_selected = (s_selected + ROW_COUNT - 1) % ROW_COUNT; draw(); }', 'if (keysDown & KEY_UP)   { s_selected = (s_selected + getRowCount() - 1) % getRowCount(); draw(); }')
text = text.replace('if (keysDown & KEY_DOWN) { s_selected = (s_selected + 1) % ROW_COUNT; draw(); }', 'if (keysDown & KEY_DOWN) { s_selected = (s_selected + 1) % getRowCount(); draw(); }')

# In open(): reset popup
text = text.replace('s_view = 0;', 's_view = 0;\n    s_showingPopUp = false;')

# In update(): handle popup inputs and option 5, 4 and 14
popup_check = """bool SettingsMenu::update(u32 keysDown) {
    if (s_showingPopUp) {
        if (keysDown & KEY_A) {
            Sound::uiClick();
            if (s_pendingOption == 4) Options::get().chunkMode = (unsigned char)s_pendingValue;
            else if (s_pendingOption == 5) Options::get().renderQuality = (unsigned char)s_pendingValue;
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
"""
text = text.replace('bool SettingsMenu::update(u32 keysDown) {', popup_check)

# Update render quality (s_selected == 5) to trigger popup if !isDSiMode() and target is 0 (high)
old_render_upd = """        } else if (s_selected == 5) {
            { int q = Options::get().renderQuality; q = (keysDown & KEY_LEFT) ? (q + 2) % 3 : (q + 1) % 3; Options::get().renderQuality = (unsigned char)q; }
            Options::save();
            draw();"""

new_render_upd = """        } else if (s_selected == 5) {
            int q = Options::get().renderQuality;
            q = (keysDown & KEY_LEFT) ? (q + 2) % 3 : (q + 1) % 3;
            if (!isDSiMode() && q == 0) {
                // Advertencia para 'high' en DS clasica
                s_showingPopUp = true;
                s_pendingOption = 5;
                s_pendingValue = 0;
                drawPopUp();
                return false;
            }
            Options::get().renderQuality = (unsigned char)q;
            Options::save();
            draw();"""
text = text.replace(old_render_upd, new_render_upd)

# Update chunk mode and option 14
old_chunk_upd = """        } else {
            // fast -> ds -> dsi (dsi solo en una DSi); con IZQUIERDA se retrocede. Vale desde el proximo mundo que se abra.
            const int top = isDSiMode() ? 2 : 1;
            int m = Options::get().chunkMode;
            if (m > top) m = top;
            if (keysDown & KEY_LEFT) m = (m + top) % (top + 1);
            else                     m = (m + 1) % (top + 1);
            Options::get().chunkMode = (unsigned char)m;
            Options::save();
            draw();
        }"""

new_chunk_upd = """        } else if (s_selected == 14 && isDSiMode()) {
            const int next = Options::get().dsiPerformanceProfile == 1 ? 0 : 1;
            Options::get().dsiPerformanceProfile = (unsigned char)next;
            if (next == 1) {
                // Perfil Fluidez (60 FPS): reduce la distancia de dibujado al minimo indispensable
                Options::get().chunkMode = 0; // fast (3x3)
            } else {
                // Perfil Distancia (30 FPS): expande la distancia de renderizado al punto optimo
                Options::get().chunkMode = 2; // dsi (7x7)
            }
            Options::save();
            draw();
        } else if (s_selected == 4) {
            // fast (0) -> ds (1) -> dsi (2)
            int m = Options::get().chunkMode;
            m = (keysDown & KEY_LEFT) ? (m + 2) % 3 : (m + 1) % 3;
            if (!isDSiMode() && m == 2) {
                // Advertencia y Pop-up en DS original
                s_showingPopUp = true;
                s_pendingOption = 4;
                s_pendingValue = 2;
                drawPopUp();
                return false;
            }
            Options::get().chunkMode = (unsigned char)m;
            Options::save();
            draw();
        }"""
text = text.replace(old_chunk_upd, new_chunk_upd)

with open('source/SettingsMenu.cpp', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated source/SettingsMenu.cpp successfully')

