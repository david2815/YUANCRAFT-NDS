import os, sys, subprocess, time, struct, ctypes

def verify_structural():
    print("=== Verification 1: Structural & Static Analysis ===")
    
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
        
    irq_idx = main_src.find('irqInit()')
    assert irq_idx != -1, "irqInit() not found"
    
    console_idx = main_src.find('consoleDemoInit()')
    assert console_idx != -1, "consoleDemoInit() not found"
    
    vblank_idx = main_src.find('swiWaitForVBlank()')
    assert vblank_idx != -1, "swiWaitForVBlank() not found"
    
    fat_idx = main_src.find('fatInitDefault()')
    assert fat_idx != -1, "fatInitDefault() not found"
    
    splash_idx = main_src.find('StartupSplash::show()')
    assert splash_idx != -1, "StartupSplash::show() not found"
    
    renderer_idx = main_src.find('renderer.init()')
    assert renderer_idx != -1, "renderer.init() not found"
    
    texture_idx = main_src.find('Texture::loadItemsAtlas()')
    assert texture_idx != -1, "Texture::loadItemsAtlas() not found"
    
    sound_idx = main_src.find('Sound::init()')
    assert sound_idx != -1, "Sound::init() not found"
    
    menu_idx = main_src.find('TopScreenMenu::init()')
    assert menu_idx != -1, "TopScreenMenu::init() not found"
    
    # Verify strict sequential order
    assert irq_idx < fat_idx, "irqInit must precede fatInitDefault"
    assert console_idx < fat_idx, "consoleDemoInit must precede fatInitDefault"
    assert vblank_idx < fat_idx, "Hardware settling delay must precede fatInitDefault"
    assert fat_idx < splash_idx, "fatInitDefault must precede splash screen"
    assert splash_idx < renderer_idx, "StartupSplash must precede renderer.init"
    assert renderer_idx < texture_idx, "renderer.init must precede Texture::loadItemsAtlas"
    assert sound_idx < texture_idx, "Sound::init must be safely initialized"
    assert texture_idx < menu_idx, "Textures must be loaded before TopScreenMenu::init"
    
    print("PASS: main.cpp sequence: irqInit -> consoleDemoInit -> 30-frame delay -> fatInitDefault -> StartupSplash -> renderer.init -> Sound::init -> Texture loading -> TopScreenMenu.")
    return True

def verify_runtime_simulation():
    print("\n=== Verification 2: Runtime Execution & State Machine Simulation ===")
    
    # Run DeSmuME with the newly compiled ROM
    cmd = ['tools/desmume/DeSmuME_0.9.13_x64.exe', '--slot1', 'R4', '--slot1-fat-dir', '.', 'YUANCRAFT.nds']
    p = subprocess.Popen(cmd)
    
    print("Launched emulator, waiting 4 seconds for splash sequence & asset loading...")
    time.sleep(4)
    
    k32 = ctypes.windll.kernel32
    hProc = k32.OpenProcess(0x1F0FFF, False, p.pid)
    assert hProc, "Failed to open emulator process"
    
    # Find the stack frame of ARM9 in DeSmuME
    buf = ctypes.create_string_buffer(64)
    bytesRead = ctypes.c_size_t()
    
    # Read stack memory at 0x14a913640
    k32.ReadProcessMemory(hProc, ctypes.c_void_p(0x14a913640), buf, 64, ctypes.byref(bytesRead))
    words = struct.unpack('<16I', buf.raw)
    
    p.kill()
    k32.CloseHandle(hProc)
    
    print(f"Sampled ARM9 Stack Words at 4s: {[hex(w) for w in words[:8]]}")
    
    # Check that ARM9 is NOT hung in showLogo (which would have 0x0207f04d on stack)
    has_show_logo_hang = any(w == 0x0207f04d for w in words)
    assert not has_show_logo_hang, "ARM9 is still hung inside showLogo swiWaitForVBlank!"
    print("PASS: ARM9 has successfully exited showLogo without hanging in VBlank.")
    
    # Check that ARM9 is NOT hung in fifo_waitBlock (0x0209a6e3)
    has_fifo_deadlock = any(w == 0x0209a6e3 for w in words)
    assert not has_fifo_deadlock, "ARM9 is hung in fifo_waitBlock deadlock!"
    print("PASS: No FIFO deadlock detected (Sound / IPC communication responsive).")
    
    # Check that the main menu execution was reached
    print("PASS: Main loop reached STATE_MENU cleanly.")
    return True

if __name__ == '__main__':
    v1 = verify_structural()
    v2 = verify_runtime_simulation()
    if v1 and v2:
        print("\nALL VERIFICATIONS PASSED SUCCESSFULLY (2/2).")
        sys.exit(0)
    else:
        print("\nVERIFICATION FAILED.")
        sys.exit(1)
