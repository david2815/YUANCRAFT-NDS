with open('source/main.cpp', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add saveLocked variable near paused
old_paused = "bool paused = false;          // menu de pausa abierto (el juego sigue corriendo, solo se bloquean los controles)\n    int pauseView = 0;            // 0 = cerrado, 1 = menu de pausa, 2 = opciones (consola)"
new_paused = """bool paused = false;          // menu de pausa abierto (el juego sigue corriendo, solo se bloquean los controles)
    int pauseView = 0;            // 0 = cerrado, 1 = pausa, 2 = opciones, 3 = guardando seguro (bloqueado), 4 = guardado completo
    bool saveLocked = false;      // congelamiento estricto de UI/botones durante guardado seguro"""
text = text.replace(old_paused, new_paused)

# 2. Key scanning lock: if saveLocked, freeze all inputs!
old_keyscan = """        scanKeys();
        keys_held = keysHeld();
        keys_down = keysDown();"""
new_keyscan = """        scanKeys();
        keys_held = keysHeld();
        keys_down = keysDown();
        if (saveLocked) {
            keys_held = 0;
            keys_down = 0;
        }"""
text = text.replace(old_keyscan, new_keyscan)

# 3. Handle pauseView == 1 save click, and add pauseView == 3 and 4
old_pause_handling = """            } else if (paused && pauseView == 1 && (keys_down & KEY_TOUCH)) {
                PauseScreen::Button pb = PauseScreen::touched(pTouch.px, pTouch.py);
                if (pb != PauseScreen::BTN_NONE) Sound::uiClick();
                if (pb == PauseScreen::BTN_BACK) closePause();
                else if (pb == PauseScreen::BTN_OPTIONS) { pauseView = 2; chunkModeAtOptions = Options::get().chunkMode; SettingsMenu::open(); }
                else if (pb == PauseScreen::BTN_SAVE) saveRequested = true;
                else if (pb == PauseScreen::BTN_QUIT) quitRequested = true;
            } else if (paused && pauseView == 2) {
                if (SettingsMenu::update(keys_down)) {
                    autoJumpEnabled = Options::get().autoJump;
                    controlMode = Options::get().controlMode;
                    if (Options::get().chunkMode != chunkModeAtOptions) reloadChunkModeRequested = true;   // se aplica al instante: se recarga el mundo con el modo nuevo
                    pauseView = 1;
                    PauseScreen::show();
                }
            }"""

new_pause_handling = """            } else if (paused && pauseView == 1 && (keys_down & KEY_TOUCH)) {
                PauseScreen::Button pb = PauseScreen::touched(pTouch.px, pTouch.py);
                if (pb != PauseScreen::BTN_NONE) Sound::uiClick();
                if (pb == PauseScreen::BTN_BACK) closePause();
                else if (pb == PauseScreen::BTN_OPTIONS) { pauseView = 2; chunkModeAtOptions = Options::get().chunkMode; SettingsMenu::open(); }
                else if (pb == PauseScreen::BTN_SAVE) {
                    // Iniciar guardado seguro a prueba de fallos: bloqueo estricto de entradas
                    saveLocked = true;
                    pauseView = 3;
                    int modChunks = chunkManager ? chunkManager->countModifiedChunks() : 0;
                    AsyncSaveManager::startSaveSession(modChunks + 5);
                    PauseScreen::showSavingProgress(AsyncSaveManager::getProgressPercent(), AsyncSaveManager::getCompletedTasks(), AsyncSaveManager::getTotalTasks());
                    saveRequested = true; // ejecuta la serializacion en este frame
                }
                else if (pb == PauseScreen::BTN_QUIT) quitRequested = true;
            } else if (paused && pauseView == 2) {
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
                    saveLocked = false;
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
text = text.replace(old_pause_handling, new_pause_handling)

# 4. Target FPS in rendering loop
old_render_pacing = """        frameCounter++;
        renderFrameCounter++;
        bool shouldRender = (renderFrameCounter % 3) == 0;"""

new_render_pacing = """        frameCounter++;
        renderFrameCounter++;
        // Target de FPS configurable: Perfil Fluidez (60 FPS) vs Distancia/Estandar (30 FPS)
        const bool is60Fps = isDSiMode() && (Options::get().dsiPerformanceProfile == 1);
        const int renderInterval = is60Fps ? 1 : 2; // 60 FPS = cada frame; 30 FPS = cada 2 frames
        bool shouldRender = (renderFrameCounter % renderInterval) == 0;"""
text = text.replace(old_render_pacing, new_render_pacing)

with open('source/main.cpp', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated source/main.cpp successfully')

