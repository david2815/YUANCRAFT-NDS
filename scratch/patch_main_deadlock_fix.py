with open('source/main.cpp', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Define bool g_isDSi
if 'bool g_isDSi = false;' not in text:
    text = '#include "Hardware.h"\n\nbool g_isDSi = false;\n' + text

# 2. In main(), set g_isDSi once at startup
init_code = "Hardware::initHardwareProfile();"
if "g_isDSi = isDSiMode();\n    Hardware::initHardwareProfile();" not in text:
    text = text.replace(init_code, "g_isDSi = isDSiMode();\n    Hardware::initHardwareProfile();", 1)

# 3. Replace saveLocked with isSavingWorld
text = text.replace("bool saveLocked = false;", "bool isSavingWorld = false;")
text = text.replace("if (saveLocked)", "if (isSavingWorld)")
text = text.replace("saveLocked = true;", "isSavingWorld = true;")
text = text.replace("saveLocked = false;", "isSavingWorld = false;")

# 4. In paused && pauseView == 2, 3, 4: add swiWaitForVBlank(); continue;
old_pause_views = """            } else if (paused && pauseView == 2) {
                if (SettingsMenu::update(keys_down)) {
                    autoJumpEnabled = Options::get().autoJump;
                    controlMode = Options::get().controlMode;
                    if (Options::get().chunkMode != chunkModeAtOptions) reloadChunkModeRequested = true;   // se aplica al instante: se recarga el mundo con el modo nuevo
                    pauseView = 1;
                    PauseScreen::show();
                }
            } else if (paused && pauseView == 3) {
                // Estado de guardado seguro bloqueado: se procesa el volcado asincrono
                AsyncSaveManager::processQueue();
                PauseScreen::showSavingProgress(AsyncSaveManager::getProgressPercent(), AsyncSaveManager::getCompletedTasks(), AsyncSaveManager::getTotalTasks());
                if (AsyncSaveManager::isSavingComplete()) {
                    isSavingWorld = false;
                    pauseView = 4;
                    PauseScreen::showSaveComplete();
                }
            } else if (paused && pauseView == 4) {
                // Estado post-guardado desbloqueado: el usuario elige continuar o salir
                bool doContinue = (keys_down & KEY_A);
                bool doQuit = (keys_down & KEY_B);
                if (keys_down & KEY_TOUCH) {
                    PauseScreen::Button cb = PauseScreen::touchedSaveComplete(pTouch.px, pTouch.py);
                    if (cb == PauseScreen::BTN_CONTINUE) doContinue = true;
                    else if (cb == PauseScreen::BTN_QUIT) doQuit = true;
                }
                if (doContinue) {
                    Sound::uiClick();
                    closePause();
                } else if (doQuit) {
                    Sound::uiClick();
                    quitRequested = true;
                }
            }"""

new_pause_views = """            } else if (paused && pauseView == 2) {
                // Menu de opciones en pausa: inputs libres y ceder ciclo con swiWaitForVBlank para evitar deadlock/congelamiento
                if (SettingsMenu::update(keys_down)) {
                    autoJumpEnabled = Options::get().autoJump;
                    controlMode = Options::get().controlMode;
                    if (Options::get().chunkMode != chunkModeAtOptions) reloadChunkModeRequested = true;   // se aplica al instante: se recarga el mundo con el modo nuevo
                    pauseView = 1;
                    PauseScreen::show();
                }
                swiWaitForVBlank();
                continue;
            } else if (paused && pauseView == 3) {
                // Estado de guardado seguro bloqueado: se procesa el volcado asincrono
                AsyncSaveManager::processQueue();
                PauseScreen::showSavingProgress(AsyncSaveManager::getProgressPercent(), AsyncSaveManager::getCompletedTasks(), AsyncSaveManager::getTotalTasks());
                if (AsyncSaveManager::isSavingComplete()) {
                    isSavingWorld = false; // Desbloqueo estricto unicamente tras completarse con exito
                    pauseView = 4;
                    PauseScreen::showSaveComplete();
                }
                swiWaitForVBlank();
                continue;
            } else if (paused && pauseView == 4) {
                // Estado post-guardado desbloqueado: el usuario elige continuar o salir
                bool doContinue = (keys_down & KEY_A);
                bool doQuit = (keys_down & KEY_B);
                if (keys_down & KEY_TOUCH) {
                    PauseScreen::Button cb = PauseScreen::touchedSaveComplete(pTouch.px, pTouch.py);
                    if (cb == PauseScreen::BTN_CONTINUE) doContinue = true;
                    else if (cb == PauseScreen::BTN_QUIT) doQuit = true;
                }
                if (doContinue) {
                    Sound::uiClick();
                    closePause();
                } else if (doQuit) {
                    Sound::uiClick();
                    quitRequested = true;
                }
                swiWaitForVBlank();
                continue;
            }"""

text = text.replace(old_pause_views, new_pause_views)

# 5. Replace isDSiMode() with g_isDSi in line 2390
text = text.replace("const bool is60Fps = isDSiMode()", "const bool is60Fps = g_isDSi")

with open('source/main.cpp', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated source/main.cpp successfully')

