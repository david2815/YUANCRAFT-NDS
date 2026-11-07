#include "PerformancePreset.h"
#include "Options.h"
#include "Hardware.h"
#include "ChunkManager.h"
#include "WorldConfig.h"
#include <string.h>

static const PerformancePreset s_presets[PRESET_COUNT] = {
    // PRESET_DS_FAST: 60 FPS en DS Nitro (67 MHz)
    {
        PRESET_DS_FAST,
        "DS Rapido (60 FPS)",
        1,      // 3x3
        2,      // 2 chunks
        60,     // 60 FPS
        1,      // 1 rebuild/frame
        false,  // texturas estáticas
        false,  // sin partículas
        true,   // packed commands
        2,      // fast quality
        false   // DS compatible
    },
    // PRESET_DS_BALANCED: 30 FPS en DS Nitro (67 MHz)
    {
        PRESET_DS_BALANCED,
        "DS Equilibrado (30 FPS)",
        2,      // 5x5
        3,      // 3 chunks
        30,     // 30 FPS
        1,      // 1 rebuild/frame
        true,   // texturas animadas
        true,   // partículas
        true,   // packed commands
        1,      // balanced quality
        false   // DS compatible
    },
    // PRESET_DSI_HIGH_PERF: 60 FPS en DSi (133 MHz)
    {
        PRESET_DSI_HIGH_PERF,
        "DSi Fluidez (60 FPS)",
        1,      // 3x3
        3,      // 3 chunks
        60,     // 60 FPS
        1,      // 1 rebuild/frame
        true,   // texturas animadas
        true,   // partículas
        true,   // packed commands
        1,      // balanced quality
        true    // DSi only
    },
    // PRESET_DSI_EXTENDED: 30 FPS en DSi (133 MHz)
    {
        PRESET_DSI_EXTENDED,
        "DSi Distancia (30 FPS)",
        3,      // 7x7
        5,      // 5 chunks
        30,     // 30 FPS
        1,      // 1 rebuild/frame
        true,   // texturas animadas
        true,   // partículas
        true,   // packed commands
        0,      // high quality
        true    // DSi only
    },
    // PRESET_CUSTOM:
    {
        PRESET_CUSTOM,
        "Personalizado",
        2,
        3,
        30,
        1,
        true,
        true,
        true,
        1,
        false
    }
};

PerformancePreset PresetManager::s_currentPreset = s_presets[PRESET_DS_BALANCED];

bool PresetManager::isPresetAllowed(PresetType type) {
    if (type >= PRESET_COUNT) return false;
    if (s_presets[type].dsi_only && !Hardware::isDSi()) return false;
    return true;
}

const PerformancePreset& PresetManager::getPreset(PresetType type) {
    if (type >= PRESET_COUNT) return s_presets[PRESET_CUSTOM];
    return s_presets[type];
}

const PerformancePreset& PresetManager::getCurrent() {
    return s_currentPreset;
}

PresetType PresetManager::getCurrentType() {
    return s_currentPreset.type;
}

const char* PresetManager::getCurrentPresetName() {
    return s_currentPreset.name;
}

void PresetManager::syncFromOptions() {
    const Options::Data& opt = Options::get();
    for (int i = 0; i < PRESET_CUSTOM; i++) {
        PresetType pt = (PresetType)i;
        if (!isPresetAllowed(pt)) continue;
        const PerformancePreset& p = s_presets[i];
        
        int optRadius = (opt.chunkMode == 0) ? 1 : ((opt.chunkMode == 1) ? 2 : 3);
        int optFps = (Hardware::isDSi() && opt.dsiPerformanceProfile == 1) ? 60 : 30;
        if (!Hardware::isDSi()) {
            optFps = (opt.chunkMode == 0 && opt.renderQuality == 2) ? 60 : 30;
        }

        if (optRadius == p.chunk_radius &&
            opt.renderQuality == p.render_quality &&
            opt.particles == p.enable_particles &&
            optFps == p.target_fps_lock) {
            s_currentPreset = p;
            return;
        }
    }
    s_currentPreset = s_presets[PRESET_CUSTOM];
    s_currentPreset.chunk_radius = (opt.chunkMode == 0) ? 1 : ((opt.chunkMode == 1) ? 2 : 3);
    s_currentPreset.render_quality = opt.renderQuality;
    s_currentPreset.enable_particles = opt.particles;
    s_currentPreset.enable_animated_textures = (opt.renderQuality < 2);
    s_currentPreset.target_fps_lock = (Hardware::isDSi() && opt.dsiPerformanceProfile == 1) ? 60 : 30;
    if (!Hardware::isDSi()) {
        s_currentPreset.target_fps_lock = (opt.chunkMode == 0 && opt.renderQuality == 2) ? 60 : 30;
    }
}

void PresetManager::init() {
    syncFromOptions();
}

void PresetManager::applyPreset(PresetType type) {
    if (!isPresetAllowed(type)) return;
    if (type == PRESET_CUSTOM) {
        s_currentPreset = s_presets[PRESET_CUSTOM];
        return;
    }

    const PerformancePreset& p = s_presets[type];
    s_currentPreset = p;

    Options::Data& opt = Options::get();
    opt.chunkMode = (p.chunk_radius == 1) ? 0 : ((p.chunk_radius == 2) ? 1 : 2);
    opt.renderQuality = (unsigned char)p.render_quality;
    opt.particles = p.enable_particles;
    opt.dsiPerformanceProfile = (p.target_fps_lock == 60) ? 1 : 0;
    Options::save();
}

void PresetManager::applyPresetRuntime(PresetType type, ChunkManager* chunkManager) {
    applyPreset(type);
    if (chunkManager) {
        chunkManager->setWindowRadius(s_currentPreset.chunk_radius);
    }
}

void PresetManager::cyclePreset(int direction, ChunkManager* chunkManager) {
    int cur = (int)s_currentPreset.type;
    for (int step = 0; step < PRESET_COUNT; step++) {
        cur = (cur + direction + PRESET_COUNT) % PRESET_COUNT;
        if (isPresetAllowed((PresetType)cur)) {
            if (chunkManager) {
                applyPresetRuntime((PresetType)cur, chunkManager);
            } else {
                applyPreset((PresetType)cur);
            }
            return;
        }
    }
}

void PresetManager::notifyOptionChanged() {
    syncFromOptions();
}

