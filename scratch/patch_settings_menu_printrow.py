import re

with open("source/SettingsMenu.cpp", "rb") as f:
    content = f.read().decode("utf-8")

# 1. Replace printRow and printOption
old_printrow = """static const int COLUMNS = 32;      // ancho de la consola

// "->  etiqueta                valor": flecha a la izquierda en la fila elegida, valor alineado a la derecha
static void printRow(bool selected, const char* label, const char* value) {
    char line[COLUMNS + 1];
    memset(line, ' ', COLUMNS);
    line[COLUMNS] = 0;
    if (selected) { line[0] = '-'; line[1] = '>'; }
    int labelLen = (int)strlen(label), valueLen = (int)strlen(value);
    if (labelLen > COLUMNS - 4 - valueLen) labelLen = COLUMNS - 4 - valueLen;
    memcpy(line + 3, label, labelLen);
    memcpy(line + COLUMNS - valueLen, value, valueLen);
    iprintf("%s\\n", line);
}"""

new_printrow = """// Devuelve la longitud visual de la cadena en columnas de consola (omitiendo codigos de escape ANSI)
static int visualLength(const char* s) {
    if (!s) return 0;
    int len = 0;
    bool inEsc = false;
    for (; *s; s++) {
        if (*s == '\\x1b') inEsc = true;
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
    if (!label || label[0] == '\\0') {
        iprintf("%s%s\\n", prefix, value ? value : "");
        return;
    }
    int labelLen = (int)strlen(label);
    int visValLen = visualLength(value ? value : "");
    int totalVis = 3 + labelLen + visValLen;
    if (totalVis < 32) {
        int spaces = 32 - 3 - labelLen - visValLen;
        if (spaces < 1) spaces = 1;
        iprintf("%s%s%*s%s\\n", prefix, label, spaces, "", value ? value : "");
    } else {
        // Si no cabe en una linea de 32 columnas, se imprime la etiqueta y debajo el valor con sangria
        iprintf("%s%s:\\n   %s\\n", prefix, label, value ? value : "");
    }
}"""

# Normalize line endings for replacement
norm_content = content.replace("\r\n", "\n")
norm_old = old_printrow.replace("\r\n", "\n")

assert norm_old in norm_content, "old_printrow block not found!"
norm_content = norm_content.replace(norm_old, new_printrow.replace("\r\n", "\n"), 1)

# Change VISIBLE = 8 to VISIBLE = 7
norm_content = norm_content.replace("static const int VISIBLE = 8;", "static const int VISIBLE = 7;")

# Change valBuf[40] to valBuf[96]
norm_content = norm_content.replace("char valBuf[40];", "char valBuf[96];")

# Add touch support in update()
old_update_head = """bool SettingsMenu::update(u32 keysDown) {
    if (s_showingPopUp) {"""

new_update_head = """bool SettingsMenu::update(u32 keysDown) {
    if (keysDown & KEY_TOUCH) {
        touchPosition touch;
        touchRead(&touch);
        if (s_showingPopUp) {
            if (touch.py >= 120 && touch.py <= 160) {
                // Confirmar
                Sound::uiClick();
                if (s_pendingOption == 4) Options::get().chunkMode = (unsigned char)s_pendingValue;
                else if (s_pendingOption == 5) Options::get().renderQuality = (unsigned char)s_pendingValue;
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

    if (s_showingPopUp) {"""

assert old_update_head in norm_content, "old_update_head not found!"
norm_content = norm_content.replace(old_update_head, new_update_head, 1)

with open("source/SettingsMenu.cpp", "w", encoding="utf-8", newline="\n") as f:
    f.write(norm_content)

print("Successfully patched source/SettingsMenu.cpp!")

