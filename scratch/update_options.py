import os

# Update Options.h
h_path = r"source/Options.h"
with open(h_path, "r", encoding="utf-8") as f:
    h_content = f.read()

target_h = "\tbool oldMobSpawnLimit;\n    };"
replacement_h = "\tbool oldMobSpawnLimit;\n        bool showFps;              // contador de FPS en pantalla sin impacto de rendimiento\n    };"

if target_h in h_content:
    h_content = h_content.replace(target_h, replacement_h, 1)
    with open(h_path, "w", encoding="utf-8") as f:
        f.write(h_content)
    print("Options.h updated.")
else:
    print("target_h not found!")

# Update Options.cpp
cpp_path = r"source/Options.cpp"
with open(cpp_path, "r", encoding="utf-8") as f:
    cpp_content = f.read()

target_init = "static Options::Data s_data = { false, 0, 0, false, 0, 0, true, true, true, true, 2, true };"
replacement_init = "static Options::Data s_data = { false, 0, 0, false, 0, 0, true, true, true, true, 2, false, false, false, 0, true, false, false };"

target_load = """    s_data.renderQuality = 0;
    s_data.oldMobSpawnLimit = false;
    FILE* f = fopen(OPTIONS_PATH, "rb");
    if (!f) return;
    unsigned char buf[24];
    size_t n = fread(buf, 1, sizeof(buf), f);"""

replacement_load = """    s_data.renderQuality = 0;
    s_data.oldMobSpawnLimit = false;
    s_data.showFps = false;
    FILE* f = fopen(OPTIONS_PATH, "rb");
    if (!f) return;
    unsigned char buf[25];
    size_t n = fread(buf, 1, sizeof(buf), f);"""

target_load_end = """        if (n >= 24) s_data.oldMobSpawnLimit = (buf[23] == 1);
    }
    fclose(f);"""

replacement_load_end = """        if (n >= 24) s_data.oldMobSpawnLimit = (buf[23] == 1);
        if (n >= 25) s_data.showFps = (buf[24] == 1);
    }
    fclose(f);"""

target_save = """    unsigned char buf[24] = { 'M', 'C', 'O', '1', (unsigned char)(s_data.debugLargeChest ? 1 : 0), s_data.chunkMode,
                              s_data.seedMode, (unsigned char)(s_data.customSeedSet ? 1 : 0),
                              (unsigned char)(s_data.customSeed & 0xFF), (unsigned char)((s_data.customSeed >> 8) & 0xFF),
                              (unsigned char)((s_data.customSeed >> 16) & 0xFF), (unsigned char)((s_data.customSeed >> 24) & 0xFF),
                              s_data.controlMode, (unsigned char)(s_data.autoJump ? 1 : 0), (unsigned char)(s_data.clockCompassInvUpdate ? 1 : 0), (unsigned char)(s_data.particles ? 1 : 0), (unsigned char)(s_data.sound ? 1 : 0), (unsigned char)(s_data.inventoryMap ? 0 : 1), (unsigned char)(s_data.debugScreenOptions ? 1 : 0), s_data.difficulty, s_data.renderQuality, (unsigned char)(s_data.spikeLog ? 1 : 0), (unsigned char)(s_data.debugCoordsOnly ? 1 : 0), (unsigned char)(s_data.oldMobSpawnLimit ? 1 : 0) };"""

replacement_save = """    unsigned char buf[25] = { 'M', 'C', 'O', '1', (unsigned char)(s_data.debugLargeChest ? 1 : 0), s_data.chunkMode,
                              s_data.seedMode, (unsigned char)(s_data.customSeedSet ? 1 : 0),
                              (unsigned char)(s_data.customSeed & 0xFF), (unsigned char)((s_data.customSeed >> 8) & 0xFF),
                              (unsigned char)((s_data.customSeed >> 16) & 0xFF), (unsigned char)((s_data.customSeed >> 24) & 0xFF),
                              s_data.controlMode, (unsigned char)(s_data.autoJump ? 1 : 0), (unsigned char)(s_data.clockCompassInvUpdate ? 1 : 0), (unsigned char)(s_data.particles ? 1 : 0), (unsigned char)(s_data.sound ? 1 : 0), (unsigned char)(s_data.inventoryMap ? 0 : 1), (unsigned char)(s_data.debugScreenOptions ? 1 : 0), s_data.difficulty, s_data.renderQuality, (unsigned char)(s_data.spikeLog ? 1 : 0), (unsigned char)(s_data.debugCoordsOnly ? 1 : 0), (unsigned char)(s_data.oldMobSpawnLimit ? 1 : 0),
                              (unsigned char)(s_data.showFps ? 1 : 0) };"""

if target_init in cpp_content:
    cpp_content = cpp_content.replace(target_init, replacement_init, 1)
if target_load in cpp_content:
    cpp_content = cpp_content.replace(target_load, replacement_load, 1)
if target_load_end in cpp_content:
    cpp_content = cpp_content.replace(target_load_end, replacement_load_end, 1)
if target_save in cpp_content:
    cpp_content = cpp_content.replace(target_save, replacement_save, 1)

with open(cpp_path, "w", encoding="utf-8") as f:
    f.write(cpp_content)
print("Options.cpp updated.")

