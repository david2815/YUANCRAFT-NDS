import os

path = r"source/Chunk.cpp"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: breakBlockDirect in Chunk.cpp
target1 = """    BlockType oldType = blocks[xi][yi][zi];
    const int oldMeta = liquidMetaGet(xi, yi, zi);
    blocks[xi][yi][zi] = BlockType::AIR;
    modified = true;"""

replacement1 = """    BlockType oldType = blocks[xi][yi][zi];
    const int oldMeta = liquidMetaGet(xi, yi, zi);
    blocks[xi][yi][zi] = BlockType::AIR;
    rleCols[xi][zi].set(yi, BlockType::AIR); // Sincronizacion RLE en RAM activa
    modified = true;"""

if target1 in content:
    content = content.replace(target1, replacement1, 1)
    print("Fix 1 applied successfully.")
else:
    print("Target 1 not found!")

# Fix 2: Liquid flow block update in Chunk.cpp
target2 = """    if (isLiquidBlock(oldType) && isLiquidBlock(type) && liquidMaterial(oldType) == liquidMaterial(type)) {
        blocks[xi][yi][zi] = type;
        liquidMetaSet(xi, yi, zi, meta);
        modified = true;
    }"""

replacement2 = """    if (isLiquidBlock(oldType) && isLiquidBlock(type) && liquidMaterial(oldType) == liquidMaterial(type)) {
        blocks[xi][yi][zi] = type;
        if (oldType != type) rleCols[xi][zi].set(yi, type); // Sincronizacion RLE
        liquidMetaSet(xi, yi, zi, meta);
        modified = true;
    }"""

if target2 in content:
    content = content.replace(target2, replacement2, 1)
    print("Fix 2 applied successfully.")
else:
    print("Target 2 not found!")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Chunk.cpp written.")

