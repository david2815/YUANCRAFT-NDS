# Graph Report - YUANCRAFT NDS PORT  (2026-11-03)

## Corpus Check
- 210 files · ~335,232 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 53 file(s) not represented in the graph (top: .grit 49, (none) 3, .exe 1)

## Summary
- 4228 nodes · 9488 edges · 170 communities (158 shown, 12 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1085 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bcd9968b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Block and Item Types
- Chunk Meshing and Bands
- PartialBlocks.cpp
- Block and Item Types
- Player Module
- Texture and Image Decoding
- Texture and Image Decoding
- HandAnimations.cpp
- Image Writing Utilities
- Block and Item Types
- Chunk.cpp
- Block and Item Types
- Painting and Art Types
- Weather.cpp
- Dropped Item Physics
- ChunkManager Module
- Block and Item Types
- AnimalModel.cpp
- Crafting Recipes
- NetherGen.h
- GameplayHotbar.cpp
- Block and Item Types
- Sound.cpp
- Inventory
- Entity AI (HostileAI)
- Furnace.cpp
- MenuFont.cpp
- DisplayListBuilder Module
- Spawners & Particles
- WorldSave Module
- ChunkManager
- string
- Pistons.cpp
- Texture & PaintingTex
- Controls & ItemOrder
- Texture and Image Decoding
- ChunkManager Module
- AnimalManager Module
- isTorchBlock
- Block and Item Types
- RailLogic Module
- Texture and Image Decoding
- Container Logic (ChestStore)
- Texture Module
- Block and Item Types
- Block and Item Types
- HostileManager Module
- Torch Module
- Vehicle Entity (MinecartManager)
- Projectiles Module
- SignManager Module
- Noise.cpp
- Profiler Module
- Profiler Module
- M
- InventoryScreen.cpp
- notify
- NewWorldMenu.cpp
- Caves & CaveSinTable
- Health Module
- HostileManager Module
- Vehicle Entity (MinecartModel)
- isLeavesBlock
- Texture and Image Decoding
- WorldSelectMenu Module
- AnimalAI.h
- BigTree
- Chunk.h
- main.cpp
- BoatManager.cpp
- Texture and Image Decoding
- PartialBlocks.h
- isPartialBlock
- Maps Module
- DebugChests.h
- nds
- NoteBlocks.cpp
- Minecraft: Nintendo DS Edition
- ModelBox.h
- GameOverScreen.cpp
- Teleporter.h
- Options Module
- 5.2 Blocks, items, inventory, crafting
- Biome & Chunk
- LightNode
- Caves Module
- Cube Module
- FishingHook.cpp
- HostileManager Module
- Projectiles Module
- Vehicle Entity (BoatModel)
- TickInput
- MobCull & Caves
- bigTreeComputeBranches
- AnimItems.cpp
- TextKeyboard Module
- Tick
- Caves Module
- Caves Module
- Vehicle Entity (MinecartManager)
- SettingsMenu Module
- Profiler.h
- MobBody & AnimalManager
- TopScreenMenu & Renderer
- TntManager.cpp
- Climate Module
- VoxelColumnRLE
- Projectiles Module
- Spike
- Env
- SheepManager Module
- SheepModel Module
- Drop
- Caves Module
- Liquid.cpp
- Lakes Module
- 7. World engine in detail
- Projectiles Module
- Drop
- build.sh
- PauseScreen Module
- 12. Rendering, textures and models
- HostileManager Module
- FlatQuad
- Climate Module
- HostileManager Module
- .isDSi
- Chunk.h
- LoadingScreen Module
- AnimalManager Module
- Clouds & CloudsData
- Texture.h
- State
- Vehicle Entity (MinecartManager)
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Caves Module
- PendingDrops.h
- HealthHudLayout Module
- Lakes Module
- RenderInput
- StartupSplash Module
- SubScreenMenu Module
- Falling
- Pose
- Chunk Module
- HostileManager Module
- Drop
- Redstone Logic (Redstone)
- RedstoneEntityCtx
- Caves Module
- Redstone.cpp
- ColorMaps & ColorMapData
- Kind
- HostileManager Module
- Redstone Logic (Redstone)
- Quad
- Redstone Logic (Redstone)
- T
- Sky.cpp
- ExplosionDamage.h
- P3
- NetherTerrain
- Chest.h
- P

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 211 edges
3. `main()` - 182 edges
4. `ChunkManager` - 95 edges
5. `Player` - 91 edges
6. `DroppedItem` - 61 edges
7. `Sim` - 48 edges
8. `isLiquidBlock()` - 44 edges
9. `isNormalCube()` - 44 edges
10. `Texture` - 42 edges

## Surprising Connections (you probably didn't know these)
- `2. Rules for an AI assistant modifying this project (read carefully)` --references--> `BlockType`  [INFERRED]
  CLAUDE.md → source/BlockType.h
- `9.5 World-generation pieces` --references--> `beginFrame()`  [INFERRED]
  CLAUDE.md → source/Caves.cpp
- `7.1c `tickLiquids` (20 Hz) and random ticks` --references--> `LiquidWorld`  [INFERRED]
  CLAUDE.md → source/ChunkManager.cpp
- `9.8 More internals (Nether, sky, saves, menus, chests, notes)` --references--> `resetLattice()`  [INFERRED]
  CLAUDE.md → source/NetherGen.h
- `9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`)` --references--> `packSpot()`  [INFERRED]
  CLAUDE.md → source/AnimalAI.h

## Import Cycles
- None detected.

## Communities (170 total, 12 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (87): 7.5 Meshing and drawing, BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor (+79 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.22
Nodes (31): 9.3 Liquids, particles, partial blocks, activate(), boxHit(), chunkOf(), cropCanStay(), cropsTick(), dropAt(), dropCrop() (+23 more)

### Community 3 - "Block and Item Types"
Cohesion: 0.06
Nodes (72): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+64 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (58): main(), ChunkManager, Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase, bobStrength, buttonLookSpeedH (+50 more)

### Community 5 - "Texture and Image Decoding"
Cohesion: 0.07
Nodes (59): main(), stbi_convert_iphone_png_to_rgb(), stbi_convert_iphone_png_to_rgb_thread(), stbi_convert_wchar_to_utf8(), stbi__do_zlib(), stbi_failure_reason(), stbi__float_postprocess(), stbi__fopen() (+51 more)

### Community 6 - "Texture and Image Decoding"
Cohesion: 0.09
Nodes (64): stbi__at_eof(), stbi__bitcount(), stbi__bmp_info(), stbi__bmp_load(), stbi__bmp_parse_header(), stbi__bmp_set_mask_defaults(), stbi__bmp_test(), stbi__bmp_test_raw() (+56 more)

### Community 7 - "HandAnimations.cpp"
Cohesion: 0.13
Nodes (26): 12.6 Mob models (`ModelBox.h`, `*Model.cpp`), isSword(), applyViewBobbing(), blockRenderColor(), brightnessOf(), drawBlockInHand(), drawFirstPersonArm(), drawItem2D() (+18 more)

### Community 8 - "Image Writing Utilities"
Cohesion: 0.09
Nodes (50): stb_image_write_test, stbi__end_write_file(), stbi_flip_vertically_on_write(), stbi__start_write_callbacks(), stbi__start_write_file(), stbi_write_bmp(), stbi_write_bmp_core(), stbi_write_bmp_to_func() (+42 more)

### Community 9 - "Block and Item Types"
Cohesion: 0.08
Nodes (23): findSpawn(), fireCatch(), fireEncourage(), isFlowingLiquid(), isLavaBlock(), isLiquidBlock(), isMaterialSolid(), isWaterBlock() (+15 more)

### Community 10 - "Chunk.cpp"
Cohesion: 0.06
Nodes (14): chunkFloorDiv(), fillDungeonChest(), getPatchAt(), oreFloorInt(), OreRng, s, oreVeinBlob(), placementTargetFree() (+6 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.06
Nodes (44): getGrassTint(), alloc(), baseMotion(), brightnessOf(), move(), P, active, age (+36 more)

### Community 12 - "Painting and Art Types"
Cohesion: 0.07
Nodes (36): Art, ox, oy, sx, sy, title, brightnessOf(), compute() (+28 more)

### Community 13 - "Weather.cpp"
Cohesion: 0.06
Nodes (39): Bolt, active, flashes, gx, gy, gz, life, seed (+31 more)

### Community 14 - "Dropped Item Physics"
Cohesion: 0.04
Nodes (42): DroppedItem, active, ageTicks, BOB_MAX, BOB_MIN, BOB_SPEED, bobPhase, count (+34 more)

### Community 15 - "ChunkManager Module"
Cohesion: 0.04
Nodes (42): ChunkManager, awaitingLoad, borderRefreshPending, CAP_CHUNKS, centerIndex, chunkPosX, chunkPosZ, chunks (+34 more)

### Community 16 - "Block and Item Types"
Cohesion: 0.13
Nodes (22): getBlockTextures(), torchMeta(), woolCell(), applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad(), drawLodTopQuad() (+14 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.19
Nodes (15): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+7 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.08
Nodes (19): CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt(), drawIconAt() (+11 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.06
Nodes (31): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+23 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.25
Nodes (3): GameplayHotbar, bgId, isInButtonRow()

### Community 21 - "Block and Item Types"
Cohesion: 0.07
Nodes (57): 8. Blocks and items, 9.7 Inventory and crafting UI internals, armorMaterial(), armorMaxDurability(), armorPiece(), armorReduceAmount(), armorRenderIndex(), blockHardness() (+49 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.06
Nodes (50): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 13. Audio, 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is (+42 more)

### Community 23 - "Inventory"
Cohesion: 0.08
Nodes (37): getToolMaxDurability(), ChestStore::transferWithInventory(), Furnace::transferWithInventory(), Inventory, ARMOR_BASE, ARMOR_SLOTS, HOTBAR_SIZE, MAX_STACK (+29 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.06
Nodes (63): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), airSpawnSpot(), arrowTick(), attackBlocked(), attackEntity(), brightnessAt(), canSee(), canSpawnHere() (+55 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.09
Nodes (30): canSmelt(), clearEntry(), clearSlot(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate(), Furnace::fuelBurnTime(), Furnace::loadFromFile() (+22 more)

### Community 26 - "MenuFont.cpp"
Cohesion: 0.23
Nodes (11): find(), Glyph, c, rows, MenuFont::draw16(), MenuFont::draw8(), MenuFont::fill16(), MenuFont::fill8() (+3 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "Spawners & Particles"
Cohesion: 0.09
Nodes (30): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+22 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.07
Nodes (28): 9.8 More internals (Nether, sky, saves, menus, chests, notes), SD card layout, clearFolderContents(), folderExists(), WorldMetadata, armorDurability, armorType, formatVersion (+20 more)

### Community 30 - "ChunkManager"
Cohesion: 0.23
Nodes (3): blockLightEmission(), isLightOpaque(), bigTreeDrawLine()

### Community 31 - "string"
Cohesion: 0.17
Nodes (4): draw(), OptionsMenu::open(), OptionsMenu::update(), printRow()

### Community 32 - "Pistons.cpp"
Cohesion: 0.08
Nodes (54): isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend(), canPush() (+46 more)

### Community 33 - "Texture & PaintingTex"
Cohesion: 0.07
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.09
Nodes (25): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+17 more)

### Community 35 - "Texture and Image Decoding"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.10
Nodes (10): AnimalManager::attack(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath(), countKind(), halfCap() (+2 more)

### Community 38 - "isTorchBlock"
Cohesion: 0.26
Nodes (5): isCrossPlant(), isTorchBlock(), callListFast(), flushList(), lodSkipTop()

### Community 40 - "RailLogic Module"
Cohesion: 0.13
Nodes (16): adjacentCount(), chainEnd(), chainPowered(), isRailAt(), Logic, c, n, powered (+8 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - "Container Logic (ChestStore)"
Cohesion: 0.10
Nodes (24): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+16 more)

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.14
Nodes (25): isRailBlock(), bodyBox(), Box, maxX, maxY, maxZ, minX, minY (+17 more)

### Community 45 - "Block and Item Types"
Cohesion: 0.09
Nodes (13): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::interact(), SheepManager::lightning() (+5 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.09
Nodes (11): 9.2 Managers: spawning, caps, explosions, collectDeath(), explode(), HostileManager::attack(), HostileManager::interact(), HostileManager::lightning(), HostileManager::popDrop(), pushDrop() (+3 more)

### Community 47 - "Torch Module"
Cohesion: 0.10
Nodes (29): isNormalCube(), autoMeta(), boundsForMeta(), Box, x0, x1, y0, y1 (+21 more)

### Community 48 - "Vehicle Entity (MinecartManager)"
Cohesion: 0.10
Nodes (15): breakCart(), cartCollision(), dismountIndex(), eyeOf(), getI32(), MinecartManager::attack(), MinecartManager::dismount(), MinecartManager::loadFromFile() (+7 more)

### Community 49 - "Projectiles Module"
Cohesion: 0.07
Nodes (28): Proj, active, inGround, kind, mx, my, mz, ownerIsPlayer (+20 more)

### Community 50 - "SignManager Module"
Cohesion: 0.08
Nodes (24): Box, q, brightnessOf(), buildBox(), ChunkManager, drawBox(), drawText(), find() (+16 more)

### Community 51 - "Noise.cpp"
Cohesion: 0.10
Nodes (15): Chunk::Chunk(), HeightCache, h, tx, tz, NetherColCache, c, tx (+7 more)

### Community 52 - "Profiler Module"
Cohesion: 0.18
Nodes (7): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike()

### Community 53 - "Profiler Module"
Cohesion: 0.13
Nodes (15): Slot, DL_CALL, DL_CULL, DL_LOD, DL_REBUILD, DRAW_ALL, ENTS, FACES (+7 more)

### Community 54 - "M"
Cohesion: 0.23
Nodes (18): burnedOut(), detectorCheck(), indirectlyGettingPowered(), indirectPowerAt(), indirectProvidingPowerTo(), M(), plateBox(), plateCheck() (+10 more)

### Community 55 - "InventoryScreen.cpp"
Cohesion: 0.08
Nodes (19): iconShapeVisible(), drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon(), getItemsPixelIndex(), getTerrainPixelIndex() (+11 more)

### Community 56 - "notify"
Cohesion: 0.21
Nodes (15): activate(), blockChanged(), blockRemoved(), buttonRelease(), drainRemoved(), flushWireSet(), handleRemoved(), notify() (+7 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.13
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves & CaveSinTable"
Cohesion: 0.16
Nodes (16): allocBlock(), beginFrame(), carveSphere(), carveStep(), emit(), floorD(), floorDiv(), floorF() (+8 more)

### Community 59 - "Health Module"
Cohesion: 0.08
Nodes (33): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), HealthState, air, armorPoints (+25 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.17
Nodes (17): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::count(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn() (+9 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "isLeavesBlock"
Cohesion: 0.14
Nodes (16): 9.5 World-generation pieces, isLeavesBlock(), isSapling(), freeOrLeaves(), genRound(), genSpruce(), isLog(), markLeaf() (+8 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.18
Nodes (4): clearLabelZone(), drawWorldName(), rebuildWorldList(), WorldSelectMenu

### Community 65 - "AnimalAI.h"
Cohesion: 0.06
Nodes (74): 12.7 Mob managers (how data, AI and model connect), anyIn(), blocking(), bodyBox(), Box, x0, x1, y0 (+66 more)

### Community 66 - "BigTree"
Cohesion: 0.13
Nodes (13): BigTree, AX, basePos, branchSlope, height, heightAttenuation, heightLimit, heightLimitLimit (+5 more)

### Community 67 - "Chunk.h"
Cohesion: 0.09
Nodes (27): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+19 more)

### Community 68 - "main.cpp"
Cohesion: 0.05
Nodes (37): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, ChunkManager, ChunkManager, ChestView, FurnaceData (+29 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.08
Nodes (23): BoatManager::attack(), BoatManager::dismount(), BoatManager::draw(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::riderEye(), BoatManager::saveToFile(), BoatManager::spawnFromRay() (+15 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "PartialBlocks.h"
Cohesion: 0.14
Nodes (18): 9.6 Audio internals (`Sound.cpp`), 9. Entities and physics notes, isPistonBlock(), isStairsBlock(), bedCell(), bedOffset(), bounds(), ChunkManager (+10 more)

### Community 72 - "isPartialBlock"
Cohesion: 0.23
Nodes (14): isDoorBlock(), isPartialBlock(), isPlateBlock(), isRedstoneComponent(), isRepeaterBlock(), isSignBlock(), isSlabBlock(), isStructureBlock() (+6 more)

### Community 73 - "Maps Module"
Cohesion: 0.13
Nodes (22): find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush(), Maps::pixels() (+14 more)

### Community 74 - "DebugChests.h"
Cohesion: 0.20
Nodes (13): buildItemList(), findSite(), groundHeight(), isGivenItem(), isReplaceable(), isSkippable(), Site, alongX (+5 more)

### Community 75 - "nds"
Cohesion: 0.09
Nodes (26): addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b, g (+18 more)

### Community 76 - "NoteBlocks.cpp"
Cohesion: 0.12
Nodes (17): ChunkManager, Entry, gx, gy, gz, note, prev, used (+9 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (19): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+11 more)

### Community 78 - "ModelBox.h"
Cohesion: 0.24
Nodes (9): build(), Face, v, Vertex, u, v, x, y (+1 more)

### Community 80 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 81 - "Options Module"
Cohesion: 0.11
Nodes (19): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+11 more)

### Community 82 - "5.2 Blocks, items, inventory, crafting"
Cohesion: 0.29
Nodes (10): 5.2 Blocks, items, inventory, crafting, EntityEnumerator, setEntityEnumerator(), setMinecartEnumerator(), bedOrientationDeg(), eyePosition(), modelShift(), nearestEmpty() (+2 more)

### Community 83 - "Biome & Chunk"
Cohesion: 0.13
Nodes (15): BiomeType, DESERT, FOREST, GENERIC, OCEAN, PLAINS, RAINFOREST, SAVANNA (+7 more)

### Community 84 - "LightNode"
Cohesion: 0.33
Nodes (5): LightNode, bx, by, bz, level

### Community 85 - "Caves Module"
Cohesion: 0.12
Nodes (17): Job, active, cx, cz, fill, nOrigins, originIdx, ox (+9 more)

### Community 86 - "Cube Module"
Cohesion: 0.17
Nodes (10): Cube, drawBox(), FaceMask, bottom, east, north, south, top (+2 more)

### Community 87 - "FishingHook.cpp"
Cohesion: 0.05
Nodes (47): Catch, damage, fish, vx, vy, vz, x, y (+39 more)

### Community 88 - "HostileManager Module"
Cohesion: 0.17
Nodes (6): exposure(), HWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 89 - "Projectiles Module"
Cohesion: 0.22
Nodes (15): brightnessOf(), cellY(), chunkOf(), eggBreak(), gaussian(), nextFloat(), nextInt(), nextU() (+7 more)

### Community 90 - "Vehicle Entity (BoatModel)"
Cohesion: 0.11
Nodes (18): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+10 more)

### Community 91 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.13
Nodes (12): state, set(), State, lx, ly, lz, maxDist2, valid (+4 more)

### Community 93 - "bigTreeComputeBranches"
Cohesion: 0.13
Nodes (16): BigTreeBranch, trunkY, x, y, z, bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches() (+8 more)

### Community 94 - "AnimItems.cpp"
Cohesion: 0.20
Nodes (3): AnimItems::init(), AnimItems::tick(), setFrame()

### Community 95 - "TextKeyboard Module"
Cohesion: 0.23
Nodes (14): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+6 more)

### Community 96 - "Tick"
Cohesion: 0.20
Nodes (8): Tick, due, gx, gy, gz, seq, type, used

### Community 97 - "Caves Module"
Cohesion: 0.19
Nodes (9): advanceOrigin(), cellRng(), initTunnel(), JRandom, seed, probeOrigins(), pushTunnel(), reset() (+1 more)

### Community 98 - "Caves Module"
Cohesion: 0.13
Nodes (15): Tunnel, branchStep, isRoom, length, pitch, pitchVel, r, radiusScale (+7 more)

### Community 99 - "Vehicle Entity (MinecartManager)"
Cohesion: 0.17
Nodes (7): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn()

### Community 100 - "SettingsMenu Module"
Cohesion: 0.30
Nodes (12): draw(), drawControls(), drawDebug(), openControls(), openDebug(), printControlsRow(), printOption(), printRow() (+4 more)

### Community 101 - "Profiler.h"
Cohesion: 0.22
Nodes (6): ProfScope, slot, start, ProfStep, label, start

### Community 102 - "MobBody & AnimalManager"
Cohesion: 0.16
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.14
Nodes (3): Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.10
Nodes (23): blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn(), Tnt, active (+15 more)

### Community 105 - "Climate Module"
Cohesion: 0.18
Nodes (8): initIfSeedChanged(), Octaves, gen, Simplex, perm, xo, yo, zo

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.16
Nodes (7): RLERun, length, type, VoxelColumnRLE, MAX_RUNS, runCount, runs

### Community 107 - "Projectiles Module"
Cohesion: 0.18
Nodes (7): drawSprite(), Projectiles::draw(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 108 - "Spike"
Cohesion: 0.20
Nodes (10): Spike, dim, frame, label, part, stepMs10, total, x (+2 more)

### Community 109 - "Env"
Cohesion: 0.25
Nodes (8): Env, burningBox, cactus, fallLanded, headInWater, inLava, insideBlock, inWater

### Community 110 - "SheepManager Module"
Cohesion: 0.17
Nodes (7): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady, SheepManager::draw(), SheepManager::explosionDamage()

### Community 111 - "SheepModel Module"
Cohesion: 0.13
Nodes (17): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+9 more)

### Community 112 - "Drop"
Cohesion: 0.22
Nodes (9): Drop, durability, type, vx, vy, vz, x, y (+1 more)

### Community 113 - "Caves Module"
Cohesion: 0.17
Nodes (9): CarveCursor, cell, sphere, Sphere, flat, r16, x8, y8 (+1 more)

### Community 114 - "Liquid.cpp"
Cohesion: 0.25
Nodes (3): isHell(), popDue(), pushTick()

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.20
Nodes (7): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.6 Saving, 7. World engine in detail

### Community 117 - "Projectiles Module"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 118 - "Drop"
Cohesion: 0.29
Nodes (7): Drop, count, durability, type, x, y, z

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 121 - "PauseScreen Module"
Cohesion: 0.20
Nodes (7): Button, BTN_BACK, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched()

### Community 123 - "12. Rendering, textures and models"
Cohesion: 0.20
Nodes (7): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), 12.2 Texture loading (`Texture.h/.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 126 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 127 - "Climate Module"
Cohesion: 0.20
Nodes (7): biomeFor(), Lattice, h, t, x0, z0, raw()

### Community 128 - "HostileManager Module"
Cohesion: 0.11
Nodes (18): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+10 more)

### Community 129 - ".isDSi"
Cohesion: 0.24
Nodes (3): cellInWindow(), ChunkManager::ChunkManager(), Hardware

### Community 130 - "Chunk.h"
Cohesion: 0.09
Nodes (11): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), dispenserFrontDir(), rand, DisplayListBuilder, Dispenser::dispense(), Dispenser::popDrop(), gauss(), typeAtGrid() (+3 more)

### Community 131 - "LoadingScreen Module"
Cohesion: 0.43
Nodes (3): copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen

### Community 132 - "AnimalManager Module"
Cohesion: 0.17
Nodes (7): AnimalManager::draw(), AnimalManager::explosionDamage(), CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 134 - "Clouds & CloudsData"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 136 - "Texture.h"
Cohesion: 0.28
Nodes (3): HealthHud::draw(), MenuBackground, texCoordCell()

### Community 137 - "State"
Cohesion: 0.33
Nodes (6): State, detail, humidity, ready, seed, temperature

### Community 138 - "Vehicle Entity (MinecartManager)"
Cohesion: 0.29
Nodes (7): Drop, count, durability, type, x, y, z

### Community 139 - "Redstone Logic (Redstone)"
Cohesion: 0.22
Nodes (9): BoxQuery, everything, found, maxX, maxY, maxZ, minX, minY (+1 more)

### Community 140 - "Redstone Logic (Redstone)"
Cohesion: 0.22
Nodes (9): Def, a, b, c, id, kind, x, y (+1 more)

### Community 141 - "SheepManager Module"
Cohesion: 0.29
Nodes (7): Drop, count, shear, type, x, y, z

### Community 142 - "Entity AI (BoatAI)"
Cohesion: 0.38
Nodes (7): 9.4 Minecarts, boats, TNT, bodyBox(), boxInWater(), moveEntity(), rayHit(), tick(), hasPower()

### Community 143 - "AnimalManager Module"
Cohesion: 0.33
Nodes (6): Drop, count, type, x, y, z

### Community 144 - "Caves Module"
Cohesion: 0.25
Nodes (8): Cell, count, cx, cz, first, lastUse, nblocks, pad

### Community 145 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 146 - "HealthHudLayout Module"
Cohesion: 0.29
Nodes (7): build(), HudQuad, layer, u, v, x, y

### Community 148 - "RenderInput"
Cohesion: 0.17
Nodes (10): ChunkManager, RenderInput, bodyLight, dimension, eyeLight, partialTicks, pitch, posX (+2 more)

### Community 151 - "Falling"
Cohesion: 0.13
Nodes (14): Falling, active, fallTime, prevY, type, vy, x, y (+6 more)

### Community 152 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 154 - "HostileManager Module"
Cohesion: 0.29
Nodes (7): SavedWolf, health, sitting, x, y, yaw, z

### Community 155 - "Drop"
Cohesion: 0.29
Nodes (7): Drop, count, durability, type, x, y, z

### Community 158 - "Redstone Logic (Redstone)"
Cohesion: 0.29
Nodes (7): Tick, due, seq, t, x, y, z

### Community 160 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "Redstone.cpp"
Cohesion: 0.16
Nodes (17): bounds(), canProvidePower(), chunkOf(), faceCode(), floorDivi(), freeCell(), gettingPowered(), isIndirectlyPoweringTo() (+9 more)

### Community 163 - "ColorMaps & ColorMapData"
Cohesion: 0.60
Nodes (3): ColorMaps::foliage(), ColorMaps::grass(), lookup()

### Community 164 - "Kind"
Cohesion: 0.25
Nodes (8): Kind, K_BACK, K_CANCEL, K_CHAR, K_CLEAR, K_OK, K_SHIFT, K_SPACE

### Community 165 - "HostileManager Module"
Cohesion: 0.33
Nodes (6): PendingExplosion, flaming, size, x, y, z

### Community 166 - "Redstone Logic (Redstone)"
Cohesion: 0.33
Nodes (6): Rem, m, t, x, y, z

### Community 171 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 178 - "T"
Cohesion: 0.21
Nodes (14): addWirePos(), anySideNormal(), cartTouchSink(), doorPower(), drainDeferred(), dropItem(), maxStrength(), neighborChanged() (+6 more)

### Community 179 - "Sky.cpp"
Cohesion: 0.53
Nodes (4): Sky::draw(), uv(), v(), vert()

### Community 183 - "ExplosionDamage.h"
Cohesion: 0.83
Nodes (3): compute(), exposure(), lineClear()

### Community 184 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 187 - "P"
Cohesion: 0.50
Nodes (4): P, x, y, z

## Knowledge Gaps
- **1442 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1437 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1869 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `HostileManager Module`, `Chunk Meshing and Bands`, `Chunk.h`, `PartialBlocks.cpp`, `AnimalManager Module`, `HandAnimations.cpp`, `Block and Item Types`, `Chunk.cpp`, `Block and Item Types`, `Vehicle Entity (MinecartManager)`, `Painting and Art Types`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `PendingDrops.h`, `Crafting Recipes`, `NetherGen.h`, `Entity AI (BoatAI)`, `Block and Item Types`, `Sound.cpp`, `Inventory`, `Falling`, `Furnace.cpp`, `Drop`, `ChunkManager`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Redstone.cpp`, `ChunkManager Module`, `AnimalManager Module`, `isTorchBlock`, `Block and Item Types`, `Redstone Logic (Redstone)`, `Block and Item Types`, `Block and Item Types`, `HostileManager Module`, `Torch Module`, `Vehicle Entity (MinecartManager)`, `T`, `M`, `InventoryScreen.cpp`, `notify`, `NetherTerrain`, `Caves & CaveSinTable`, `Vehicle Entity (MinecartModel)`, `isLeavesBlock`, `BigTree`, `Chunk.h`, `BoatManager.cpp`, `SheepManager Module`, `PartialBlocks.h`, `isPartialBlock`, `Maps Module`, `DebugChests.h`, `nds`, `NoteBlocks.cpp`, `FishingHook.cpp`, `HostileManager Module`, `TickInput`, `bigTreeComputeBranches`, `Vehicle Entity (MinecartManager)`, `TntManager.cpp`, `VoxelColumnRLE`, `Projectiles Module`, `SheepManager Module`, `Drop`, `Liquid.cpp`, `7. World engine in detail`, `Drop`?**
  _High betweenness centrality (0.285) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1442 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Player Module` to `.isDSi`, `Chunk.h`, `LoadingScreen Module`, `HandAnimations.cpp`, `Block and Item Types`, `PendingDrops.h`, `Crafting Recipes`, `GameplayHotbar.cpp`, `Block and Item Types`, `SubScreenMenu Module`, `Inventory`, `WorldSave Module`, `Pistons.cpp`, `Texture & PaintingTex`, `isTorchBlock`, `Texture Module`, `Block and Item Types`, `Torch Module`, `Noise.cpp`, `InventoryScreen.cpp`, `NewWorldMenu.cpp`, `isLeavesBlock`, `WorldSelectMenu Module`, `Chunk.h`, `main.cpp`, `isPartialBlock`, `GameOverScreen.cpp`, `FishingHook.cpp`, `TopScreenMenu & Renderer`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 87 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 87 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020475020475020474 - nodes in this community are weakly interconnected._