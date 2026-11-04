# Graph Report - YUANCRAFT NDS PORT  (2026-11-03)

## Corpus Check
- 261 files · ~367,499 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 55 file(s) not represented in the graph (top: .grit 49, (none) 4, .ini 1)

## Summary
- 4494 nodes · 9960 edges · 227 communities (190 shown, 37 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1154 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

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
- Sim
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
- BlockType.h
- Sound.cpp
- Inventory
- Entity AI (HostileAI)
- Furnace.cpp
- AsyncSaveManager
- DisplayListBuilder Module
- Spawners & Particles
- WorldSave Module
- .setBlockDirect
- string
- Pistons.cpp
- Texture & PaintingTex
- Controls & ItemOrder
- stbi_uc
- ChunkManager Module
- AnimalManager Module
- CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)
- Block and Item Types
- RailLogic Module
- Texture and Image Decoding
- isNormalCube
- Texture Module
- Block and Item Types
- Block and Item Types
- HostileManager Module
- PartialBlocks.h
- MinecartManager.cpp
- Projectiles Module
- SignManager Module
- Noise.cpp
- Profiler Module
- Profiler Module
- M
- LoadingScreen.cpp
- notify
- NewWorldMenu.cpp
- Caves.cpp
- Health Module
- HostileManager Module
- Vehicle Entity (MinecartModel)
- InventoryScreen.cpp
- Texture and Image Decoding
- WorldSelectMenu Module
- AnimalAI.h
- PathWork
- AnimItems.cpp
- main.cpp
- BoatManager.cpp
- Texture and Image Decoding
- bigTreeComputeBranches
- CMWorld
- Maps Module
- DebugChests.h
- nds
- NoteBlocks.cpp
- Minecraft: Nintendo DS Edition
- BigTree
- IpcChunkLoader
- CartWorld
- Options Module
- rand
- Biome & Chunk
- .floodFillSkyLight
- Caves Module
- Cube Module
- FishingHook.cpp
- HostileManager Module
- Projectiles Module
- BoatModel.cpp
- Recipe
- MobCull & Caves
- WorldMetadata
- Tick
- TextKeyboard Module
- Hardware
- re
- Caves Module
- MenuFont.cpp
- verify_world_select_simulation.py
- JRandom
- MobBody & AnimalManager
- TopScreenMenu & Renderer
- TntManager.cpp
- Simplex
- VoxelColumnRLE
- Projectiles Module
- ChestStore.cpp
- ChestStore.cpp
- .sqrtf
- SheepModel Module
- Drop
- Caves.h
- verify_ipc_streaming_simulation.py
- Lakes Module
- 7. World engine in detail
- Projectiles Module
- Env
- build.sh
- BoatWorld
- PauseScreen Module
- TickInput
- Painting
- HostileManager Module
- SettingsMenu.cpp
- .computeColumnFacesBitwise
- Climate.h
- HostileManager Module
- math
- stdlib
- CMWorld
- T
- MockAsyncSaveManager
- Teleporter.h
- Part
- Texture.h
- Chunk.h
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- HealthHudLayout Module
- Redstone.cpp
- FlatQuad
- StartupSplash Module
- IpcChunkExchange
- Chunk.h
- Pose
- Chunk Module
- HostileManager Module
- Drop
- RenderInput
- Redstone Logic (Redstone)
- Kind
- ModelBox.h
- Caves Module
- chunkOf
- ColorMaps & ColorMapData
- Kind
- HostileManager Module
- Redstone Logic (Redstone)
- verify_simulation
- Cell
- JRandom
- PendingDrops.h
- Redstone Logic (Redstone)
- os
- BlockFace
- Glow
- verify_occupancy_simulation.py
- 9. Entities and physics notes
- Climate.h
- Lat
- AnimalAI.h
- verify_ui_logic_sim.py
- Liquid.cpp
- Clouds.cpp
- test_print_row_safety.py
- NetherTerrain
- 9. Entities and physics notes
- P
- ExplosionDamage.h
- Profiler.h
- Quad
- Drop
- Sound.h
- Rng
- Drop
- 12. Rendering, textures and models
- Quad
- P3
- RedstoneEntityCtx
- Box
- ctypes
- ArrowHurtCtx
- PlayerPos
- Quad
- isLiquidBlock
- .saveToFileAsync
- Art
- Sign
- Sky.cpp
- Rng
- MockChunk
- bump

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 214 edges
3. `main()` - 195 edges
4. `ChunkManager` - 98 edges
5. `Player` - 91 edges
6. `DroppedItem` - 61 edges
7. `Sim` - 48 edges
8. `isLiquidBlock()` - 44 edges
9. `isNormalCube()` - 43 edges
10. `Texture` - 42 edges

## Surprising Connections (you probably didn't know these)
- `2. Rules for an AI assistant modifying this project (read carefully)` --references--> `BlockType`  [INFERRED]
  CLAUDE.md → source/BlockType.h
- `7.1c `tickLiquids` (20 Hz) and random ticks` --references--> `LiquidWorld`  [INFERRED]
  CLAUDE.md → source/ChunkManager.cpp
- `9.8 More internals (Nether, sky, saves, menus, chests, notes)` --references--> `resetLattice()`  [INFERRED]
  CLAUDE.md → source/NetherGen.h
- `9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`)` --references--> `packSpot()`  [INFERRED]
  CLAUDE.md → source/AnimalAI.h
- `7.2 Memory model` --references--> `BlockType`  [INFERRED]
  CLAUDE.md → source/BlockType.h

## Import Cycles
- None detected.

## Communities (227 total, 37 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (84): Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor, CACHE_RECALC_BATCH, cacheRecalcPending, cacheRecalcXi (+76 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.21
Nodes (33): 9.3 Liquids, particles, partial blocks, doubleOfSlab(), activate(), boxHit(), chunkOf(), cropCanStay(), cropsTick(), dropAt() (+25 more)

### Community 3 - "Block and Item Types"
Cohesion: 0.06
Nodes (73): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+65 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (56): Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase, bobStrength, buttonLookSpeedH, buttonLookSpeedV, currentTickDistance (+48 more)

### Community 5 - "Texture and Image Decoding"
Cohesion: 0.07
Nodes (59): main(), stbi_convert_iphone_png_to_rgb(), stbi_convert_iphone_png_to_rgb_thread(), stbi_convert_wchar_to_utf8(), stbi__do_zlib(), stbi_failure_reason(), stbi__float_postprocess(), stbi__fopen() (+51 more)

### Community 6 - "Texture and Image Decoding"
Cohesion: 0.09
Nodes (64): stbi__at_eof(), stbi__bitcount(), stbi__bmp_info(), stbi__bmp_load(), stbi__bmp_parse_header(), stbi__bmp_set_mask_defaults(), stbi__bmp_test(), stbi__bmp_test_raw() (+56 more)

### Community 7 - "HandAnimations.cpp"
Cohesion: 0.14
Nodes (25): 12.6 Mob models (`ModelBox.h`, `*Model.cpp`), applyViewBobbing(), blockRenderColor(), brightnessOf(), drawBlockInHand(), drawFirstPersonArm(), drawItem2D(), drawMapHeld() (+17 more)

### Community 8 - "Image Writing Utilities"
Cohesion: 0.09
Nodes (50): stb_image_write_test, stbi__end_write_file(), stbi_flip_vertically_on_write(), stbi__start_write_callbacks(), stbi__start_write_file(), stbi_write_bmp(), stbi_write_bmp_core(), stbi_write_bmp_to_func() (+42 more)

### Community 9 - "Sim"
Cohesion: 0.11
Nodes (11): isFlowingLiquid(), isLavaBlock(), isMaterialSolid(), liquidMaterial(), percentAir(), Sim, editing, flowCost (+3 more)

### Community 10 - "Chunk.cpp"
Cohesion: 0.08
Nodes (8): chunkFloorDiv(), fillDungeonChest(), oreFloorInt(), OreRng, s, oreVeinBlob(), terrainHeightCached(), terrainHeightFrom()

### Community 11 - "Block and Item Types"
Cohesion: 0.06
Nodes (44): getGrassTint(), alloc(), baseMotion(), brightnessOf(), move(), P, active, age (+36 more)

### Community 12 - "Painting and Art Types"
Cohesion: 0.19
Nodes (13): brightnessOf(), compute(), halfSnap(), isValid(), PaintingManager::attack(), PaintingManager::draw(), PaintingManager::loadFromFile(), PaintingManager::place() (+5 more)

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
Cohesion: 0.12
Nodes (25): blockLightEmission(), furnaceIsLit(), getBlockTextures(), getDropType(), isJackBlock(), isPumpkinBlock(), woolCell(), applyLight() (+17 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.19
Nodes (15): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+7 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.08
Nodes (18): CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt(), drawIconAt() (+10 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.13
Nodes (13): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+5 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.13
Nodes (10): GameplayHotbar, bgId, isInButtonRow(), drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon() (+2 more)

### Community 21 - "BlockType.h"
Cohesion: 0.06
Nodes (52): ChunkManager, armorMaterial(), armorRenderIndex(), blockHardness(), canHarvestBlock(), dyeDamage(), fireCatch(), fireEncourage() (+44 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.18
Nodes (17): at(), cellToWorld(), digBase(), mobClip(), pick(), rnd(), Sound::blockBreak(), Sound::blockPlace() (+9 more)

### Community 23 - "Inventory"
Cohesion: 0.11
Nodes (30): 9.7 Inventory and crafting UI internals, armorMaxDurability(), armorPiece(), armorReduceAmount(), getToolMaxDurability(), hasDurability(), isArmor(), isRecord() (+22 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.06
Nodes (63): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), arrowTick(), attackBlocked(), attackEntity(), boxClear(), brightnessAt(), canSee(), canSpawnHere() (+55 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.08
Nodes (34): furnaceFrontDir(), makeFurnaceBlock(), canSmelt(), clearEntry(), clearSlot(), floorDivInt(), Furnace::clearAll(), Furnace::find() (+26 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.08
Nodes (19): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+11 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "Spawners & Particles"
Cohesion: 0.17
Nodes (18): chunkAt(), ChunkManager, cx(), cy(), cz(), Entry, delay, gx (+10 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.13
Nodes (9): SD card layout, clearFolderContents(), folderExists(), WorldSave, s_activeBasePath, s_activeWorldNum, s_dimension, s_promoted (+1 more)

### Community 30 - ".setBlockDirect"
Cohesion: 0.20
Nodes (3): isSapling(), torchFromMeta(), bigTreeDrawLine()

### Community 31 - "string"
Cohesion: 0.13
Nodes (5): draw(), OptionsMenu::open(), OptionsMenu::update(), printRow(), ChunkManager

### Community 32 - "Pistons.cpp"
Cohesion: 0.07
Nodes (64): 5.2 Blocks, items, inventory, crafting, isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend() (+56 more)

### Community 33 - "Texture & PaintingTex"
Cohesion: 0.07
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.09
Nodes (26): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+18 more)

### Community 35 - "stbi_uc"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.09
Nodes (12): AnimalManager::attack(), AnimalManager::draw(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath() (+4 more)

### Community 38 - "CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)"
Cohesion: 0.10
Nodes (19): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is, 2. Rules for an AI assistant modifying this project (read carefully) (+11 more)

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - "isNormalCube"
Cohesion: 0.09
Nodes (31): isNormalCube(), airSpawnSpot(), waterSpawnSpot(), autoMeta(), boundsForMeta(), Box, x0, x1 (+23 more)

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.20
Nodes (18): isRailBlock(), bodyBox(), calcX(), calcY(), calcZ(), fl(), hyp(), moveEntity() (+10 more)

### Community 45 - "Block and Item Types"
Cohesion: 0.09
Nodes (13): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::interact(), SheepManager::lightning() (+5 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.09
Nodes (11): 9.2 Managers: spawning, caps, explosions, collectDeath(), explode(), HostileManager::attack(), HostileManager::interact(), HostileManager::lightning(), HostileManager::popDrop(), pushDrop() (+3 more)

### Community 47 - "PartialBlocks.h"
Cohesion: 0.13
Nodes (25): 9.6 Audio internals (`Sound.cpp`), isDoorBlock(), isPistonBlock(), isRedstoneComponent(), isRepeaterBlock(), isSignBlock(), isStairsBlock(), isStructureBlock() (+17 more)

### Community 48 - "MinecartManager.cpp"
Cohesion: 0.11
Nodes (13): breakCart(), cartCollision(), dismountIndex(), eyeOf(), getI32(), MinecartManager::attack(), MinecartManager::dismount(), MinecartManager::loadFromFile() (+5 more)

### Community 49 - "Projectiles Module"
Cohesion: 0.07
Nodes (28): Proj, active, inGround, kind, mx, my, mz, ownerIsPlayer (+20 more)

### Community 50 - "SignManager Module"
Cohesion: 0.15
Nodes (12): Box, q, brightnessOf(), buildBox(), ChunkManager, drawBox(), drawText(), find() (+4 more)

### Community 51 - "Noise.cpp"
Cohesion: 0.10
Nodes (16): Chunk::Chunk(), getPatchAt(), HeightCache, h, tx, tz, NetherColCache, c (+8 more)

### Community 52 - "Profiler Module"
Cohesion: 0.10
Nodes (17): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike(), Spike (+9 more)

### Community 53 - "Profiler Module"
Cohesion: 0.13
Nodes (15): Slot, DL_CALL, DL_CULL, DL_LOD, DL_REBUILD, DRAW_ALL, ENTS, FACES (+7 more)

### Community 54 - "M"
Cohesion: 0.26
Nodes (16): isPlateBlock(), detectorCheck(), faceCode(), freeCell(), M(), plateBox(), plateCheck(), randomTick() (+8 more)

### Community 55 - "LoadingScreen.cpp"
Cohesion: 0.29
Nodes (4): 9.8 More internals (Nether, sky, saves, menus, chests, notes), copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen

### Community 56 - "notify"
Cohesion: 0.20
Nodes (16): activate(), blockChanged(), blockRemoved(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved() (+8 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves.cpp"
Cohesion: 0.19
Nodes (11): allocBlock(), carveSphere(), emit(), floorD(), floorF(), freeCellBlocks(), isDecoration(), jcos() (+3 more)

### Community 59 - "Health Module"
Cohesion: 0.09
Nodes (30): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), HealthState, air, armorPoints (+22 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.17
Nodes (17): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::count(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn() (+9 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "InventoryScreen.cpp"
Cohesion: 0.09
Nodes (14): ChestView, FurnaceData, ChunkManager, HotbarIcons, drawCountAt(), drawDigit(), drawDurabilityBar(), drawIconAt() (+6 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.19
Nodes (3): clearLabelZone(), drawWorldName(), WorldSelectMenu

### Community 65 - "AnimalAI.h"
Cohesion: 0.27
Nodes (18): anyIn(), cellY(), damage(), faceEntity(), headInWater(), inFire(), inLava(), insideOpaque() (+10 more)

### Community 66 - "PathWork"
Cohesion: 0.11
Nodes (28): findPath(), heapAdd(), heapChange(), heapDequeue(), heapSortBack(), heapSortForward(), openPoint(), pathHash() (+20 more)

### Community 67 - "AnimItems.cpp"
Cohesion: 0.20
Nodes (3): AnimItems::init(), AnimItems::tick(), setFrame()

### Community 68 - "main.cpp"
Cohesion: 0.05
Nodes (33): 15. Recipes for common tasks, 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, getDamageVsEntity(), makeDispenserBlock(), GameOverScreen (+25 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.14
Nodes (11): BoatManager::attack(), BoatManager::dismount(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::saveToFile(), breakBoat(), dismountIndex(), forceDismount() (+3 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "bigTreeComputeBranches"
Cohesion: 0.13
Nodes (16): BigTreeBranch, trunkY, x, y, z, bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches() (+8 more)

### Community 72 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 73 - "Maps Module"
Cohesion: 0.13
Nodes (22): find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush(), Maps::pixels() (+14 more)

### Community 74 - "DebugChests.h"
Cohesion: 0.20
Nodes (13): buildItemList(), findSite(), groundHeight(), isGivenItem(), isReplaceable(), isSkippable(), Site, alongX (+5 more)

### Community 75 - "nds"
Cohesion: 0.16
Nodes (14): addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b, g (+6 more)

### Community 76 - "NoteBlocks.cpp"
Cohesion: 0.12
Nodes (17): ChunkManager, Entry, gx, gy, gz, note, prev, used (+9 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (20): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+12 more)

### Community 78 - "BigTree"
Cohesion: 0.13
Nodes (13): BigTree, AX, basePos, branchSlope, height, heightAttenuation, heightLimit, heightLimitLimit (+5 more)

### Community 79 - "IpcChunkLoader"
Cohesion: 0.10
Nodes (15): Chunk, ChunkManager, IpcChunkLoader, s_exchange, s_initialized, TICKS_PER_MS, TIMEOUT_MS, TIMEOUT_TICKS (+7 more)

### Community 80 - "CartWorld"
Cohesion: 0.15
Nodes (9): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn(), MinecartManager::tick() (+1 more)

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "rand"
Cohesion: 0.20
Nodes (13): isLeavesBlock(), rand, freeOrLeaves(), genRound(), genSpruce(), isLog(), markLeaf(), Trees::grow() (+5 more)

### Community 83 - "Biome & Chunk"
Cohesion: 0.12
Nodes (15): BiomeType, DESERT, FOREST, GENERIC, OCEAN, PLAINS, RAINFOREST, SAVANNA (+7 more)

### Community 84 - ".floodFillSkyLight"
Cohesion: 0.23
Nodes (6): lightDim(), LightNode, bx, by, bz, level

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

### Community 90 - "BoatModel.cpp"
Cohesion: 0.17
Nodes (12): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+4 more)

### Community 91 - "Recipe"
Cohesion: 0.13
Nodes (15): Recipe, altA, altB, altC, altD, pattern, requiresTable, result (+7 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.13
Nodes (12): state, set(), State, lx, ly, lz, maxDist2, valid (+4 more)

### Community 93 - "WorldMetadata"
Cohesion: 0.11
Nodes (18): WorldMetadata, armorDurability, armorType, formatVersion, gameTimeTicks, hotbarCount, hotbarDurability, hotbarType (+10 more)

### Community 94 - "Tick"
Cohesion: 0.20
Nodes (8): Tick, due, gx, gy, gz, seq, type, used

### Community 95 - "TextKeyboard Module"
Cohesion: 0.23
Nodes (14): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+6 more)

### Community 98 - "Caves Module"
Cohesion: 0.13
Nodes (15): Tunnel, branchStep, isRoom, length, pitch, pitchVel, r, radiusScale (+7 more)

### Community 99 - "MenuFont.cpp"
Cohesion: 0.21
Nodes (11): find(), Glyph, c, rows, MenuFont::draw16(), MenuFont::draw8(), MenuFont::fill16(), MenuFont::fill8() (+3 more)

### Community 100 - "verify_world_select_simulation.py"
Cohesion: 0.17
Nodes (6): main(), simulate_world_select_menu(), test_empty_and_corrupt_world_directory(), test_math_division_shortcut(), test_polygon_budget_and_overflow(), test_world_lifecycle_and_deletion()

### Community 101 - "JRandom"
Cohesion: 0.18
Nodes (11): advanceOrigin(), cellRng(), initTunnel(), JRandom, seed, prepare(), probeOrigins(), pushTunnel() (+3 more)

### Community 102 - "MobBody & AnimalManager"
Cohesion: 0.18
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.12
Nodes (5): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), 12.2 Texture loading (`Texture.h/.cpp`), Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.10
Nodes (23): blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn(), Tnt, active (+15 more)

### Community 105 - "Simplex"
Cohesion: 0.22
Nodes (5): Simplex, perm, xo, yo, zo

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.14
Nodes (8): RLERun, length, type, VoxelColumnRLE, MAX_RUNS, _pad, runCount, runs

### Community 107 - "Projectiles Module"
Cohesion: 0.18
Nodes (7): drawSprite(), Projectiles::draw(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 108 - "ChestStore.cpp"
Cohesion: 0.29
Nodes (9): ChestStore::clearAll(), ChestStore::findOrCreate(), ChestStore::loadFromFile(), ChestStore::remove(), ChestStore::saveToFile(), clearEntry(), clearSlot(), getI32() (+1 more)

### Community 109 - "ChestStore.cpp"
Cohesion: 0.12
Nodes (15): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+7 more)

### Community 111 - "SheepModel Module"
Cohesion: 0.13
Nodes (17): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+9 more)

### Community 112 - "Drop"
Cohesion: 0.22
Nodes (9): Drop, durability, type, vx, vy, vz, x, y (+1 more)

### Community 113 - "Caves.h"
Cohesion: 0.25
Nodes (6): Sphere, flat, r16, x8, y8, z8

### Community 114 - "verify_ipc_streaming_simulation.py"
Cohesion: 0.24
Nodes (7): main(), MockChunkManager, SimulatedIpcChunkLoader, test_async_streaming_flow(), test_corrupted_file_failsafe(), test_sd_timeout_failsafe(), test_ui_stability_and_vblank_loop()

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.18
Nodes (8): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.5 Meshing and drawing, 7.6 Saving, 7. World engine in detail

### Community 117 - "Projectiles Module"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 118 - "Env"
Cohesion: 0.25
Nodes (8): Env, burningBox, cactus, fallLanded, headInWater, inLava, insideBlock, inWater

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 120 - "BoatWorld"
Cohesion: 0.18
Nodes (9): BoatManager::draw(), BoatManager::spawnFromRay(), BoatManager::tick(), BoatWorld, cacheChunk, cacheCx, cacheCz, cacheReady (+1 more)

### Community 121 - "PauseScreen Module"
Cohesion: 0.15
Nodes (9): Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched() (+1 more)

### Community 122 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 123 - "Painting"
Cohesion: 0.12
Nodes (17): Painting, active, art, dir, gx, gy, gz, maxX (+9 more)

### Community 125 - "SettingsMenu.cpp"
Cohesion: 0.27
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 126 - ".computeColumnFacesBitwise"
Cohesion: 0.16
Nodes (5): BandFlags, v, sameFaces(), shiftDown1(), shiftUp1()

### Community 127 - "Climate.h"
Cohesion: 0.29
Nodes (6): Lattice, h, t, x0, z0, raw()

### Community 128 - "HostileManager Module"
Cohesion: 0.11
Nodes (18): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+10 more)

### Community 129 - "math"
Cohesion: 0.43
Nodes (4): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math()

### Community 131 - "CMWorld"
Cohesion: 0.17
Nodes (7): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady, SheepManager::draw(), SheepManager::explosionDamage()

### Community 132 - "T"
Cohesion: 0.24
Nodes (12): addWirePos(), anySideNormal(), cartTouchSink(), doorPower(), maxStrength(), neighborChanged(), neighborDo(), normal() (+4 more)

### Community 134 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 135 - "Part"
Cohesion: 0.17
Nodes (12): Part, faceMask, pointX, pointY, pointZ, px, py, pz (+4 more)

### Community 136 - "Texture.h"
Cohesion: 0.28
Nodes (3): HealthHud::draw(), MenuBackground, texCoordCell()

### Community 137 - "Chunk.h"
Cohesion: 0.12
Nodes (8): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), dispenserFrontDir(), DisplayListBuilder, Dispenser::dispense(), Dispenser::popDrop(), gauss(), typeAtGrid(), genColsPerFrame()

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
Cohesion: 0.54
Nodes (5): bodyBox(), boxInWater(), moveEntity(), rayHit(), tick()

### Community 143 - "AnimalManager Module"
Cohesion: 0.33
Nodes (6): Drop, count, type, x, y, z

### Community 146 - "HealthHudLayout Module"
Cohesion: 0.29
Nodes (7): build(), HudQuad, layer, u, v, x, y

### Community 147 - "Redstone.cpp"
Cohesion: 0.19
Nodes (15): bounds(), burnedOut(), canProvidePower(), dropItem(), gettingPowered(), indirectlyGettingPowered(), indirectPowerAt(), indirectProvidingPowerTo() (+7 more)

### Community 148 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 150 - "IpcChunkExchange"
Cohesion: 0.18
Nodes (10): IpcChunkExchange, chunkX, chunkZ, compBuffer, dataSize, path, rawBuffer, requestStartTick (+2 more)

### Community 151 - "Chunk.h"
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

### Community 157 - "RenderInput"
Cohesion: 0.17
Nodes (10): ChunkManager, RenderInput, bodyLight, dimension, eyeLight, partialTicks, pitch, posX (+2 more)

### Community 158 - "Redstone Logic (Redstone)"
Cohesion: 0.29
Nodes (7): Tick, due, seq, t, x, y, z

### Community 159 - "Kind"
Cohesion: 0.18
Nodes (11): Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA, REDDUST (+3 more)

### Community 160 - "ModelBox.h"
Cohesion: 0.24
Nodes (9): build(), Face, v, Vertex, u, v, x, y (+1 more)

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "chunkOf"
Cohesion: 0.29
Nodes (6): chunkOf(), floorDivi(), lightOre(), put(), removeBlock(), setTM()

### Community 163 - "ColorMaps & ColorMapData"
Cohesion: 0.48
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

### Community 168 - "verify_simulation"
Cohesion: 0.32
Nodes (5): verify_simulation(), is_vram(), setup_projection(), simulate_frame(), validate_decompress_args()

### Community 169 - "Cell"
Cohesion: 0.25
Nodes (8): Cell, count, cx, cz, first, lastUse, nblocks, pad

### Community 171 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 173 - "os"
Cohesion: 0.09
Nodes (3): verify_structural(), verify_structural(), verify_all()

### Community 174 - "BlockFace"
Cohesion: 0.08
Nodes (28): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+20 more)

### Community 175 - "Glow"
Cohesion: 0.24
Nodes (7): firePatch(), Glow, cell, ox, oy, oz, glowCluster()

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

### Community 177 - "9. Entities and physics notes"
Cohesion: 0.22
Nodes (8): 9.5 World-generation pieces, 9. Entities and physics notes, beginFrame(), CarveCursor, cell, sphere, carveStep(), floorDiv()

### Community 178 - "Climate.h"
Cohesion: 0.20
Nodes (10): biomeFor(), initIfSeedChanged(), Octaves, gen, State, detail, humidity, ready (+2 more)

### Community 179 - "Lat"
Cohesion: 0.18
Nodes (11): Lat, a, b, n1, n2, n3, LatCache, ready (+3 more)

### Community 180 - "AnimalAI.h"
Cohesion: 0.14
Nodes (22): 12.7 Mob managers (how data, AI and model connect), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+14 more)

### Community 181 - "verify_ui_logic_sim.py"
Cohesion: 0.38
Nodes (3): MockOptions, test_ds_original_menu_logic(), test_dsi_profile_and_fps_target()

### Community 182 - "Liquid.cpp"
Cohesion: 0.25
Nodes (3): isHell(), popDue(), pushTick()

### Community 183 - "Clouds.cpp"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 184 - "test_print_row_safety.py"
Cohesion: 1.00
Nodes (3): print_row_sim(), test_all_options(), visual_length()

### Community 186 - "9. Entities and physics notes"
Cohesion: 0.29
Nodes (7): 13. Audio, playClip(), raw(), Sound::note(), Sound::playerHurt(), Sound::rain(), Sound::thunder()

### Community 187 - "P"
Cohesion: 0.50
Nodes (4): P, x, y, z

### Community 188 - "ExplosionDamage.h"
Cohesion: 0.83
Nodes (3): compute(), exposure(), lineClear()

### Community 189 - "Profiler.h"
Cohesion: 0.22
Nodes (6): ProfScope, slot, start, ProfStep, label, start

### Community 191 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 193 - "Drop"
Cohesion: 0.29
Nodes (7): Drop, count, durability, type, x, y, z

### Community 200 - "Sound.h"
Cohesion: 0.22
Nodes (8): Group, G_GRASS, G_GRAVEL, G_SAND, G_SNOW, G_STONE, G_WOOD, Sound::groupOf()

### Community 202 - "Drop"
Cohesion: 0.29
Nodes (7): Drop, count, durability, type, x, y, z

### Community 203 - "12. Rendering, textures and models"
Cohesion: 0.29
Nodes (5): 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 204 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 205 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 206 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

### Community 207 - "Box"
Cohesion: 0.29
Nodes (7): Box, maxX, maxY, maxZ, minX, minY, minZ

### Community 209 - "ArrowHurtCtx"
Cohesion: 0.67
Nodes (3): ArrowHurtCtx, hs, player

### Community 210 - "PlayerPos"
Cohesion: 0.40
Nodes (5): PlayerPos, valid, x, y, z

### Community 211 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 212 - "isLiquidBlock"
Cohesion: 0.12
Nodes (16): isCrossPlant(), isFlatInHand(), isLightOpaque(), isLiquidBlock(), isPartialBlock(), isTorchBlock(), isWaterBlock(), torchMeta() (+8 more)

### Community 217 - "Art"
Cohesion: 0.33
Nodes (6): Art, ox, oy, sx, sy, title

### Community 221 - "Sign"
Cohesion: 0.33
Nodes (6): Sign, active, gx, gy, gz, text

### Community 222 - "Sky.cpp"
Cohesion: 0.53
Nodes (4): Sky::draw(), uv(), v(), vert()

### Community 225 - "bump"
Cohesion: 0.50
Nodes (3): BoatManager::riderEye(), bump(), eyeOf()

## Knowledge Gaps
- **1482 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1477 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1987 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **37 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `HandAnimations.cpp`, `Sim`, `Chunk.cpp`, `Block and Item Types`, `Painting and Art Types`, `Dropped Item Physics`, `Block and Item Types`, `Crafting Recipes`, `NetherGen.h`, `GameplayHotbar.cpp`, `BlockType.h`, `Sound.cpp`, `Inventory`, `Furnace.cpp`, `.setBlockDirect`, `Pistons.cpp`, `Controls & ItemOrder`, `ChunkManager Module`, `AnimalManager Module`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `Block and Item Types`, `RailLogic Module`, `isNormalCube`, `Block and Item Types`, `Block and Item Types`, `HostileManager Module`, `PartialBlocks.h`, `MinecartManager.cpp`, `Noise.cpp`, `M`, `notify`, `Caves.cpp`, `Vehicle Entity (MinecartModel)`, `InventoryScreen.cpp`, `main.cpp`, `BoatManager.cpp`, `bigTreeComputeBranches`, `CMWorld`, `Maps Module`, `DebugChests.h`, `nds`, `NoteBlocks.cpp`, `BigTree`, `CartWorld`, `rand`, `.floodFillSkyLight`, `FishingHook.cpp`, `HostileManager Module`, `Recipe`, `TntManager.cpp`, `VoxelColumnRLE`, `Projectiles Module`, `Drop`, `7. World engine in detail`, `BoatWorld`, `TickInput`, `HostileManager Module`, `stdlib`, `CMWorld`, `T`, `Chunk.h`, `SheepManager Module`, `AnimalManager Module`, `Redstone.cpp`, `Chunk.h`, `Drop`, `Redstone Logic (Redstone)`, `chunkOf`, `Redstone Logic (Redstone)`, `PendingDrops.h`, `BlockFace`, `9. Entities and physics notes`, `Liquid.cpp`, `NetherTerrain`, `Drop`, `Sound.h`, `Drop`, `isLiquidBlock`?**
  _High betweenness centrality (0.265) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1482 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `Chunk` connect `Chunk Meshing and Bands` to `Block and Item Types`, `Chunk.h`, `Chunk.cpp`, `VoxelColumnRLE`, `Block and Item Types`, `9. Entities and physics notes`, `Biome & Chunk`, `isLiquidBlock`, `7. World engine in detail`, `Noise.cpp`, `.setBlockDirect`, `.saveToFileAsync`, `Cube Module`, `.computeColumnFacesBitwise`, `Climate.h`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 88 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 88 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020833333333333332 - nodes in this community are weakly interconnected._