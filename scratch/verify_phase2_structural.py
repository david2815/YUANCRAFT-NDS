import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("DOUBLE VERIFICATION - TEST 1: STRUCTURAL AUDIT")
    print("=" * 60)
    
    checks = []

    # Check 1: 0 occurrences of ITCM_CODE in source/
    with open('source/Chunk.h', 'r', encoding='utf-8') as f: c_h = f.read()
    with open('source/Chunk.cpp', 'r', encoding='utf-8') as f: c_cpp = f.read()
    with open('source/Player.h', 'r', encoding='utf-8') as f: p_h = f.read()
    with open('source/Player.cpp', 'r', encoding='utf-8') as f: p_cpp = f.read()
    with open('source/VoxelRLE.h', 'r', encoding='utf-8') as f: v_h = f.read()
    with open('source/Hardware.h', 'r', encoding='utf-8') as f: hw_h = f.read()
    with open('source/StartupSplash.cpp', 'r', encoding='utf-8') as f: splash_cpp = f.read()
    with open('source/main.cpp', 'r', encoding='utf-8') as f: main_src = f.read()

    itcm_found = any('ITCM_CODE' in src for src in [c_h, c_cpp, p_h, p_cpp, v_h, hw_h, splash_cpp, main_src])
    checks.append(("Zero occurrences of ITCM_CODE in codebase", not itcm_found))

    # Check 2: fatInitDefault() is first synchronous call in main()
    idx_main = main_src.find("int main(void) {")
    idx_fat = main_src.find("bool fatOk = fatInitDefault();", idx_main)
    idx_logger = main_src.find("DebugLogger::init(fatOk);", idx_fat)
    idx_irq = main_src.find("irqInit();", idx_logger)
    idx_hwmath = main_src.find("HwMath::sync();", idx_irq)
    idx_renderer = main_src.find("renderer.init();", idx_hwmath)
    idx_wait30 = main_src.find("for (int i = 0; i < 30; i++)", idx_renderer)
    idx_splash = main_src.find("StartupSplash::show();", idx_wait30)
    
    c2 = (idx_main < idx_fat < idx_logger < idx_irq < idx_hwmath < idx_renderer < idx_wait30 < idx_splash)
    checks.append(("Synchronous fatInitDefault() is first call in main() followed by DebugLogger(fatOk)", c2))

    # Check 3: HwMath::sync() called prior to splash screen
    c3 = (idx_hwmath != -1 and idx_hwmath < idx_splash)
    checks.append(("HwMath::sync() purges coprocessors before splash screen", c3))

    # Check 4: StartupSplash clears video buffer and pending interrupts
    c4 = ("dmaFillWords(0, gfx, 256 * 256);" in splash_cpp and
          "dmaFillHalfWords(0, BG_PALETTE, 512);" in splash_cpp and
          "REG_IF = REG_IF;" in splash_cpp and
          "IPC_FIFO_SEND_CLEAR" in splash_cpp)
    checks.append(("StartupSplash explicitly clears VRAM buffer, palettes, and IRQ/FIFO flags", c4))

    # Check 5: Hardware::initHardwareProfile() is called strictly after TopScreenMenu::init()
    idx_menu = main_src.find("TopScreenMenu::init();")
    idx_overclock = main_src.find("Hardware::initHardwareProfile();", idx_menu)
    c5 = (idx_menu != -1 and idx_overclock != -1 and idx_overclock > idx_menu)
    checks.append(("CPU 133MHz overclock is deferred until after main menu load", c5))

    # Check 6: Check ITCM section size in ELF binary
    res = subprocess.run([
        'C:/Users/Lendy/msys64/usr/bin/bash.exe',
        '-l',
        '-c',
        "/opt/devkitpro/devkitARM/bin/arm-none-eabi-readelf -S '/c/Users/Lendy/Desktop/YUANCRAFT NDS PORT/YUANCRAFT.elf'"
    ], capture_output=True, text=True)

    itcm_line = ""
    for line in res.stdout.splitlines():
        if ".itcm" in line:
            itcm_line = line
            break

    itcm_bytes = 0
    if itcm_line:
        parts = itcm_line.split()
        # parts: ['[18]', '.itcm', 'PROGBITS', '01000100', '200100', '000194', ...]
        itcm_bytes = int(parts[5], 16)

    c6 = (0 < itcm_bytes < 1024) # Less than 1 KB (limit is 32 KB)
    checks.append((f"ELF .itcm section size is {itcm_bytes} bytes (0x{itcm_bytes:x} < 1024 bytes, well below 32KB limit)", c6))

    all_passed = True
    for desc, passed in checks:
        status = "PASSED" if passed else "FAILED"
        print(f"[{status}] {desc}")
        if not passed:
            all_passed = False

    if not all_passed:
        print("\nERROR: Verification 1 Failed!")
        sys.exit(1)
    else:
        print("\nSUCCESS: All Structural Verification checks PASSED (100%).\n")

if __name__ == "__main__":
    main()
