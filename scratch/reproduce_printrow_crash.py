import ctypes

def simulate_old_printrow(selected, label, value):
    COLUMNS = 32
    labelLen = len(label)
    valueLen = len(value)
    diff = COLUMNS - 4 - valueLen
    print(f"Old printRow: label='{label}' (len={labelLen}), value='{value}' (len={valueLen})")
    print(f"COLUMNS - 4 - valueLen = 32 - 4 - {valueLen} = {diff}")
    if labelLen > diff:
        labelLen = diff
    print(f"Resulting labelLen = {labelLen}")
    
    # In C++, memcpy takes size_t (unsigned 32-bit int)
    size_t_val = ctypes.c_uint32(labelLen).value
    print(f"Cast to size_t for memcpy: {size_t_val} (0x{size_t_val:08X})")
    dest_offset = COLUMNS - valueLen
    print(f"Dest offset for value memcpy: {dest_offset}")
    if size_t_val > 1000 or dest_offset < 0:
        print("--> FATAL CRASH / MEMORY CORRUPTION CONFIRMED! <--\n")
        return False
    return True

print("=== TESTING OLD printRow WITH VARIOUS OPTIONS ===")
print("1. 'difficulty', 'normal':")
simulate_old_printrow(False, "difficulty", "normal")

print("2. 'chunk mode', 'dsi \\x1b[31m[Exclusivo DSi]\\x1b[39m':")
simulate_old_printrow(False, "chunk mode", "dsi \x1b[31m[Exclusivo DSi]\x1b[39m")

print("3. 'render', 'high \\x1b[33m[Riesgo: Caida FPS]\\x1b[39m':")
simulate_old_printrow(False, "render", "high \x1b[33m[Riesgo: Caida FPS]\x1b[39m")

