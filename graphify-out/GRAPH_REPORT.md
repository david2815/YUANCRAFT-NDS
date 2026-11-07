# Graph Report - YUANCRAFT NDS PORT  (2026-11-07)

## Corpus Check
- 297 files · ~384,827 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 70 file(s) not represented in the graph (top: .grit 49, (none) 8, .ini 3)

## Summary
- 4704 nodes · 10414 edges · 236 communities (191 shown, 45 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1199 edges (avg confidence: 0.86)
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
- isMaterialSolid
- Inventory
- Entity AI (HostileAI)
- Furnace.cpp
- AsyncSaveManager
- DisplayListBuilder Module
- main
- WorldSave Module
- .generateBigOakTree
- nds
- Pistons.cpp
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
- AnimalAI.h
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
- ChunkManager
- verify_world_select_simulation.py
- JRandom
- BigTree
- TopScreenMenu & Renderer
- TntManager.cpp
- FaceMask
- VoxelColumnRLE
- CMWorld
- NoteBlocks.cpp
- ChestStore.cpp
- RaycastHit
- SheepModel Module
- DroppedItem.cpp
- Sphere
- verify_ipc_streaming_simulation.py
- WorldMetadata
- MenuFont.cpp
- verify_deadlock_and_memory_simulation.py
- isWaterBlock
- build.sh
- Climate.h
- PauseScreen Module
- TickInput
- isPlaceable
- HostileManager Module
- SettingsMenu.cpp
- HwMath
- .reloadEntityTextures
- ChestStore.cpp
- MockHardwareState
- Lakes.h
- Moving
- T
- MockAsyncSaveManager
- Teleporter.h
- FlatQuad
- 7. World engine in detail
- Catch
- PerlinNoise
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- .update
- isPistonBase
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
- .updateTick
- verify_simulation
- Cell
- ModelBox.h
- HudQuad
- Redstone Logic (Redstone)
- os
- Projectiles.h
- test_emulator_run.py
- verify_occupancy_simulation.py
- FallingBlocks.cpp
- HostileModel.cpp
- Glow
- Profiler.h
- verify_ui_logic_sim.py
- LakeTerrain
- Clouds.cpp
- test_print_row_safety.py
- NetherTerrain
- run_full_hardware_verification.py
- P
- math
- Spike
- Falling
- Sound.h
- JRandom
- JavaRandom
- Liquid.cpp
- StartupSplash.cpp
- Quad
- debug_single_run.py
- Box
- Chest.h
- ctypes
- isRedstoneComponent
- GameOverScreen.cpp
- P3
- Pose
- SubScreenMenu.cpp
- .loadHostileAtlases
- Rng
- 9. Entities and physics notes
- ExplosionDamage.h
- Sky.cpp
- RedstoneEntityCtx
- DrawCtx
- ArrowHurtCtx

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 217 edges
3. `main()` - 207 edges
4. `ChunkManager` - 107 edges
5. `Player` - 98 edges
6. `DroppedItem` - 61 edges
7. `Sim` - 48 edges
8. `isLiquidBlock()` - 44 edges
9. `isNormalCube()` - 43 edges
10. `Texture` - 42 edges

## Surprising Connections (you probably didn't know these)
- `2. Rules for an AI assistant modifying this project (read carefully)` --references--> `BlockType`  [INFERRED]
  CLAUDE.md → source/BlockType.h
- `9.5 World-generation pieces` --references--> `beginFrame()`  [INFERRED]
  CLAUDE.md → source/Caves.cpp
- `7.1c `tickLiquids` (20 Hz) and random ticks` --references--> `LiquidWorld`  [INFERRED]
  CLAUDE.md → source/ChunkManager.cpp
- `9.2 Managers: spawning, caps, explosions` --references--> `resistanceOf()`  [INFERRED]
  CLAUDE.md → source/HostileManager.cpp
- `9.8 More internals (Nether, sky, saves, menus, chests, notes)` --references--> `resetLattice()`  [INFERRED]
  CLAUDE.md → source/NetherGen.h

## Import Cycles
- None detected.

## Communities (236 total, 45 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (86): BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor, CACHE_RECALC_BATCH (+78 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.22
Nodes (31): doubleOfSlab(), activate(), chunkOf(), cropCanStay(), cropsTick(), dropAt(), dropCrop(), eatCake() (+23 more)

### Community 3 - "Block and Item Types"
Cohesion: 0.06
Nodes (72): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+64 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (61): Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase, bobStrength, buttonLookSpeedH, buttonLookSpeedV, currentTickDistance (+53 more)

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

### Community 9 - "Spawners.cpp"
Cohesion: 0.09
Nodes (30): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+22 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.07
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
Cohesion: 0.13
Nodes (21): isDoorBlock(), isPistonBlock(), applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad(), drawLodTopQuad(), emitCenteredCrossQuad() (+13 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.13
Nodes (21): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+13 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.08
Nodes (20): ChestView, CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt() (+12 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.20
Nodes (9): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+1 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.12
Nodes (11): GameplayHotbar, bgId, isInButtonRow(), drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon() (+3 more)

### Community 21 - "BlockType.h"
Cohesion: 0.09
Nodes (45): armorMaterial(), armorMaxDurability(), armorPiece(), armorReduceAmount(), armorRenderIndex(), blockHardness(), canHarvestBlock(), dyeDamage() (+37 more)

### Community 22 - "isMaterialSolid"
Cohesion: 0.25
Nodes (3): findSpawn(), isMaterialSolid(), findSpawn()

### Community 23 - "Inventory"
Cohesion: 0.08
Nodes (43): 8. Blocks and items, 9.7 Inventory and crafting UI internals, getToolMaxDurability(), hasDurability(), isArmor(), isRecord(), maxStackFor(), ChestStore::transferWithInventory() (+35 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.30
Nodes (20): attackBlocked(), attackEntity(), brightnessAt(), canSee(), dist3(), findTarget(), ghastCourseClear(), isMobKind() (+12 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.09
Nodes (31): canSmelt(), ChunkManager, clearEntry(), clearSlot(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate(), Furnace::fuelBurnTime() (+23 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.08
Nodes (19): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+11 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (12): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), lastPolyFormat, out, overflow (+4 more)

### Community 28 - "main"
Cohesion: 0.07
Nodes (4): main(), clearLabelZone(), drawWorldName(), WorldSelectMenu

### Community 29 - "WorldSave Module"
Cohesion: 0.14
Nodes (10): 9.8 More internals (Nether, sky, saves, menus, chests, notes), SD card layout, clearFolderContents(), folderExists(), WorldSave, s_activeBasePath, s_activeWorldNum, s_dimension (+2 more)

### Community 30 - ".generateBigOakTree"
Cohesion: 0.17
Nodes (11): BigTreeBranch, trunkY, x, y, z, bigTreeComputeBranches(), bigTreeEnvelope(), BigTreeRng (+3 more)

### Community 31 - "nds"
Cohesion: 0.11
Nodes (8): DSI_DebugInit(), DSI_Log(), openLogFile(), draw(), OptionsMenu::open(), OptionsMenu::update(), printRow(), ChunkManager

### Community 32 - "Pistons.cpp"
Cohesion: 0.19
Nodes (27): addMoving(), baseAdded(), baseNeighborChanged(), canExtend(), canPush(), check(), chunkOf(), cleanupOrphan() (+19 more)

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.09
Nodes (26): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+18 more)

### Community 35 - "stbi_uc"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.09
Nodes (12): AnimalManager::attack(), AnimalManager::draw(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath() (+4 more)

### Community 38 - "isNormalCube"
Cohesion: 0.09
Nodes (30): isNormalCube(), airSpawnSpot(), autoMeta(), boundsForMeta(), Box, x0, x1, y0 (+22 more)

### Community 39 - "Block and Item Types"
Cohesion: 0.12
Nodes (3): isLavaBlock(), LiquidWorld, m

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - "isLiquidBlock"
Cohesion: 0.13
Nodes (14): blockLightEmission(), isCrossPlant(), isLiquidBlock(), isPartialBlock(), isTorchBlock(), torchFromMeta(), torchMeta(), hidesLiquidFace() (+6 more)

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.20
Nodes (18): isRailBlock(), bodyBox(), calcX(), calcY(), calcZ(), fl(), hyp(), moveEntity() (+10 more)

### Community 45 - "SheepManager.cpp"
Cohesion: 0.09
Nodes (13): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::interact(), SheepManager::lightning() (+5 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.07
Nodes (16): collectDeath(), explode(), HostileManager::attack(), HostileManager::count(), HostileManager::draw(), HostileManager::interact(), HostileManager::lightning(), HostileManager::popDrop() (+8 more)

### Community 47 - "DebugLogger"
Cohesion: 0.14
Nodes (10): DebugLogger, LINE_LEN, MAX_HISTORY, s_count, s_fatAvailable, s_head, s_history, s_initialized (+2 more)

### Community 48 - "MinecartManager.cpp"
Cohesion: 0.11
Nodes (13): breakCart(), cartCollision(), dismountIndex(), eyeOf(), getI32(), MinecartManager::attack(), MinecartManager::dismount(), MinecartManager::loadFromFile() (+5 more)

### Community 49 - "Projectiles Module"
Cohesion: 0.07
Nodes (28): Proj, active, inGround, kind, mx, my, mz, ownerIsPlayer (+20 more)

### Community 50 - "SignManager Module"
Cohesion: 0.08
Nodes (24): Box, q, brightnessOf(), buildBox(), ChunkManager, drawBox(), drawText(), find() (+16 more)

### Community 51 - "Noise.cpp"
Cohesion: 0.17
Nodes (8): HeightCache, h, tx, tz, NetherColCache, c, tx, tz

### Community 52 - "Profiler Module"
Cohesion: 0.18
Nodes (7): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike()

### Community 53 - "Profiler Module"
Cohesion: 0.13
Nodes (15): Slot, DL_CALL, DL_CULL, DL_LOD, DL_REBUILD, DRAW_ALL, ENTS, FACES (+7 more)

### Community 54 - "FishingHook.cpp"
Cohesion: 0.23
Nodes (13): cellY(), FishingHook::cast(), FishingHook::clear(), FishingHook::draw(), gaussian(), handPos(), nextFloat(), nextInt() (+5 more)

### Community 55 - "PartialBlocks.h"
Cohesion: 0.18
Nodes (14): 9.6 Audio internals (`Sound.cpp`), bedCell(), bedOffset(), ChunkManager, collisionBounds(), collisionBoxes(), cropDrops(), doorCell() (+6 more)

### Community 56 - "Redstone.cpp"
Cohesion: 0.16
Nodes (17): bounds(), canProvidePower(), chunkOf(), faceCode(), floorDivi(), freeCell(), gettingPowered(), isIndirectlyPoweringTo() (+9 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves.cpp"
Cohesion: 0.15
Nodes (19): allocBlock(), beginFrame(), carveSphere(), carveStep(), cellRng(), emit(), floorD(), floorDiv() (+11 more)

### Community 59 - "Health Module"
Cohesion: 0.07
Nodes (38): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), Env, burningBox, cactus, fallLanded (+30 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.28
Nodes (12): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn(), HostileManager::tick(), kindCap() (+4 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)"
Cohesion: 0.05
Nodes (26): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is (+18 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

### Community 64 - "Texture.h"
Cohesion: 0.14
Nodes (3): HealthHud::draw(), MenuBackground, texCoordCell()

### Community 65 - "MobBody"
Cohesion: 0.18
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 66 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 67 - "AnimalAI.h"
Cohesion: 0.05
Nodes (77): 12.3 Texture coordinates, 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12.7 Mob managers (how data, AI and model connect), 12. Rendering, textures and models, anyIn(), blocking(), bodyBox(), Box (+69 more)

### Community 68 - "main.cpp"
Cohesion: 0.09
Nodes (25): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, computeCelestialAngle(), computeNightFactor(), computeSkyBrightness(), computeSkylightSubtract() (+17 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.06
Nodes (31): BoatManager::attack(), BoatManager::dismount(), BoatManager::draw(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::riderEye(), BoatManager::saveToFile(), BoatManager::spawnFromRay() (+23 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "Chunk.cpp"
Cohesion: 0.07
Nodes (14): alloc(), callListFast(), Chunk::Chunk(), chunkFloorDiv(), flushList(), free(), init(), oreFloorInt() (+6 more)

### Community 72 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 73 - "Maps Module"
Cohesion: 0.12
Nodes (23): ChunkManager, find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush() (+15 more)

### Community 74 - "DebugChests.h"
Cohesion: 0.18
Nodes (11): buildItemList(), findSite(), isGivenItem(), isReplaceable(), Site, alongX, groundA, groundB (+3 more)

### Community 75 - "SteveModel.cpp"
Cohesion: 0.16
Nodes (14): addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b, g (+6 more)

### Community 76 - "PerformancePreset.cpp"
Cohesion: 0.09
Nodes (22): ChunkManager, PerformancePreset, chunk_radius, dsi_only, enable_animated_textures, enable_particles, max_mesh_rebuilds_per_frame, name (+14 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (20): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+12 more)

### Community 78 - "Sim"
Cohesion: 0.14
Nodes (8): fireEncourage(), isFlowingLiquid(), Sim, editing, flowCost, numAdjacentSources, optimal, tickRateOf()

### Community 79 - "IpcChunkLoader"
Cohesion: 0.06
Nodes (27): Chunk, ChunkManager, IpcChunkExchange, chunkX, chunkZ, compBuffer, dataSize, frameCounter (+19 more)

### Community 80 - "CartWorld"
Cohesion: 0.15
Nodes (9): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn(), MinecartManager::tick() (+1 more)

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "isLeavesBlock"
Cohesion: 0.15
Nodes (16): 9.5 World-generation pieces, isLeavesBlock(), isSapling(), rand, ChunkManager, freeOrLeaves(), genRound(), genSpruce() (+8 more)

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
Cohesion: 0.21
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

### Community 91 - "Sound.cpp"
Cohesion: 0.14
Nodes (24): 13. Audio, at(), cellToWorld(), digBase(), mobClip(), pick(), playClip(), raw() (+16 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.13
Nodes (12): state, set(), State, lx, ly, lz, maxDist2, valid (+4 more)

### Community 93 - "BlockFace"
Cohesion: 0.17
Nodes (14): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+6 more)

### Community 94 - "Tick"
Cohesion: 0.20
Nodes (8): Tick, due, gx, gy, gz, seq, type, used

### Community 95 - "TextKeyboard Module"
Cohesion: 0.13
Nodes (22): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+14 more)

### Community 98 - "Caves Module"
Cohesion: 0.13
Nodes (15): Tunnel, branchStep, isRoom, length, pitch, pitchVel, r, radiusScale (+7 more)

### Community 99 - "ChunkManager"
Cohesion: 0.16
Nodes (8): isLightOpaque(), bigTreeCheckClearance(), bigTreeClearance(), bigTreeDrawLine(), bigTreeLeafLayerRadius(), bigTreePlaceLeafCluster(), bigTreePlaceSphereLayer(), fillDungeonChest()

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
Cohesion: 0.13
Nodes (7): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen, Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.10
Nodes (23): blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn(), Tnt, active (+15 more)

### Community 105 - "FaceMask"
Cohesion: 0.15
Nodes (11): sameFaces(), Cube, drawBox(), FaceMask, bottom, east, north, south (+3 more)

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.14
Nodes (10): isValidMainRamPointer(), isVramPointer(), RLERun, length, type, VoxelColumnRLE, MAX_RUNS, _pad (+2 more)

### Community 107 - "CMWorld"
Cohesion: 0.17
Nodes (7): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady, SheepManager::draw(), SheepManager::explosionDamage()

### Community 108 - "NoteBlocks.cpp"
Cohesion: 0.12
Nodes (17): ChunkManager, Entry, gx, gy, gz, note, prev, used (+9 more)

### Community 109 - "ChestStore.cpp"
Cohesion: 0.12
Nodes (15): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+7 more)

### Community 110 - "RaycastHit"
Cohesion: 0.12
Nodes (14): ChunkManager, Chunk, ChunkManager, Raycaster, RaycastHit, blockXi, blockYi, blockZi (+6 more)

### Community 111 - "SheepModel Module"
Cohesion: 0.13
Nodes (17): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+9 more)

### Community 113 - "Sphere"
Cohesion: 0.10
Nodes (12): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), CarveCursor, cell, sphere, Sphere, flat, r16, x8 (+4 more)

### Community 114 - "verify_ipc_streaming_simulation.py"
Cohesion: 0.19
Nodes (8): main(), MockChunk, MockChunkManager, SimulatedIpcChunkLoader, test_async_streaming_flow(), test_corrupted_file_failsafe(), test_sd_timeout_failsafe(), test_ui_stability_and_vblank_loop()

### Community 115 - "WorldMetadata"
Cohesion: 0.11
Nodes (18): WorldMetadata, armorDurability, armorType, formatVersion, gameTimeTicks, hotbarCount, hotbarDurability, hotbarType (+10 more)

### Community 116 - "MenuFont.cpp"
Cohesion: 0.21
Nodes (11): find(), Glyph, c, rows, MenuFont::draw16(), MenuFont::draw8(), MenuFont::fill16(), MenuFont::fill8() (+3 more)

### Community 117 - "verify_deadlock_and_memory_simulation.py"
Cohesion: 0.33
Nodes (6): is_valid_main_ram_pointer(), main(), test_60_frame_escape_mechanism(), test_debug_logger_sd_output(), test_ds_4mb_profile(), test_dsi_16mb_profile()

### Community 118 - "isWaterBlock"
Cohesion: 0.16
Nodes (13): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), isWaterBlock(), liquidFlowingOf(), liquidStillOf(), arrowTick(), boxClear(), canSpawnHere(), fireballTick() (+5 more)

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

### Community 123 - "isPlaceable"
Cohesion: 0.21
Nodes (14): isAnimalItem(), isBucket(), isDiamondTool(), isFarmItem(), isFlatInHand(), isGoldTool(), isHoeTool(), isMinecartItem() (+6 more)

### Community 125 - "SettingsMenu.cpp"
Cohesion: 0.27
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 128 - "ChestStore.cpp"
Cohesion: 0.29
Nodes (9): ChestStore::clearAll(), ChestStore::findOrCreate(), ChestStore::loadFromFile(), ChestStore::remove(), ChestStore::saveToFile(), clearEntry(), clearSlot(), getI32() (+1 more)

### Community 129 - "MockHardwareState"
Cohesion: 0.29
Nodes (3): main(), MockHardwareState, simulate()

### Community 130 - "Lakes.h"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 131 - "Moving"
Cohesion: 0.17
Nodes (12): Moving, active, extending, facing, last, meta, progress, source (+4 more)

### Community 132 - "T"
Cohesion: 0.23
Nodes (13): addWirePos(), anySideNormal(), doorPower(), dropItem(), indirectlyGettingPowered(), maxStrength(), neighborChanged(), neighborDo() (+5 more)

### Community 134 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 135 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 136 - "7. World engine in detail"
Cohesion: 0.20
Nodes (7): 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.5 Meshing and drawing, 7.6 Saving, 7. World engine in detail

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
Cohesion: 0.26
Nodes (3): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), cellInWindow(), ChunkManager::ChunkManager()

### Community 147 - "isPistonBase"
Cohesion: 0.33
Nodes (11): isPistonBase(), bounds(), box(), cross3(), draw(), emitBase(), emitBox(), emitHead() (+3 more)

### Community 148 - "notify"
Cohesion: 0.24
Nodes (14): activate(), blockChanged(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved(), notify() (+6 more)

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
Cohesion: 0.12
Nodes (15): dispenserFrontDir(), ChunkManager, Dispenser::dispense(), Dispenser::popDrop(), Drop, durability, type, vx (+7 more)

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
Nodes (14): 5.2 Blocks, items, inventory, crafting, blockRemoved(), EntityEnumerator, indirectPowerAt(), notifyNeighbors(), randomTick(), setEntityEnumerator(), setMinecartEnumerator() (+6 more)

### Community 160 - "Drop"
Cohesion: 0.11
Nodes (18): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+10 more)

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
Cohesion: 0.24
Nodes (17): isPlateBlock(), burnedOut(), cartTouchSink(), detectorCheck(), indirectProvidingPowerTo(), M(), plateBox(), plateCheck() (+9 more)

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

### Community 170 - "ModelBox.h"
Cohesion: 0.24
Nodes (9): build(), Face, v, Vertex, u, v, x, y (+1 more)

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
Cohesion: 0.24
Nodes (6): ChunkManager, FallingBlocks::draw(), FallingBlocks::spawn(), FallingBlocks::update(), placeable(), texCoordCell()

### Community 178 - "HostileModel.cpp"
Cohesion: 0.16
Nodes (23): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawPartAt() (+15 more)

### Community 179 - "Glow"
Cohesion: 0.24
Nodes (7): firePatch(), Glow, cell, ox, oy, oz, glowCluster()

### Community 180 - "Profiler.h"
Cohesion: 0.22
Nodes (6): ProfScope, slot, start, ProfStep, label, start

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
Cohesion: 0.20
Nodes (4): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math()

### Community 189 - "Spike"
Cohesion: 0.20
Nodes (10): Spike, dim, frame, label, part, stepMs10, total, x (+2 more)

### Community 191 - "Falling"
Cohesion: 0.22
Nodes (9): Falling, active, fallTime, prevY, type, vy, x, y (+1 more)

### Community 193 - "Sound.h"
Cohesion: 0.22
Nodes (8): Group, G_GRASS, G_GRAVEL, G_SAND, G_SNOW, G_STONE, G_WOOD, Sound::groupOf()

### Community 201 - "JavaRandom"
Cohesion: 0.29
Nodes (4): JavaRandom, seed, HostileModel::init(), make()

### Community 202 - "Liquid.cpp"
Cohesion: 0.18
Nodes (4): isHell(), percentAir(), popDue(), pushTick()

### Community 204 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 205 - "debug_single_run.py"
Cohesion: 0.36
Nodes (4): get_elf_sym(), get_target_ds_addr(), main(), MEMORY_BASIC_INFORMATION

### Community 206 - "Box"
Cohesion: 0.29
Nodes (7): Box, maxX, maxY, maxZ, minX, minY, minZ

### Community 208 - "ctypes"
Cohesion: 0.10
Nodes (22): enum_child_proc(), inspect_desmume(), inspect(), MEMORY_BASIC_INFORMATION, simulate_old_printrow(), click_coords(), run_test(), capture_window() (+14 more)

### Community 209 - "isRedstoneComponent"
Cohesion: 0.53
Nodes (6): isRedstoneComponent(), isRepeaterBlock(), isSignBlock(), hasCollision(), isInteractive(), reactsToNeighbors()

### Community 212 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 213 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 222 - ".loadHostileAtlases"
Cohesion: 0.33
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 224 - "9. Entities and physics notes"
Cohesion: 0.50
Nodes (4): 9.2 Managers: spawning, caps, explosions, 9.3 Liquids, particles, partial blocks, 9. Entities and physics notes, boxHit()

### Community 225 - "ExplosionDamage.h"
Cohesion: 0.83
Nodes (3): compute(), exposure(), lineClear()

### Community 227 - "Sky.cpp"
Cohesion: 0.53
Nodes (4): Sky::draw(), uv(), v(), vert()

### Community 228 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

### Community 229 - "DrawCtx"
Cohesion: 0.50
Nodes (4): DrawCtx, x, y, z

### Community 230 - "ArrowHurtCtx"
Cohesion: 0.67
Nodes (3): ArrowHurtCtx, hs, player

## Knowledge Gaps
- **1516 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1511 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2067 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **45 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `HandAnimations.cpp`, `Block and Item Types`, `PaintingManager.cpp`, `Dropped Item Physics`, `Block and Item Types`, `Crafting Recipes`, `NetherGen.h`, `GameplayHotbar.cpp`, `BlockType.h`, `isMaterialSolid`, `Inventory`, `Furnace.cpp`, `Pistons.cpp`, `Controls & ItemOrder`, `ChunkManager Module`, `AnimalManager Module`, `isNormalCube`, `Block and Item Types`, `RailLogic Module`, `isLiquidBlock`, `Block and Item Types`, `SheepManager.cpp`, `HostileManager Module`, `MinecartManager.cpp`, `PartialBlocks.h`, `Redstone.cpp`, `Caves.cpp`, `Vehicle Entity (MinecartModel)`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `CMWorld`, `BoatManager.cpp`, `Chunk.cpp`, `World`, `Maps Module`, `DebugChests.h`, `SteveModel.cpp`, `Sim`, `CartWorld`, `isLeavesBlock`, `.floodFillSkyLight`, `InventoryScreen.cpp`, `HostileManager Module`, `Sound.cpp`, `BlockFace`, `ChunkManager`, `BigTree`, `TntManager.cpp`, `VoxelColumnRLE`, `CMWorld`, `NoteBlocks.cpp`, `DroppedItem.cpp`, `isWaterBlock`, `TickInput`, `isPlaceable`, `Moving`, `T`, `7. World engine in detail`, `SheepManager Module`, `AnimalManager Module`, `isPistonBase`, `notify`, `PendingDrops.h`, `World`, `Dispenser.cpp`, `.generateColumn`, `Drop`, `Redstone Logic (Redstone)`, `5.2 Blocks, items, inventory, crafting`, `Drop`, `M`, `Redstone Logic (Redstone)`, `.updateTick`, `FallingBlocks.cpp`, `NetherTerrain`, `Falling`, `Sound.h`, `Liquid.cpp`, `isRedstoneComponent`?**
  _High betweenness centrality (0.240) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1516 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `Chunk` connect `Chunk Meshing and Bands` to `Block and Item Types`, `ChunkManager`, `Chunk.cpp`, `7. World engine in detail`, `FaceMask`, `isLiquidBlock`, `.saveToFileAsync`, `VoxelColumnRLE`, `Block and Item Types`, `Sphere`, `BiomeType`, `Climate.h`, `.generateColumn`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 92 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 92 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020879120879120878 - nodes in this community are weakly interconnected._