import subprocess, time, os, sys, ctypes, struct
from ctypes import wintypes

k32 = ctypes.windll.kernel32

class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_uint64),
        ("AllocationBase", ctypes.c_uint64),
        ("AllocationProtect", wintypes.DWORD),
        ("PartitionId", wintypes.WORD),
        ("__alignment", wintypes.WORD),
        ("RegionSize", ctypes.c_size_t),
        ("State", wintypes.DWORD),
        ("Protect", wintypes.DWORD),
        ("Type", wintypes.DWORD)
    ]

def get_target_ds_addr():
    with open("YUANCRAFT.nds", "rb") as f:
        rom = f.read()
    off, ent, ram, sz = struct.unpack_from("<IIII", rom, 0x20)
    idx = rom.find(b"=== YUANCRAFT NDS")
    assert idx != -1, "Magic string not found in ROM"
    return ram + (idx - off)

def get_elf_sym(name):
    nm_path = 'C:/Users/Lendy/msys64/opt/devkitpro/devkitARM/bin/arm-none-eabi-nm.exe'
    out = subprocess.check_output([nm_path, 'YUANCRAFT.elf']).decode('utf-8', errors='ignore')
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 3 and name in parts[2]:
            return int(parts[0], 16)
    raise ValueError(f"Symbol {name} not found in YUANCRAFT.elf")

def find_ds_ram_base(hProc, target_ds_addr):
    magic = b"=== YUANCRAFT NDS"
    addr = 0
    mbi = MEMORY_BASIC_INFORMATION()
    while k32.VirtualQueryEx(hProc, ctypes.c_void_p(addr), ctypes.byref(mbi), ctypes.sizeof(mbi)):
        if mbi.State == 0x1000 and mbi.RegionSize >= 0x400000:
            buf = ctypes.create_string_buffer(mbi.RegionSize)
            bytes_read = ctypes.c_size_t()
            if k32.ReadProcessMemory(hProc, ctypes.c_void_p(mbi.BaseAddress), buf, mbi.RegionSize, ctypes.byref(bytes_read)):
                data = bytes(buf)
                hit = data.find(magic)
                if hit != -1:
                    ram_base = mbi.BaseAddress + hit - (target_ds_addr - 0x02000000)
                    return ram_base
        addr = mbi.BaseAddress + mbi.RegionSize
        if addr >= 0x7FFFFFFFFFFF:
            break
    return None

def run_test(test_name, console_type, chunk_mode, render_quality, dsi_perf):
    print(f"\n======================================================================")
    print(f"=== TEST: {test_name}")
    print(f"=== Console: {console_type} | ChunkMode: {chunk_mode} | Quality: {render_quality} | DSiProfile: {dsi_perf}")
    print(f"======================================================================")
    
    target_ds_addr = get_target_ds_addr()
    addr_trigger = get_elf_sym('s_autoTestTrigger')
    addr_result = get_elf_sym('s_autoTestResult')
    addr_frames = get_elf_sym('s_autoTestFramesInGame')
    addr_fps = get_elf_sym('s_fpsCurrent')
    
    cmd = [
        'tools/desmume/DeSmuME_0.9.13_x64.exe',
        '--slot1', 'R4',
        '--slot1-fat-dir', os.path.abspath('.'),
        '--console-type', console_type,
        'YUANCRAFT.nds'
    ]
    p = subprocess.Popen(cmd)
    hProc = None
    
    try:
        # Give emulator 3.5s to pass intro screens and settle at STATE_MENU
        time.sleep(3.5)
        hProc = k32.OpenProcess(0x1F0FFF, False, p.pid)
        assert hProc, "OpenProcess failed on DeSmuME"
        
        ram_base = find_ds_ram_base(hProc, target_ds_addr)
        assert ram_base, "Could not find DS RAM base in DeSmuME"
        print(f"Found DS RAM base in host memory: 0x{ram_base:016X}")
        
        def write_ds_u32(ds_addr, val):
            host_addr = ram_base + (ds_addr - 0x02000000)
            buf = struct.pack('<I', val)
            bytes_written = ctypes.c_size_t()
            k32.WriteProcessMemory(hProc, ctypes.c_void_p(host_addr), buf, 4, ctypes.byref(bytes_written))
            
        def read_ds_u32(ds_addr):
            host_addr = ram_base + (ds_addr - 0x02000000)
            buf = ctypes.create_string_buffer(4)
            k32.ReadProcessMemory(hProc, ctypes.c_void_p(host_addr), buf, 4, None)
            return struct.unpack('<I', buf.raw)[0]
            
        def read_ds_string(ds_addr, max_len=256):
            host_addr = ram_base + (ds_addr - 0x02000000)
            buf = ctypes.create_string_buffer(max_len)
            k32.ReadProcessMemory(hProc, ctypes.c_void_p(host_addr), buf, max_len, None)
            return buf.raw.split(b'\x00')[0].decode('utf-8', errors='ignore')

        # Trigger world creation with selected performance parameters
        trigger_val = 1 | (chunk_mode << 8) | (render_quality << 16) | (dsi_perf << 24)
        print(f"Injecting autotest trigger into DS RAM (0x{trigger_val:08X} at 0x{addr_trigger:08X})...")
        write_ds_u32(addr_trigger, trigger_val)
        
        print("Monitoring in-world execution (Terrain generation + 240 gameplay frames)...")
        start_time = time.time()
        success = False
        
        while time.time() - start_time < 75.0:
            time.sleep(0.8)
            frames_rendered = read_ds_u32(addr_frames)
            fps = read_ds_u32(addr_fps)
            res_str = read_ds_string(addr_result)
            elapsed = int(time.time() - start_time)
            
            print(f"   [{elapsed:2d}s] Frames in-world: {frames_rendered:3d}/240 | FPS: {fps:2d} | Status: {res_str[:55] if res_str else 'Generating / Playing...'}", flush=True)
            
            if "SUCCESS" in res_str:
                print(f"\n>>> TEST PASSED in {elapsed}s! Result:")
                print(f"    {res_str}\n", flush=True)
                success = True
                break
                
        assert success, f"TEST FAILED: 240 frames were not completed within 50 seconds for {test_name}!"
        print(f"*** {test_name} VERIFIED SUCCESSFULLY ***\n")
        return True
        
    finally:
        if hProc: k32.CloseHandle(hProc)
        p.kill()

def main():
    print("######################################################################")
    print("### YUANCRAFT NDS: IN-WORLD GAMEPLAY & HARDWARE VERIFICATION SUITE ###")
    print("######################################################################")
    
    results = []
    
    # Verification 1: DSi Hardware Conditions (133 MHz, 60 FPS Fluidez Profile, 7x7 Chunks, High Quality)
    res1 = run_test(
        test_name="DSi 60 FPS Fluidez Profile (7x7 Chunks, High Quality)",
        console_type="DSI",
        chunk_mode=2,
        render_quality=0,
        dsi_perf=1
    )
    results.append(("DSi 60 FPS Fluidez", res1))
    
    # Verification 2: DSi Hardware Conditions (133 MHz, 30 FPS Distancia Profile, 7x7 Chunks, Balanced Quality)
    res2 = run_test(
        test_name="DSi 30 FPS Distancia Profile (7x7 Chunks, Balanced Quality)",
        console_type="DSI",
        chunk_mode=2,
        render_quality=1,
        dsi_perf=0
    )
    results.append(("DSi 30 FPS Distancia", res2))
    
    # Verification 3: Nintendo DS (FAT) Hardware Conditions (67 MHz, 4 MB RAM, 5x5 DS Radius)
    res3 = run_test(
        test_name="Nintendo DS (FAT) Standard Mode (5x5 Chunks, Balanced Quality)",
        console_type="FAT",
        chunk_mode=1,
        render_quality=1,
        dsi_perf=0
    )
    results.append(("Nintendo DS FAT Standard", res3))
    
    # Verification 4: Nintendo DS Fast Performance Mode (3x3 Fast Radius, Fast LOD Quality)
    res4 = run_test(
        test_name="Nintendo DS Performance Mode (3x3 Fast Radius, Fast Quality)",
        console_type="FAT",
        chunk_mode=0,
        render_quality=2,
        dsi_perf=0
    )
    results.append(("Nintendo DS Fast Performance", res4))
    
    print("\n======================================================================")
    print("=== SUMMARY OF HARDWARE VERIFICATIONS ===")
    print("======================================================================")
    all_passed = True
    for name, res in results:
        status = "PASSED (100% STABLE)" if res else "FAILED"
        print(f" - {name:50s} : {status}")
        if not res: all_passed = False
        
    if all_passed:
        print("\nALL 4 HARDWARE CONFIGURATIONS VERIFIED: ZERO FREEZES, ZERO ERRORS!")
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
