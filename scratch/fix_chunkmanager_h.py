with open("source/ChunkManager.h", "r", encoding="utf-8") as f:
    text = f.read()

# Remove from private:
old_private = """    int findOrCreateSlot(int cx, int cz, const int* protectX = nullptr, const int* protectZ = nullptr, int protectCount = 0);
    Chunk* getChunkSlot(int slot) {
        if (slot >= 0 && slot < maxChunks && slotUsed[slot]) return chunks[slot];
        return nullptr;
    }
    void clearAwaitingLoad(int slot) {
        if (slot >= 0 && slot < maxChunks) {
            awaitingLoad[slot] = false;
            loadingBiome[slot] = false;
        }
    }"""

new_private = "    int findOrCreateSlot(int cx, int cz, const int* protectX = nullptr, const int* protectZ = nullptr, int protectCount = 0);"
assert old_private in text, "old_private not found"
text = text.replace(old_private, new_private)

# Add to public:
old_public = "    Chunk* getCenterChunk() const { return chunks[centerIndex]; }"
new_public = """    Chunk* getCenterChunk() const { return chunks[centerIndex]; }
    Chunk* getChunkSlot(int slot) {
        if (slot >= 0 && slot < maxChunks && slotUsed[slot]) return chunks[slot];
        return nullptr;
    }
    void clearAwaitingLoad(int slot) {
        if (slot >= 0 && slot < maxChunks) {
            awaitingLoad[slot] = false;
            loadingBiome[slot] = false;
        }
    }"""
assert old_public in text, "old_public not found"
text = text.replace(old_public, new_public)

with open("source/ChunkManager.h", "w", encoding="utf-8") as f:
    f.write(text)
print("Moved getChunkSlot and clearAwaitingLoad to public section of ChunkManager.h")

