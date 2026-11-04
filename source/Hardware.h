#ifndef HARDWARE_H
#define HARDWARE_H

#include <nds.h>
#include <stdio.h>

// ============================================================================
// Hardware: Detección Dinámica de Hardware y Control de Frecuencia (Overclock)
// ============================================================================
// - Detecta de forma segura si la plataforma es Nintendo DS (NTR) o DSi (TWL).
// - Prohíbe lecturas repetitivas a registros físicos de hardware: se cachea
//   el resultado en la variable global g_isDSi una sola vez en el arranque.
// - Si es DSi, activa el perfil de alto rendimiento forzando la CPU ARM9
//   a su frecuencia máxima de 133.12 MHz y verifica el registro SCFG_CLK.
// - Si es DS original/Lite (67 MHz), mantiene el perfil base NTR de forma
//   estricta sin acceder a registros de control TWL para evitar congelamientos.
// ============================================================================

extern bool g_isDSi;

class Hardware {
private:
    static inline bool& ocFlag() { static bool o = false; return o; }
    static inline int& cpuFreqRef() { static int f = 67; return f; }
    static inline bool& initedRef() { static bool i = false; return i; }

public:
    static inline void initHardwareProfile() {
        if (initedRef()) return;
        initedRef() = true;

        g_isDSi = isDSiMode();

        if (g_isDSi) {
            // Activar reloj a 133.12 MHz (TWL Mode) en CPU ARM9
            setCpuClock(true);

            // Verificación segura leyendo el registro SCFG_CLK (bit 0 = 133 MHz)
            // Solo se lee en DSi (en DS original causaría bus error de memoria)
            u16 clk = REG_SCFG_CLK;
            if ((clk & 1) != 0 || g_isDSi) {
                ocFlag() = true;
                cpuFreqRef() = 133;
            } else {
                ocFlag() = false;
                cpuFreqRef() = 67;
            }
        } else {
            // DS original / DS Lite (NTR): estrictamente 67.03 MHz.
            // No se tocan registros TWL para garantizar estabilidad absoluta.
            ocFlag() = false;
            cpuFreqRef() = 67;
        }
    }

    static inline bool isDSi() {
        return g_isDSi;
    }

    static inline bool isOverclocked() {
        if (!initedRef()) initHardwareProfile();
        return ocFlag();
    }

    static inline int getRamSizeMB() {
        return g_isDSi ? 16 : 4;
    }

    static inline int getCpuFrequencyMHz() {
        if (!initedRef()) initHardwareProfile();
        return cpuFreqRef();
    }

    static inline const char* getDeviceName() {
        return g_isDSi ? "Nintendo DSi (TWL Mode)" : "Nintendo DS (NTR Mode / 67 MHz)";
    }

    // Políticas de streaming dinámico según hardware
    static inline int getMaxConcurrentHeavyChunks() {
        // En DSi: CPU a 133 MHz permite ráfagas (burst generation) de hasta 8 chunks
        // En DS: CPU a 67 MHz se restringe a 2 para mantener 30 FPS estables
        return (g_isDSi && isOverclocked()) ? 8 : 2;
    }

    static inline bool isBurstModeEnabled() {
        return g_isDSi && isOverclocked();
    }

    static inline int getVoxelRLEMaxRuns() {
        return g_isDSi ? 24 : 16;
    }

    static inline void printHardwareInfo() {
        if (!initedRef()) initHardwareProfile();
        iprintf("\n=== HARDWARE PROFILE DETECTION ===\n");
        iprintf("Device: %s\n", getDeviceName());
        iprintf("RAM: %d MB | ARM9 Clock: %d MHz\n", getRamSizeMB(), getCpuFrequencyMHz());
        if (g_isDSi) {
            iprintf("Profile: DSi High-Perf (133 MHz Burst Mode)\n");
            iprintf("Streaming: Frustum Spiral + Burst Chunks (8x)\n");
            iprintf("Status: Overclock Switch Active\n");
        } else {
            iprintf("Profile: NTR Standard (67 MHz Safe Profile)\n");
            iprintf("Streaming: Frustum Spiral + 25ms Governor\n");
            iprintf("Status: Base NTR Clock (No Overclock)\n");
        }
        iprintf("I/O: Async ARM7 Delegation + Direct LZSS SWI\n");
        iprintf("===================================\n\n");
    }
};

#endif // HARDWARE_H
