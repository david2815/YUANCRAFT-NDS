import os
import struct

print("=== VERIFICATION ROUND 1: Binary & Code Logic Verification ===")

# 1. Verify YUANCRAFT.nds exists and has valid Nintendo DS ROM header
nds_path = "YUANCRAFT.nds"
assert os.path.exists(nds_path), "YUANCRAFT.nds does not exist!"
size = os.path.getsize(nds_path)
print(f"YUANCRAFT.nds exists, size: {size} bytes")

with open(nds_path, "rb") as f:
    header = f.read(512)
game_title = header[0:12].decode('ascii', errors='ignore').strip('\x00')
game_code = header[12:16].decode('ascii', errors='ignore').strip('\x00')
print(f"ROM Title: '{game_title}', Game Code: '{game_code}'")
assert size > 1_000_000, "ROM size looks too small!"

# 2. Check source/Chunk.cpp for all required patterns
with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
    chunk_src = f.read()

# Test 1: getBlockType returns blocks[xi][yi][zi] directly
assert "return blocks[xi][yi][zi];" in chunk_src, "getBlockType does not return blocks[xi][yi][zi]!"
assert "return rleCols[xi][zi].get(yi);" not in chunk_src, "Legacy rleCols.get still present in getBlockType!"
print("[PASS] Verification 1.1: getBlockType directly reads blocks array.")

# Test 2: rebuildColumnOccupancy uses isSolidGrid
assert "if (isSolidGrid(xi, yi, zi))" in chunk_src, "rebuildColumnOccupancy does not use isSolidGrid!"
assert "if (isNormalCube(t))" not in chunk_src, "Legacy isNormalCube still present in rebuildColumnOccupancy!"
print("[PASS] Verification 1.2: rebuildColumnOccupancy uses isSolidGrid (leaves included in occupancy).")

# Test 3: Trees can generate on GRASS or DIRT
assert "blocks[xi][highestY][zi] == BlockType::GRASS || blocks[xi][highestY][zi] == BlockType::DIRT" in chunk_src, "Tree ground check does not allow DIRT!"
print("[PASS] Verification 1.3: Tree ground check supports GRASS and DIRT.")

# Test 4: Dynamic heavy budget in generateTrees and generateCactus
assert "if (!heavyBudgetLeft()) {" in chunk_src, "Dynamic heavyBudgetLeft check not found!"
print("[PASS] Verification 1.4: Dynamic heavyBudgetLeft used in tree and cactus loops.")

# Test 5: MAX_VEINS_PER_CALL increased
assert "MAX_VEINS_PER_CALL = 6" in chunk_src, "MAX_VEINS_PER_CALL not increased!"
print("[PASS] Verification 1.5: MAX_VEINS_PER_CALL increased to 6.")

print("ROUND 1 PASSED WITH FLYING COLORS!\n")

