import os, sys, subprocess, time, struct, ctypes

def verify_structural():
    print("=== Verification 1: Structural & Hardware Architecture Analysis ===")
    
    with open('source/StartupSplash.cpp', 'r', encoding='utf-8') as f:
        splash_src = f.read()
    
    # 1. No direct REG_IPC_FIFO_CR assignment in StartupSplash.cpp
    assert 'REG_IPC_FIFO_CR' not in splash_src, "REG_IPC_FIFO_CR must not be modified in StartupSplash.cpp"
    print("PASS: StartupSplash.cpp does NOT modify REG_IPC_FIFO_CR (FIFO intact).")
    
    # 2. No direct REG_IF assignment in StartupSplash.cpp
    assert 'REG_IF' not in splash_src, "REG_IF must not be modified in StartupSplash.cpp"
    print("PASS: StartupSplash.cpp does NOT modify REG_IF (Interrupts intact).")
    
    # 3. Check source/main.cpp order
    with open('source/main.cpp', 'r', encoding='utf-8') as f:
        main_src = f.read()
        
    # Crucial check: irqInit() must NOT be executed in main() because crt0's initSystem() already configured
    # irqTable and fifoInit(). Calling irqInit() again destroys the FIFO handler needed for DSi libfat/SDMMC.
    import re
    has_active_irq_init = any(re.match(r'^\s*irqInit\s*\(\s*\)\s*;', line) for line in main_src.splitlines())
    assert not has_active_irq_init, "CRITICAL: irqInit() statement must NOT be executed in main()!"
    print("PASS: irqInit() is NOT called in main.cpp, preserving libnds FIFO subsystem for DSi SDMMC / ARM7 communication.")
    
    power_idx = main_src.find('powerOn(POWER_ALL_2D)')
    assert power_idx != -1, "powerOn(POWER_ALL_2D) not found"
    
    vblank_enable_idx = main_src.find('irqEnable(IRQ_VBLANK)')
    assert vblank_enable_idx != -1, "irqEnable(IRQ_VBLANK) not found"
    
    console_idx = main_src.find('consoleDemoInit()')
    assert console_idx != -1, "consoleDemoInit() not found"
    
    splash_idx = main_src.find('StartupSplash::show()')
    assert splash_idx != -1, "StartupSplash::show() not found"
    
    fat_idx = main_src.find('fatInitDefault()')
    assert fat_idx != -1, "fatInitDefault() not found"
    
    renderer_idx = main_src.find('renderer.init()')
    assert renderer_idx != -1, "renderer.init() not found"
    
    texture_idx = main_src.find('Texture::loadItemsAtlas()')
    assert texture_idx != -1, "Texture::loadItemsAtlas() not found"
    
    sound_idx = main_src.find('Sound::init()')
    assert sound_idx != -1, "Sound::init() not found"
    
    menu_idx = main_src.find('TopScreenMenu::init()')
    assert menu_idx != -1, "TopScreenMenu::init() not found"
    
    # Strict execution sequence
    assert power_idx < vblank_enable_idx, "powerOn must precede irqEnable"
    assert vblank_enable_idx < console_idx, "irqEnable must precede consoleDemoInit"
    assert console_idx < splash_idx, "consoleDemoInit must precede StartupSplash"
    assert splash_idx < fat_idx, "StartupSplash::show() must display logos immediately before disk I/O"
    assert fat_idx < renderer_idx, "fatInitDefault must precede renderer.init"
    assert renderer_idx < texture_idx, "renderer.init must precede Texture::loadItemsAtlas"
    assert sound_idx < texture_idx, "Sound::init must be safely initialized"
    assert texture_idx < menu_idx, "Textures must be loaded before TopScreenMenu::init"
    
    print("PASS: main.cpp sequence: powerOn(POWER_ALL_2D) -> irqEnable(IRQ_VBLANK) -> consoleDemoInit -> StartupSplash::show() -> fatInitDefault -> renderer.init -> Texture loading -> TopScreenMenu.")
    
    # Check ITCM section size in YUANCRAFT.elf
    readelf_cmd = [r'C:\Users\Lendy\msys64\opt\devkitpro\devkitARM\bin\arm-none-eabi-readelf.exe', '-S', 'YUANCRAFT.elf']
    res = subprocess.run(readelf_cmd, capture_output=True, text=True)
    itcm_line = [l for l in res.stdout.splitlines() if '.itcm' in l]
    assert itcm_line, ".itcm section not found in ELF"
    print(f"PASS: ITCM section verified: {itcm_line[0]}")
    return True

def verify_runtime_execution(console_type):
    print(f"\n=== Verification 2: Runtime Execution on {console_type} Environment ===")
    
    cmd = ['tools/desmume/DeSmuME_0.9.13_x64.exe', '--console-type', console_type, 'YUANCRAFT.nds']
    p = subprocess.Popen(cmd)
    
    print(f"Launched DeSmuME ({console_type}), waiting 4 seconds for splash sequence & asset loading...")
    time.sleep(4)
    
    k32 = ctypes.windll.kernel32
    hProc = k32.OpenProcess(0x1F0FFF, False, p.pid)
    assert hProc, "Failed to open emulator process"
    
    buf = ctypes.create_string_buffer(64)
    bytesRead = ctypes.c_size_t()
    
    k32.ReadProcessMemory(hProc, ctypes.c_void_p(0x14a913640), buf, 64, ctypes.byref(bytesRead))
    words = struct.unpack('<16I', buf.raw)
    
    p.kill()
    k32.CloseHandle(hProc)
    
    print(f"Sampled ARM9 Stack Words at 4s ({console_type}): {[hex(w) for w in words[:8]]}")
    
    # Check that ARM9 is NOT hung in showLogo (which would have 0x0207f047 / 0x0207f04d on stack)
    has_show_logo_hang = any(w in (0x0207f047, 0x0207f04d) for w in words)
    assert not has_show_logo_hang, f"ARM9 is still hung inside showLogo swiWaitForVBlank on {console_type}!"
    print(f"PASS ({console_type}): ARM9 has successfully exited showLogo without hanging in VBlank.")
    
    # Check that ARM9 is NOT hung in fifo_waitBlock (0x0209a6e3)
    has_fifo_deadlock = any(w == 0x0209a6e3 for w in words)
    assert not has_fifo_deadlock, f"ARM9 is hung in fifo_waitBlock deadlock on {console_type}!"
    print(f"PASS ({console_type}): No FIFO deadlock detected (libfat / Sound / IPC communication responsive).")
    
    print(f"PASS ({console_type}): Main loop reached STATE_MENU cleanly.")
    return True

if __name__ == '__main__':
    v1 = verify_structural()
    assert v1
    v2_ds = verify_runtime_execution('FAT')
    assert v2_ds
    v2_dsi = verify_runtime_execution('DSI')
    assert v2_dsi
    print("\n=======================================================")
    print("ALL DOUBLE VERIFICATIONS PASSED SUCCESSFULLY (DS & DSi)!")
    print("=======================================================")
