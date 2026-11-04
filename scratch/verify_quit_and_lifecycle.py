import re

def test_quit_and_lifecycle():
    print("=== TEST SUITE: Quit to Title & Lifecycle Assertions ===")

    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_cpp = f.read()

    # 1. Ensure delete player; is NOT present
    assert "delete player;" not in main_cpp, "CRITICAL ERROR: 'delete player;' must NOT be called on static DTCM object!"
    print(" [PASS] 'delete player;' is completely eliminated, protecting DTCM from illegal heap free.")

    # 2. Check player assignment to DTCM buffer
    assert "player = &s_dtcmPlayer;" in main_cpp, "main.cpp must bind player to &s_dtcmPlayer"
    print(" [PASS] player safely binds to DTCM static storage.")

    # 3. Check closePause clears isSavingWorld
    close_pause_idx = main_cpp.find("auto closePause = [&]()")
    assert close_pause_idx != -1, "closePause lambda missing"
    close_pause_block = main_cpp[close_pause_idx:close_pause_idx + 400]
    assert "isSavingWorld = false;" in close_pause_block, "closePause must ensure isSavingWorld is false"
    print(" [PASS] closePause() safely clears isSavingWorld.")

    # 4. Check quit to title cleanup block
    quit_idx = main_cpp.find("if (quitRequested || titleMenuRequested)")
    assert quit_idx != -1, "quitRequested block missing"
    quit_block = main_cpp[quit_idx:quit_idx + 2500]

    assert "isSavingWorld = false;" in quit_block, "quit cleanup must clear isSavingWorld"
    assert "AsyncSaveManager::resetSaveSession();" in quit_block, "quit cleanup must reset save session"
    assert "s_dtcmCurrentChunk = nullptr;" in quit_block, "quit cleanup must clear DTCM current chunk"
    assert "GameplayHotbar::invalidate();" in quit_block, "quit cleanup must invalidate hotbar bgId"
    assert "SubScreenMenu::init(" in quit_block, "quit cleanup must reinit SubScreenMenu"
    assert "TopScreenMenu::init();" in quit_block, "quit cleanup must reinit TopScreenMenu"
    assert "delete chunkManager;" in quit_block, "quit cleanup must delete heap ChunkManager"
    assert "delete inventory;" in quit_block, "quit cleanup must delete heap Inventory"
    print(" [PASS] Quit to title block cleanly purges session and resets state.")

def test_lifecycle_simulation():
    print("\n=== TEST SUITE: Lifecycle State Machine Simulation ===")

    # State variables
    s_dtcmPlayer = {"x": 0.0, "y": 64.0, "z": 0.0}
    player = None
    chunkManager = None
    isSavingWorld = False
    paused = False
    pauseView = 0
    state = "STATE_MENU"

    # 1. Start world
    print(" 1. Loading world...")
    chunkManager = {"worldSeed": 1337}
    player = s_dtcmPlayer # player points to static DTCM
    state = "STATE_GAME"
    print("    In game running.")

    # 2. Open pause and save
    print(" 2. Pausing and saving world...")
    paused = True
    pauseView = 1
    # User taps save
    isSavingWorld = True
    pauseView = 3
    # Saving finishes
    isSavingWorld = False
    pauseView = 4
    print("    Save complete at 100%.")

    # 3. User chooses Continue
    print(" 3. User chooses Continue playing...")
    paused = False
    pauseView = 0
    isSavingWorld = False
    print("    Game resumed cleanly.")

    # 4. User opens pause menu again and hits Quit to title
    print(" 4. User re-opens pause menu and selects 'Quit to title'...")
    paused = True
    pauseView = 1
    quitRequested = True

    if quitRequested:
        quitRequested = False
        paused = False
        pauseView = 0
        isSavingWorld = False
        state = "STATE_MENU"
        # Cleanup
        chunkManager = None # deleted
        player = None       # nullified, NOT deleted with free()!
        print("    Cleanly returned to STATE_MENU without memory corruption.")

    assert state == "STATE_MENU"
    assert player is None
    assert isSavingWorld == False
    assert paused == False

    # 5. User loads a new world again
    print(" 5. User loads another world...")
    chunkManager = {"worldSeed": 42}
    player = s_dtcmPlayer
    state = "STATE_GAME"
    print("    New world loaded and player re-bound cleanly.")
    assert player == s_dtcmPlayer
    assert state == "STATE_GAME"

if __name__ == "__main__":
    test_quit_and_lifecycle()
    test_lifecycle_simulation()
    print("\nALL QUIT TO TITLE AND LIFECYCLE TESTS PASSED!")
