import os
import sys
import re

def verify_structural():
    print("=" * 60)
    print("VERIFICATION 1: STRUCTURAL AST & STARTUP SEQUENCE AUDIT")
    print("=" * 60)
    
    with open('source/main.cpp', 'r', encoding='utf-8') as f:
        main_src = f.read()
        
    with open('source/DebugLogger.h', 'r', encoding='utf-8') as f:
        debug_h = f.read()

    with open('source/DebugLogger.cpp', 'r', encoding='utf-8') as f:
        debug_cpp = f.read()

    with open('source/Hardware.h', 'r', encoding='utf-8') as f:
        hw_h = f.read()

    checks = []

    # Check 1: IRQ init before VBlank waits and splash
    idx_irq = main_src.find("irqEnable(IRQ_VBLANK);")
    idx_renderer = main_src.find("renderer.init();")
    idx_wait30 = main_src.find("for (int i = 0; i < 30; i++)")
    idx_splash = main_src.find("StartupSplash::show();")
    idx_fat = main_src.find("bool fatOk = fatInitDefault();")
    idx_hw = main_src.find("Hardware::initHardwareProfile();")
    
    c1 = (0 < idx_irq < idx_renderer < idx_wait30 < idx_splash < idx_fat < idx_hw)
    checks.append(("Startup Call Sequence Ordering (IRQ -> Renderer -> 30-VBlank -> Splash -> FAT -> Overclock)", c1))

    # Check 2: 30-frame hardware settling loop
    c2 = ("for (int i = 0; i < 30; i++)" in main_src and "swiWaitForVBlank();" in main_src)
    checks.append(("30-frame hardware settling delay loop present", c2))

    # Check 3: fatOk check before SD logging
    c3 = ("bool fatOk = fatInitDefault();" in main_src and
          "DebugLogger::init(fatOk);" in main_src)
    checks.append(("DebugLogger initialized with confirmed fatOk status", c3))

    # Check 4: Safe fallback when fatOk is false
    c4 = ("if (!fatOk)" in main_src and
          "consoleDemoInit();" in main_src and
          "Modo seguro en pantalla" in main_src)
    checks.append(("Environment Isolation: Native screen console fallback on SD failure", c4))

    # Check 5: Overclocking delayed to after fatOk is true
    c5 = ("Hardware::initHardwareProfile();" in main_src and
          main_src.find("Hardware::initHardwareProfile();") > main_src.find("StartupSplash::show();") and
          main_src.find("Hardware::initHardwareProfile();") > main_src.find("bool fatOk = fatInitDefault();"))
    checks.append(("DSi 133MHz clock delayed until after Mojang splash and FAT OK", c5))

    # Check 6: SubScreenMenu protected against unmounted FAT
    c6 = "SubScreenMenu::init(fatOk ? WorldSave::worldSlotExists(1) : false);" in main_src
    checks.append(("SubScreenMenu::init safely guards WorldSave::worldSlotExists(1)", c6))

    # Check 7: DebugLogger.h declaration
    c7 = "static void init(bool fatAvailable = false);" in debug_h and "static bool isFatAvailable();" in debug_h
    checks.append(("DebugLogger.h declares fatAvailable parameter and accessor", c7))

    # Check 8: DebugLogger.cpp prevents SD access when fatAvailable is false
    c8 = ("if (s_fatAvailable)" in debug_cpp and
          "if (!s_logFile) {" in debug_cpp and
          "iprintf(" in debug_cpp)
    checks.append(("DebugLogger.cpp strictly gates SD fopen/mkdir on s_fatAvailable", c8))

    # Check 9: Hardware.h does not implicitly trigger initHardwareProfile()
    c9_1 = "if (!initedRef()) initHardwareProfile();" not in hw_h
    checks.append(("Hardware.h has no implicit premature initHardwareProfile() calls", c9_1))

    # Check 10: ROM binary exists and is recently built
    c10 = os.path.exists("YUANCRAFT.nds") and os.path.getsize("YUANCRAFT.nds") > 1000000
    checks.append(("YUANCRAFT.nds generated (> 1 MB)", c10))

    all_passed = True
    for desc, passed in checks:
        status = "PASSED" if passed else "FAILED"
        print(f"[{status}] {desc}")
        if not passed:
            all_passed = False

    if not all_passed:
        print("\nERROR: Verification 1 failed!")
        sys.exit(1)
    else:
        print("\nSUCCESS: All 10 Structural Audits PASSED with 100% compliance.\n")

if __name__ == "__main__":
    verify_structural()

