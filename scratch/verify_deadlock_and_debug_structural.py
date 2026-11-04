import os, sys

def verify_structural():
    print("=== VERIFICATION 1: STRUCTURAL AST & DEADLOCK AUDIT ===")
    errors = []

    # 1. DebugLogger
    if not os.path.exists("source/DebugLogger.h"):
        errors.append("source/DebugLogger.h missing")
    if not os.path.exists("source/DebugLogger.cpp"):
        errors.append("source/DebugLogger.cpp missing")
    else:
        with open("source/DebugLogger.cpp", "r", encoding="utf-8") as f:
            dl = f.read()
        if "/mcdsefiles/worlds/debug_load.txt" not in dl:
            errors.append("DebugLogger.cpp does not target /mcdsefiles/worlds/debug_load.txt")
        if "fflush" not in dl:
            errors.append("DebugLogger.cpp missing fflush() for immediate SD write")

    # 2. Required debug messages in main.cpp and IpcChunkLoader.cpp
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        mc = f.read()
    if "[DEBUG] Inicializando sistema de archivos FAT..." not in mc:
        errors.append("main.cpp: missing log '[DEBUG] Inicializando sistema de archivos FAT...'")
    if "irqInit();" not in mc or "irqEnable(IRQ_VBLANK);" not in mc:
        errors.append("main.cpp: irqInit() or irqEnable(IRQ_VBLANK) missing")

    with open("source/IpcChunkLoader.cpp", "r", encoding="utf-8") as f:
        ipc_c = f.read()
    if "[DEBUG] Enviando señal FIFO al ARM7 para descompresión LZSS del Chunk Inicial..." not in ipc_c:
        errors.append("IpcChunkLoader.cpp: missing log '[DEBUG] Enviando señal FIFO al ARM7 para descompresión LZSS del Chunk Inicial...'")
    if "[DEBUG] Esperando interrupción IPC del ARM7..." not in ipc_c:
        errors.append("IpcChunkLoader.cpp: missing log '[DEBUG] Esperando interrupción IPC del ARM7...'")
    if "[DEBUG] Datos de bloques recibidos en RAM. Tamaño: %d bytes." not in ipc_c:
        errors.append("IpcChunkLoader.cpp: missing log '[DEBUG] Datos de bloques recibidos en RAM. Tamaño: %d bytes.'")

    # 3. Non-blocking FIFO in IpcChunkLoader.h
    with open("source/IpcChunkLoader.h", "r", encoding="utf-8") as f:
        ipc_h = f.read()
    if "while (REG_IPC_FIFO_CR & IPC_FIFO_SEND_FULL);" in ipc_h:
        errors.append("IpcChunkLoader.h: blind while loop on IPC_FIFO_SEND_FULL found in irqSendFIFO!")
    if "MAX_WAIT_FRAMES = 60" not in ipc_h:
        errors.append("IpcChunkLoader.h: MAX_WAIT_FRAMES = 60 missing")

    # 4. 60-frame escape mechanism in IpcChunkLoader.cpp
    if "frameCounter >= MAX_WAIT_FRAMES" not in ipc_c:
        errors.append("IpcChunkLoader.cpp: 60-frame escape check missing")
    if "c->generateEmergencyChunk();" not in ipc_c:
        errors.append("IpcChunkLoader.cpp: generateEmergencyChunk() call missing on timeout/error")

    # 5. Chunk emergency chunk in Chunk.h & Chunk.cpp
    with open("source/Chunk.h", "r", encoding="utf-8") as f:
        ch = f.read()
    if "void generateEmergencyChunk();" not in ch:
        errors.append("Chunk.h: generateEmergencyChunk() declaration missing")

    with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
        cc = f.read()
    if "void Chunk::generateEmergencyChunk()" not in cc:
        errors.append("Chunk.cpp: Chunk::generateEmergencyChunk() definition missing")
    if "blocks[xi][yi][zi] = BlockType::STONE;" not in cc:
        errors.append("Chunk.cpp: emergency chunk does not generate stone blocks")
    if "blocks[xi][62][zi] = BlockType::GRASS;" not in cc:
        errors.append("Chunk.cpp: emergency chunk does not generate grass top")

    # 6. ChunkManager drawAll overflow reset
    with open("source/ChunkManager.cpp", "r", encoding="utf-8") as f:
        cm = f.read()
    if "GFX_CONTROL |= GL_POLY_OVERFLOW;" not in cm:
        errors.append("ChunkManager.cpp: GFX_CONTROL |= GL_POLY_OVERFLOW hardware reset missing in drawAll")

    # 7. VoxelRLE memory pointer validation
    with open("source/VoxelRLE.h", "r", encoding="utf-8") as f:
        vrle = f.read()
    if "isValidMainRamPointer" not in vrle:
        errors.append("VoxelRLE.h: isValidMainRamPointer helper missing")

    if errors:
        print("[FAIL] Verification 1 encountered errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("[PASS] Verification 1 PASSED: All structural AST and deadlock escape rules verified successfully!")

if __name__ == "__main__":
    verify_structural()
