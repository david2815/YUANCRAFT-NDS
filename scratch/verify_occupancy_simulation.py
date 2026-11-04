print("=== VERIFICATION ROUND 2: Bitwise Simulation of Occupancy & Face Masks ===")

# Voxel types
AIR = 0
GRASS = 1
OAK_LOG = 2
OAK_LEAVES = 3

def isSolidGrid(block_type):
    return block_type in (GRASS, OAK_LOG, OAK_LEAVES)

def isNormalCube_BUGGY(block_type):
    # This was the bug: leaves were NOT normal cubes
    return block_type in (GRASS, OAK_LOG)

def simulate_column(blocks_col, use_fixed_version=True):
    # 128 layers, 4 x 32-bit words
    occupancy = [0, 0, 0, 0]
    for yi in range(128):
        solid = isSolidGrid(blocks_col[yi]) if use_fixed_version else isNormalCube_BUGGY(blocks_col[yi])
        if solid:
            occupancy[yi // 32] |= (1 << (yi % 32))
    return occupancy

def shiftDown1(occ):
    # bit yi = occupacion de yi + 1
    out = [0, 0, 0, 0]
    out[0] = (occ[0] >> 1) | ((occ[1] & 1) << 31)
    out[1] = (occ[1] >> 1) | ((occ[2] & 1) << 31)
    out[2] = (occ[2] >> 1) | ((occ[3] & 1) << 31)
    out[3] = (occ[3] >> 1)
    return out

def shiftUp1(occ):
    # bit yi = occupacion de yi - 1
    out = [0, 0, 0, 0]
    out[0] = (occ[0] << 1) & 0xFFFFFFFF
    out[1] = ((occ[1] << 1) | (occ[0] >> 31)) & 0xFFFFFFFF
    out[2] = ((occ[2] << 1) | (occ[1] >> 31)) & 0xFFFFFFFF
    out[3] = ((occ[3] << 1) | (occ[2] >> 31)) & 0xFFFFFFFF
    return out

# Set up column with a tree leaf at yi = 68 and air above at yi = 69
blocks = [AIR] * 128
for y in range(0, 64):
    blocks[y] = GRASS
blocks[64] = OAK_LOG
blocks[65] = OAK_LOG
blocks[66] = OAK_LOG
blocks[67] = OAK_LEAVES
blocks[68] = OAK_LEAVES
# y=69..127 is AIR

print("Testing tree column: y=67..68 has OAK_LEAVES, y=69 has AIR")

# 1. Buggy simulation
occ_buggy = simulate_column(blocks, use_fixed_version=False)
above_buggy = shiftDown1(occ_buggy)
topMask_buggy = [occ_buggy[w] & ~above_buggy[w] for w in range(4)]
leaf_top_face_buggy = (topMask_buggy[68 // 32] & (1 << (68 % 32))) != 0

print(f"[BUGGY BEHAVIOR CONFIRMED] Leaf at y=68 top face visible? {leaf_top_face_buggy}")
assert leaf_top_face_buggy == False, "Buggy code should have rendered no leaf face!"

# 2. Fixed simulation
occ_fixed = simulate_column(blocks, use_fixed_version=True)
above_fixed = shiftDown1(occ_fixed)
below_fixed = shiftUp1(occ_fixed)

topMask_fixed = [occ_fixed[w] & ~above_fixed[w] for w in range(4)]
bottomMask_fixed = [occ_fixed[w] & ~below_fixed[w] for w in range(4)]

leaf_top_face_fixed = (topMask_fixed[68 // 32] & (1 << (68 % 32))) != 0
leaf_between_cull_fixed = (topMask_fixed[67 // 32] & (1 << (67 % 32))) != 0

print(f"[FIXED BEHAVIOR CONFIRMED] Leaf at y=68 (adjacent to AIR) top face visible? {leaf_top_face_fixed}")
print(f"[FIXED BEHAVIOR CONFIRMED] Leaf at y=67 (adjacent to leaf at y=68) top face culled? {not leaf_between_cull_fixed}")

assert leaf_top_face_fixed == True, "Fixed code MUST render top face when adjacent to AIR!"
assert leaf_between_cull_fixed == False, "Fixed code MUST cull internal face when adjacent to another LEAF!"

print("\nROUND 2 PASSED: Mathematical proof that tree leaves are rendered to air and culled internally!")

