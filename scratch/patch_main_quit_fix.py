with open("source/main.cpp", "r", encoding="utf-8") as f:
    main_src = f.read()

# 1. In closePause: ensure isSavingWorld is false
old_close_pause = """            auto closePause = [&]() {
                paused = false; pauseView = 0;
                if (consoleVisible) { consoleDemoInit(); }"""

new_close_pause = """            auto closePause = [&]() {
                paused = false; pauseView = 0;
                isSavingWorld = false;
                if (consoleVisible) { consoleDemoInit(); }"""

assert old_close_pause in main_src, "old_close_pause not found"
main_src = main_src.replace(old_close_pause, new_close_pause)

# 2. In quitRequested || titleMenuRequested: remove delete player; and reset DTCM pointers and managers
old_quit_block = """        if (quitRequested || titleMenuRequested) {
            quitRequested = false; paused = false; pauseView = 0;
            Prof::flushSpikes();   // se guardan los picos anotados antes de salir
            state = STATE_MENU;

            WorldSave::endSession();

            AsyncSaveManager::flushAll();
        delete chunkManager;
            delete player;
            delete inventory;
            chunkManager = nullptr;
            player = nullptr;
            inventory = nullptr;

            SubScreenMenu::init(WorldSave::worldSlotExists(1));
            TopScreenMenu::init();

            continue;
        }"""

new_quit_block = """        if (quitRequested || titleMenuRequested) {
            quitRequested = false; paused = false; pauseView = 0;
            isSavingWorld = false;
            Prof::flushSpikes();   // se guardan los picos anotados antes de salir
            state = STATE_MENU;

            WorldSave::endSession();

            AsyncSaveManager::flushAll();
            AsyncSaveManager::resetSaveSession();
            delete chunkManager;
            // s_dtcmPlayer resides in DTCM static memory: must NOT call delete player!
            delete inventory;
            chunkManager = nullptr;
            player = nullptr;
            inventory = nullptr;
            s_dtcmCurrentChunk = nullptr;
            for (int i = 0; i < 9; i++) s_dtcmActiveChunks[i] = nullptr;
            GameplayHotbar::invalidate();

            Furnace::clearAll();
            ChestStore::clearAll();
            MinecartManager::clear();
            BoatManager::clear(); Maps::reset(); Weather::reset(); Spawners::clear(); Clouds::reset(); Particles::clear();
            PaintingManager::clear();
            SignManager::clear();
            HostileManager::clearWolves();
            TntManager::clear();
            Projectiles::clear(); FishingHook::clear();
            Dispenser::clearQueue();
            NoteBlocks::clearAll();

            SubScreenMenu::init(WorldSave::worldSlotExists(1));
            TopScreenMenu::init();

            continue;
        }"""

assert old_quit_block in main_src, "old_quit_block not found"
main_src = main_src.replace(old_quit_block, new_quit_block)

with open("source/main.cpp", "w", encoding="utf-8", newline="\n") as f:
    f.write(main_src)

print("source/main.cpp patched successfully!")

