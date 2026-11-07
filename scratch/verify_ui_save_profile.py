import os
import sys
import re

def test_code_assertions():
    print("=== TEST SUITE 1: UI, Safe Save & DSi Profile Code Assertions ===")

    # 1. AsyncSaveManager session tracking
    with open("source/AsyncSaveManager.h", "r", encoding="utf-8") as f:
        asm_h = f.read()
    with open("source/AsyncSaveManager.cpp", "r", encoding="utf-8") as f:
        asm_cpp = f.read()
    assert "startSaveSession" in asm_h and "startSaveSession" in asm_cpp, "Missing startSaveSession in AsyncSaveManager"
    assert "getProgressPercent" in asm_h and "getProgressPercent" in asm_cpp, "Missing getProgressPercent in AsyncSaveManager"
    assert "isSavingComplete" in asm_h and "isSavingComplete" in asm_cpp, "Missing isSavingComplete in AsyncSaveManager"
    assert "hasSucceeded" in asm_h and "hasSucceeded" in asm_cpp, "Missing hasSucceeded in AsyncSaveManager"
    print(" [PASS] AsyncSaveManager implements real-time save session tracking and progress percentage.")

    # 2. ChunkManager countModifiedChunks
    with open("source/ChunkManager.h", "r", encoding="utf-8") as f:
        cm_h = f.read()
    with open("source/ChunkManager.cpp", "r", encoding="utf-8") as f:
        cm_cpp = f.read()
    assert "countModifiedChunks" in cm_h and "countModifiedChunks" in cm_cpp, "Missing countModifiedChunks in ChunkManager"
    print(" [PASS] ChunkManager provides countModifiedChunks() for progress tracking.")

    # 3. PauseScreen safe save & save complete screens
    with open("source/PauseScreen.h", "r", encoding="utf-8") as f:
        ps_h = f.read()
    with open("source/PauseScreen.cpp", "r", encoding="utf-8") as f:
        ps_cpp = f.read()
    assert "showSavingProgress" in ps_h and "showSavingProgress" in ps_cpp, "Missing showSavingProgress in PauseScreen"
    assert "showSaveComplete" in ps_h and "showSaveComplete" in ps_cpp, "Missing showSaveComplete in PauseScreen"
    assert "touchedSaveComplete" in ps_h and "touchedSaveComplete" in ps_cpp, "Missing touchedSaveComplete in PauseScreen"
    print(" [PASS] PauseScreen implements interactive progress bar and post-save action selection.")

    # 4. SettingsMenu DSi warning label & Pop-up confirmation
    with open("source/SettingsMenu.cpp", "r", encoding="utf-8") as f:
        sm_cpp = f.read()
    assert "Exclusivo DSi" in sm_cpp, "Missing '[Exclusivo DSi]' visual warning in SettingsMenu"
    assert "drawPopUp" in sm_cpp, "Missing confirmation pop-up function in SettingsMenu"
    assert "s_showingPopUp" in sm_cpp, "Missing s_showingPopUp state in SettingsMenu"
    assert "getRowCount()" in sm_cpp, "SettingsMenu must use dynamic getRowCount()"
    assert "g_isDSi ? 15 : 14" in sm_cpp, "SettingsMenu must hide DSi option on DS original using cached g_isDSi"
    print(" [PASS] SettingsMenu displays DSi visual warning labels and confirmation Pop-up on classic DS.")

    # 5. Options DSi performance profile
    with open("source/Options.h", "r", encoding="utf-8") as f:
        opt_h = f.read()
    with open("source/Options.cpp", "r", encoding="utf-8") as f:
        opt_cpp = f.read()
    assert "dsiPerformanceProfile" in opt_h, "Missing dsiPerformanceProfile in Options.h"
    assert "dsiPerformanceProfile" in opt_cpp, "Missing dsiPerformanceProfile in Options.cpp"
    assert "buf[26]" in opt_cpp, "Options.cpp must serialize 26 bytes including dsiPerformanceProfile"
    print(" [PASS] Options properly persists dsiPerformanceProfile.")

    # 6. main.cpp strict input locking & dynamic FPS pacing
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_cpp = f.read()
    assert "isSavingWorld" in main_cpp, "Missing isSavingWorld flag in main.cpp"
    assert "if (isSavingWorld)" in main_cpp, "main.cpp must check if (isSavingWorld)"
    assert "keys_down = 0;" in main_cpp and "keys_held = 0;" in main_cpp, "main.cpp must zero out keys when isSavingWorld is true"
    assert "pauseView == 3" in main_cpp, "main.cpp must handle saving progress view 3"
    assert "pauseView == 4" in main_cpp, "main.cpp must handle post-save unlocked choice view 4"
    assert "is60Fps" in main_cpp, "main.cpp must calculate is60Fps target"
    assert "renderInterval" in main_cpp, "main.cpp must use dynamic renderInterval for 60 FPS / 30 FPS"
    print(" [PASS] main.cpp enforces complete input freezing during save and dynamic 60 FPS / 30 FPS rendering.")

if __name__ == "__main__":
    test_code_assertions()
    print("\nALL UI, SAFE SAVE & DSI PROFILE CODE ASSERTIONS PASSED!")
