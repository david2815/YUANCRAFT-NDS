import re, sys

def verify_all():
    print("=== VERIFICATION 1: STRUCTURAL & STATIC ANALYSIS ===")
    errors = []

    # 1. Check source/VoxelRLE.h
    with open("source/VoxelRLE.h", "r", encoding="utf-8") as f:
        rle = f.read()
    if "__attribute__((aligned(4)))" not in rle:
        errors.append("VoxelColumnRLE missing __attribute__((aligned(4)))")
    if "_pad[3]" not in rle:
        errors.append("VoxelColumnRLE missing _pad[3] 32-bit alignment padding")
    if "isVramPointer" not in rle:
        errors.append("VoxelRLE.h missing isVramPointer check")

    # 2. Check source/AsyncSaveManager.h & .cpp
    with open("source/AsyncSaveManager.h", "r", encoding="utf-8") as f:
        asm_h = f.read()
    if "__attribute__((aligned(4)))" not in asm_h:
        errors.append("AsyncSaveManager.h missing __attribute__((aligned(4)))")
    with open("source/AsyncSaveManager.cpp", "r", encoding="utf-8") as f:
        asm_c = f.read()
    if "0x06000000" not in asm_c:
        errors.append("AsyncSaveManager.cpp missing VRAM protection check (0x06000000)")

    # 3. Check source/ChunkCompression.h
    with open("source/ChunkCompression.h", "r", encoding="utf-8") as f:
        cc_h = f.read()
    if "0x06000000" not in cc_h:
        errors.append("ChunkCompression.h missing VRAM protection check")
    if "((srcAddr | dstAddr) & 3) != 0" not in cc_h:
        errors.append("ChunkCompression.h missing 32-bit alignment check")

    # 4. Check source/Chunk.h
    with open("source/Chunk.h", "r", encoding="utf-8") as f:
        chk_h = f.read()
    if "blocks[WorldConfig::SIZE_X][WorldConfig::SIZE_Y][WorldConfig::SIZE_Z] __attribute__((aligned(4)))" not in chk_h:
        errors.append("Chunk.h blocks array missing __attribute__((aligned(4)))")
    if "rleCols[WorldConfig::SIZE_X][WorldConfig::SIZE_Z] __attribute__((aligned(4)))" not in chk_h:
        errors.append("Chunk.h rleCols array missing __attribute__((aligned(4)))")
    if "liquidMeta[LIQUID_META_BYTES] __attribute__((aligned(4)))" not in chk_h:
        errors.append("Chunk.h liquidMeta array missing __attribute__((aligned(4)))")

    # 5. Check source/Chunk.cpp
    with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
        chk_c = f.read()
    if "s_rawSaveBuf[sizeof(blocks) + sizeof(liquidMeta)] __attribute__((aligned(4)))" not in chk_c:
        errors.append("Chunk.cpp s_rawSaveBuf missing alignment")
    if "while (GFX_BUSY)" not in chk_c:
        errors.append("Chunk.cpp callListFast missing GFX_BUSY synchronization")

    # 6. Check source/Hardware.h
    with open("source/Hardware.h", "r", encoding="utf-8") as f:
        hw_h = f.read()
    if "ITCM_CODE static void applyClockSafeTWL()" not in hw_h:
        errors.append("Hardware.h missing applyClockSafeTWL in ITCM_CODE")
    if "u16 oldExmem = REG_EXMEMCNT" not in hw_h or "REG_EXMEMCNT = oldExmem" not in hw_h:
        errors.append("Hardware.h not preserving REG_EXMEMCNT waitstates")
    if "DC_FlushAll()" not in hw_h or "IC_InvalidateAll()" not in hw_h:
        errors.append("Hardware.h missing cache synchronization")

    # 7. Check source/Renderer.cpp
    with open("source/Renderer.cpp", "r", encoding="utf-8") as f:
        rend_c = f.read()
    if "glMatrixMode(GL_MODELVIEW); // Restablecer siempre el modo de matrices a MODELVIEW" not in rend_c:
        errors.append("Renderer.cpp setupProjection not restoring GL_MODELVIEW")

    # 8. Check source/main.cpp
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_c = f.read()
    if "while ((DMA_CR(0) | DMA_CR(3)) & DMA_BUSY);" not in main_c:
        errors.append("main.cpp missing DMA drain check after drawAll")
    if "while (GFX_BUSY);" not in main_c:
        errors.append("main.cpp missing GFX_BUSY wait")
    if "GFX_STATUS & BIT(15)" not in main_c or "glResetMatrixStack()" not in main_c:
        errors.append("main.cpp missing matrix stack error recovery")
    if "glEnd();" not in main_c:
        errors.append("main.cpp missing glEnd vertex cleanup before glFlush")

    if errors:
        print(f"VERIFICATION 1 FAILED WITH {len(errors)} ERRORS:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    else:
        print("VERIFICATION 1 PASSED: All structural rules, alignments, and safeguards verified successfully!")

if __name__ == "__main__":
    verify_all()

