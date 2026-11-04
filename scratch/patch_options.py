with open('source/Options.cpp', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'static Options::Data s_data = { false, 0, 0, false, 0, 0, true, true, true, true, 2, false, false, false, 0, true, false, false };',
    'static Options::Data s_data = { false, 0, 0, false, 0, 0, true, true, true, true, 2, false, false, false, 0, true, false, false, 0 };'
)

text = text.replace(
    's_data.showFps = false;\n    FILE* f = fopen(OPTIONS_PATH, "rb");\n    if (!f) return;\n    unsigned char buf[25];',
    's_data.showFps = false;\n    s_data.dsiPerformanceProfile = 0;\n    FILE* f = fopen(OPTIONS_PATH, "rb");\n    if (!f) return;\n    unsigned char buf[26];'
)

text = text.replace(
    'if (n >= 25) s_data.showFps = (buf[24] == 1);',
    'if (n >= 25) s_data.showFps = (buf[24] == 1);\n        if (n >= 26) s_data.dsiPerformanceProfile = (buf[25] <= 1) ? buf[25] : 0;'
)

old_save = """    unsigned char buf[25] = { 'M', 'C', 'O', '1', (unsigned char)(s_data.debugLargeChest ? 1 : 0), s_data.chunkMode,
                              s_data.seedMode, (unsigned char)(s_data.customSeedSet ? 1 : 0),
                              (unsigned char)(s_data.customSeed & 0xFF), (unsigned char)((s_data.customSeed >> 8) & 0xFF),
                              (unsigned char)((s_data.customSeed >> 16) & 0xFF), (unsigned char)((s_data.customSeed >> 24) & 0xFF),
                              s_data.controlMode, (unsigned char)(s_data.autoJump ? 1 : 0), (unsigned char)(s_data.clockCompassInvUpdate ? 1 : 0), (unsigned char)(s_data.particles ? 1 : 0), (unsigned char)(s_data.sound ? 1 : 0), (unsigned char)(s_data.inventoryMap ? 0 : 1), (unsigned char)(s_data.debugScreenOptions ? 1 : 0), s_data.difficulty, s_data.renderQuality, (unsigned char)(s_data.spikeLog ? 1 : 0), (unsigned char)(s_data.debugCoordsOnly ? 1 : 0), (unsigned char)(s_data.oldMobSpawnLimit ? 1 : 0),
                              (unsigned char)(s_data.showFps ? 1 : 0) };
    const bool ok = fwrite(buf, 1, sizeof(buf), f) == sizeof(buf);"""

new_save = """    unsigned char buf[26] = { 'M', 'C', 'O', '1', (unsigned char)(s_data.debugLargeChest ? 1 : 0), s_data.chunkMode,
                              s_data.seedMode, (unsigned char)(s_data.customSeedSet ? 1 : 0),
                              (unsigned char)(s_data.customSeed & 0xFF), (unsigned char)((s_data.customSeed >> 8) & 0xFF),
                              (unsigned char)((s_data.customSeed >> 16) & 0xFF), (unsigned char)((s_data.customSeed >> 24) & 0xFF),
                              s_data.controlMode, (unsigned char)(s_data.autoJump ? 1 : 0), (unsigned char)(s_data.clockCompassInvUpdate ? 1 : 0), (unsigned char)(s_data.particles ? 1 : 0), (unsigned char)(s_data.sound ? 1 : 0), (unsigned char)(s_data.inventoryMap ? 0 : 1), (unsigned char)(s_data.debugScreenOptions ? 1 : 0), s_data.difficulty, s_data.renderQuality, (unsigned char)(s_data.spikeLog ? 1 : 0), (unsigned char)(s_data.debugCoordsOnly ? 1 : 0), (unsigned char)(s_data.oldMobSpawnLimit ? 1 : 0),
                              (unsigned char)(s_data.showFps ? 1 : 0), s_data.dsiPerformanceProfile };
    const bool ok = fwrite(buf, 1, sizeof(buf), f) == sizeof(buf);"""

text = text.replace(old_save, new_save)

with open('source/Options.cpp', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated source/Options.cpp successfully')

