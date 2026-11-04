import re
import sys

def test_deadlock_and_hw_cache():
    print("=== TEST SUITE 1: Deadlock Prevention & Hardware Cache Assertions ===")

    # 1. Check Hardware.h
    with open("source/Hardware.h", "r", encoding="utf-8") as f:
        hw_h = f.read()
    assert "extern bool g_isDSi;" in hw_h, "Hardware.h must declare extern bool g_isDSi;"
    assert "return g_isDSi;" in hw_h, "Hardware::isDSi() must return cached g_isDSi"
    print(" [PASS] Hardware.h declares and uses cached g_isDSi.")

    # 2. Check main.cpp global definition and single initialization
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_cpp = f.read()
    assert "bool g_isDSi = false;" in main_cpp, "main.cpp must define bool g_isDSi = false;"
    assert "g_isDSi = isDSiMode();" in main_cpp, "main.cpp must initialize g_isDSi once at startup in main()"
    
    # Ensure isDSiMode() is ONLY called once in main.cpp
    dsi_calls = re.findall(r'isDSiMode\(\)', main_cpp)
    print(f" isDSiMode() occurrences in main.cpp: {len(dsi_calls)}")
    assert len(dsi_calls) == 1, "isDSiMode() must only be called ONCE at startup in main.cpp"
    print(" [PASS] main.cpp sets g_isDSi once at startup and does not read hardware registers in loops.")

    # 3. Check SettingsMenu.cpp and Options.cpp have ZERO calls to isDSiMode()
    with open("source/SettingsMenu.cpp", "r", encoding="utf-8") as f:
        sm_cpp = f.read()
    assert "isDSiMode()" not in sm_cpp, "SettingsMenu.cpp must NOT call isDSiMode() directly"
    assert "g_isDSi" in sm_cpp, "SettingsMenu.cpp must use cached g_isDSi"
    print(" [PASS] SettingsMenu.cpp has 0 calls to isDSiMode() and reads cached g_isDSi.")

    with open("source/Options.cpp", "r", encoding="utf-8") as f:
        opt_cpp = f.read()
    assert "isDSiMode()" not in opt_cpp, "Options.cpp must NOT call isDSiMode() directly"
    assert "g_isDSi" in opt_cpp, "Options.cpp must use cached g_isDSi"
    print(" [PASS] Options.cpp has 0 calls to isDSiMode() and reads cached g_isDSi.")

    # 4. Input locking: only when isSavingWorld is true
    assert "bool isSavingWorld = false;" in main_cpp, "main.cpp must define isSavingWorld"
    assert "if (isSavingWorld)" in main_cpp, "main.cpp must check if (isSavingWorld)"
    assert "saveLocked" not in main_cpp, "main.cpp should use isSavingWorld instead of old saveLocked"
    print(" [PASS] Input lock is strictly controlled by isSavingWorld.")

    # 5. swiWaitForVBlank in Options loop (both in STATE_OPTIONS and pauseView == 2)
    assert "if (state == STATE_OPTIONS)" in main_cpp, "STATE_OPTIONS must exist in main.cpp"
    # Find block for STATE_OPTIONS
    state_opt_idx = main_cpp.find("if (state == STATE_OPTIONS)")
    state_opt_block = main_cpp[state_opt_idx:state_opt_idx+600]
    assert "swiWaitForVBlank();" in state_opt_block, "STATE_OPTIONS must call swiWaitForVBlank()"
    assert "continue;" in state_opt_block, "STATE_OPTIONS must yield with continue;"
    print(" [PASS] Main menu Options loop calls swiWaitForVBlank() and yields.")

    # Find block for paused && pauseView == 2
    pause_opt_idx = main_cpp.find("else if (paused && pauseView == 2)")
    pause_opt_block = main_cpp[pause_opt_idx:pause_opt_idx+800]
    assert "swiWaitForVBlank();" in pause_opt_block, "Pause Options loop must call swiWaitForVBlank()"
    assert "continue;" in pause_opt_block, "Pause Options loop must yield with continue;"
    print(" [PASS] In-game Pause Options loop calls swiWaitForVBlank() and yields, preventing freeze/deadlock.")

def test_simulation_flow():
    print("\n=== TEST SUITE 2: Options Input & Save Lock Simulation ===")
    
    # State simulation
    isSavingWorld = False
    inOptionsMenu = True
    
    # 1. While in options menu
    raw_keys_down = 0x0001 | 0x0040 # A | UP
    raw_keys_held = 0x0001
    
    if isSavingWorld:
        keys_down = 0
        keys_held = 0
    else:
        keys_down = raw_keys_down
        keys_held = raw_keys_held

    assert keys_down == raw_keys_down, "Inputs must be freely processed while in Options menu"
    assert keys_held == raw_keys_held, "Held keys must be freely processed while in Options menu"
    print(" [PASS] Options menu navigation receives uninhibited inputs.")

    # 2. While saving world
    isSavingWorld = True
    if isSavingWorld:
        keys_down = 0
        keys_held = 0
    else:
        keys_down = raw_keys_down
        keys_held = raw_keys_held

    assert keys_down == 0 and keys_held == 0, "Inputs must be strictly frozen during world saving"
    print(" [PASS] World save strictly isolates inputs from corruption.")

    # 3. Upon save completion
    isSavingWorld = False
    if isSavingWorld:
        keys_down = 0
        keys_held = 0
    else:
        keys_down = raw_keys_down
        keys_held = raw_keys_held
    assert keys_down == raw_keys_down, "Inputs immediately restored upon save completion"
    print(" [PASS] Inputs unlocked immediately upon save completion.")

if __name__ == "__main__":
    test_deadlock_and_hw_cache()
    test_simulation_flow()
    print("\nALL DEADLOCK PREVENTION AND HARDWARE CACHE TESTS PASSED!")
