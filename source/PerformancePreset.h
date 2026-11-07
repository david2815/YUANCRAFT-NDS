#ifndef PERFORMANCE_PRESET_H
#define PERFORMANCE_PRESET_H

#include <nds.h>

enum PresetType {
    PRESET_DS_FAST = 0,         // DS Nitro 60 FPS
    PRESET_DS_BALANCED = 1,     // DS Nitro 30 FPS
    PRESET_DSI_HIGH_PERF = 2,   // DSi TWL 60 FPS (Fluidez)
    PRESET_DSI_EXTENDED = 3,    // DSi TWL 30 FPS (Distancia)
    PRESET_CUSTOM = 4,          // Personalizado
    PRESET_COUNT = 5
};

struct PerformancePreset {
    PresetType type;
    const char* name;
    int chunk_radius;               // 1 = 3x3, 2 = 5x5, 3 = 7x7
    int render_distance;            // 2, 3, 4, 5
    int target_fps_lock;            // 30 o 60
    int max_mesh_rebuilds_per_frame;// 1
    bool enable_animated_textures;  // agua/lava animada
    bool enable_particles;          // partículas
    bool use_packed_commands;       // comandos empaquetados FIFO
    int render_quality;             // 0 = high, 1 = balanced, 2 = fast
    bool dsi_only;                  // exclusivo de DSi
};

class ChunkManager;

class PresetManager {
public:
    static void init();
    static const PerformancePreset& getPreset(PresetType type);
    static const PerformancePreset& getCurrent();
    static PresetType getCurrentType();
    
    // Aplica el preset actualizando Options
    static void applyPreset(PresetType type);
    
    // Aplica el preset en caliente (runtime) sin recargar el mundo
    static void applyPresetRuntime(PresetType type, ChunkManager* chunkManager);
    
    // Cicla entre presets compatibles con el hardware
    static void cyclePreset(int direction, ChunkManager* chunkManager = nullptr);
    
    static const char* getCurrentPresetName();
    static bool isPresetAllowed(PresetType type);
    
    // Sincroniza el preset si el usuario modifica opciones manualmente
    static void notifyOptionChanged();

    static inline int getTargetFpsLock() { return s_currentPreset.target_fps_lock; }
    static inline bool areAnimatedTexturesEnabled() { return s_currentPreset.enable_animated_textures; }
    static inline bool areParticlesEnabled() { return s_currentPreset.enable_particles; }

private:
    static PerformancePreset s_currentPreset;
    static void syncFromOptions();
};

#endif

