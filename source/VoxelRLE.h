#ifndef VOXEL_RLE_H
#define VOXEL_RLE_H

#include <nds.h>
#include <string.h>
#include "BlockType.h"
#include "WorldConfig.h"

// ============================================================================
// VoxelRLE: Codificación RLE (Run-Length Encoding) ultraligera para RAM activa
// ============================================================================
// - Diseñado para optimizar FPS y minimizar uso de RAM en CPUs ARM9 (67 / 133 MHz).
// - Prohíbe el uso de diccionarios complejos, PPMd o árboles de Huffman en RAM activa.
// - Aprovecha la homogeneidad vertical de Minecraft (columnas de 128 bloques con
//   grandes masas consecutivas de piedra, tierra, agua y aire).
// - Permite lectura directa en tiempo real O(runs) donde runs <= 6 en promedio.
// ============================================================================

struct RLERun {
    BlockType type; // 1 byte: tipo de bloque
    u8 length;      // 1 byte: longitud del tramo (1..128)
};

class VoxelColumnRLE {
public:
    // 24 tramos x 2 bytes = 48 bytes por columna (cabe perfectamente en 2 líneas de caché de 32B)
    static constexpr int MAX_RUNS = 24;

    u8 runCount;
    RLERun runs[MAX_RUNS];

    inline void initEmpty() {
        runCount = 1;
        runs[0].type = BlockType::AIR;
        runs[0].length = (u8)WorldConfig::SIZE_Y; // 128 bloques de aire
    }

    // Lectura directa en tiempo real O(runs) sin tocar punto flotante ni diccionarios
    inline BlockType get(int y) const {
        if (y < 0 || y >= WorldConfig::SIZE_Y) return BlockType::AIR;
        int accum = 0;
        for (int i = 0; i < runCount; i++) {
            accum += runs[i].length;
            if (y < accum) {
                return runs[i].type;
            }
        }
        return BlockType::AIR;
    }

    // Modificación de un voxel actualizando los tramos RLE en caliente
    void set(int y, BlockType newType) {
        if (y < 0 || y >= WorldConfig::SIZE_Y) return;
        int accum = 0;
        for (int i = 0; i < runCount; i++) {
            int runStart = accum;
            int runLen = runs[i].length;
            accum += runLen;

            if (y >= accum) continue;

            if (runs[i].type == newType) return; // Ya es de ese tipo

            // Caso 1: El tramo mide exactamente 1
            if (runLen == 1) {
                runs[i].type = newType;
                // Fusión con anterior
                if (i > 0 && runs[i - 1].type == newType) {
                    runs[i - 1].length += runs[i].length;
                    for (int j = i; j < runCount - 1; j++) runs[j] = runs[j + 1];
                    runCount--;
                    i--;
                }
                // Fusión con posterior
                if (i + 1 < runCount && runs[i + 1].type == newType) {
                    runs[i].length += runs[i + 1].length;
                    for (int j = i + 1; j < runCount - 1; j++) runs[j] = runs[j + 1];
                    runCount--;
                }
                return;
            }

            // Caso 2: Al inicio del tramo (y == runStart)
            if (y == runStart) {
                if (i > 0 && runs[i - 1].type == newType) {
                    runs[i - 1].length++;
                    runs[i].length--;
                    return;
                }
                if (runCount < MAX_RUNS) {
                    for (int j = runCount; j > i; j--) runs[j] = runs[j - 1];
                    runs[i].type = newType;
                    runs[i].length = 1;
                    runs[i + 1].length--;
                    runCount++;
                    return;
                }
            }

            // Caso 3: Al final del tramo (y == runStart + runLen - 1)
            if (y == runStart + runLen - 1) {
                if (i + 1 < runCount && runs[i + 1].type == newType) {
                    runs[i + 1].length++;
                    runs[i].length--;
                    return;
                }
                if (runCount < MAX_RUNS) {
                    for (int j = runCount; j > i + 1; j--) runs[j] = runs[j - 1];
                    runs[i + 1].type = newType;
                    runs[i + 1].length = 1;
                    runs[i].length--;
                    runCount++;
                    return;
                }
            }

            // Caso 4: En medio del tramo (se divide en: anterior, nuevo, posterior)
            if (runCount + 2 <= MAX_RUNS) {
                int leftLen = y - runStart;
                int rightLen = runLen - leftLen - 1;
                for (int j = runCount + 1; j > i + 2; j--) runs[j] = runs[j - 2];
                runs[i].length = (u8)leftLen;
                runs[i + 1].type = newType;
                runs[i + 1].length = 1;
                runs[i + 2].type = runs[i].type;
                runs[i + 2].length = (u8)rightLen;
                runCount += 2;
                return;
            }

            // Si se alcanza el tope de runs, se actualiza el tipo
            runs[i].type = newType;
            return;
        }
    }

    // Empaquetado rápido desde un buffer lineal (128 bloques)
    void pack(const BlockType* in128) {
        runCount = 0;
        int y = 0;
        while (y < WorldConfig::SIZE_Y && runCount < MAX_RUNS) {
            BlockType currentType = in128[y];
            int count = 1;
            while (y + count < WorldConfig::SIZE_Y && in128[y + count] == currentType && count < 255) {
                count++;
            }
            runs[runCount].type = currentType;
            runs[runCount].length = (u8)count;
            runCount++;
            y += count;
        }
    }

    // Desempaquetado a un buffer lineal
    ITCM_CODE void unpack(BlockType* out128) const {
        int idx = 0;
        for (int i = 0; i < runCount; i++) {
            BlockType t = runs[i].type;
            int len = runs[i].length;
            for (int k = 0; k < len; k++) {
                out128[idx++] = t;
            }
        }
        while (idx < WorldConfig::SIZE_Y) {
            out128[idx++] = BlockType::AIR;
        }
    }
};

#endif // VOXEL_RLE_H

