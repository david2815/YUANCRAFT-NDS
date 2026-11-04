# Graph Report - YUANCRAFT NDS PORT  (2026-11-04)

## Corpus Check
- 269 files · ~373,331 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 55 file(s) not represented in the graph (top: .grit 49, (none) 4, .ini 1)

## Summary
- 4548 nodes · 10072 edges · 222 communities (184 shown, 38 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1174 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ce0b55fc`
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
- isNormalCube
- Chunk.cpp
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
- Sound.cpp
- Inventory
- Entity AI (HostileAI)
- Furnace.cpp
- AsyncSaveManager
- DisplayListBuilder Module
- Spawners & Particles
- WorldSave Module
- ChunkManager
- stdio
- Pistons.cpp
- Texture & PaintingTex
- Controls & ItemOrder
- stb_image.h
- AnimalManager Module
- GameOverScreen.cpp
- Block and Item Types
- RailLogic Module
- Texture and Image Decoding
- isLiquidBlock
- Texture Module
- Block and Item Types
- Block and Item Types
- HostileManager Module
- DebugLogger
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
- HotbarIcons.cpp
- Texture and Image Decoding
- WorldSelectMenu Module
- AnimalAI.h
- PathWork
- HostileModel.cpp
- main.cpp
- BoatManager.cpp
- Texture and Image Decoding
- bigTreeComputeBranches
- CMWorld
- Maps Module
- DebugChests.h
- SteveModel.cpp
- NoteBlocks.cpp
- Minecraft: Nintendo DS Edition
- Sim
- IpcChunkLoader
- CartWorld
- Options Module
- BigTree
- BiomeType
- .floodFillSkyLight
- Caves Module
- InventoryScreen.cpp
- Hook
- HostileManager Module
- Projectiles.cpp
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
- .setBlockWithNotify
- VoxelColumnRLE
- MockHardwareNDS
- FishingHook.cpp
- ChestStore.cpp
- .sqrtf
- SheepModel Module
- Dispenser.cpp
- Sphere
- verify_ipc_streaming_simulation.py
- Lakes Module
- 7. World engine in detail
- verify_deadlock_and_memory_simulation.py
- Env
- build.sh
- PNode
- PauseScreen Module
- TickInput
- World
- HostileManager Module
- SettingsMenu.cpp
- explode
- isPlaceable
- PlayerHit
- Chunk.h
- CMWorld
- T
- MockAsyncSaveManager
- Teleporter.h
- World
- .update
- SubScreenMenu.cpp
- PartialBlocks.h
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- HealthHudLayout Module
- Redstone.cpp
- AnimItems.cpp
- StartupSplash Module
- IpcChunkExchange
- FallingBlocks.cpp
- ChestStore.cpp
- Chunk Module
- HostileManager Module
- Drop
- RenderInput
- Redstone Logic (Redstone)
- Catch
- Drop
- Caves Module
- useItem
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
- PerlinNoise
- verify_occupancy_simulation.py
- Projectiles.h
- FlatQuad
- isStructureBlock
- Box
- verify_ui_logic_sim.py
- Liquid.h
- Clouds.cpp
- test_print_row_safety.py
- NetherTerrain
- Lat
- P
- math
- Profiler.h
- ModelBox.h
- Spike
- .fireUpdateTick
- Rng
- Box
- 12. Rendering, textures and models
- Quad
- Pose
- Sign
- MockChunk
- ctypes
- PlayerPos
- packSpot
- P3
- Result
- .markDisplayListDirty
- Texture.h

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 215 edges
3. `main()` - 199 edges
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

## Communities (222 total, 38 thin omitted)

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
Nodes (72): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+64 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (57): main(), Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase, bobStrength, buttonLookSpeedH, buttonLookSpeedV (+49 more)

### Community 5 - "Texture and Image Decoding"
Cohesion: 0.10
Nodes (35): main(), stbi_convert_iphone_png_to_rgb(), stbi_convert_iphone_png_to_rgb_thread(), stbi_convert_wchar_to_utf8(), stbi_failure_reason(), stbi__fopen(), stbi_hdr_to_ldr_gamma(), stbi_hdr_to_ldr_scale() (+27 more)

### Community 6 - "Texture and Image Decoding"
Cohesion: 0.11
Nodes (60): stbi__at_eof(), stbi__bmp_info(), stbi__bmp_load(), stbi__bmp_parse_header(), stbi__bmp_set_mask_defaults(), stbi__bmp_test(), stbi__bmp_test_raw(), stbi__check_png_header() (+52 more)

### Community 7 - "HandAnimations.cpp"
Cohesion: 0.14
Nodes (25): 12.6 Mob models (`ModelBox.h`, `*Model.cpp`), applyViewBobbing(), blockRenderColor(), brightnessOf(), drawBlockInHand(), drawFirstPersonArm(), drawItem2D(), drawMapHeld() (+17 more)

### Community 8 - "Image Writing Utilities"
Cohesion: 0.09
Nodes (50): stb_image_write_test, stbi__end_write_file(), stbi_flip_vertically_on_write(), stbi__start_write_callbacks(), stbi__start_write_file(), stbi_write_bmp(), stbi_write_bmp_core(), stbi_write_bmp_to_func() (+42 more)

### Community 9 - "isNormalCube"
Cohesion: 0.09
Nodes (30): isNormalCube(), airSpawnSpot(), autoMeta(), boundsForMeta(), Box, x0, x1, y0 (+22 more)

### Community 10 - "Chunk.cpp"
Cohesion: 0.06
Nodes (15): callListFast(), chunkFloorDiv(), fillDungeonChest(), flushList(), oreFloorInt(), OreRng, s, oreVeinBlob() (+7 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.06
Nodes (44): getGrassTint(), alloc(), baseMotion(), brightnessOf(), move(), P, active, age (+36 more)

### Community 12 - "PaintingManager.cpp"
Cohesion: 0.05
Nodes (44): Art, ox, oy, sx, sy, title, brightnessOf(), ChunkManager (+36 more)

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
Cohesion: 0.10
Nodes (26): applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad(), drawLodTopQuad(), emitCenteredCrossQuad(), emitCrossQuad(), emitCube() (+18 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.13
Nodes (21): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+13 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.10
Nodes (19): getToolMaxDurability(), CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt() (+11 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.12
Nodes (16): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+8 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.22
Nodes (3): GameplayHotbar, bgId, isInButtonRow()

### Community 21 - "BlockType.h"
Cohesion: 0.09
Nodes (44): armorMaterial(), armorMaxDurability(), armorPiece(), armorReduceAmount(), armorRenderIndex(), blockHardness(), canHarvestBlock(), dyeDamage() (+36 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.05
Nodes (51): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 13. Audio, 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is (+43 more)

### Community 23 - "Inventory"
Cohesion: 0.11
Nodes (28): 9.7 Inventory and crafting UI internals, hasDurability(), isArmor(), isBucket(), isMinecartItem(), isRecord(), maxStackFor(), ChestStore::transferWithInventory() (+20 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.12
Nodes (35): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), isWaterBlock(), liquidFlowingOf(), liquidStillOf(), arrowTick(), attackBlocked(), attackEntity(), brightnessAt() (+27 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.09
Nodes (30): canSmelt(), clearEntry(), clearSlot(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate(), Furnace::fuelBurnTime(), Furnace::loadFromFile() (+22 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.08
Nodes (19): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+11 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "Spawners & Particles"
Cohesion: 0.09
Nodes (30): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+22 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.14
Nodes (10): 9.8 More internals (Nether, sky, saves, menus, chests, notes), SD card layout, clearFolderContents(), folderExists(), WorldSave, s_activeBasePath, s_activeWorldNum, s_dimension (+2 more)

### Community 30 - "ChunkManager"
Cohesion: 0.17
Nodes (3): blockLightEmission(), torchFromMeta(), bigTreeDrawLine()

### Community 31 - "stdio"
Cohesion: 0.17
Nodes (4): draw(), OptionsMenu::open(), OptionsMenu::update(), printRow()

### Community 32 - "Pistons.cpp"
Cohesion: 0.07
Nodes (65): 5.2 Blocks, items, inventory, crafting, isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend() (+57 more)

### Community 33 - "Texture & PaintingTex"
Cohesion: 0.07
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.09
Nodes (25): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+17 more)

### Community 35 - "stb_image.h"
Cohesion: 0.06
Nodes (61): load_jpeg_image(), resample_row_1(), stbi__bitcount(), stbi__blinn_8x8(), stbi__clamp(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16() (+53 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.09
Nodes (12): AnimalManager::attack(), AnimalManager::draw(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath() (+4 more)

### Community 39 - "Block and Item Types"
Cohesion: 0.12
Nodes (4): isLavaBlock(), rayStops(), LiquidWorld, m

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.19
Nodes (23): stbi__addints_valid(), stbi__bitreverse16(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__extend_receive(), stbi__get_marker() (+15 more)

### Community 42 - "isLiquidBlock"
Cohesion: 0.12
Nodes (16): findSpawn(), isCrossPlant(), isLightOpaque(), isLiquidBlock(), isMaterialSolid(), isPartialBlock(), isTorchBlock(), torchMeta() (+8 more)

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
Nodes (5): countAlive(), HostileManager::count(), HostileManager::interact(), HostileManager::popDrop(), rf01()

### Community 47 - "DebugLogger"
Cohesion: 0.14
Nodes (9): DebugLogger, LINE_LEN, MAX_HISTORY, s_count, s_fatAvailable, s_head, s_history, s_initialized (+1 more)

### Community 48 - "MinecartManager.cpp"
Cohesion: 0.11
Nodes (13): breakCart(), cartCollision(), dismountIndex(), eyeOf(), getI32(), MinecartManager::attack(), MinecartManager::dismount(), MinecartManager::loadFromFile() (+5 more)

### Community 49 - "Projectiles Module"
Cohesion: 0.07
Nodes (28): Proj, active, inGround, kind, mx, my, mz, ownerIsPlayer (+20 more)

### Community 50 - "SignManager Module"
Cohesion: 0.14
Nodes (12): Box, q, brightnessOf(), buildBox(), ChunkManager, drawBox(), drawText(), find() (+4 more)

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
Cohesion: 0.26
Nodes (17): isPlateBlock(), detectorCheck(), indirectlyGettingPowered(), indirectProvidingPowerTo(), M(), plateBox(), plateCheck(), randomTick() (+9 more)

### Community 55 - "LoadingScreen.cpp"
Cohesion: 0.43
Nodes (3): copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen

### Community 56 - "notify"
Cohesion: 0.17
Nodes (21): activate(), blockChanged(), blockRemoved(), bounds(), burnedOut(), buttonRelease(), drainDeferred(), drainRemoved() (+13 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.21
Nodes (6): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, show()

### Community 58 - "Caves.cpp"
Cohesion: 0.18
Nodes (14): allocBlock(), cellRng(), emit(), floorD(), floorDiv(), freeCellBlocks(), jcos(), jsin() (+6 more)

### Community 59 - "Health Module"
Cohesion: 0.09
Nodes (30): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), HealthState, air, armorPoints (+22 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.19
Nodes (15): addMob(), categoryCount(), halfCap(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn(), HostileManager::spawnPigZombie(), HostileManager::tick() (+7 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "HotbarIcons.cpp"
Cohesion: 0.16
Nodes (8): drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon(), getItemsPixelIndex(), getTerrainPixelIndex(), HotbarIcons

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.14
Nodes (23): stbi__addsizes_valid(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone(), stbi__do_png() (+15 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.19
Nodes (3): clearLabelZone(), drawWorldName(), WorldSelectMenu

### Community 65 - "AnimalAI.h"
Cohesion: 0.20
Nodes (28): anyIn(), blocking(), bodyBox(), calcX(), calcY(), calcZ(), cellBox(), cellY() (+20 more)

### Community 66 - "PathWork"
Cohesion: 0.19
Nodes (18): findPath(), heapAdd(), heapChange(), heapDequeue(), heapSortBack(), heapSortForward(), openPoint(), pathHash() (+10 more)

### Community 67 - "HostileModel.cpp"
Cohesion: 0.11
Nodes (31): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawPartAt() (+23 more)

### Community 68 - "main.cpp"
Cohesion: 0.06
Nodes (35): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, ChestView, FurnaceData, ChunkManager, ArrowHurtCtx (+27 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.06
Nodes (30): BoatManager::attack(), BoatManager::dismount(), BoatManager::draw(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::riderEye(), BoatManager::saveToFile(), BoatManager::spawnFromRay() (+22 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.34
Nodes (15): stbi__bit_reverse(), stbi__compute_huffman_codes(), stbi__err(), stbi__fill_bits(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block(), stbi__parse_zlib(), stbi__parse_zlib_header() (+7 more)

### Community 71 - "bigTreeComputeBranches"
Cohesion: 0.13
Nodes (16): BigTreeBranch, trunkY, x, y, z, bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches() (+8 more)

### Community 72 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 73 - "Maps Module"
Cohesion: 0.12
Nodes (23): ChunkManager, find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush() (+15 more)

### Community 74 - "DebugChests.h"
Cohesion: 0.15
Nodes (14): buildItemList(), findSite(), groundHeight(), isGivenItem(), isReplaceable(), isSkippable(), Site, alongX (+6 more)

### Community 75 - "SteveModel.cpp"
Cohesion: 0.09
Nodes (26): addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b, g (+18 more)

### Community 76 - "NoteBlocks.cpp"
Cohesion: 0.12
Nodes (17): ChunkManager, Entry, gx, gy, gz, note, prev, used (+9 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (20): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+12 more)

### Community 78 - "Sim"
Cohesion: 0.20
Nodes (6): liquidMaterial(), Sim, editing, flowCost, numAdjacentSources, optimal

### Community 79 - "IpcChunkLoader"
Cohesion: 0.10
Nodes (16): Chunk, ChunkManager, IpcChunkLoader, MAX_WAIT_FRAMES, s_exchange, s_initialized, TICKS_PER_MS, TIMEOUT_MS (+8 more)

### Community 80 - "CartWorld"
Cohesion: 0.15
Nodes (9): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn(), MinecartManager::tick() (+1 more)

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "BigTree"
Cohesion: 0.07
Nodes (31): 9.5 World-generation pieces, isLeavesBlock(), isSapling(), beginFrame(), BigTree, AX, basePos, branchSlope (+23 more)

### Community 83 - "BiomeType"
Cohesion: 0.05
Nodes (36): BiomeType, DESERT, FOREST, GENERIC, OCEAN, PLAINS, RAINFOREST, SAVANNA (+28 more)

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
Cohesion: 0.17
Nodes (6): exposure(), HWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 89 - "Projectiles.cpp"
Cohesion: 0.22
Nodes (15): brightnessOf(), cellY(), chunkOf(), eggBreak(), gaussian(), nextFloat(), nextInt(), nextU() (+7 more)

### Community 90 - "BoatModel.cpp"
Cohesion: 0.11
Nodes (18): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+10 more)

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
Cohesion: 0.21
Nodes (6): main(), simulate_world_select_menu(), test_empty_and_corrupt_world_directory(), test_math_division_shortcut(), test_polygon_budget_and_overflow(), test_world_lifecycle_and_deletion()

### Community 101 - "JRandom"
Cohesion: 0.24
Nodes (6): advanceOrigin(), initTunnel(), JRandom, seed, pushTunnel(), reset()

### Community 102 - "MobBody & AnimalManager"
Cohesion: 0.18
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.14
Nodes (3): Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.08
Nodes (25): rand, cropDrops(), blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn() (+17 more)

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.13
Nodes (10): isValidMainRamPointer(), isVramPointer(), RLERun, length, type, VoxelColumnRLE, MAX_RUNS, _pad (+2 more)

### Community 107 - "MockHardwareNDS"
Cohesion: 0.23
Nodes (3): main(), MockHardwareNDS, run_simulation()

### Community 108 - "FishingHook.cpp"
Cohesion: 0.23
Nodes (13): cellY(), FishingHook::cast(), FishingHook::clear(), FishingHook::draw(), gaussian(), handPos(), nextFloat(), nextInt() (+5 more)

### Community 109 - "ChestStore.cpp"
Cohesion: 0.12
Nodes (15): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+7 more)

### Community 111 - "SheepModel Module"
Cohesion: 0.13
Nodes (17): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+9 more)

### Community 112 - "Dispenser.cpp"
Cohesion: 0.12
Nodes (15): dispenserFrontDir(), ChunkManager, Dispenser::dispense(), Dispenser::popDrop(), Drop, durability, type, vx (+7 more)

### Community 113 - "Sphere"
Cohesion: 0.13
Nodes (13): CarveCursor, cell, sphere, carveSphere(), carveStep(), floorF(), isDecoration(), Sphere (+5 more)

### Community 114 - "verify_ipc_streaming_simulation.py"
Cohesion: 0.27
Nodes (7): main(), MockChunkManager, SimulatedIpcChunkLoader, test_async_streaming_flow(), test_corrupted_file_failsafe(), test_sd_timeout_failsafe(), test_ui_stability_and_vblank_loop()

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.20
Nodes (7): 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.5 Meshing and drawing, 7.6 Saving, 7. World engine in detail

### Community 117 - "verify_deadlock_and_memory_simulation.py"
Cohesion: 0.33
Nodes (6): is_valid_main_ram_pointer(), main(), test_60_frame_escape_mechanism(), test_debug_logger_sd_output(), test_ds_4mb_profile(), test_dsi_16mb_profile()

### Community 118 - "Env"
Cohesion: 0.25
Nodes (8): Env, burningBox, cactus, fallLanded, headInWater, inLava, insideBlock, inWater

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 120 - "PNode"
Cohesion: 0.20
Nodes (10): PNode, closed, heapIndex, prev, toNext, total, toTarget, x (+2 more)

### Community 121 - "PauseScreen Module"
Cohesion: 0.13
Nodes (9): Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched() (+1 more)

### Community 122 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 123 - "World"
Cohesion: 0.18
Nodes (7): drawSprite(), Projectiles::draw(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 125 - "SettingsMenu.cpp"
Cohesion: 0.25
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 126 - "explode"
Cohesion: 0.29
Nodes (8): 9.2 Managers: spawning, caps, explosions, 9. Entities and physics notes, collectDeath(), explode(), HostileManager::attack(), HostileManager::lightning(), pushDrop(), resistanceOf()

### Community 127 - "isPlaceable"
Cohesion: 0.24
Nodes (12): isAnimalItem(), isDiamondTool(), isFarmItem(), isFlatInHand(), isGoldTool(), isHoeTool(), isMiscItem(), isPlaceable() (+4 more)

### Community 128 - "PlayerHit"
Cohesion: 0.22
Nodes (9): HostileManager::popPlayerHit(), PlayerHit, amount, explosion, kx, ky, kz, srcX (+1 more)

### Community 130 - "Chunk.h"
Cohesion: 0.12
Nodes (5): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), DisplayListBuilder, ChunkManager, texCoordCell(), genColsPerFrame()

### Community 131 - "CMWorld"
Cohesion: 0.17
Nodes (7): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady, SheepManager::draw(), SheepManager::explosionDamage()

### Community 132 - "T"
Cohesion: 0.18
Nodes (15): addWirePos(), anySideNormal(), cartTouchSink(), chunkOf(), doorPower(), dropItem(), floorDivi(), maxStrength() (+7 more)

### Community 134 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 135 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 136 - ".update"
Cohesion: 0.24
Nodes (3): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), cellInWindow(), ChunkManager::ChunkManager()

### Community 138 - "PartialBlocks.h"
Cohesion: 0.23
Nodes (8): 9.6 Audio internals (`Sound.cpp`), bedCell(), bedOffset(), ChunkManager, doorCell(), doorState(), mobWalked(), ChunkManager

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

### Community 146 - "HealthHudLayout Module"
Cohesion: 0.20
Nodes (8): HealthHud::draw(), build(), HudQuad, layer, u, v, x, y

### Community 147 - "Redstone.cpp"
Cohesion: 0.24
Nodes (12): isRedstoneComponent(), isRepeaterBlock(), isSignBlock(), hasCollision(), isInteractive(), canProvidePower(), gettingPowered(), isIndirectlyPoweringTo() (+4 more)

### Community 148 - "AnimItems.cpp"
Cohesion: 0.20
Nodes (3): AnimItems::init(), AnimItems::tick(), setFrame()

### Community 150 - "IpcChunkExchange"
Cohesion: 0.17
Nodes (11): IpcChunkExchange, chunkX, chunkZ, compBuffer, dataSize, frameCounter, path, rawBuffer (+3 more)

### Community 151 - "FallingBlocks.cpp"
Cohesion: 0.12
Nodes (15): ChunkManager, Falling, active, fallTime, prevY, type, vy, x (+7 more)

### Community 152 - "ChestStore.cpp"
Cohesion: 0.29
Nodes (9): ChestStore::clearAll(), ChestStore::findOrCreate(), ChestStore::loadFromFile(), ChestStore::remove(), ChestStore::saveToFile(), clearEntry(), clearSlot(), getI32() (+1 more)

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

### Community 159 - "Catch"
Cohesion: 0.17
Nodes (11): Catch, damage, fish, vx, vy, vz, x, y (+3 more)

### Community 160 - "Drop"
Cohesion: 0.20
Nodes (9): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+1 more)

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "useItem"
Cohesion: 0.33
Nodes (6): faceCode(), freeCell(), lightOre(), put(), setTM(), useItem()

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
Cohesion: 0.08
Nodes (5): verify_structural(), verify_structural(), verify_structural(), verify_structural(), verify_all()

### Community 174 - "BlockFace"
Cohesion: 0.09
Nodes (27): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+19 more)

### Community 175 - "PerlinNoise"
Cohesion: 0.32
Nodes (4): PerlinNoise, initialized, OCTAVE_COUNT, permutations

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

### Community 177 - "Projectiles.h"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 178 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 179 - "isStructureBlock"
Cohesion: 0.24
Nodes (11): isDoorBlock(), isPistonBlock(), isStairsBlock(), isStructureBlock(), bounds(), collisionBounds(), collisionBoxes(), dropsOnMining() (+3 more)

### Community 180 - "Box"
Cohesion: 0.29
Nodes (7): Box, x0, x1, y0, y1, z0, z1

### Community 181 - "verify_ui_logic_sim.py"
Cohesion: 0.38
Nodes (3): MockOptions, test_ds_original_menu_logic(), test_dsi_profile_and_fps_target()

### Community 182 - "Liquid.h"
Cohesion: 0.18
Nodes (4): isHell(), percentAir(), popDue(), pushTick()

### Community 183 - "Clouds.cpp"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 184 - "test_print_row_safety.py"
Cohesion: 1.00
Nodes (3): print_row_sim(), test_all_options(), visual_length()

### Community 186 - "Lat"
Cohesion: 0.18
Nodes (11): Lat, a, b, n1, n2, n3, LatCache, ready (+3 more)

### Community 187 - "P"
Cohesion: 0.50
Nodes (4): P, x, y, z

### Community 188 - "math"
Cohesion: 0.27
Nodes (7): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math(), compute(), exposure(), lineClear()

### Community 189 - "Profiler.h"
Cohesion: 0.22
Nodes (6): ProfScope, slot, start, ProfStep, label, start

### Community 191 - "ModelBox.h"
Cohesion: 0.24
Nodes (9): build(), Face, v, Vertex, u, v, x, y (+1 more)

### Community 193 - "Spike"
Cohesion: 0.20
Nodes (10): Spike, dim, frame, label, part, stepMs10, total, x (+2 more)

### Community 202 - "Box"
Cohesion: 0.29
Nodes (7): Box, maxX, maxY, maxZ, minX, minY, minZ

### Community 203 - "12. Rendering, textures and models"
Cohesion: 0.20
Nodes (7): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), 12.2 Texture loading (`Texture.h/.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 204 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 205 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 206 - "Sign"
Cohesion: 0.33
Nodes (6): Sign, active, gx, gy, gz, text

### Community 209 - "PlayerPos"
Cohesion: 0.40
Nodes (5): PlayerPos, valid, x, y, z

### Community 210 - "packSpot"
Cohesion: 0.50
Nodes (4): 12.7 Mob managers (how data, AI and model connect), chunkOf(), packSpot(), shouldDespawn()

### Community 211 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 212 - "Result"
Cohesion: 0.50
Nodes (4): Result, RES_CANCEL, RES_CREATE, RES_NONE

### Community 222 - "Texture.h"
Cohesion: 0.24
Nodes (6): MenuBackground, texCoordCell(), Sky::draw(), uv(), v(), vert()

## Knowledge Gaps
- **1492 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1487 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2001 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `CMWorld`, `T`, `World`, `HandAnimations.cpp`, `isNormalCube`, `Chunk.cpp`, `Block and Item Types`, `PaintingManager.cpp`, `PartialBlocks.h`, `Dropped Item Physics`, `AnimalManager Module`, `SheepManager Module`, `Crafting Recipes`, `Redstone.cpp`, `NetherGen.h`, `BlockType.h`, `Sound.cpp`, `Inventory`, `Entity AI (HostileAI)`, `FallingBlocks.cpp`, `Furnace.cpp`, `Drop`, `ChunkManager`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Drop`, `useItem`, `ChunkManager Module`, `AnimalManager Module`, `Redstone Logic (Redstone)`, `Block and Item Types`, `RailLogic Module`, `isLiquidBlock`, `PendingDrops.h`, `Block and Item Types`, `Block and Item Types`, `BlockFace`, `MinecartManager.cpp`, `isStructureBlock`, `M`, `Liquid.h`, `notify`, `NetherTerrain`, `Vehicle Entity (MinecartModel)`, `HotbarIcons.cpp`, `BoatManager.cpp`, `bigTreeComputeBranches`, `CMWorld`, `.fireUpdateTick`, `DebugChests.h`, `Maps Module`, `NoteBlocks.cpp`, `SteveModel.cpp`, `Sim`, `CartWorld`, `BigTree`, `.floodFillSkyLight`, `InventoryScreen.cpp`, `HostileManager Module`, `Recipe`, `TntManager.cpp`, `.setBlockWithNotify`, `VoxelColumnRLE`, `Dispenser.cpp`, `Sphere`, `7. World engine in detail`, `TickInput`, `World`, `explode`, `isPlaceable`?**
  _High betweenness centrality (0.255) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1492 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Player Module` to `isNormalCube`, `SubScreenMenu.cpp`, `Crafting Recipes`, `GameplayHotbar.cpp`, `BlockType.h`, `Inventory`, `Entity AI (HostileAI)`, `AsyncSaveManager`, `WorldSave Module`, `Catch`, `Pistons.cpp`, `Texture & PaintingTex`, `GameOverScreen.cpp`, `isLiquidBlock`, `PendingDrops.h`, `Block and Item Types`, `Texture Module`, `BlockFace`, `DebugLogger`, `isStructureBlock`, `Noise.cpp`, `M`, `LoadingScreen.cpp`, `NewWorldMenu.cpp`, `HotbarIcons.cpp`, `WorldSelectMenu Module`, `main.cpp`, `SteveModel.cpp`, `BigTree`, `InventoryScreen.cpp`, `Hardware`, `TopScreenMenu & Renderer`, `TntManager.cpp`, `.sqrtf`, `isPlaceable`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Are the 88 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 88 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.02099009900990099 - nodes in this community are weakly interconnected._