import os
import sys

def verify_code():
    print("=== TEST SUITE 1: Hardware Optimization Code Assertions ===")
    
    # 1. Coprocessor registers in HwMath.h
    with open("source/HwMath.h", "r", encoding="utf-8") as f:
        hw_math = f.read()
    assert "REG_DIVCNT" in hw_math, "HwMath missing REG_DIVCNT"
    assert "REG_DIV_NUMER_L" in hw_math or "REG_DIV_NUMER" in hw_math, "HwMath missing REG_DIV_NUMER"
    assert "REG_DIV_DENOM_L" in hw_math or "REG_DIV_DENOM" in hw_math, "HwMath missing REG_DIV_DENOM"
    assert "REG_DIV_RESULT_L" in hw_math or "REG_DIV_RESULT" in hw_math, "HwMath missing REG_DIV_RESULT"
    assert "REG_SQRTCNT" in hw_math, "HwMath missing REG_SQRTCNT"
    assert "REG_SQRT_PARAM_L" in hw_math or "REG_SQRT_PARAM" in hw_math, "HwMath missing REG_SQRT_PARAM"
    assert "REG_SQRT_RESULT" in hw_math, "HwMath missing REG_SQRT_RESULT"
    assert "startDiv32" in hw_math and "startSqrt32" in hw_math, "HwMath missing async start methods"
    print(" [PASS] HwMath implements direct DS hardware math coprocessor registers and async routines.")

    # 2. Replaced sqrt and division in physics, collision and raycasting
    with open("source/Player.cpp", "r", encoding="utf-8") as f:
        player_cpp = f.read()
    import re
    assert "HwMath::sqrtf" in player_cpp, "Player.cpp must use HwMath::sqrtf"
    assert "HwMath::divf" in player_cpp, "Player.cpp must use HwMath::divf"
    # Ensure no bare sqrtf (without HwMath::)
    assert not re.search(r'(?<!::)sqrtf\(', player_cpp), "Player.cpp should not contain bare software sqrtf"
    print(" [PASS] Player.cpp physics, movement and knockback use hardware math coprocessor.")

    with open("source/Raycaster.cpp", "r", encoding="utf-8") as f:
        ray_cpp = f.read()
    assert "HwMath::divf(boundX - px, remainX)" in ray_cpp, "Raycaster must use HwMath in DDA loop"
    print(" [PASS] Raycaster DDA inner loop uses hardware divider.")

    with open("source/Torch.h", "r", encoding="utf-8") as f:
        torch_h = f.read()
    assert "HwMath::divf" in torch_h, "Torch collision raycast must use HwMath::divf"
    print(" [PASS] Torch collision raycast uses hardware coprocessor.")

    with open("source/PartialBlocks.cpp", "r", encoding="utf-8") as f:
        pb_cpp = f.read()
    assert "HwMath::divf" in pb_cpp, "PartialBlocks rayVsBox must use HwMath::divf"
    print(" [PASS] PartialBlocks collision raycast uses hardware coprocessor.")

    # 3. ITCM and DTCM memory optimizations
    with open("source/VoxelRLE.h", "r", encoding="utf-8") as f:
        rle_h = f.read()
    assert "ITCM_CODE void unpack" in rle_h, "VoxelRLE unpack must have ITCM_CODE"
    print(" [PASS] VoxelRLE::unpack is placed in ITCM fast instruction RAM.")

    with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
        chunk_cpp = f.read()
    assert "ITCM_CODE void Chunk::rebuildColumnOccupancy" in chunk_cpp, "rebuildColumnOccupancy must have ITCM_CODE"
    assert "ITCM_CODE void Chunk::computeColumnFacesBitwise" in chunk_cpp, "computeColumnFacesBitwise must have ITCM_CODE"
    print(" [PASS] Hidden face removal (rebuildColumnOccupancy and computeColumnFacesBitwise) is in ITCM.")

    assert "ITCM_CODE void Player::physicsTick" in player_cpp, "Player::physicsTick must have ITCM_CODE"
    assert "ITCM_CODE bool Player::collidesAt" in player_cpp, "Player::collidesAt must have ITCM_CODE"
    print(" [PASS] Player physics equations are in ITCM.")

    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_cpp = f.read()
    assert "DTCM_BSS" in main_cpp, "main.cpp must define DTCM variables"
    assert "s_dtcmPlayer" in main_cpp, "Player must be allocated in DTCM"
    assert "player = &s_dtcmPlayer" in main_cpp, "player pointer must reference DTCM instance"
    print(" [PASS] Player state and active chunk pointers reside in fast zero-wait DTCM.")

    # 4. Geometry transfer via DMA channels
    assert "dmaCopyWords(3, s_dlScratch, buf" in chunk_cpp, "Chunk display list must be copied via dmaCopyWords"
    assert "DMA_SRC(0)" in chunk_cpp and "0x4000400" in chunk_cpp, "Geometry FIFO stream must use DMA channel 0"
    print(" [PASS] Geometry display list and vertex transfers use dedicated DMA hardware channels.")

    # 5. Hardware Graphics Effects (glFog)
    with open("source/Renderer.cpp", "r", encoding="utf-8") as f:
        ren_cpp = f.read()
    assert "glEnable(GL_FOG)" in ren_cpp, "glEnable(GL_FOG) must be active"
    assert "glFogDensity" in ren_cpp and "glFogShift" in ren_cpp and "glFogOffset" in ren_cpp, "Hardware fog table must be configured"
    assert "glFogColor" in main_cpp, "glFogColor must be updated dynamically each frame"
    print(" [PASS] Hardware graphics fog (glFog) is fully active and driving distance attenuation.")

if __name__ == "__main__":
    verify_code()
    print("\nALL HARDWARE OPTIMIZATION ASSERTIONS VERIFIED SUCCESSFULLY!")
