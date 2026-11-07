import os, sys

def verify_structural():
    print("=== VERIFICATION 1: STRUCTURAL AST & HARDWARE STATIC AUDIT ===")
    errors = []

    # 1. IpcChunkLoader.h
    if not os.path.exists("source/IpcChunkLoader.h"):
        errors.append("source/IpcChunkLoader.h does not exist")
    else:
        with open("source/IpcChunkLoader.h", "r", encoding="utf-8") as f:
            c = f.read()
        if "struct __attribute__((aligned(4))) IpcChunkExchange" not in c:
            errors.append("IpcChunkLoader.h: IpcChunkExchange not 32-bit aligned")
        if "static inline void irqSendFIFO(u32 cmd)" not in c:
            errors.append("IpcChunkLoader.h: irqSendFIFO() inline helper missing")
        if "REG_IPC_FIFO_CR |= IPC_FIFO_SEND_IRQ | IPC_FIFO_ENABLE;" not in c:
            errors.append("IpcChunkLoader.h: REG_IPC_FIFO_CR interrupt flags missing in irqSendFIFO")
        if "TIMEOUT_MS = 3000" not in c:
            errors.append("IpcChunkLoader.h: TIMEOUT_MS 3000ms definition missing")

    # 2. IpcChunkLoader.cpp
    if not os.path.exists("source/IpcChunkLoader.cpp"):
        errors.append("source/IpcChunkLoader.cpp does not exist")
    else:
        with open("source/IpcChunkLoader.cpp", "r", encoding="utf-8") as f:
            c = f.read()
        if "irqSendFIFO(0x4C430000 | (slotIndex & 0xFFFF));" not in c:
            errors.append("IpcChunkLoader.cpp: irqSendFIFO with command code missing in requestChunkLoad")
        if "s_exchange.status = IPC_STATUS_READING;" not in c:
            errors.append("IpcChunkLoader.cpp: asynchronous state transition to READING missing")
        if "if (elapsed >= TIMEOUT_TICKS)" not in c:
            errors.append("IpcChunkLoader.cpp: 3000ms timeout check missing in update()")
        if "REG_IPC_FIFO_CR |= IPC_FIFO_RECV_IRQ;" not in c:
            errors.append("IpcChunkLoader.cpp: REG_IPC_FIFO_CR hardware interrupt notification missing")
        if "c->fillWithAir();" not in c:
            errors.append("IpcChunkLoader.cpp: fail-safe fillWithAir() call missing on timeout/error")

    # 3. Chunk.h & Chunk.cpp
    with open("source/Chunk.h", "r", encoding="utf-8") as f:
        ch = f.read()
    if "void fillWithAir();" not in ch or "bool loadFromRawBuffer(" not in ch:
        errors.append("Chunk.h: fillWithAir() or loadFromRawBuffer() declarations missing")

    with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
        cc = f.read()
    if "void Chunk::fillWithAir()" not in cc:
        errors.append("Chunk.cpp: Chunk::fillWithAir() definition missing")
    if "blocks[xi][yi][zi] = BlockType::AIR;" not in cc:
        errors.append("Chunk.cpp: Chunk::fillWithAir() does not reset blocks to AIR")
    if "bool Chunk::loadFromRawBuffer(const u8* rawData, int rawSize)" not in cc:
        errors.append("Chunk.cpp: Chunk::loadFromRawBuffer() definition missing")

    # 4. ChunkManager.h & ChunkManager.cpp
    with open("source/ChunkManager.h", "r", encoding="utf-8") as f:
        cmh = f.read()
    if "Chunk* getChunkSlot(int slot)" not in cmh or "void clearAwaitingLoad(int slot)" not in cmh:
        errors.append("ChunkManager.h: getChunkSlot or clearAwaitingLoad missing in public section")

    with open("source/ChunkManager.cpp", "r", encoding="utf-8") as f:
        cmc = f.read()
    if "IpcChunkLoader::update(this);" not in cmc:
        errors.append("ChunkManager.cpp: IpcChunkLoader::update(this) missing in update()")
    if "IpcChunkLoader::requestChunkLoad(" not in cmc:
        errors.append("ChunkManager.cpp: IpcChunkLoader::requestChunkLoad missing in update()")

    # 5. main.cpp
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        mc = f.read()
    if "if (state == STATE_LOADING)" not in mc:
        errors.append("main.cpp: state == STATE_LOADING block not found")
    else:
        loading_block = mc[mc.find("if (state == STATE_LOADING)"):mc.find("if (state == STATE_LOADING)") + 400]
        if "scanKeys();" not in loading_block:
            errors.append("main.cpp: active scanKeys() missing inside STATE_LOADING")
        if "swiWaitForVBlank();" not in loading_block:
            errors.append("main.cpp: active swiWaitForVBlank() missing inside STATE_LOADING")

    # 6. AsyncSaveManager.cpp
    with open("source/AsyncSaveManager.cpp", "r", encoding="utf-8") as f:
        ac = f.read()
    flush_block = ac[ac.find("void AsyncSaveManager::flushAll()"):ac.find("void AsyncSaveManager::flushAll()") + 200]
    if "scanKeys();" not in flush_block or "swiWaitForVBlank();" not in flush_block:
        errors.append("AsyncSaveManager.cpp: scanKeys() or swiWaitForVBlank() missing in flushAll loop")

    if errors:
        print("[FAIL] Verification 1 encountered errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("[PASS] Verification 1 PASSED: All structural AST and hardware rules successfully verified!")

if __name__ == "__main__":
    verify_structural()

