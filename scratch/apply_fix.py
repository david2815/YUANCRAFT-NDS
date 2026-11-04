import sys

file_path = "source/Chunk.cpp"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. getBlockType
target_1 = """BlockType Chunk::getBlockType(int xi, int yi, int zi) const {
    if (xi < 0 || xi >= SIZE_X) return BlockType::AIR;
    if (yi < 0 || yi >= SIZE_Y) return BlockType::AIR;
    if (zi < 0 || zi >= SIZE_Z) return BlockType::AIR;
    // Lectura directa desde el formato RLE en RAM activa para maximo rendimiento
    return rleCols[xi][zi].get(yi);
}"""

replacement_1 = """BlockType Chunk::getBlockType(int xi, int yi, int zi) const {
    if (xi < 0 || xi >= SIZE_X) return BlockType::AIR;
    if (yi < 0 || yi >= SIZE_Y) return BlockType::AIR;
    if (zi < 0 || zi >= SIZE_Z) return BlockType::AIR;
    return blocks[xi][yi][zi];
}"""

assert target_1 in content, "target_1 not found"
content = content.replace(target_1, replacement_1, 1)

# 2. rebuildColumnOccupancy
target_2 = """void Chunk::rebuildColumnOccupancy(int xi, int zi) {
    occupancy[xi][zi][0] = 0;
    occupancy[xi][zi][1] = 0;
    occupancy[xi][zi][2] = 0;
    occupancy[xi][zi][3] = 0;

    // Aceleracion RLE: iteramos los tramos continuos directamente O(runs)
    // en lugar de 128 iteraciones individuales. Zonas continuas de aire o piedra
    // se procesan de un solo paso.
    const VoxelColumnRLE& col = rleCols[xi][zi];
    int y = 0;
    for (int r = 0; r < col.runCount; r++) {
        BlockType t = col.runs[r].type;
        int len = col.runs[r].length;
        if (isNormalCube(t)) {
            for (int k = 0; k < len; k++) {
                int yi = y + k;
                occupancy[xi][zi][yi / 32] |= (1u << (yi % 32));
            }
        }
        y += len;
    }
}"""

replacement_2 = """void Chunk::rebuildColumnOccupancy(int xi, int zi) {
    occupancy[xi][zi][0] = 0;
    occupancy[xi][zi][1] = 0;
    occupancy[xi][zi][2] = 0;
    occupancy[xi][zi][3] = 0;

    for (int yi = 0; yi < SIZE_Y; yi++) {
        if (isSolidGrid(xi, yi, zi)) {
            occupancy[xi][zi][yi >> 5] |= (1u << (yi & 31));
        }
    }
}"""

assert target_2 in content, "target_2 not found"
content = content.replace(target_2, replacement_2, 1)

# 3. generateSpruceTree1 leaf check
target_3 = """                if (nlXi >= 0 && nlXi < SIZE_X && nlZi >= 0 && nlZi < SIZE_Z) {
                    if (worldLy >= 0 && worldLy < SIZE_Y && blocks[nlXi][worldLy][nlZi] == BlockType::AIR) {
                        setBlockDirect(nlXi, worldLy, nlZi, BlockType::SPRUCE_LEAVES, manager);
                    }
                } else if (manager) {
                    Chunk* neighbor = manager->getChunkAt(worldX, worldZ);
                    if (neighbor) {
                        int nXi, nYi, nZi;
                        if (neighbor->worldToGrid(worldX, worldY, worldZ, nXi, nYi, nZi)) {
                            if (neighbor->getBlockType(nXi, nYi, nZi) == BlockType::AIR) {
                                neighbor->setBlockDirect(nXi, nYi, nZi, BlockType::SPRUCE_LEAVES, manager);
                            }
                        }
                    }
                }"""

replacement_3 = """                if (nlXi >= 0 && nlXi < SIZE_X && nlZi >= 0 && nlZi < SIZE_Z) {
                    if (worldLy >= 0 && worldLy < SIZE_Y) {
                        BlockType cur = blocks[nlXi][worldLy][nlZi];
                        if (cur == BlockType::AIR || cur == BlockType::SNOW_LAYER || cur == BlockType::TALLGRASS) {
                            setBlockDirect(nlXi, worldLy, nlZi, BlockType::SPRUCE_LEAVES, manager);
                        }
                    }
                } else if (manager) {
                    Chunk* neighbor = manager->getChunkAt(worldX, worldZ);
                    if (neighbor) {
                        int nXi, nYi, nZi;
                        if (neighbor->worldToGrid(worldX, worldY, worldZ, nXi, nYi, nZi)) {
                            BlockType cur = neighbor->getBlockType(nXi, nYi, nZi);
                            if (cur == BlockType::AIR || cur == BlockType::SNOW_LAYER || cur == BlockType::TALLGRASS) {
                                neighbor->setBlockDirect(nXi, nYi, nZi, BlockType::SPRUCE_LEAVES, manager);
                            }
                        }
                    }
                }"""

assert target_3 in content, "target_3 not found"
# Replace first occurrence (in generateSpruceTree1)
content = content.replace(target_3, replacement_3, 1)
# Replace second occurrence (in generateSpruceTree2)
assert target_3 in content, "target_3 second occurrence not found"
content = content.replace(target_3, replacement_3, 1)

# 4. bigTreePlaceSphereLayer
target_4 = """            BlockType existing = self->bigTreeGetBlock(manager, pos[0], pos[1], pos[2]);
            if (existing != BlockType::AIR && existing != BlockType::OAK_LEAVES) continue;

            self->bigTreeSetBlock(manager, pos[0], pos[1], pos[2], blockType);"""

replacement_4 = """            BlockType existing = self->bigTreeGetBlock(manager, pos[0], pos[1], pos[2]);
            if (existing != BlockType::AIR && existing != BlockType::OAK_LEAVES &&
                existing != BlockType::SNOW_LAYER && existing != BlockType::TALLGRASS) continue;

            self->bigTreeSetBlock(manager, pos[0], pos[1], pos[2], blockType);"""

assert target_4 in content, "target_4 not found"
content = content.replace(target_4, replacement_4, 1)

# 5. generateTrees ground check and leaf placement
target_5_ground = """                    int highestY = getHighestSolidY(xi, zi);
                    if (highestY >= 0 && blocks[xi][highestY][zi] == BlockType::GRASS) {"""

replacement_5_ground = """                    int highestY = getHighestSolidY(xi, zi);
                    if (highestY >= 0 && (blocks[xi][highestY][zi] == BlockType::GRASS || blocks[xi][highestY][zi] == BlockType::DIRT)) {"""

assert target_5_ground in content, "target_5_ground not found"
content = content.replace(target_5_ground, replacement_5_ground, 1)

target_5_leaves = """                                            if (nlXi >= 0 && nlXi < SIZE_X && nlZi >= 0 && nlZi < SIZE_Z) {
                                                if (ly >= 0 && ly < SIZE_Y && blocks[nlXi][ly][nlZi] == BlockType::AIR) {
                                                    setBlockDirect(nlXi, ly, nlZi, leafType, manager);
                                                }
                                            } else if (manager) {
                                                Chunk* neighbor = manager->getChunkAt(worldX, worldZ);
                                                if (neighbor) {
                                                    int nXi, nYi, nZi;
                                                    if (neighbor->worldToGrid(worldX, worldY, worldZ, nXi, nYi, nZi)) {
                                                        if (neighbor->getBlockType(nXi, nYi, nZi) == BlockType::AIR) {
                                                            neighbor->setBlockDirect(nXi, nYi, nZi, leafType, manager);
                                                        }
                                                    }
                                                }
                                            }"""

replacement_5_leaves = """                                            if (nlXi >= 0 && nlXi < SIZE_X && nlZi >= 0 && nlZi < SIZE_Z) {
                                                if (ly >= 0 && ly < SIZE_Y) {
                                                    BlockType cur = blocks[nlXi][ly][nlZi];
                                                    if (cur == BlockType::AIR || cur == BlockType::SNOW_LAYER || cur == BlockType::TALLGRASS) {
                                                        setBlockDirect(nlXi, ly, nlZi, leafType, manager);
                                                    }
                                                }
                                            } else if (manager) {
                                                Chunk* neighbor = manager->getChunkAt(worldX, worldZ);
                                                if (neighbor) {
                                                    int nXi, nYi, nZi;
                                                    if (neighbor->worldToGrid(worldX, worldY, worldZ, nXi, nYi, nZi)) {
                                                        BlockType cur = neighbor->getBlockType(nXi, nYi, nZi);
                                                        if (cur == BlockType::AIR || cur == BlockType::SNOW_LAYER || cur == BlockType::TALLGRASS) {
                                                            neighbor->setBlockDirect(nXi, nYi, nZi, leafType, manager);
                                                        }
                                                    }
                                                }
                                            }"""

assert target_5_leaves in content, "target_5_leaves not found"
content = content.replace(target_5_leaves, replacement_5_leaves, 1)

# 6. generateTrees loop budget
target_6 = """            zi++;
            processed++;
            s_heavyDidOne = true;
            if (processed >= BATCH_SIZE || !heavyBudgetLeft()) {
                outXi = xi;
                outZi = zi;
                done = false;
                return;
            }"""

replacement_6 = """            zi++;
            processed++;
            s_heavyDidOne = true;
            if (!heavyBudgetLeft()) {
                outXi = xi;
                outZi = zi;
                done = false;
                return;
            }"""

assert target_6 in content, "target_6 not found"
# Replace first occurrence (in generateTrees)
content = content.replace(target_6, replacement_6, 1)
# Replace second occurrence (in generateCactus)
assert target_6 in content, "target_6 second occurrence (generateCactus) not found"
content = content.replace(target_6, replacement_6, 1)

# 7. generateOres MAX_VEINS_PER_CALL
target_7 = """    const int UNITS = 9 * UNITS_PER_SRC;               // 9 chunks de origen
    const int MAX_VEINS_PER_CALL = 1;          // vetas con trabajo real por llamada"""

replacement_7 = """    const int UNITS = 9 * UNITS_PER_SRC;               // 9 chunks de origen
    const int MAX_VEINS_PER_CALL = 6;          // vetas con trabajo real por llamada dentro del presupuesto"""

assert target_7 in content, "target_7 not found"
content = content.replace(target_7, replacement_7, 1)

with open(file_path, "w", encoding="utf-8", newline="\r\n") as f:
    f.write(content)

print("All fixes applied successfully to source/Chunk.cpp!")

