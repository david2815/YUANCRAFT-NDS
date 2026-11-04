class MockAsyncSaveManager:
    QUEUE_CAPACITY = 8
    
    def __init__(self):
        self.s_queue = [None] * self.QUEUE_CAPACITY
        self.s_head = 0
        self.s_tail = 0
        self.s_pendingCount = 0
        self.s_totalTasks = 0
        self.s_completedTasks = 0
        self.s_sessionActive = False
        self.s_sessionSuccess = False
        self.s_allEnqueued = False

    def startSaveSession(self, totalTasks):
        self.s_totalTasks = max(0, totalTasks)
        self.s_completedTasks = 0
        self.s_sessionActive = True
        self.s_sessionSuccess = False
        self.s_allEnqueued = False

    def enqueueSave(self, path):
        if self.s_pendingCount >= self.QUEUE_CAPACITY:
            self.processQueue()

        slot = -1
        for i in range(self.QUEUE_CAPACITY):
            idx = (self.s_tail + i) % self.QUEUE_CAPACITY
            if self.s_queue[idx] is None:
                slot = idx
                break
        if slot == -1:
            return False

        self.s_queue[slot] = path
        self.s_tail = (slot + 1) % self.QUEUE_CAPACITY
        self.s_pendingCount += 1
        return True

    def processQueue(self):
        if self.s_pendingCount <= 0:
            if self.s_sessionActive and self.s_allEnqueued and self.s_pendingCount == 0:
                self.s_completedTasks = self.s_totalTasks
                self.s_sessionActive = False
                self.s_sessionSuccess = True
            return

        slot = -1
        for i in range(self.QUEUE_CAPACITY):
            idx = (self.s_head + i) % self.QUEUE_CAPACITY
            if self.s_queue[idx] is not None:
                slot = idx
                break
        if slot == -1:
            if self.s_sessionActive and self.s_allEnqueued:
                self.s_completedTasks = self.s_totalTasks
                self.s_sessionActive = False
                self.s_sessionSuccess = True
            return

        self.s_queue[slot] = None
        self.s_head = (slot + 1) % self.QUEUE_CAPACITY
        self.s_pendingCount -= 1
        self.s_completedTasks += 1

        if self.s_sessionActive and self.s_allEnqueued and self.s_pendingCount == 0:
            self.s_completedTasks = self.s_totalTasks
            self.s_sessionActive = False
            self.s_sessionSuccess = True
        elif self.s_sessionActive and self.s_totalTasks > 0 and self.s_completedTasks >= self.s_totalTasks and self.s_pendingCount == 0:
            self.s_sessionActive = False
            self.s_sessionSuccess = True

    def notifyAllEnqueued(self, totalActual):
        if totalActual >= 0:
            self.s_totalTasks = totalActual
        self.s_allEnqueued = True
        if self.s_sessionActive and self.s_pendingCount == 0:
            self.s_completedTasks = self.s_totalTasks
            self.s_sessionActive = False
            self.s_sessionSuccess = True

    def getProgressPercent(self):
        if not self.s_sessionActive and self.s_sessionSuccess:
            return 100
        if self.s_totalTasks <= 0:
            return 100 if (self.s_allEnqueued and self.s_pendingCount == 0) else 0
        p = int((self.s_completedTasks * 100) / self.s_totalTasks)
        return min(100, p)

    def isSavingComplete(self):
        if not self.s_sessionActive:
            return True
        if self.s_allEnqueued and self.s_pendingCount == 0:
            self.s_completedTasks = self.s_totalTasks
            self.s_sessionActive = False
            self.s_sessionSuccess = True
            return True
        if self.s_totalTasks > 0 and self.s_completedTasks >= self.s_totalTasks and self.s_pendingCount == 0:
            self.s_sessionActive = False
            self.s_sessionSuccess = True
            return True
        return False


def test_scenario(mod_chunks):
    print(f"\n--- Testing Scenario: modChunks = {mod_chunks} ---")
    asm = MockAsyncSaveManager()

    # Step 1: User hits Save
    asm.startSaveSession(mod_chunks)
    assert asm.getProgressPercent() == 0

    # Step 2: Serialization frame (enqueuing all chunks)
    for i in range(mod_chunks):
        asm.enqueueSave(f"/chunk_{i}.dat")
    asm.notifyAllEnqueued(mod_chunks)

    # Step 3: Pacing frames (draining queue)
    history = [asm.getProgressPercent()]
    frames = 0
    while not asm.isSavingComplete():
        frames += 1
        asm.processQueue()
        history.append(asm.getProgressPercent())
        assert frames <= 100, "Deadlock detected! Exceeded 100 frames!"

    print(f" Frames to complete: {frames}")
    print(f" Progress history: {history}")
    assert asm.isSavingComplete() == True
    assert asm.getProgressPercent() == 100
    assert asm.s_completedTasks == asm.s_totalTasks
    assert asm.s_sessionSuccess == True
    print(f" [PASS] modChunks = {mod_chunks} completed cleanly to 100% without getting stuck!")

if __name__ == "__main__":
    print("=== SAVE PROGRESS SIMULATION TEST ===")
    test_scenario(8)   # The exact 61% case
    test_scenario(0)   # Empty save case
    test_scenario(1)   # 1 chunk case
    test_scenario(20)  # Overflow capacity case (20 chunks)
    print("\nALL SAVE PROGRESS TESTS PASSED SUCCESSFULLY!")
