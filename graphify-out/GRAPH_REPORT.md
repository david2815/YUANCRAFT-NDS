# Graph Report - YUANCRAFT NDS PORT  (2026-11-04)

## Corpus Check
- 273 files · ~375,081 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 55 file(s) not represented in the graph (top: .grit 49, (none) 4, .ini 1)

## Summary
- 4561 nodes · 10095 edges · 225 communities (185 shown, 40 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1180 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `20e3daf2`
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
- Kind
- WorldSave Module
- ChunkManager
- stdio
- Pistons.cpp
- Texture & PaintingTex
- Controls & ItemOrder
- stbi_uc
- AnimalManager Module
- GameOverScreen.cpp
- Block and Item Types
- RailLogic Module
- Texture and Image Decoding
- .generateColumn
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
- CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)
- HostileModel.cpp
- main.cpp
- BoatManager.cpp
- Texture and Image Decoding
- ChunkManager
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
- FaceMask
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
- BoatWorld
- build.sh
- Simplex
- PauseScreen Module
- TickInput
- World
- HostileManager Module
- SettingsMenu.cpp
- isLeavesBlock
- stdlib
- Bolt
- MockHardwareState
- Chunk.h
- CMWorld
- T
- MockAsyncSaveManager
- Teleporter.h
- World
- .update
- SubScreenMenu.cpp
- Climate.h
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- Drop
- Redstone.cpp
- nds
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
- Redstone.cpp
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
- Falling
- Sound.h
- verify_occupancy_simulation.py
- Projectiles.h
- Weather::tick
- SaveTask
- Quad
- verify_ui_logic_sim.py
- IpcLoadStatus
- Clouds.cpp
- test_print_row_safety.py
- NetherTerrain
- P
- math
- Profiler.h
- ModelBox.h
- Spike
- State
- W
- Box
- 12. Rendering, textures and models
- Rng
- Pose
- Sign
- topOf
- ctypes
- Col
- IpcChunkLoader.h
- P3
- BigTreeBranch
- bump
- Chest.h
- Controls::gameHeld
- RedstoneEntityCtx

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
- `13. Audio` --references--> `playClip()`  [INFERRED]
  CLAUDE.md → source/Sound.cpp
- `9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`)` --references--> `packSpot()`  [INFERRED]
  CLAUDE.md → source/AnimalAI.h

## Import Cycles
- None detected.

## Communities (225 total, 40 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (86): BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor, CACHE_RECALC_BATCH (+78 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.05
Nodes (86): 9.3 Liquids, particles, partial blocks, 9.6 Audio internals (`Sound.cpp`), BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH (+78 more)

### Community 3 - "Block and Item Types"
Cohesion: 0.06
Nodes (72): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+64 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (57): main(), Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase, bobStrength, buttonLookSpeedH, buttonLookSpeedV (+49 more)

### Community 5 - "Texture and Image Decoding"
Cohesion: 0.07
Nodes (59): main(), stbi_convert_iphone_png_to_rgb(), stbi_convert_iphone_png_to_rgb_thread(), stbi_convert_wchar_to_utf8(), stbi__do_zlib(), stbi_failure_reason(), stbi__float_postprocess(), stbi__fopen() (+51 more)

### Community 6 - "Texture and Image Decoding"
Cohesion: 0.09
Nodes (64): stbi__at_eof(), stbi__bitcount(), stbi__bmp_info(), stbi__bmp_load(), stbi__bmp_parse_header(), stbi__bmp_set_mask_defaults(), stbi__bmp_test(), stbi__bmp_test_raw() (+56 more)

### Community 7 - "HandAnimations.cpp"
Cohesion: 0.12
Nodes (30): 12.6 Mob models (`ModelBox.h`, `*Model.cpp`), isSword(), applyViewBobbing(), blockRenderColor(), blockSideTextures(), brightnessOf(), clickAttack(), drawBlockInHand() (+22 more)

### Community 8 - "Image Writing Utilities"
Cohesion: 0.09
Nodes (50): stb_image_write_test, stbi__end_write_file(), stbi_flip_vertically_on_write(), stbi__start_write_callbacks(), stbi__start_write_file(), stbi_write_bmp(), stbi_write_bmp_core(), stbi_write_bmp_to_func() (+42 more)

### Community 9 - "isNormalCube"
Cohesion: 0.10
Nodes (29): isNormalCube(), autoMeta(), boundsForMeta(), Box, x0, x1, y0, y1 (+21 more)

### Community 10 - "Chunk.cpp"
Cohesion: 0.06
Nodes (13): 7.5 Meshing and drawing, callListFast(), chunkFloorDiv(), flushList(), oreFloorInt(), OreRng, s, oreVeinBlob() (+5 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.06
Nodes (44): getGrassTint(), alloc(), baseMotion(), brightnessOf(), move(), P, active, age (+36 more)

### Community 12 - "PaintingManager.cpp"
Cohesion: 0.05
Nodes (44): Art, ox, oy, sx, sy, title, brightnessOf(), ChunkManager (+36 more)

### Community 13 - "Weather.cpp"
Cohesion: 0.14
Nodes (8): ChunkManager, drawBolt(), drawPrecip(), hash2(), quad4(), Weather::draw(), Weather::load(), Weather::save()

### Community 14 - "Dropped Item Physics"
Cohesion: 0.04
Nodes (42): DroppedItem, active, ageTicks, BOB_MAX, BOB_MIN, BOB_SPEED, bobPhase, count (+34 more)

### Community 15 - "ChunkManager Module"
Cohesion: 0.04
Nodes (42): ChunkManager, awaitingLoad, borderRefreshPending, CAP_CHUNKS, centerIndex, chunkPosX, chunkPosZ, chunks (+34 more)

### Community 16 - "Block and Item Types"
Cohesion: 0.14
Nodes (21): getBlockTextures(), woolCell(), applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad(), drawLodTopQuad(), emitCenteredCrossQuad() (+13 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.07
Nodes (39): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+31 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.09
Nodes (18): CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt(), drawIconAt() (+10 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.06
Nodes (31): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+23 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.19
Nodes (5): ChestView, FurnaceData, GameplayHotbar, bgId, isInButtonRow()

### Community 21 - "BlockType.h"
Cohesion: 0.07
Nodes (55): 8. Blocks and items, armorMaterial(), armorMaxDurability(), armorPiece(), armorReduceAmount(), armorRenderIndex(), blockHardness(), canHarvestBlock() (+47 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.15
Nodes (23): at(), cellToWorld(), digBase(), mobClip(), pick(), playClip(), raw(), rnd() (+15 more)

### Community 23 - "Inventory"
Cohesion: 0.13
Nodes (21): 9.7 Inventory and crafting UI internals, hasDurability(), maxStackFor(), ChestStore::transferWithInventory(), Furnace::transferWithInventory(), Inventory, ARMOR_BASE, ARMOR_SLOTS (+13 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.14
Nodes (33): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), isWaterBlock(), arrowTick(), attackBlocked(), attackEntity(), brightnessAt(), canSee(), canSpawnHere() (+25 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.09
Nodes (31): canSmelt(), ChunkManager, clearEntry(), clearSlot(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate(), Furnace::fuelBurnTime() (+23 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.09
Nodes (13): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+5 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "Kind"
Cohesion: 0.15
Nodes (12): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+4 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.14
Nodes (10): 9.8 More internals (Nether, sky, saves, menus, chests, notes), SD card layout, clearFolderContents(), folderExists(), WorldSave, s_activeBasePath, s_activeWorldNum, s_dimension (+2 more)

### Community 30 - "ChunkManager"
Cohesion: 0.16
Nodes (13): blockLightEmission(), getDropType(), isCrossPlant(), isFlatInHand(), isJackBlock(), isLightOpaque(), isPartialBlock(), isPumpkinBlock() (+5 more)

### Community 31 - "stdio"
Cohesion: 0.21
Nodes (4): draw(), OptionsMenu::open(), OptionsMenu::update(), printRow()

### Community 32 - "Pistons.cpp"
Cohesion: 0.07
Nodes (64): 5.2 Blocks, items, inventory, crafting, isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend() (+56 more)

### Community 33 - "Texture & PaintingTex"
Cohesion: 0.07
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.10
Nodes (23): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+15 more)

### Community 35 - "stbi_uc"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.09
Nodes (12): AnimalManager::attack(), AnimalManager::draw(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath() (+4 more)

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - ".generateColumn"
Cohesion: 0.22
Nodes (6): getPatchAt(), findLandChunkOffset(), hash2D(), Noise, randomGridValue(), smoothstep()

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.20
Nodes (18): isRailBlock(), bodyBox(), calcX(), calcY(), calcZ(), fl(), hyp(), moveEntity() (+10 more)

### Community 45 - "Block and Item Types"
Cohesion: 0.08
Nodes (15): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::draw(), SheepManager::explosionDamage() (+7 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.09
Nodes (11): 9.2 Managers: spawning, caps, explosions, collectDeath(), explode(), HostileManager::attack(), HostileManager::interact(), HostileManager::lightning(), HostileManager::popDrop(), pushDrop() (+3 more)

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
Cohesion: 0.10
Nodes (19): isSignBlock(), Box, q, brightnessOf(), buildBox(), ChunkManager, drawBox(), drawText() (+11 more)

### Community 51 - "Noise.cpp"
Cohesion: 0.13
Nodes (10): Chunk::Chunk(), HeightCache, h, tx, tz, NetherColCache, c, tx (+2 more)

### Community 52 - "Profiler Module"
Cohesion: 0.18
Nodes (7): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike()

### Community 53 - "Profiler Module"
Cohesion: 0.13
Nodes (15): Slot, DL_CALL, DL_CULL, DL_LOD, DL_REBUILD, DRAW_ALL, ENTS, FACES (+7 more)

### Community 54 - "M"
Cohesion: 0.33
Nodes (13): isPlateBlock(), detectorCheck(), M(), plateBox(), plateCheck(), randomTick(), repeaterCheck(), repeaterInput() (+5 more)

### Community 55 - "LoadingScreen.cpp"
Cohesion: 0.36
Nodes (3): copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen

### Community 56 - "notify"
Cohesion: 0.20
Nodes (16): activate(), blockChanged(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved(), indirectPowerAt() (+8 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves.cpp"
Cohesion: 0.18
Nodes (13): carveSphere(), carveStep(), cellRng(), floorDiv(), floorF(), isDecoration(), jcos(), jsin() (+5 more)

### Community 59 - "Health Module"
Cohesion: 0.05
Nodes (48): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), Env, burningBox, cactus, fallLanded (+40 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.17
Nodes (17): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::count(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn() (+9 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "HotbarIcons.cpp"
Cohesion: 0.23
Nodes (8): drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon(), getItemsPixelIndex(), getTerrainPixelIndex(), HotbarIcons

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.17
Nodes (3): clearLabelZone(), drawWorldName(), WorldSelectMenu

### Community 65 - "AnimalAI.h"
Cohesion: 0.06
Nodes (74): 12.7 Mob managers (how data, AI and model connect), anyIn(), blocking(), bodyBox(), Box, x0, x1, y0 (+66 more)

### Community 66 - "CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)"
Cohesion: 0.10
Nodes (19): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 13. Audio, 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is (+11 more)

### Community 67 - "HostileModel.cpp"
Cohesion: 0.11
Nodes (31): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawPartAt() (+23 more)

### Community 68 - "main.cpp"
Cohesion: 0.08
Nodes (26): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, computeCelestialAngle(), computeNightFactor(), computeSkyBrightness(), computeSkylightSubtract() (+18 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.14
Nodes (11): BoatManager::attack(), BoatManager::dismount(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::saveToFile(), breakBoat(), dismountIndex(), forceDismount() (+3 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "ChunkManager"
Cohesion: 0.12
Nodes (13): bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches(), bigTreeDrawLine(), bigTreeEnvelope(), bigTreeLeafLayerRadius(), bigTreePlaceLeafCluster(), bigTreePlaceSphereLayer() (+5 more)

### Community 72 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 73 - "Maps Module"
Cohesion: 0.12
Nodes (23): ChunkManager, find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush() (+15 more)

### Community 74 - "DebugChests.h"
Cohesion: 0.17
Nodes (13): buildItemList(), findSite(), groundHeight(), isGivenItem(), isReplaceable(), isSkippable(), Site, alongX (+5 more)

### Community 75 - "SteveModel.cpp"
Cohesion: 0.06
Nodes (37): addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b, g (+29 more)

### Community 76 - "NoteBlocks.cpp"
Cohesion: 0.12
Nodes (17): ChunkManager, Entry, gx, gy, gz, note, prev, used (+9 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (20): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+12 more)

### Community 78 - "Sim"
Cohesion: 0.09
Nodes (18): findSpawn(), fireEncourage(), isFlowingLiquid(), isLavaBlock(), isLiquidBlock(), isMaterialSolid(), liquidMaterial(), placementTargetFree() (+10 more)

### Community 79 - "IpcChunkLoader"
Cohesion: 0.18
Nodes (7): IpcChunkLoader, MAX_WAIT_FRAMES, s_exchange, s_initialized, TICKS_PER_MS, TIMEOUT_MS, TIMEOUT_TICKS

### Community 80 - "CartWorld"
Cohesion: 0.15
Nodes (9): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn(), MinecartManager::tick() (+1 more)

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "BigTree"
Cohesion: 0.13
Nodes (13): BigTree, AX, basePos, branchSlope, height, heightAttenuation, heightLimit, heightLimitLimit (+5 more)

### Community 83 - "BiomeType"
Cohesion: 0.13
Nodes (15): BiomeType, DESERT, FOREST, GENERIC, OCEAN, PLAINS, RAINFOREST, SAVANNA (+7 more)

### Community 84 - ".floodFillSkyLight"
Cohesion: 0.23
Nodes (6): lightDim(), LightNode, bx, by, bz, level

### Community 85 - "Caves Module"
Cohesion: 0.12
Nodes (17): Job, active, cx, cz, fill, nOrigins, originIdx, ox (+9 more)

### Community 86 - "InventoryScreen.cpp"
Cohesion: 0.17
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
Cohesion: 0.17
Nodes (12): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+4 more)

### Community 91 - "Recipe"
Cohesion: 0.15
Nodes (18): canCraft(), countPatternCells(), doCraft(), Recipe, altA, altB, altC, altD (+10 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.13
Nodes (12): state, set(), State, lx, ly, lz, maxDist2, valid (+4 more)

### Community 93 - "WorldMetadata"
Cohesion: 0.11
Nodes (18): WorldMetadata, armorDurability, armorType, formatVersion, gameTimeTicks, hotbarCount, hotbarDurability, hotbarType (+10 more)

### Community 94 - "Tick"
Cohesion: 0.11
Nodes (11): isHell(), popDue(), pushTick(), Tick, due, gx, gy, gz (+3 more)

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
Cohesion: 0.22
Nodes (7): advanceOrigin(), initTunnel(), JRandom, seed, pushTunnel(), reset(), startJob()

### Community 102 - "MobBody & AnimalManager"
Cohesion: 0.18
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.22
Nodes (4): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.11
Nodes (20): blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), Tnt, active, fuse (+12 more)

### Community 105 - "FaceMask"
Cohesion: 0.16
Nodes (11): sameFaces(), Cube, drawBox(), FaceMask, bottom, east, north, south (+3 more)

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.14
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
Cohesion: 0.17
Nodes (9): CarveCursor, cell, sphere, Sphere, flat, r16, x8, y8 (+1 more)

### Community 114 - "verify_ipc_streaming_simulation.py"
Cohesion: 0.19
Nodes (8): main(), MockChunk, MockChunkManager, SimulatedIpcChunkLoader, test_async_streaming_flow(), test_corrupted_file_failsafe(), test_sd_timeout_failsafe(), test_ui_stability_and_vblank_loop()

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.22
Nodes (6): 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.6 Saving, 7. World engine in detail

### Community 117 - "verify_deadlock_and_memory_simulation.py"
Cohesion: 0.33
Nodes (6): is_valid_main_ram_pointer(), main(), test_60_frame_escape_mechanism(), test_debug_logger_sd_output(), test_ds_4mb_profile(), test_dsi_16mb_profile()

### Community 118 - "BoatWorld"
Cohesion: 0.18
Nodes (9): BoatManager::draw(), BoatManager::spawnFromRay(), BoatManager::tick(), BoatWorld, cacheChunk, cacheCx, cacheCz, cacheReady (+1 more)

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 120 - "Simplex"
Cohesion: 0.18
Nodes (8): initIfSeedChanged(), Octaves, gen, Simplex, perm, xo, yo, zo

### Community 121 - "PauseScreen Module"
Cohesion: 0.15
Nodes (9): Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched() (+1 more)

### Community 122 - "TickInput"
Cohesion: 0.15
Nodes (13): TickInput, attackHeld, heldDurability, heldSlot, heldType, movedX, movedZ, onGround (+5 more)

### Community 123 - "World"
Cohesion: 0.18
Nodes (7): drawSprite(), Projectiles::draw(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 125 - "SettingsMenu.cpp"
Cohesion: 0.25
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 126 - "isLeavesBlock"
Cohesion: 0.22
Nodes (14): 9.5 World-generation pieces, 9. Entities and physics notes, isLeavesBlock(), beginFrame(), freeOrLeaves(), genRound(), genSpruce(), isLog() (+6 more)

### Community 128 - "Bolt"
Cohesion: 0.15
Nodes (13): Bolt, active, flashes, gx, gy, gz, life, seed (+5 more)

### Community 129 - "MockHardwareState"
Cohesion: 0.29
Nodes (3): main(), MockHardwareState, simulate()

### Community 130 - "Chunk.h"
Cohesion: 0.20
Nodes (3): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), DisplayListBuilder, genColsPerFrame()

### Community 131 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 132 - "T"
Cohesion: 0.20
Nodes (14): addWirePos(), anySideNormal(), cartTouchSink(), doorPower(), dropItem(), maxStrength(), neighborChanged(), neighborDo() (+6 more)

### Community 134 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 135 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 136 - ".update"
Cohesion: 0.24
Nodes (3): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), cellInWindow(), ChunkManager::ChunkManager()

### Community 138 - "Climate.h"
Cohesion: 0.24
Nodes (7): biomeFor(), Lattice, h, t, x0, z0, raw()

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

### Community 146 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 147 - "Redstone.cpp"
Cohesion: 0.22
Nodes (13): isRedstoneComponent(), isRepeaterBlock(), hasCollision(), blockRemoved(), canProvidePower(), gettingPowered(), indirectlyGettingPowered(), indirectProvidingPowerTo() (+5 more)

### Community 148 - "nds"
Cohesion: 0.07
Nodes (11): AnimItems::init(), AnimItems::tick(), setFrame(), HealthHud::draw(), MenuBackground, texCoordCell(), ChunkManager, Sky::draw() (+3 more)

### Community 150 - "IpcChunkExchange"
Cohesion: 0.17
Nodes (11): IpcChunkExchange, chunkX, chunkZ, compBuffer, dataSize, frameCounter, path, rawBuffer (+3 more)

### Community 151 - "FallingBlocks.cpp"
Cohesion: 0.24
Nodes (6): ChunkManager, FallingBlocks::draw(), FallingBlocks::spawn(), FallingBlocks::update(), placeable(), texCoordCell()

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
Cohesion: 0.11
Nodes (18): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+10 more)

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "Redstone.cpp"
Cohesion: 0.18
Nodes (13): bounds(), burnedOut(), chunkOf(), faceCode(), floorDivi(), freeCell(), lightOre(), put() (+5 more)

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
Cohesion: 0.18
Nodes (12): allocBlock(), Cell, count, cx, cz, first, lastUse, nblocks (+4 more)

### Community 171 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 173 - "os"
Cohesion: 0.07
Nodes (6): verify_structural(), verify_structural(), main(), verify_structural(), verify_structural(), verify_all()

### Community 174 - "Falling"
Cohesion: 0.22
Nodes (9): Falling, active, fallTime, prevY, type, vy, x, y (+1 more)

### Community 175 - "Sound.h"
Cohesion: 0.22
Nodes (8): Group, G_GRASS, G_GRAVEL, G_SAND, G_SNOW, G_STONE, G_WOOD, Sound::groupOf()

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

### Community 177 - "Projectiles.h"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 178 - "Weather::tick"
Cohesion: 0.46
Nodes (7): fireAt(), nextInt(), rnd(), spawnBolt(), tickBolt(), updateWeather(), Weather::tick()

### Community 179 - "SaveTask"
Cohesion: 0.29
Nodes (6): SaveTask, data, dataSize, inUse, _pad, path

### Community 180 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 181 - "verify_ui_logic_sim.py"
Cohesion: 0.38
Nodes (3): MockOptions, test_ds_original_menu_logic(), test_dsi_profile_and_fps_target()

### Community 182 - "IpcLoadStatus"
Cohesion: 0.29
Nodes (7): IpcLoadStatus, IPC_STATUS_ERROR, IPC_STATUS_IDLE, IPC_STATUS_READING, IPC_STATUS_READY, IPC_STATUS_REQUESTED, IPC_STATUS_TIMEOUT

### Community 183 - "Clouds.cpp"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 184 - "test_print_row_safety.py"
Cohesion: 1.00
Nodes (3): print_row_sim(), test_all_options(), visual_length()

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

### Community 200 - "State"
Cohesion: 0.33
Nodes (6): State, detail, humidity, ready, seed, temperature

### Community 202 - "Box"
Cohesion: 0.29
Nodes (7): Box, maxX, maxY, maxZ, minX, minY, minZ

### Community 203 - "12. Rendering, textures and models"
Cohesion: 0.29
Nodes (6): 12.2 Texture loading (`Texture.h/.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 205 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 206 - "Sign"
Cohesion: 0.33
Nodes (6): Sign, active, gx, gy, gz, text

### Community 207 - "topOf"
Cohesion: 0.60
Nodes (5): chunkAtGrid(), kindOf(), refresh(), topOf(), Weather::canRainAtGrid()

### Community 209 - "Col"
Cohesion: 0.33
Nodes (6): Col, gx, gz, kind, top, valid

### Community 211 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 212 - "BigTreeBranch"
Cohesion: 0.40
Nodes (5): BigTreeBranch, trunkY, x, y, z

### Community 213 - "bump"
Cohesion: 0.50
Nodes (3): BoatManager::riderEye(), bump(), eyeOf()

### Community 221 - "Controls::gameHeld"
Cohesion: 0.50
Nodes (3): Controls::gameHeld(), Controls::isBindable(), key()

### Community 222 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

## Knowledge Gaps
- **1492 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1487 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2003 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **40 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `CMWorld`, `T`, `HandAnimations.cpp`, `World`, `isNormalCube`, `Chunk.cpp`, `Block and Item Types`, `PaintingManager.cpp`, `SheepManager Module`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `Drop`, `Redstone.cpp`, `Crafting Recipes`, `BlockType.h`, `NetherGen.h`, `Inventory`, `Entity AI (HostileAI)`, `FallingBlocks.cpp`, `Furnace.cpp`, `Drop`, `Sound.cpp`, `ChunkManager`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Drop`, `Redstone.cpp`, `ChunkManager Module`, `AnimalManager Module`, `Redstone Logic (Redstone)`, `Block and Item Types`, `RailLogic Module`, `.generateColumn`, `PendingDrops.h`, `Block and Item Types`, `Block and Item Types`, `Falling`, `HostileManager Module`, `MinecartManager.cpp`, `Sound.h`, `SignManager Module`, `M`, `notify`, `NetherTerrain`, `Caves.cpp`, `Vehicle Entity (MinecartModel)`, `HotbarIcons.cpp`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `BoatManager.cpp`, `ChunkManager`, `CMWorld`, `Maps Module`, `DebugChests.h`, `SteveModel.cpp`, `NoteBlocks.cpp`, `W`, `Sim`, `CartWorld`, `BigTree`, `.floodFillSkyLight`, `InventoryScreen.cpp`, `HostileManager Module`, `Recipe`, `Controls::gameHeld`, `Tick`, `TntManager.cpp`, `VoxelColumnRLE`, `Dispenser.cpp`, `7. World engine in detail`, `BoatWorld`, `TickInput`, `World`, `isLeavesBlock`?**
  _High betweenness centrality (0.211) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1492 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Player Module` to `PartialBlocks.cpp`, `HandAnimations.cpp`, `isNormalCube`, `SubScreenMenu.cpp`, `Crafting Recipes`, `GameplayHotbar.cpp`, `BlockType.h`, `Inventory`, `AsyncSaveManager`, `WorldSave Module`, `ChunkManager`, `Catch`, `Pistons.cpp`, `Texture & PaintingTex`, `GameOverScreen.cpp`, `.generateColumn`, `PendingDrops.h`, `Block and Item Types`, `Texture Module`, `DebugLogger`, `M`, `LoadingScreen.cpp`, `NewWorldMenu.cpp`, `HotbarIcons.cpp`, `WorldSelectMenu Module`, `main.cpp`, `Sim`, `IpcChunkLoader`, `InventoryScreen.cpp`, `Recipe`, `Hardware`, `TopScreenMenu & Renderer`, `.sqrtf`, `isLeavesBlock`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Are the 88 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 88 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.02089704383282365 - nodes in this community are weakly interconnected._