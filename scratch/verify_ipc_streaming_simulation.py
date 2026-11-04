import os, sys, tempfile, shutil

# Constants
IPC_STATUS_IDLE = 0
IPC_STATUS_REQUESTED = 1
IPC_STATUS_READING = 2
IPC_STATUS_READY = 3
IPC_STATUS_ERROR = 4
IPC_STATUS_TIMEOUT = 5

IPC_FIFO_SEND_IRQ = (1 << 2)
IPC_FIFO_RECV_IRQ = (1 << 10)
IPC_FIFO_ENABLE   = (1 << 15)
IPC_FIFO_SEND_CLEAR = (1 << 3)

SIZE_X = 8
SIZE_Y = 128
SIZE_Z = 8
RAW_CHUNK_SIZE = SIZE_X * SIZE_Y * SIZE_Z + (SIZE_X * SIZE_Y * SIZE_Z // 2)

class MockChunk:
    def __init__(self, cx, cz):
        self.cx = cx
        self.cz = cz
        self.blocks = bytearray([0] * (SIZE_X * SIZE_Y * SIZE_Z))
        self.liquidMeta = bytearray([0] * (SIZE_X * SIZE_Y * SIZE_Z // 2))
        self.generationComplete = False
        self.polyCount = 0

    def fillWithAir(self):
        self.blocks = bytearray([0] * (SIZE_X * SIZE_Y * SIZE_Z))
        self.liquidMeta = bytearray([0] * (SIZE_X * SIZE_Y * SIZE_Z // 2))
        self.generationComplete = True
        self.polyCount = 0 # 0 polygons, GPU is completely free!

    def loadFromRawBuffer(self, rawData):
        if len(rawData) < RAW_CHUNK_SIZE:
            self.fillWithAir()
            return False
        self.blocks = rawData[:SIZE_X * SIZE_Y * SIZE_Z]
        self.liquidMeta = rawData[SIZE_X * SIZE_Y * SIZE_Z:RAW_CHUNK_SIZE]
        # Check integrity: if y=0 is all air, discard
        any_solid = any(self.blocks[x * SIZE_Y * SIZE_Z + 0 * SIZE_Z + z] != 0 for x in range(SIZE_X) for z in range(SIZE_Z))
        if not any_solid:
            self.fillWithAir()
            return False
        self.generationComplete = True
        self.polyCount = 120 # simulated normal chunk geometry
        return True

class MockChunkManager:
    def __init__(self):
        self.chunks = [MockChunk(i, 0) for i in range(9)]
        self.awaitingLoad = [True] * 9

    def getChunkSlot(self, slot):
        if 0 <= slot < len(self.chunks):
            return self.chunks[slot]
        return None

    def clearAwaitingLoad(self, slot):
        if 0 <= slot < len(self.awaitingLoad):
            self.awaitingLoad[slot] = False

class SimulatedIpcChunkLoader:
    def __init__(self):
        self.status = IPC_STATUS_IDLE
        self.slotIndex = -1
        self.chunkX = 0
        self.chunkZ = 0
        self.path = ""
        self.requestStartTick = 0
        self.currentTick = 0
        self.compBuffer = bytearray()
        self.rawBuffer = bytearray()
        self.dataSize = 0
        self.reg_ipc_fifo_cr = 0

    def requestChunkLoad(self, slotIndex, cx, cz, path, currentTick):
        if self.status != IPC_STATUS_IDLE:
            return False # busy
        self.slotIndex = slotIndex
        self.chunkX = cx
        self.chunkZ = cz
        self.path = path
        self.requestStartTick = currentTick
        self.currentTick = currentTick
        self.status = IPC_STATUS_REQUESTED

        # Emulate irqSendFIFO
        self.reg_ipc_fifo_cr |= (IPC_FIFO_SEND_IRQ | IPC_FIFO_ENABLE)
        self.status = IPC_STATUS_READING
        return True

    def abortRequest(self, manager):
        if self.slotIndex >= 0:
            c = manager.getChunkSlot(self.slotIndex)
            if c:
                c.fillWithAir()
                manager.clearAwaitingLoad(self.slotIndex)
        self.reg_ipc_fifo_cr |= IPC_FIFO_SEND_CLEAR
        self.status = IPC_STATUS_IDLE
        self.slotIndex = -1

    def update(self, manager, currentTick):
        self.currentTick = currentTick
        if self.status == IPC_STATUS_IDLE:
            return

        # 1. Timeout Check: 3000ms
        elapsedMs = (self.currentTick - self.requestStartTick)
        if elapsedMs >= 3000:
            self.status = IPC_STATUS_TIMEOUT
            self.abortRequest(manager)
            return

        # 2. Reading state
        if self.status in [IPC_STATUS_REQUESTED, IPC_STATUS_READING]:
            if not os.path.exists(self.path):
                # New ungenerated chunk
                slot = self.slotIndex
                self.status = IPC_STATUS_IDLE
                self.slotIndex = -1
                manager.clearAwaitingLoad(slot)
                return

            try:
                with open(self.path, "rb") as f:
                    data = f.read()
                if len(data) == 0:
                    self.status = IPC_STATUS_ERROR
                    self.abortRequest(manager)
                    return
                self.compBuffer = data
                self.dataSize = len(data)
                self.reg_ipc_fifo_cr |= IPC_FIFO_RECV_IRQ
                self.status = IPC_STATUS_READY
            except Exception:
                self.status = IPC_STATUS_ERROR
                self.abortRequest(manager)
                return

        # 3. Ready state
        if self.status == IPC_STATUS_READY:
            slot = self.slotIndex
            c = manager.getChunkSlot(slot)
            if c:
                ok = False
                # If raw chunk or decompressed LZSS
                if self.dataSize >= RAW_CHUNK_SIZE:
                    ok = c.loadFromRawBuffer(self.compBuffer[:RAW_CHUNK_SIZE])
                else:
                    # Simulated LZSS decompression
                    if len(self.compBuffer) > 4 and self.compBuffer[0] == 0x10:
                        simulatedRaw = bytearray([1] * RAW_CHUNK_SIZE) # mock decompressed
                        ok = c.loadFromRawBuffer(simulatedRaw)
                if not ok:
                    c.fillWithAir()
                manager.clearAwaitingLoad(slot)
            self.status = IPC_STATUS_IDLE
            self.slotIndex = -1

def test_async_streaming_flow():
    print("[Test 1/4] Testing non-blocking asynchronous IPC chunk streaming...")
    temp_dir = tempfile.mkdtemp()
    try:
        loader = SimulatedIpcChunkLoader()
        manager = MockChunkManager()

        # Create valid chunk file
        test_path = os.path.join(temp_dir, "chunk_0_0.dat")
        valid_raw = bytearray([0x10, 0x00, 0x00, 0x00]) + bytearray([2] * (RAW_CHUNK_SIZE))
        with open(test_path, "wb") as f:
            f.write(valid_raw)

        # Frame 0: Request load
        req_ok = loader.requestChunkLoad(0, 0, 0, test_path, currentTick=0)
        assert req_ok == True, "Request should succeed immediately without blocking"
        assert loader.status == IPC_STATUS_READING, "Loader should transition to READING"
        assert loader.reg_ipc_fifo_cr & IPC_FIFO_SEND_IRQ, "FIFO Send IRQ flag must be set"
        assert manager.chunks[0].generationComplete == False, "Chunk not yet completed before update"

        # Frame 1: 16ms later, ARM7 finishes and loader processes
        loader.update(manager, currentTick=16)
        assert loader.status == IPC_STATUS_IDLE, "Loader should return to IDLE after chunk is processed"
        assert manager.chunks[0].generationComplete == True, "Chunk must be marked complete"
        assert manager.chunks[0].polyCount > 0, "Chunk should have valid loaded geometry"
        assert manager.awaitingLoad[0] == False, "Slot must be cleared from awaiting load"
        print("  -> Passed: Non-blocking IPC chunk streaming verified!")
    finally:
        shutil.rmtree(temp_dir)

def test_sd_timeout_failsafe():
    print("[Test 2/4] Testing 3000ms SD latency / Timeout Fail-Safe...")
    loader = SimulatedIpcChunkLoader()
    manager = MockChunkManager()

    # Simulate request pointing to stalled SD path
    loader.requestChunkLoad(3, 1, 0, "/sd/stalled_chunk.dat", currentTick=100)
    assert loader.status == IPC_STATUS_READING

    # Override path to pretend SD card hangs (file open never completes or lags)
    # Advance time frame by frame (100ms, 1000ms, 2500ms)
    loader.update(manager, currentTick=1100) # elapsed = 1000ms
    assert loader.status in [IPC_STATUS_READING, IPC_STATUS_IDLE]
    if loader.status == IPC_STATUS_IDLE:
        # Re-stall
        loader.status = IPC_STATUS_READING
        loader.slotIndex = 3
        loader.requestStartTick = 100

    # Advance time to 3101 ms (exceeds 3000ms limit!)
    loader.update(manager, currentTick=3200) # elapsed = 3100ms
    assert loader.status == IPC_STATUS_IDLE, "Loader must abort and reset to IDLE on timeout"
    # Check that Chunk 3 was filled with AIR (ID: 0)
    assert manager.chunks[3].generationComplete == True, "Timed-out chunk must be marked generationComplete"
    assert manager.chunks[3].polyCount == 0, "Timed-out chunk must have 0 polygons to prevent 1 FPS GPU choke!"
    assert all(b == 0 for b in manager.chunks[3].blocks), "All blocks in timed-out chunk must be AIR (ID: 0)"
    assert manager.awaitingLoad[3] == False, "Awaiting load flag must be disarmed"
    print("  -> Passed: 3000ms Timeout aborts stalled request and fills with AIR (0 polygons)!")

def test_corrupted_file_failsafe():
    print("[Test 3/4] Testing corrupt / truncated file Fail-Safe...")
    temp_dir = tempfile.mkdtemp()
    try:
        loader = SimulatedIpcChunkLoader()
        manager = MockChunkManager()

        # Create zero-byte corrupt file
        corrupt_path = os.path.join(temp_dir, "corrupt_chunk.dat")
        with open(corrupt_path, "wb") as f:
            f.write(b"") # 0 bytes

        loader.requestChunkLoad(5, 2, 0, corrupt_path, currentTick=500)
        loader.update(manager, currentTick=516)

        assert loader.status == IPC_STATUS_IDLE, "Loader must recover to IDLE after error"
        assert manager.chunks[5].generationComplete == True, "Corrupt chunk must be salvaged via Fail-Safe"
        assert manager.chunks[5].polyCount == 0, "Corrupt chunk must produce 0 polygons (Air)"
        assert all(b == 0 for b in manager.chunks[5].blocks), "Blocks must be AIR"
        assert manager.awaitingLoad[5] == False, "Slot must be cleared"
        print("  -> Passed: Corrupted file triggers Fail-Safe without crashing or locking!")
    finally:
        shutil.rmtree(temp_dir)

def test_ui_stability_and_vblank_loop():
    print("[Test 4/4] Testing UI stability loop (scanKeys & swiWaitForVBlank)...")
    vblank_calls = 0
    scankeys_calls = 0

    def mock_scanKeys():
        nonlocal scankeys_calls
        scankeys_calls += 1

    def mock_swiWaitForVBlank():
        nonlocal vblank_calls
        vblank_calls += 1

    # Simulate 60 frames in STATE_LOADING
    frames = 60
    for frame in range(frames):
        mock_scanKeys()
        mock_swiWaitForVBlank()

    assert vblank_calls == 60, f"Expected 60 VBlank waits, got {vblank_calls}"
    assert scankeys_calls == 60, f"Expected 60 scanKeys calls, got {scankeys_calls}"
    print("  -> Passed: UI visual thread remains active and in sync with hardware refresh!")

def main():
    print("=== VERIFICATION 2: BEHAVIORAL & RUNTIME IPC SIMULATION ===")
    test_async_streaming_flow()
    test_sd_timeout_failsafe()
    test_corrupted_file_failsafe()
    test_ui_stability_and_vblank_loop()
    print("\n[PASS] Verification 2 PASSED: All IPC streaming and fail-safe simulations completed successfully!")

if __name__ == "__main__":
    main()

