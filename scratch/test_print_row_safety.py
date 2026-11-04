import sys

def visual_length(s):
    if not s:
        return 0
    length = 0
    in_esc = False
    for ch in s:
        if ch == '\x1b':
            in_esc = True
        elif in_esc:
            if ch == 'm':
                in_esc = False
        else:
            length += 1
    return length

def print_row_sim(selected, label, value):
    prefix = "-> " if selected else "   "
    if not label or len(label) == 0:
        return f"{prefix}{value}"
    
    label_len = len(label)
    vis_val_len = visual_length(value)
    total_vis = 3 + label_len + vis_val_len
    if total_vis < 32:
        spaces = 32 - 3 - label_len - vis_val_len
        if spaces < 1:
            spaces = 1
        return f"{prefix}{label}{' ' * spaces}{value}"
    else:
        return f"{prefix}{label}:\n   {value}"

def test_all_options(is_dsi):
    print(f"\n=== TESTING SETTINGS MENU OPTIONS (is_dsi={is_dsi}) ===")
    options_rows = []
    
    # 0: back
    options_rows.append(("", "back"))
    # 1: difficulty
    options_rows.append(("difficulty", "normal"))
    # 2: controls
    options_rows.append(("controls", "normal >"))
    # 3: auto jump
    options_rows.append(("auto jump", "on"))
    
    # 4: chunk mode
    for m in [0, 1, 2]:
        val = ["fast", "ds", "dsi"][m]
        if not is_dsi and m == 2:
            val = "dsi \x1b[31m[Exclusivo DSi]\x1b[39m"
        options_rows.append((f"chunk mode (m={m})", val))
        
    # 5: render quality
    for q in [0, 1, 2]:
        val = ["high", "balanced", "fast"][q]
        if not is_dsi and q == 0:
            val = "high \x1b[33m[Riesgo: Caida FPS]\x1b[39m"
        options_rows.append((f"render (q={q})", val))
        
    # 6: default seed
    options_rows.append(("default seed", "random"))
    # 7: custom default seed
    options_rows.append(("custom default seed", "123456789"))
    # 8: clockcompass
    options_rows.append(("clockcompassinvupdate", "true"))
    # 9: debug options
    options_rows.append(("debug options", ">"))
    # 10: particles
    options_rows.append(("particles", "on"))
    # 11: sound
    options_rows.append(("sound", "on"))
    # 12: inventoryMap
    options_rows.append(("inventoryMap", "true"))
    # 13: fps counter
    options_rows.append(("fps counter", "on"))
    
    if is_dsi:
        options_rows.append(("dsi perf profile", "fluid (60fps)"))
        options_rows.append(("dsi perf profile", "distance (30fps)"))

    for label, val in options_rows:
        out = print_row_sim(True, label, val)
        lines = out.split("\n")
        for line in lines:
            vis = visual_length(line)
            print(f"[{vis:2d} cols] {line}")
            assert vis <= 32, f"Line exceeds 32 columns: '{line}' ({vis} cols)"

test_all_options(False)
test_all_options(True)
print("\nALL OPTIONS FIT WITHIN 32 COLUMNS SAFELY!")

