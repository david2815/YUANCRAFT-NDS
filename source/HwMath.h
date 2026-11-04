#ifndef HW_MATH_H
#define HW_MATH_H

#include <nds.h>
#include <nds/arm9/math.h>

/**
 * ============================================================================
 * HwMath: Acelerador Matemático por Hardware Asíncrono para Nintendo DS (ARM9)
 * ============================================================================
 * Aprovecha los registros de división (REG_DIV_NUMER, REG_DIV_DENOM) y de
 * raíz cuadrada (REG_SQRT_PARAM, REG_SQRT_RESULT) del coprocesador de hardware
 * del procesador ARM946E-S.
 *
 * Latencias de hardware:
 *  - División 32/32 o 64/32: 18 ciclos (36 ciclos en 64/64).
 *  - Raíz cuadrada 32-bit: 13 ciclos (26 ciclos en 64-bit).
 *
 * Al desacoplar la carga de registros del consumo del resultado, la CPU puede
 * intercalar instrucciones intermedias sin bloquear el bus de ejecución.
 * ============================================================================
 */

class HwMath {
public:
    // ------------------------------------------------------------------------
    // Operaciones de División Asíncronas
    // ------------------------------------------------------------------------

    // Inicia división entera 32 / 32
    static inline void startDiv32(int32_t numer, int32_t denom) {
        REG_DIVCNT = DIV_32_32;
        REG_DIV_NUMER_L = numer;
        REG_DIV_DENOM_L = denom;
    }

    // Inicia división 64 / 32 (útil para números grandes o punto fijo)
    static inline void startDiv64_32(int64_t numer, int32_t denom) {
        REG_DIVCNT = DIV_64_32;
        REG_DIV_NUMER = numer;
        REG_DIV_DENOM_L = denom;
    }

    // Inicia división en punto fijo 20.12: (num << 12) / den
    static inline void startDivFixed20_12(int32_t numFixed, int32_t denFixed) {
        REG_DIVCNT = DIV_64_32;
        REG_DIV_NUMER = ((int64_t)numFixed) << 12;
        REG_DIV_DENOM_L = denFixed;
    }

    // Espera la finalización si es necesario y devuelve el cociente de 32 bits
    static inline int32_t getDivResult32() {
        while (REG_DIVCNT & DIV_BUSY);
        return REG_DIV_RESULT_L;
    }

    // Devuelve el residuo de 32 bits
    static inline int32_t getDivRemainder32() {
        while (REG_DIVCNT & DIV_BUSY);
        return REG_DIVREM_RESULT_L;
    }

    // División sincrónica acelerada por hardware (32 / 32)
    static inline int32_t div(int32_t numer, int32_t denom) {
        if (denom == 0) return 0;
        startDiv32(numer, denom);
        return getDivResult32();
    }

    // Módulo sincrónico acelerado por hardware (32 % 32)
    static inline int32_t mod(int32_t numer, int32_t denom) {
        if (denom == 0) return 0;
        startDiv32(numer, denom);
        return getDivRemainder32();
    }

    // División sincrónica en punto fijo 20.12
    static inline int32_t divFixed(int32_t numFixed, int32_t denFixed) {
        if (denFixed == 0) return 0;
        startDivFixed20_12(numFixed, denFixed);
        return getDivResult32();
    }

    // División de punto flotante delegada directamente a los registros de hardware
    static inline float divf(float a, float b) {
        if (b == 0.0f) return 0.0f;
        int32_t fa = (int32_t)(a * 4096.0f);
        int32_t fb = (int32_t)(b * 4096.0f);
        if (fb == 0) return 0.0f;
        startDivFixed20_12(fa, fb);
        int32_t res = getDivResult32();
        return (float)res * (1.0f / 4096.0f);
    }

    // ------------------------------------------------------------------------
    // Operaciones de Raíz Cuadrada Asíncronas
    // ------------------------------------------------------------------------

    // Inicia raíz cuadrada de 32 bits
    static inline void startSqrt32(uint32_t param) {
        REG_SQRTCNT = SQRT_32;
        REG_SQRT_PARAM_L = param;
    }

    // Inicia raíz cuadrada de 64 bits
    static inline void startSqrt64(int64_t param) {
        REG_SQRTCNT = SQRT_64;
        REG_SQRT_PARAM = param;
    }

    // Inicia raíz cuadrada en punto fijo 20.12: sqrt((int64_t)valFixed << 12)
    static inline void startSqrtFixed20_12(int32_t valFixed) {
        REG_SQRTCNT = SQRT_64;
        REG_SQRT_PARAM = ((int64_t)valFixed) << 12;
    }

    // Espera la finalización si es necesario y devuelve la raíz cuadrada
    static inline uint32_t getSqrtResult() {
        while (REG_SQRTCNT & SQRT_BUSY);
        return REG_SQRT_RESULT;
    }

    // Raíz cuadrada entera sincrónica (32 bits)
    static inline uint32_t sqrt32(uint32_t param) {
        startSqrt32(param);
        return getSqrtResult();
    }

    // Raíz cuadrada en punto flotante acelerada por coprocesador de hardware
    static inline float sqrtf(float val) {
        if (val <= 0.0f) return 0.0f;
        int32_t fixedVal = (int32_t)(val * 4096.0f);
        startSqrtFixed20_12(fixedVal);
        int32_t res = (int32_t)getSqrtResult();
        return (float)res * (1.0f / 4096.0f);
    }
};

#endif // HW_MATH_H

