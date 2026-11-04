# Patch main.cpp
with open("source/main.cpp", "r", encoding="utf-8") as f:
    main_src = f.read()

# 1. Update startSaveSession call
old_start_save = """                    int modChunks = chunkManager ? chunkManager->countModifiedChunks() : 0;
                    AsyncSaveManager::startSaveSession(modChunks + 5);
                    PauseScreen::showSavingProgress(AsyncSaveManager::getProgressPercent(), AsyncSaveManager::getCompletedTasks(), AsyncSaveManager::getTotalTasks());
                    saveRequested = true; // ejecuta la serializacion en este frame"""

new_start_save = """                    int modChunks = chunkManager ? chunkManager->countModifiedChunks() : 0;
                    AsyncSaveManager::startSaveSession(modChunks);
                    consoleDemoInit();
                    PauseScreen::showSavingProgress(AsyncSaveManager::getProgressPercent(), AsyncSaveManager::getCompletedTasks(), AsyncSaveManager::getTotalTasks());
                    saveRequested = true; // ejecuta la serializacion en este frame"""

assert old_start_save in main_src, "old_start_save not found in main.cpp"
main_src = main_src.replace(old_start_save, new_start_save)

# 2. Update saveRequested handling to capture actualSaved and notifyAllEnqueued
old_save_chunk = """            Prof::flushSpikes(); // muerto no se guarda: el mundo debe poder volver a antes de morir
            chunkManager->saveModifiedChunks();"""

new_save_chunk = """            Prof::flushSpikes(); // muerto no se guarda: el mundo debe poder volver a antes de morir
            int actualSaved = chunkManager ? chunkManager->saveModifiedChunks() : 0;"""

assert old_save_chunk in main_src, "old_save_chunk not found in main.cpp"
main_src = main_src.replace(old_save_chunk, new_save_chunk)

old_commit = """            WorldSave::commitSession();
        }"""

new_commit = """            WorldSave::commitSession();
            AsyncSaveManager::notifyAllEnqueued(actualSaved);
        }"""

assert old_commit in main_src, "old_commit not found in main.cpp"
main_src = main_src.replace(old_commit, new_commit)

with open("source/main.cpp", "w", encoding="utf-8", newline="\n") as f:
    f.write(main_src)

print("source/main.cpp updated successfully")

# Patch PauseScreen.cpp
with open("source/PauseScreen.cpp", "r", encoding="utf-8") as f:
    ps_src = f.read()

old_show_prog = """void PauseScreen::showSavingProgress(int percent, int current, int total) {
    consoleDemoInit();
    consoleClear();"""

new_show_prog = """void PauseScreen::showSavingProgress(int percent, int current, int total) {
    consoleClear();"""

assert old_show_prog in ps_src, "old_show_prog not found in PauseScreen.cpp"
ps_src = ps_src.replace(old_show_prog, new_show_prog)

with open("source/PauseScreen.cpp", "w", encoding="utf-8", newline="\n") as f:
    f.write(ps_src)

print("source/PauseScreen.cpp updated successfully")

