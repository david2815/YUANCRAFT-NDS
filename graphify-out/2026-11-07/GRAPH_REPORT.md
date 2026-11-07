# Graph Report - YUANCRAFT NDS PORT  (2026-11-07)

## Corpus Check
- 297 files · ~384,653 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 70 file(s) not represented in the graph (top: .grit 49, (none) 8, .ini 3)

## Summary
- 4695 nodes · 10400 edges · 236 communities (194 shown, 42 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1195 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1466598d`
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
- Spawners.cpp
- .saveToFileAsync
- Block and Item Types
- PaintingManager.cpp
- Weather.cpp
- Dropped Item Physics
- ChunkManager Module
- Block and Item Types
- AnimalModel.cpp
- Crafting Recipes
- NetherGen.h
- GameplayHotbar.cpp
- BlockType.h
- AnimalAI.h
- Inventory
- Entity AI (HostileAI)
- Furnace.cpp
- AsyncSaveManager
- DisplayListBuilder Module
- WorldSelectMenu.cpp
- WorldSave Module
- .generateBigOakTree
- nds
- Pistons.cpp
- Texture & PaintingTex
- Controls & ItemOrder
- stbi_uc
- AnimalManager Module
- isNormalCube
- Block and Item Types
- RailLogic Module
- Texture and Image Decoding
- isLiquidBlock
- Texture Module
- Block and Item Types
- SheepManager.cpp
- HostileManager Module
- DebugLogger
- MinecartManager.cpp
- Projectiles Module
- SignManager Module
- Noise.cpp
- Profiler Module
- Profiler Module
- FishingHook.cpp
- PartialBlocks.h
- Redstone.cpp
- NewWorldMenu.cpp
- Caves.cpp
- Health Module
- HostileManager Module
- Vehicle Entity (MinecartModel)
- CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)
- Texture and Image Decoding
- Texture.h
- MobBody
- CMWorld
- PathWork
- main.cpp
- BoatManager.cpp
- Texture and Image Decoding
- Chunk.cpp
- World
- Maps Module
- DebugChests.h
- SteveModel.cpp
- PerformancePreset.cpp
- Minecraft: Nintendo DS Edition
- Sim
- IpcChunkLoader
- CartWorld
- Options Module
- isLeavesBlock
- BiomeType
- .floodFillSkyLight
- Caves Module
- InventoryScreen.cpp
- Hook
- HostileManager Module
- Projectiles.cpp
- BoatModel.cpp
- Sound.cpp
- MobCull & Caves
- BlockFace
- Tick
- TextKeyboard Module
- Hardware
- re
- Caves Module
- Particles.cpp
- verify_world_select_simulation.py
- JRandom
- BigTree
- TopScreenMenu & Renderer
- TntManager.cpp
- FaceMask
- VoxelColumnRLE
- CMWorld
- rand
- ChestStore.cpp
- Recipe
- SheepModel Module
- Chunk.h
- Sphere
- verify_ipc_streaming_simulation.py
- WorldMetadata
- Animal
- verify_deadlock_and_memory_simulation.py
- Painting
- build.sh
- Climate.h
- PauseScreen Module
- TickInput
- MockHardwareNDS
- HostileManager Module
- SettingsMenu.cpp
- HwMath
- 12. Rendering, textures and models
- BoatWorld
- MockHardwareState
- PerformancePreset
- Env
- T
- MockAsyncSaveManager
- Lakes.h
- FlatQuad
- HotbarIcons.cpp
- Catch
- PerlinNoise
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- .update
- AnimItems.cpp
- notify
- PendingDrops.h
- World
- Part
- Dispenser.cpp
- .generateColumn
- HostileManager Module
- Drop
- RenderInput
- Redstone Logic (Redstone)
- 5.2 Blocks, items, inventory, crafting
- Drop
- Caves Module
- Lat
- ColorMaps & ColorMapData
- M
- HostileManager Module
- Redstone Logic (Redstone)
- PlayerHit
- verify_simulation
- Cell
- Kind
- HudQuad
- Redstone Logic (Redstone)
- os
- Projectiles.h
- test_emulator_run.py
- verify_occupancy_simulation.py
- FallingBlocks.cpp
- HostileModel.cpp
- Health.h
- Drop
- verify_ui_logic_sim.py
- LakeTerrain
- Clouds.cpp
- test_print_row_safety.py
- NetherTerrain
- run_full_hardware_verification.py
- P
- math
- Drop
- Particles::tick
- LoadingScreen.cpp
- Quad
- Kind
- Liquid.cpp
- StartupSplash.cpp
- Quad
- debug_single_run.py
- Quad
- isLiquidBlock
- ctypes
- Vtx
- GameOverScreen.cpp
- P3
- Pose
- SubScreenMenu.cpp
- Rng
- Rng
- HandAnimations::renderItemThirdPerson
- Art
- Sky.cpp
- PlayerPos
- bump
- Maps.h
- Trees.h

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 217 edges
3. `main()` - 205 edges
4. `ChunkManager` - 107 edges
5. `Player` - 94 edges
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

## Communities (236 total, 42 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (86): BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor, CACHE_RECALC_BATCH (+78 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.21
Nodes (33): 9.3 Liquids, particles, partial blocks, doubleOfSlab(), activate(), boxHit(), chunkOf(), cropCanStay(), cropsTick(), dropAt() (+25 more)

### Community 3 - "Block and Item Types"
Cohesion: 0.06
Nodes (73): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+65 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (60): main(), Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase, bobStrength, buttonLookSpeedH, buttonLookSpeedV (+52 more)

### Community 5 - "Texture and Image Decoding"
Cohesion: 0.07
Nodes (59): main(), stbi_convert_iphone_png_to_rgb(), stbi_convert_iphone_png_to_rgb_thread(), stbi_convert_wchar_to_utf8(), stbi__do_zlib(), stbi_failure_reason(), stbi__float_postprocess(), stbi__fopen() (+51 more)

### Community 6 - "Texture and Image Decoding"
Cohesion: 0.09
Nodes (64): stbi__at_eof(), stbi__bitcount(), stbi__bmp_info(), stbi__bmp_load(), stbi__bmp_parse_header(), stbi__bmp_set_mask_defaults(), stbi__bmp_test(), stbi__bmp_test_raw() (+56 more)

### Community 7 - "HandAnimations.cpp"
Cohesion: 0.17
Nodes (21): 12.6 Mob models (`ModelBox.h`, `*Model.cpp`), applyViewBobbing(), blockRenderColor(), drawBlockInHand(), drawFirstPersonArm(), drawItem2D(), drawMapHeld(), HandAnimations::applyWorldViewBobbing() (+13 more)

### Community 8 - "Image Writing Utilities"
Cohesion: 0.09
Nodes (50): stb_image_write_test, stbi__end_write_file(), stbi_flip_vertically_on_write(), stbi__start_write_callbacks(), stbi__start_write_file(), stbi_write_bmp(), stbi_write_bmp_core(), stbi_write_bmp_to_func() (+42 more)

### Community 9 - "Spawners.cpp"
Cohesion: 0.17
Nodes (18): chunkAt(), ChunkManager, cx(), cy(), cz(), Entry, delay, gx (+10 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.07
Nodes (27): P, active, age, b, baseScale, col, g, gravity (+19 more)

### Community 12 - "PaintingManager.cpp"
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
Cohesion: 0.15
Nodes (19): getBlockTextures(), woolCell(), applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad(), drawLodTopQuad(), emitCenteredCrossQuad() (+11 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.19
Nodes (15): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+7 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.09
Nodes (22): 9.7 Inventory and crafting UI internals, hasDurability(), ChestView, CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt() (+14 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.12
Nodes (16): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+8 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.22
Nodes (3): GameplayHotbar, bgId, isInButtonRow()

### Community 21 - "BlockType.h"
Cohesion: 0.08
Nodes (51): armorMaterial(), armorRenderIndex(), blockHardness(), canHarvestBlock(), dyeDamage(), fireCatch(), fireEncourage(), furnaceFrontDir() (+43 more)

### Community 22 - "AnimalAI.h"
Cohesion: 0.14
Nodes (22): 12.7 Mob managers (how data, AI and model connect), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+14 more)

### Community 23 - "Inventory"
Cohesion: 0.11
Nodes (26): armorMaxDurability(), armorPiece(), armorReduceAmount(), getToolMaxDurability(), isArmor(), isBucket(), isRecord(), maxStackFor() (+18 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.14
Nodes (32): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), arrowTick(), attackBlocked(), attackEntity(), boxClear(), brightnessAt(), canSee(), canSpawnHere() (+24 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.09
Nodes (30): canSmelt(), clearEntry(), clearSlot(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate(), Furnace::fuelBurnTime(), Furnace::loadFromFile() (+22 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.08
Nodes (19): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+11 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "WorldSelectMenu.cpp"
Cohesion: 0.17
Nodes (3): clearLabelZone(), drawWorldName(), WorldSelectMenu

### Community 29 - "WorldSave Module"
Cohesion: 0.14
Nodes (9): SD card layout, clearFolderContents(), folderExists(), WorldSave, s_activeBasePath, s_activeWorldNum, s_dimension, s_promoted (+1 more)

### Community 30 - ".generateBigOakTree"
Cohesion: 0.12
Nodes (17): BigTreeBranch, trunkY, x, y, z, bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches() (+9 more)

### Community 31 - "nds"
Cohesion: 0.12
Nodes (7): DSI_DebugInit(), DSI_Log(), openLogFile(), draw(), OptionsMenu::open(), OptionsMenu::update(), printRow()

### Community 32 - "Pistons.cpp"
Cohesion: 0.08
Nodes (54): isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend(), canPush() (+46 more)

### Community 33 - "Texture & PaintingTex"
Cohesion: 0.07
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.09
Nodes (25): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+17 more)

### Community 35 - "stbi_uc"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.09
Nodes (12): AnimalManager::attack(), AnimalManager::draw(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath() (+4 more)

### Community 38 - "isNormalCube"
Cohesion: 0.13
Nodes (23): isNormalCube(), airSpawnSpot(), autoMeta(), boundsForMeta(), Box, x0, x1, y0 (+15 more)

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - "isLiquidBlock"
Cohesion: 0.16
Nodes (4): blockLightEmission(), isSapling(), torchFromMeta(), torchMeta()

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.14
Nodes (25): isRailBlock(), bodyBox(), Box, maxX, maxY, maxZ, minX, minY (+17 more)

### Community 45 - "SheepManager.cpp"
Cohesion: 0.08
Nodes (15): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::draw(), SheepManager::explosionDamage() (+7 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.09
Nodes (11): 9.2 Managers: spawning, caps, explosions, 9. Entities and physics notes, collectDeath(), explode(), HostileManager::attack(), HostileManager::interact(), HostileManager::lightning(), HostileManager::popDrop() (+3 more)

### Community 47 - "DebugLogger"
Cohesion: 0.15
Nodes (9): DebugLogger, LINE_LEN, MAX_HISTORY, s_count, s_fatAvailable, s_head, s_history, s_initialized (+1 more)

### Community 48 - "MinecartManager.cpp"
Cohesion: 0.10
Nodes (15): breakCart(), cartCollision(), dismountIndex(), eyeOf(), getI32(), MinecartManager::attack(), MinecartManager::dismount(), MinecartManager::loadFromFile() (+7 more)

### Community 49 - "Projectiles Module"
Cohesion: 0.07
Nodes (28): Proj, active, inGround, kind, mx, my, mz, ownerIsPlayer (+20 more)

### Community 50 - "SignManager Module"
Cohesion: 0.06
Nodes (35): find(), Glyph, c, rows, MenuFont::draw16(), MenuFont::draw8(), MenuFont::fill16(), MenuFont::fill8() (+27 more)

### Community 51 - "Noise.cpp"
Cohesion: 0.13
Nodes (10): Chunk::Chunk(), HeightCache, h, tx, tz, NetherColCache, c, tx (+2 more)

### Community 52 - "Profiler Module"
Cohesion: 0.10
Nodes (17): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike(), Spike (+9 more)

### Community 53 - "Profiler Module"
Cohesion: 0.08
Nodes (21): ProfScope, slot, start, ProfStep, label, start, Slot, DL_CALL (+13 more)

### Community 54 - "FishingHook.cpp"
Cohesion: 0.23
Nodes (13): cellY(), FishingHook::cast(), FishingHook::clear(), FishingHook::draw(), gaussian(), handPos(), nextFloat(), nextInt() (+5 more)

### Community 55 - "PartialBlocks.h"
Cohesion: 0.11
Nodes (26): 9.6 Audio internals (`Sound.cpp`), iconShapeVisible(), isDoorBlock(), isRedstoneComponent(), isRepeaterBlock(), isSignBlock(), isStairsBlock(), bedCell() (+18 more)

### Community 56 - "Redstone.cpp"
Cohesion: 0.19
Nodes (13): bounds(), burnedOut(), canProvidePower(), faceCode(), freeCell(), gettingPowered(), isIndirectlyPoweringTo(), isPoweringTo() (+5 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves.cpp"
Cohesion: 0.18
Nodes (14): allocBlock(), cellRng(), emit(), floorD(), floorDiv(), freeCellBlocks(), jcos(), jsin() (+6 more)

### Community 59 - "Health Module"
Cohesion: 0.09
Nodes (22): HealthState, air, armorPoints, armorWear, armorWearCount, attackedAtYaw, damageRemainder, dead (+14 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.17
Nodes (17): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::count(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn() (+9 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)"
Cohesion: 0.10
Nodes (19): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is, 2. Rules for an AI assistant modifying this project (read carefully) (+11 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

### Community 64 - "Texture.h"
Cohesion: 0.28
Nodes (3): HealthHud::draw(), MenuBackground, texCoordCell()

### Community 65 - "MobBody"
Cohesion: 0.18
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 66 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 67 - "PathWork"
Cohesion: 0.11
Nodes (28): findPath(), heapAdd(), heapChange(), heapDequeue(), heapSortBack(), heapSortForward(), openPoint(), pathHash() (+20 more)

### Community 68 - "main.cpp"
Cohesion: 0.06
Nodes (33): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, ChunkManager, ArrowHurtCtx, hs, player (+25 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.14
Nodes (11): BoatManager::attack(), BoatManager::dismount(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::saveToFile(), breakBoat(), dismountIndex(), forceDismount() (+3 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "Chunk.cpp"
Cohesion: 0.06
Nodes (17): alloc(), callListFast(), chunkFloorDiv(), fillDungeonChest(), flushList(), free(), init(), oreFloorInt() (+9 more)

### Community 72 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 73 - "Maps Module"
Cohesion: 0.13
Nodes (22): find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush(), Maps::pixels() (+14 more)

### Community 74 - "DebugChests.h"
Cohesion: 0.15
Nodes (14): buildItemList(), findSite(), groundHeight(), isGivenItem(), isReplaceable(), isSkippable(), Site, alongX (+6 more)

### Community 75 - "SteveModel.cpp"
Cohesion: 0.16
Nodes (14): addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b, g (+6 more)

### Community 76 - "PerformancePreset.cpp"
Cohesion: 0.15
Nodes (10): ChunkManager, PresetManager, s_currentPreset, PresetType, PRESET_COUNT, PRESET_CUSTOM, PRESET_DS_BALANCED, PRESET_DS_FAST (+2 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (20): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+12 more)

### Community 78 - "Sim"
Cohesion: 0.10
Nodes (15): isFlowingLiquid(), isLavaBlock(), isMaterialSolid(), isWaterBlock(), liquidFlowingOf(), liquidMaterial(), liquidStillOf(), waterSpawnSpot() (+7 more)

### Community 79 - "IpcChunkLoader"
Cohesion: 0.06
Nodes (27): Chunk, ChunkManager, IpcChunkExchange, chunkX, chunkZ, compBuffer, dataSize, frameCounter (+19 more)

### Community 80 - "CartWorld"
Cohesion: 0.17
Nodes (7): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn()

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "isLeavesBlock"
Cohesion: 0.18
Nodes (14): 9.5 World-generation pieces, isLeavesBlock(), beginFrame(), freeOrLeaves(), genRound(), genSpruce(), isLog(), markLeaf() (+6 more)

### Community 83 - "BiomeType"
Cohesion: 0.12
Nodes (15): BiomeType, DESERT, FOREST, GENERIC, OCEAN, PLAINS, RAINFOREST, SAVANNA (+7 more)

### Community 84 - ".floodFillSkyLight"
Cohesion: 0.23
Nodes (6): lightDim(), LightNode, bx, by, bz, level

### Community 85 - "Caves Module"
Cohesion: 0.12
Nodes (17): Job, active, cx, cz, fill, nOrigins, originIdx, ox (+9 more)

### Community 86 - "InventoryScreen.cpp"
Cohesion: 0.19
Nodes (10): drawCountAt(), drawDigit(), drawDurabilityBar(), drawIconAt(), drawSelectionBoxAt(), getItemsPixelIndex(), getSlotPosition(), getTerrainPixelIndex() (+2 more)

### Community 87 - "Hook"
Cohesion: 0.12
Nodes (17): Hook, active, hooked, inGround, mobIndex, mx, my, mz (+9 more)

### Community 88 - "HostileManager Module"
Cohesion: 0.18
Nodes (6): exposure(), HWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 89 - "Projectiles.cpp"
Cohesion: 0.22
Nodes (15): brightnessOf(), cellY(), chunkOf(), eggBreak(), gaussian(), nextFloat(), nextInt(), nextU() (+7 more)

### Community 90 - "BoatModel.cpp"
Cohesion: 0.17
Nodes (12): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+4 more)

### Community 91 - "Sound.cpp"
Cohesion: 0.05
Nodes (49): 13. Audio, ChunkManager, Entry, gx, gy, gz, note, prev (+41 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.13
Nodes (12): state, set(), State, lx, ly, lz, maxDist2, valid (+4 more)

### Community 93 - "BlockFace"
Cohesion: 0.09
Nodes (26): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+18 more)

### Community 94 - "Tick"
Cohesion: 0.20
Nodes (8): Tick, due, gx, gy, gz, seq, type, used

### Community 95 - "TextKeyboard Module"
Cohesion: 0.23
Nodes (14): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+6 more)

### Community 98 - "Caves Module"
Cohesion: 0.13
Nodes (15): Tunnel, branchStep, isRoom, length, pitch, pitchVel, r, radiusScale (+7 more)

### Community 99 - "Particles.cpp"
Cohesion: 0.37
Nodes (10): alloc(), baseMotion(), Particles::blockBreak(), Particles::blockHit(), Particles::explosion(), Particles::spawn(), Particles::spawnerBurst(), rf() (+2 more)

### Community 100 - "verify_world_select_simulation.py"
Cohesion: 0.21
Nodes (6): main(), simulate_world_select_menu(), test_empty_and_corrupt_world_directory(), test_math_division_shortcut(), test_polygon_budget_and_overflow(), test_world_lifecycle_and_deletion()

### Community 101 - "JRandom"
Cohesion: 0.24
Nodes (6): advanceOrigin(), initTunnel(), JRandom, seed, pushTunnel(), reset()

### Community 102 - "BigTree"
Cohesion: 0.13
Nodes (13): BigTree, AX, basePos, branchSlope, height, heightAttenuation, heightLimit, heightLimitLimit (+5 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.14
Nodes (4): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.11
Nodes (20): blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), Tnt, active, fuse (+12 more)

### Community 105 - "FaceMask"
Cohesion: 0.17
Nodes (10): Cube, drawBox(), FaceMask, bottom, east, north, south, top (+2 more)

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.15
Nodes (8): RLERun, length, type, VoxelColumnRLE, MAX_RUNS, _pad, runCount, runs

### Community 107 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 108 - "rand"
Cohesion: 0.24
Nodes (9): dispenserFrontDir(), rand, Dispenser::dispense(), gauss(), typeAtGrid(), cropDrops(), spawn(), TntManager::primeCell() (+1 more)

### Community 109 - "ChestStore.cpp"
Cohesion: 0.09
Nodes (24): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+16 more)

### Community 110 - "Recipe"
Cohesion: 0.15
Nodes (18): canCraft(), countPatternCells(), doCraft(), Recipe, altA, altB, altC, altD (+10 more)

### Community 111 - "SheepModel Module"
Cohesion: 0.24
Nodes (11): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+3 more)

### Community 112 - "Chunk.h"
Cohesion: 0.09
Nodes (8): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), DisplayListBuilder, Dispenser::popDrop(), ChunkManager, texCoordCell(), isValidMainRamPointer(), isVramPointer(), genColsPerFrame()

### Community 113 - "Sphere"
Cohesion: 0.13
Nodes (13): CarveCursor, cell, sphere, carveSphere(), carveStep(), floorF(), isDecoration(), Sphere (+5 more)

### Community 114 - "verify_ipc_streaming_simulation.py"
Cohesion: 0.19
Nodes (8): main(), MockChunk, MockChunkManager, SimulatedIpcChunkLoader, test_async_streaming_flow(), test_corrupted_file_failsafe(), test_sd_timeout_failsafe(), test_ui_stability_and_vblank_loop()

### Community 115 - "WorldMetadata"
Cohesion: 0.11
Nodes (18): WorldMetadata, armorDurability, armorType, formatVersion, gameTimeTicks, hotbarCount, hotbarDurability, hotbarType (+10 more)

### Community 116 - "Animal"
Cohesion: 0.27
Nodes (18): anyIn(), cellY(), damage(), faceEntity(), headInWater(), inFire(), inLava(), insideOpaque() (+10 more)

### Community 117 - "verify_deadlock_and_memory_simulation.py"
Cohesion: 0.33
Nodes (6): is_valid_main_ram_pointer(), main(), test_60_frame_escape_mechanism(), test_debug_logger_sd_output(), test_ds_4mb_profile(), test_dsi_16mb_profile()

### Community 118 - "Painting"
Cohesion: 0.12
Nodes (17): Painting, active, art, dir, gx, gy, gz, maxX (+9 more)

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 120 - "Climate.h"
Cohesion: 0.09
Nodes (21): biomeFor(), initIfSeedChanged(), Lattice, h, t, x0, z0, Octaves (+13 more)

### Community 121 - "PauseScreen Module"
Cohesion: 0.15
Nodes (9): Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched() (+1 more)

### Community 122 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 123 - "MockHardwareNDS"
Cohesion: 0.23
Nodes (3): main(), MockHardwareNDS, run_simulation()

### Community 125 - "SettingsMenu.cpp"
Cohesion: 0.27
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 127 - "12. Rendering, textures and models"
Cohesion: 0.22
Nodes (6): 12.2 Texture loading (`Texture.h/.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 128 - "BoatWorld"
Cohesion: 0.18
Nodes (9): BoatManager::draw(), BoatManager::spawnFromRay(), BoatManager::tick(), BoatWorld, cacheChunk, cacheCx, cacheCz, cacheReady (+1 more)

### Community 129 - "MockHardwareState"
Cohesion: 0.29
Nodes (3): main(), MockHardwareState, simulate()

### Community 130 - "PerformancePreset"
Cohesion: 0.17
Nodes (12): PerformancePreset, chunk_radius, dsi_only, enable_animated_textures, enable_particles, max_mesh_rebuilds_per_frame, name, render_distance (+4 more)

### Community 131 - "Env"
Cohesion: 0.25
Nodes (8): Env, burningBox, cactus, fallLanded, headInWater, inLava, insideBlock, inWater

### Community 132 - "T"
Cohesion: 0.17
Nodes (16): addWirePos(), anySideNormal(), cartTouchSink(), chunkOf(), doorPower(), dropItem(), floorDivi(), indirectlyGettingPowered() (+8 more)

### Community 134 - "Lakes.h"
Cohesion: 0.09
Nodes (25): apply(), build(), cellIndex(), isShell(), JRandom, seed, Result, lake (+17 more)

### Community 135 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 136 - "HotbarIcons.cpp"
Cohesion: 0.16
Nodes (8): drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon(), getItemsPixelIndex(), getTerrainPixelIndex(), HotbarIcons

### Community 137 - "Catch"
Cohesion: 0.17
Nodes (11): Catch, damage, fish, vx, vy, vz, x, y (+3 more)

### Community 138 - "PerlinNoise"
Cohesion: 0.32
Nodes (4): PerlinNoise, initialized, OCTAVE_COUNT, permutations

### Community 139 - "Redstone Logic (Redstone)"
Cohesion: 0.22
Nodes (9): BoxQuery, everything, found, maxX, maxY, maxZ, minX, minY (+1 more)

### Community 140 - "Redstone Logic (Redstone)"
Cohesion: 0.22
Nodes (9): Def, a, b, c, id, kind, x, y (+1 more)

### Community 141 - "SheepManager Module"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, shear, type, x, y, z

### Community 142 - "Entity AI (BoatAI)"
Cohesion: 0.54
Nodes (5): bodyBox(), boxInWater(), moveEntity(), rayHit(), tick()

### Community 143 - "AnimalManager Module"
Cohesion: 0.25
Nodes (7): ChunkManager, Drop, count, type, x, y, z

### Community 146 - ".update"
Cohesion: 0.12
Nodes (10): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.5 Meshing and drawing, 7.6 Saving, 7. World engine in detail (+2 more)

### Community 147 - "AnimItems.cpp"
Cohesion: 0.20
Nodes (3): AnimItems::init(), AnimItems::tick(), setFrame()

### Community 148 - "notify"
Cohesion: 0.23
Nodes (15): activate(), blockChanged(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved(), neighborChanged() (+7 more)

### Community 149 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 150 - "World"
Cohesion: 0.18
Nodes (7): drawSprite(), Projectiles::draw(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 151 - "Part"
Cohesion: 0.17
Nodes (12): Part, faceMask, pointX, pointY, pointZ, px, py, pz (+4 more)

### Community 152 - "Dispenser.cpp"
Cohesion: 0.18
Nodes (10): ChunkManager, Drop, durability, type, vx, vy, vz, x (+2 more)

### Community 153 - ".generateColumn"
Cohesion: 0.22
Nodes (6): getPatchAt(), findLandChunkOffset(), hash2D(), Noise, randomGridValue(), smoothstep()

### Community 154 - "HostileManager Module"
Cohesion: 0.29
Nodes (7): SavedWolf, health, sitting, x, y, yaw, z

### Community 155 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 157 - "RenderInput"
Cohesion: 0.17
Nodes (10): ChunkManager, RenderInput, bodyLight, dimension, eyeLight, partialTicks, pitch, posX (+2 more)

### Community 158 - "Redstone Logic (Redstone)"
Cohesion: 0.29
Nodes (7): Tick, due, seq, t, x, y, z

### Community 159 - "5.2 Blocks, items, inventory, crafting"
Cohesion: 0.19
Nodes (14): 5.2 Blocks, items, inventory, crafting, blockRemoved(), EntityEnumerator, indirectPowerAt(), lightOre(), notifyNeighbors(), setEntityEnumerator(), setMinecartEnumerator() (+6 more)

### Community 160 - "Drop"
Cohesion: 0.20
Nodes (9): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+1 more)

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "Lat"
Cohesion: 0.18
Nodes (11): Lat, a, b, n1, n2, n3, LatCache, ready (+3 more)

### Community 163 - "ColorMaps & ColorMapData"
Cohesion: 0.48
Nodes (3): ColorMaps::foliage(), ColorMaps::grass(), lookup()

### Community 164 - "M"
Cohesion: 0.26
Nodes (17): isPlateBlock(), detectorCheck(), indirectProvidingPowerTo(), M(), plateBox(), plateCheck(), randomTick(), repeaterCheck() (+9 more)

### Community 165 - "HostileManager Module"
Cohesion: 0.33
Nodes (6): PendingExplosion, flaming, size, x, y, z

### Community 166 - "Redstone Logic (Redstone)"
Cohesion: 0.33
Nodes (6): Rem, m, t, x, y, z

### Community 167 - "PlayerHit"
Cohesion: 0.22
Nodes (9): HostileManager::popPlayerHit(), PlayerHit, amount, explosion, kx, ky, kz, srcX (+1 more)

### Community 168 - "verify_simulation"
Cohesion: 0.32
Nodes (5): verify_simulation(), is_vram(), setup_projection(), simulate_frame(), validate_decompress_args()

### Community 169 - "Cell"
Cohesion: 0.25
Nodes (8): Cell, count, cx, cz, first, lastUse, nblocks, pad

### Community 170 - "Kind"
Cohesion: 0.15
Nodes (12): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+4 more)

### Community 171 - "HudQuad"
Cohesion: 0.29
Nodes (7): build(), HudQuad, layer, u, v, x, y

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 173 - "os"
Cohesion: 0.08
Nodes (6): verify_structural(), verify_structural(), main(), verify_structural(), verify_structural(), verify_all()

### Community 174 - "Projectiles.h"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

### Community 177 - "FallingBlocks.cpp"
Cohesion: 0.12
Nodes (15): ChunkManager, Falling, active, fallTime, prevY, type, vy, x (+7 more)

### Community 178 - "HostileModel.cpp"
Cohesion: 0.08
Nodes (40): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawPartAt() (+32 more)

### Community 179 - "Health.h"
Cohesion: 0.24
Nodes (8): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), hurtCameraRoll(), randomBit(), tick()

### Community 180 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 181 - "verify_ui_logic_sim.py"
Cohesion: 0.38
Nodes (3): MockOptions, test_ds_original_menu_logic(), test_dsi_profile_and_fps_target()

### Community 183 - "Clouds.cpp"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 184 - "test_print_row_safety.py"
Cohesion: 1.00
Nodes (3): print_row_sim(), test_all_options(), visual_length()

### Community 186 - "run_full_hardware_verification.py"
Cohesion: 0.31
Nodes (6): find_ds_ram_base(), get_elf_sym(), get_target_ds_addr(), main(), MEMORY_BASIC_INFORMATION, run_test()

### Community 187 - "P"
Cohesion: 0.50
Nodes (4): P, x, y, z

### Community 188 - "math"
Cohesion: 0.27
Nodes (7): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math(), compute(), exposure(), lineClear()

### Community 189 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 191 - "Particles::tick"
Cohesion: 0.31
Nodes (6): brightnessOf(), move(), Particles::draw(), Particles::tick(), update(), W

### Community 193 - "LoadingScreen.cpp"
Cohesion: 0.29
Nodes (4): 9.8 More internals (Nether, sky, saves, menus, chests, notes), copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen

### Community 200 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 201 - "Kind"
Cohesion: 0.25
Nodes (8): Kind, K_BACK, K_CANCEL, K_CHAR, K_CLEAR, K_OK, K_SHIFT, K_SPACE

### Community 202 - "Liquid.cpp"
Cohesion: 0.25
Nodes (3): isHell(), popDue(), pushTick()

### Community 204 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 205 - "debug_single_run.py"
Cohesion: 0.36
Nodes (4): get_elf_sym(), get_target_ds_addr(), main(), MEMORY_BASIC_INFORMATION

### Community 206 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 207 - "isLiquidBlock"
Cohesion: 0.15
Nodes (13): getGrassTint(), isCrossPlant(), isFlatInHand(), isLightOpaque(), isLiquidBlock(), isPartialBlock(), isStructureBlock(), isTorchBlock() (+5 more)

### Community 208 - "ctypes"
Cohesion: 0.10
Nodes (22): enum_child_proc(), inspect_desmume(), inspect(), MEMORY_BASIC_INFORMATION, simulate_old_printrow(), click_coords(), run_test(), capture_window() (+14 more)

### Community 209 - "Vtx"
Cohesion: 0.29
Nodes (7): buildModel(), Vtx, u, v, x, y, z

### Community 212 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 213 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 224 - "HandAnimations::renderItemThirdPerson"
Cohesion: 0.40
Nodes (4): brightnessOf(), HandAnimations::lightLevelAt(), HandAnimations::renderItemThirdPerson(), mapRunCount()

### Community 225 - "Art"
Cohesion: 0.33
Nodes (6): Art, ox, oy, sx, sy, title

### Community 227 - "Sky.cpp"
Cohesion: 0.53
Nodes (4): Sky::draw(), uv(), v(), vert()

### Community 228 - "PlayerPos"
Cohesion: 0.40
Nodes (5): PlayerPos, valid, x, y, z

### Community 229 - "bump"
Cohesion: 0.50
Nodes (3): BoatManager::riderEye(), bump(), eyeOf()

## Knowledge Gaps
- **1513 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1508 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2062 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `BoatWorld`, `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `T`, `HandAnimations.cpp`, `HotbarIcons.cpp`, `PaintingManager.cpp`, `SheepManager Module`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `.update`, `Crafting Recipes`, `NetherGen.h`, `BlockType.h`, `PendingDrops.h`, `Inventory`, `Dispenser.cpp`, `.generateColumn`, `Furnace.cpp`, `Drop`, `World`, `notify`, `.generateBigOakTree`, `5.2 Blocks, items, inventory, crafting`, `Pistons.cpp`, `Drop`, `Redstone Logic (Redstone)`, `M`, `AnimalManager Module`, `isNormalCube`, `Block and Item Types`, `ChunkManager Module`, `RailLogic Module`, `isLiquidBlock`, `Redstone Logic (Redstone)`, `Block and Item Types`, `SheepManager.cpp`, `HostileManager Module`, `MinecartManager.cpp`, `FallingBlocks.cpp`, `Drop`, `PartialBlocks.h`, `Redstone.cpp`, `NetherTerrain`, `Drop`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `Vehicle Entity (MinecartModel)`, `CMWorld`, `BoatManager.cpp`, `Chunk.cpp`, `World`, `Maps Module`, `DebugChests.h`, `Liquid.cpp`, `SteveModel.cpp`, `Sim`, `isLiquidBlock`, `CartWorld`, `isLeavesBlock`, `.floodFillSkyLight`, `InventoryScreen.cpp`, `HostileManager Module`, `Sound.cpp`, `BlockFace`, `HandAnimations::renderItemThirdPerson`, `Particles.cpp`, `BigTree`, `TntManager.cpp`, `VoxelColumnRLE`, `CMWorld`, `rand`, `Recipe`, `Sphere`, `TickInput`?**
  _High betweenness centrality (0.230) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1513 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Player Module` to `HandAnimations.cpp`, `HotbarIcons.cpp`, `Catch`, `Crafting Recipes`, `GameplayHotbar.cpp`, `BlockType.h`, `PendingDrops.h`, `Inventory`, `.generateColumn`, `AsyncSaveManager`, `WorldSelectMenu.cpp`, `WorldSave Module`, `nds`, `Pistons.cpp`, `Texture & PaintingTex`, `M`, `isNormalCube`, `Block and Item Types`, `DebugLogger`, `PartialBlocks.h`, `NewWorldMenu.cpp`, `LoadingScreen.cpp`, `main.cpp`, `PerformancePreset.cpp`, `Sim`, `isLiquidBlock`, `IpcChunkLoader`, `isLeavesBlock`, `GameOverScreen.cpp`, `InventoryScreen.cpp`, `SubScreenMenu.cpp`, `BlockFace`, `Hardware`, `TopScreenMenu & Renderer`, `rand`, `Recipe`, `HwMath`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 90 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 90 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020631281960853464 - nodes in this community are weakly interconnected._