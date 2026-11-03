#ifndef HARDWARE_H
#define HARDWARE_H

#include <nds.h>
#include <stdio.h>

class Hardware {
public:
    static inline bool isDSi() {
        return isDSiMode();
    }

    static inline int getRamSizeMB() {
        return isDSi() ? 16 : 4;
    }

    static inline int getCpuFrequencyMHz() {
        return isDSi() ? 133 : 67;
    }

    static inline const char* getDeviceName() {
        return isDSi() ? "Nintendo DSi" : "Nintendo DS (Lite/Original)";
    }

    // Políticas de streaming dinámico según hardware
    static inline int getMaxConcurrentHeavyChunks() {
        // En DSi: CPU a 133 MHz permite procesar hasta 5 chunks pesados por frame
        // En DS: CPU a 67 MHz y 4MB de RAM limitan a 2 para mantener 60 FPS estables
        return isDSi() ? 5 : 2;
    }

    static inline int getVoxelRLEMaxRuns() {
        // En DSi: 24 tramos por columna
        // En DS: 16 tramos por columna para reducir aún más el espacio en RAM
        return isDSi() ? 24 : 16;
    }

    static inline void printHardwareInfo() {
        iprintf("\n=== HARDWARE DETECTION ===\n");
        iprintf("Device: %s\n", getDeviceName());
        iprintf("RAM: %d MB | ARM9: %d MHz\n", getRamSizeMB(), getCpuFrequencyMHz());
        if (isDSi()) {
            iprintf("Mode: TWL Extended 16MB Memory\n");
            iprintf("Streaming: DSi Extended Radius (7x7)\n");
            iprintf("Voxel RAM: Dynamic Extended RLE\n");
        } else {
            iprintf("Mode: NTR Strict 4MB Memory\n");
            iprintf("Streaming: ARM7/Async Strict Stream\n");
            iprintf("Voxel RAM: Ultra-Compact RLE\n");
        }
        iprintf("SD Compress: Nintendo BIOS LZSS (SWI)\n");
        iprintf("==========================\n\n");
    }
};

#endif // HARDWARE_H
