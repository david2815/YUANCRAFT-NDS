#ifndef CHUNK_COMPRESSION_H
#define CHUNK_COMPRESSION_H

#include <nds.h>
#include <nds/arm9/decompress.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ============================================================================
// ChunkCompression: Compresión por Hardware / BIOS para Almacenamiento en SD
// ============================================================================
// - Para guardar en la SD: comprime los datos usando el formato LZSS nativo
//   de Nintendo (LZ10, con cabecera de 4 bytes 0x10 y tamaño de 24 bits).
// - Para cargar desde la SD: delega la descompresión estrictamente a las
//   rutinas de la BIOS mediante libnds (`decompress(src, dst, LZ77)`),
//   utilizando la interrupción software (SWI) por hardware.
// - Esto libera la CPU ARM9 de algoritmos costosos durante el streaming.
// ============================================================================

class ChunkCompression {
public:
    // Compresor LZ10 nativo de Nintendo (compatible con la BIOS de la consola)
    static int compressLZ10(const u8* src, int srcLen, u8* dst, int maxDstLen) {
        if (!src || !dst || srcLen <= 0 || maxDstLen < 8) return 0;

        // Protección absoluta de VRAM: no comprimir desde ni hacia bancos VRAM de la GPU
        uintptr_t srcAddr = (uintptr_t)src;
        uintptr_t dstAddr = (uintptr_t)dst;
        if ((srcAddr >= 0x06000000 && srcAddr < 0x07000000) ||
            (dstAddr >= 0x06000000 && dstAddr < 0x07000000)) {
            return 0;
        }

        // Cabecera Nintendo LZ10:
        // Byte 0: 0x10 (formato LZ77 / LZSS)
        // Bytes 1-3: tamaño sin comprimir en 24 bits little-endian
        dst[0] = 0x10;
        dst[1] = (u8)(srcLen & 0xFF);
        dst[2] = (u8)((srcLen >> 8) & 0xFF);
        dst[3] = (u8)((srcLen >> 16) & 0xFF);

        int dstPos = 4;
        int srcPos = 0;

        while (srcPos < srcLen && dstPos + 10 < maxDstLen) {
            int flagPos = dstPos++;
            u8 flagByte = 0;

            for (int bit = 7; bit >= 0; bit--) {
                if (srcPos >= srcLen) {
                    flagByte <<= 1;
                    continue;
                }

                // Ventana deslizante de hasta 4096 bytes
                int winStart = (srcPos > 4096) ? (srcPos - 4096) : 0;
                int maxLen = (srcLen - srcPos < 18) ? (srcLen - srcPos) : 18;
                int bestLen = 0;
                int bestDisp = 0;

                if (maxLen >= 3) {
                    for (int cand = srcPos - 1; cand >= winStart; cand--) {
                        if (src[cand] != src[srcPos]) continue;
                        int l = 1;
                        while (l < maxLen && src[cand + l] == src[srcPos + l]) {
                            l++;
                        }
                        if (l > bestLen) {
                            bestLen = l;
                            bestDisp = srcPos - cand;
                            if (bestLen == maxLen) break;
                        }
                    }
                }

                if (bestLen >= 3) {
                    // Referencia comprimida (2 bytes)
                    flagByte = (flagByte << 1) | 1;
                    u8 b1 = (u8)(((bestLen - 3) << 4) | (((bestDisp - 1) >> 8) & 0x0F));
                    u8 b2 = (u8)((bestDisp - 1) & 0xFF);
                    dst[dstPos++] = b1;
                    dst[dstPos++] = b2;
                    srcPos += bestLen;
                } else {
                    // Byte literal
                    flagByte = (flagByte << 1) | 0;
                    dst[dstPos++] = src[srcPos++];
                }
            }
            dst[flagPos] = flagByte;
        }

        return dstPos;
    }

    // Descompresión por hardware/BIOS usando libnds
    static inline bool decompressBIOS(const void* src, void* dst) {
        if (!src || !dst) return false;

        uintptr_t srcAddr = (uintptr_t)src;
        uintptr_t dstAddr = (uintptr_t)dst;

        // Protección absoluta de VRAM: no descompresión a bancos VRAM del motor 3D
        if ((srcAddr >= 0x06000000 && srcAddr < 0x07000000) ||
            (dstAddr >= 0x06000000 && dstAddr < 0x07000000)) {
            return false;
        }

        // Validación estricta de alineación de 32 bits requerida por la BIOS (SWI LZ77)
        if (((srcAddr | dstAddr) & 3) != 0) return false;

        const u8* p = (const u8*)src;
        if (p[0] != 0x10) return false; // Comprobación de cabecera LZ10

        // Llama a la rutina en ROM/BIOS a través de la SWI de libnds
        decompress(src, dst, LZ77);
        return true;
    }
};

#endif // CHUNK_COMPRESSION_H

