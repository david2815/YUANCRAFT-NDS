# Graph Report - YUANCRAFT NDS PORT  (2026-11-05)

## Corpus Check
- 295 files · ~383,713 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 70 file(s) not represented in the graph (top: .grit 49, (none) 8, .ini 3)

## Summary
- 4649 nodes · 10310 edges · 221 communities (174 shown, 47 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1191 edges (avg confidence: 0.86)
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
- Sound.cpp
- Inventory
- Entity AI (HostileAI)
- Furnace.cpp
- AsyncSaveManager
- DisplayListBuilder Module
- isRedstoneComponent
- WorldSave Module
- ChunkManager
- main.cpp
- Pistons.cpp
- Controls & ItemOrder
- stbi_uc
- ChunkManager Module
- AnimalManager Module
- GameOverScreen.cpp
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
- main
- AnimalAI.h
- notify
- NewWorldMenu.cpp
- Caves.cpp
- Health Module
- HostileManager Module
- Vehicle Entity (MinecartModel)
- CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)
- Texture and Image Decoding
- WorldSelectMenu Module
- PathWork
- HotbarIcons.cpp
- Animal
- GameState
- BoatManager.cpp
- Texture and Image Decoding
- Chunk.cpp
- HostileModel.cpp
- Maps Module
- DebugChests.h
- SteveModel.cpp
- NoteBlocks.cpp
- Minecraft: Nintendo DS Edition
- Sim
- IpcChunkLoader
- CartWorld
- Options Module
- rand
- BiomeType
- .floodFillSkyLight
- Caves Module
- InventoryScreen.cpp
- FishingHook.cpp
- HostileManager Module
- Projectiles.cpp
- BoatModel.cpp
- BlockFace
- MobCull & Caves
- WorldMetadata
- Tick
- TextKeyboard Module
- Hardware
- re
- Caves Module
- BigTree
- verify_world_select_simulation.py
- JRandom
- Recipe
- TopScreenMenu & Renderer
- TntManager.cpp
- FaceMask
- VoxelColumnRLE
- MenuFont.cpp
- TntManager.cpp
- ChestStore.cpp
- .sqrtf
- SheepModel Module
- Chunk.h
- Sphere
- verify_ipc_streaming_simulation.py
- Lakes Module
- 7. World engine in detail
- verify_deadlock_and_memory_simulation.py
- IpcChunkExchange
- build.sh
- Lattice
- PauseScreen Module
- TickInput
- PendingDrops.h
- HostileManager Module
- SettingsMenu.cpp
- PNode
- Profiler.h
- MockHardwareState
- Env
- T
- MockAsyncSaveManager
- Teleporter.h
- FlatQuad
- IpcLoadStatus
- Group
- SaveTask
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- Drop
- Redstone.cpp
- AnimItems.cpp
- chunkOf
- .loadHostileAtlases
- Rng
- Drop
- .hashInt
- HostileManager Module
- Drop
- RenderInput
- Redstone Logic (Redstone)
- IpcChunkLoader.h
- Drop
- Caves Module
- Dispenser::dispense
- ColorMaps & ColorMapData
- M
- HostileManager Module
- Redstone Logic (Redstone)
- PlayerHit
- verify_simulation
- Cell
- JRandom
- HudQuad
- Redstone Logic (Redstone)
- os
- .continueDisplayListRebuild
- test_emulator_run.py
- verify_occupancy_simulation.py
- verify_ui_logic_sim.py
- LakeTerrain
- Clouds.cpp
- test_print_row_safety.py
- NetherTerrain
- run_full_hardware_verification.py
- P
- math
- Falling
- Rng
- .reloadEntityTextures
- PlayerPos
- debug_single_run.py
- Chest.h
- ctypes
- ArrowHurtCtx
- Liquid.cpp
- P3
- SubScreenMenu.cpp
- RedstoneEntityCtx
- Quad

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 217 edges
3. `main()` - 201 edges
4. `ChunkManager` - 104 edges
5. `Player` - 91 edges
6. `DroppedItem` - 61 edges
7. `Sim` - 48 edges
8. `isLiquidBlock()` - 44 edges
9. `isNormalCube()` - 43 edges
10. `Texture` - 42 edges

## Surprising Connections (you probably didn't know these)
- `2. Rules for an AI assistant modifying this project (read carefully)` --references--> `BlockType`  [INFERRED]
  CLAUDE.md → source/BlockType.h
- `9.8 More internals (Nether, sky, saves, menus, chests, notes)` --references--> `resetLattice()`  [INFERRED]
  CLAUDE.md → source/NetherGen.h
- `9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`)` --references--> `packSpot()`  [INFERRED]
  CLAUDE.md → source/AnimalAI.h
- `7.2 Memory model` --references--> `BlockType`  [INFERRED]
  CLAUDE.md → source/BlockType.h
- `7.6 Saving` --references--> `BlockType`  [INFERRED]
  CLAUDE.md → source/BlockType.h

## Import Cycles
- None detected.

## Communities (221 total, 47 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (258): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+250 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (86): BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor, CACHE_RECALC_BATCH (+78 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.22
Nodes (32): 9.3 Liquids, particles, partial blocks, doubleOfSlab(), activate(), boxHit(), chunkOf(), cropCanStay(), cropsTick(), dropAt() (+24 more)

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
Nodes (26): 12.6 Mob models (`ModelBox.h`, `*Model.cpp`), isFlatInHand(), applyViewBobbing(), blockRenderColor(), brightnessOf(), drawBlockInHand(), drawFirstPersonArm(), drawItem2D() (+18 more)

### Community 8 - "Image Writing Utilities"
Cohesion: 0.09
Nodes (50): stb_image_write_test, stbi__end_write_file(), stbi_flip_vertically_on_write(), stbi__start_write_callbacks(), stbi__start_write_file(), stbi_write_bmp(), stbi_write_bmp_core(), stbi_write_bmp_to_func() (+42 more)

### Community 9 - "Spawners.cpp"
Cohesion: 0.09
Nodes (30): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+22 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.06
Nodes (44): getGrassTint(), alloc(), baseMotion(), brightnessOf(), move(), P, active, age (+36 more)

### Community 12 - "PaintingManager.cpp"
Cohesion: 0.06
Nodes (37): Art, ox, oy, sx, sy, title, brightnessOf(), ChunkManager (+29 more)

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
Nodes (20): getBlockTextures(), woolCell(), applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad(), drawLodTopQuad(), emitCenteredCrossQuad() (+12 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.26
Nodes (15): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+7 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.09
Nodes (18): CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt(), drawIconAt() (+10 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.06
Nodes (31): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+23 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.18
Nodes (5): ChestView, FurnaceData, GameplayHotbar, bgId, isInButtonRow()

### Community 21 - "BlockType.h"
Cohesion: 0.07
Nodes (57): armorMaterial(), armorMaxDurability(), armorPiece(), armorReduceAmount(), armorRenderIndex(), blockHardness(), canHarvestBlock(), dyeDamage() (+49 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.14
Nodes (24): 13. Audio, at(), cellToWorld(), digBase(), mobClip(), pick(), playClip(), raw() (+16 more)

### Community 23 - "Inventory"
Cohesion: 0.12
Nodes (23): 8. Blocks and items, 9.7 Inventory and crafting UI internals, getToolMaxDurability(), hasDurability(), isArmor(), isRecord(), maxStackFor(), ChestStore::transferWithInventory() (+15 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.06
Nodes (63): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), isNormalCube(), airSpawnSpot(), arrowTick(), attackBlocked(), attackEntity(), boxClear(), brightnessAt() (+55 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.09
Nodes (30): canSmelt(), clearEntry(), clearSlot(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate(), Furnace::fuelBurnTime(), Furnace::loadFromFile() (+22 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.10
Nodes (13): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+5 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "isRedstoneComponent"
Cohesion: 0.13
Nodes (20): 9.6 Audio internals (`Sound.cpp`), isDoorBlock(), isPistonBlock(), isRedstoneComponent(), isRedstoneTorch(), isRepeaterBlock(), isSignBlock(), bounds() (+12 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.11
Nodes (13): 9.8 More internals (Nether, sky, saves, menus, chests, notes), SD card layout, copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen, clearFolderContents(), folderExists(), WorldSave (+5 more)

### Community 30 - "ChunkManager"
Cohesion: 0.11
Nodes (14): bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches(), bigTreeDrawLine(), bigTreeEnvelope(), bigTreeLeafLayerRadius(), bigTreePlaceLeafCluster(), bigTreePlaceSphereLayer() (+6 more)

### Community 31 - "main.cpp"
Cohesion: 0.06
Nodes (20): DSI_DebugInit(), openLogFile(), ChunkManager, redstoneEnumerateEntities(), redstoneEnumerateMinecarts(), ChunkManager, draw(), OptionsMenu::open() (+12 more)

### Community 32 - "Pistons.cpp"
Cohesion: 0.07
Nodes (64): 5.2 Blocks, items, inventory, crafting, isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend() (+56 more)

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.09
Nodes (25): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+17 more)

### Community 35 - "stbi_uc"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.07
Nodes (17): AnimalManager::attack(), AnimalManager::draw(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), CMWorld (+9 more)

### Community 39 - "Block and Item Types"
Cohesion: 0.11
Nodes (6): 7.1c `tickLiquids` (20 Hz) and random ticks, isWaterBlock(), liquidFlowingOf(), liquidStillOf(), LiquidWorld, m

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - "isLiquidBlock"
Cohesion: 0.15
Nodes (13): blockLightEmission(), isCrossPlant(), isLightOpaque(), isLiquidBlock(), isPartialBlock(), isTorchBlock(), torchFromMeta(), torchMeta() (+5 more)

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.14
Nodes (25): isRailBlock(), bodyBox(), Box, maxX, maxY, maxZ, minX, minY (+17 more)

### Community 45 - "SheepManager.cpp"
Cohesion: 0.05
Nodes (34): AnimalManager::collectBodies(), ChunkManager, woolType(), ChunkManager, HostileManager::collectBodies(), collide(), MobBody, h (+26 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.07
Nodes (15): 9.2 Managers: spawning, caps, explosions, collectDeath(), countAlive(), explode(), ExplosionListener, HostileManager::attack(), HostileManager::count(), HostileManager::interact() (+7 more)

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
Cohesion: 0.08
Nodes (24): Box, q, brightnessOf(), buildBox(), ChunkManager, drawBox(), drawText(), find() (+16 more)

### Community 51 - "Noise.cpp"
Cohesion: 0.15
Nodes (9): HeightCache, h, tx, tz, NetherColCache, c, tx, tz (+1 more)

### Community 52 - "Profiler Module"
Cohesion: 0.10
Nodes (17): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike(), Spike (+9 more)

### Community 53 - "Profiler Module"
Cohesion: 0.13
Nodes (15): Slot, DL_CALL, DL_CULL, DL_LOD, DL_REBUILD, DRAW_ALL, ENTS, FACES (+7 more)

### Community 54 - "main"
Cohesion: 0.08
Nodes (6): drawBreakingOverlay(), drawDeathOverlay(), drawPortalOverlay(), drawSleepOverlay(), furnaceFrontDirFromYaw(), main()

### Community 55 - "AnimalAI.h"
Cohesion: 0.17
Nodes (19): 12.7 Mob managers (how data, AI and model connect), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+11 more)

### Community 56 - "notify"
Cohesion: 0.20
Nodes (16): activate(), blockChanged(), blockRemoved(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved() (+8 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves.cpp"
Cohesion: 0.21
Nodes (10): allocBlock(), cellRng(), emit(), floorD(), floorDiv(), freeCellBlocks(), prepare(), probeOrigins() (+2 more)

### Community 59 - "Health Module"
Cohesion: 0.08
Nodes (30): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), HealthState, air, armorPoints (+22 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.19
Nodes (15): addMob(), categoryCount(), halfCap(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn(), HostileManager::spawnPigZombie(), HostileManager::tick() (+7 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.09
Nodes (26): Pose, pitchDeg, x, y, yawDeg, z, addBox(), brightnessOf() (+18 more)

### Community 62 - "CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)"
Cohesion: 0.08
Nodes (21): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is, 2. Rules for an AI assistant modifying this project (read carefully) (+13 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.19
Nodes (3): clearLabelZone(), drawWorldName(), WorldSelectMenu

### Community 65 - "PathWork"
Cohesion: 0.19
Nodes (18): findPath(), heapAdd(), heapChange(), heapDequeue(), heapSortBack(), heapSortForward(), openPoint(), pathHash() (+10 more)

### Community 66 - "HotbarIcons.cpp"
Cohesion: 0.27
Nodes (8): drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon(), getItemsPixelIndex(), getTerrainPixelIndex(), HotbarIcons

### Community 67 - "Animal"
Cohesion: 0.21
Nodes (21): anyIn(), cellY(), damage(), faceEntity(), headInWater(), inFire(), inLava(), insideOpaque() (+13 more)

### Community 68 - "GameState"
Cohesion: 0.15
Nodes (16): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, computeCelestialAngle(), computeNightFactor(), computeSkyBrightness(), computeSkylightSubtract() (+8 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.06
Nodes (31): BoatManager::attack(), BoatManager::dismount(), BoatManager::draw(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::riderEye(), BoatManager::saveToFile(), BoatManager::spawnFromRay() (+23 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "Chunk.cpp"
Cohesion: 0.07
Nodes (12): BigTreeBranch, trunkY, x, y, z, oreFloorInt(), OreRng, s (+4 more)

### Community 72 - "HostileModel.cpp"
Cohesion: 0.11
Nodes (31): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawPartAt() (+23 more)

### Community 73 - "Maps Module"
Cohesion: 0.13
Nodes (22): find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush(), Maps::pixels() (+14 more)

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
Cohesion: 0.11
Nodes (11): isFlowingLiquid(), isLavaBlock(), isMaterialSolid(), liquidMaterial(), percentAir(), Sim, editing, flowCost (+3 more)

### Community 79 - "IpcChunkLoader"
Cohesion: 0.18
Nodes (7): IpcChunkLoader, MAX_WAIT_FRAMES, s_exchange, s_initialized, TICKS_PER_MS, TIMEOUT_MS, TIMEOUT_TICKS

### Community 80 - "CartWorld"
Cohesion: 0.17
Nodes (7): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn()

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "rand"
Cohesion: 0.13
Nodes (20): 9.5 World-generation pieces, 9. Entities and physics notes, isLeavesBlock(), isSapling(), beginFrame(), rand, cropDrops(), useBoneMeal() (+12 more)

### Community 83 - "BiomeType"
Cohesion: 0.12
Nodes (16): BiomeType, DESERT, FOREST, GENERIC, OCEAN, PLAINS, RAINFOREST, SAVANNA (+8 more)

### Community 84 - ".floodFillSkyLight"
Cohesion: 0.23
Nodes (6): lightDim(), LightNode, bx, by, bz, level

### Community 85 - "Caves Module"
Cohesion: 0.12
Nodes (17): Job, active, cx, cz, fill, nOrigins, originIdx, ox (+9 more)

### Community 86 - "InventoryScreen.cpp"
Cohesion: 0.20
Nodes (10): drawCountAt(), drawDigit(), drawDurabilityBar(), drawIconAt(), drawSelectionBoxAt(), getItemsPixelIndex(), getSlotPosition(), getTerrainPixelIndex() (+2 more)

### Community 87 - "FishingHook.cpp"
Cohesion: 0.05
Nodes (47): Catch, damage, fish, vx, vy, vz, x, y (+39 more)

### Community 88 - "HostileManager Module"
Cohesion: 0.18
Nodes (6): exposure(), HWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 89 - "Projectiles.cpp"
Cohesion: 0.07
Nodes (34): brightnessOf(), cellY(), ChunkManager, chunkOf(), drawSprite(), eggBreak(), gaussian(), Kind (+26 more)

### Community 90 - "BoatModel.cpp"
Cohesion: 0.08
Nodes (27): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+19 more)

### Community 91 - "BlockFace"
Cohesion: 0.09
Nodes (26): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+18 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.22
Nodes (9): State, lx, ly, lz, maxDist2, valid, x, y (+1 more)

### Community 93 - "WorldMetadata"
Cohesion: 0.11
Nodes (18): WorldMetadata, armorDurability, armorType, formatVersion, gameTimeTicks, hotbarCount, hotbarDurability, hotbarType (+10 more)

### Community 94 - "Tick"
Cohesion: 0.20
Nodes (8): Tick, due, gx, gy, gz, seq, type, used

### Community 95 - "TextKeyboard Module"
Cohesion: 0.13
Nodes (22): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+14 more)

### Community 98 - "Caves Module"
Cohesion: 0.13
Nodes (15): Tunnel, branchStep, isRoom, length, pitch, pitchVel, r, radiusScale (+7 more)

### Community 99 - "BigTree"
Cohesion: 0.13
Nodes (13): BigTree, AX, basePos, branchSlope, height, heightAttenuation, heightLimit, heightLimitLimit (+5 more)

### Community 100 - "verify_world_select_simulation.py"
Cohesion: 0.21
Nodes (6): main(), simulate_world_select_menu(), test_empty_and_corrupt_world_directory(), test_math_division_shortcut(), test_polygon_budget_and_overflow(), test_world_lifecycle_and_deletion()

### Community 101 - "JRandom"
Cohesion: 0.19
Nodes (10): advanceOrigin(), initTunnel(), jcos(), JRandom, seed, jsin(), pushTunnel(), reset() (+2 more)

### Community 102 - "Recipe"
Cohesion: 0.14
Nodes (20): canCraft(), countMatchingIngredient(), countPatternCells(), doCraft(), ingredientMatches(), Recipe, altA, altB (+12 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.22
Nodes (3): Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.15
Nodes (13): Tnt, active, fuse, mx, my, mz, onGround, prevX (+5 more)

### Community 105 - "FaceMask"
Cohesion: 0.17
Nodes (10): Cube, drawBox(), FaceMask, bottom, east, north, south, top (+2 more)

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.15
Nodes (8): RLERun, length, type, VoxelColumnRLE, MAX_RUNS, _pad, runCount, runs

### Community 107 - "MenuFont.cpp"
Cohesion: 0.23
Nodes (11): find(), Glyph, c, rows, MenuFont::draw16(), MenuFont::draw8(), MenuFont::fill16(), MenuFont::fill8() (+3 more)

### Community 108 - "TntManager.cpp"
Cohesion: 0.17
Nodes (11): ChunkManager, blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn(), TntManager::draw() (+3 more)

### Community 109 - "ChestStore.cpp"
Cohesion: 0.09
Nodes (24): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+16 more)

### Community 111 - "SheepModel Module"
Cohesion: 0.13
Nodes (17): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+9 more)

### Community 112 - "Chunk.h"
Cohesion: 0.08
Nodes (11): DisplayListBuilder, ChunkManager, Dispenser::popDrop(), ChunkManager, ChunkManager, FallingBlocks::draw(), texCoordCell(), MenuBackground (+3 more)

### Community 113 - "Sphere"
Cohesion: 0.14
Nodes (13): CarveCursor, cell, sphere, carveSphere(), carveStep(), floorF(), isDecoration(), Sphere (+5 more)

### Community 114 - "verify_ipc_streaming_simulation.py"
Cohesion: 0.19
Nodes (8): main(), MockChunk, MockChunkManager, SimulatedIpcChunkLoader, test_async_streaming_flow(), test_corrupted_file_failsafe(), test_sd_timeout_failsafe(), test_ui_stability_and_vblank_loop()

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.17
Nodes (9): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), 7.1b `ChunkManager::update` order (every main-loop iteration), 7.2 Memory model, 7.3 Generation pipeline (`Chunk::update`, spread across many frames), 7.4 Lighting, 7.5 Meshing and drawing, 7.6 Saving, 7. World engine in detail (+1 more)

### Community 117 - "verify_deadlock_and_memory_simulation.py"
Cohesion: 0.33
Nodes (6): is_valid_main_ram_pointer(), main(), test_60_frame_escape_mechanism(), test_debug_logger_sd_output(), test_ds_4mb_profile(), test_dsi_16mb_profile()

### Community 118 - "IpcChunkExchange"
Cohesion: 0.17
Nodes (11): IpcChunkExchange, chunkX, chunkZ, compBuffer, dataSize, frameCounter, path, rawBuffer (+3 more)

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 120 - "Lattice"
Cohesion: 0.07
Nodes (23): state, initIfSeedChanged(), Lattice, h, t, x0, z0, Octaves (+15 more)

### Community 121 - "PauseScreen Module"
Cohesion: 0.15
Nodes (9): Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched() (+1 more)

### Community 122 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 123 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 125 - "SettingsMenu.cpp"
Cohesion: 0.27
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 126 - "PNode"
Cohesion: 0.20
Nodes (10): PNode, closed, heapIndex, prev, toNext, total, toTarget, x (+2 more)

### Community 128 - "Profiler.h"
Cohesion: 0.22
Nodes (6): ProfScope, slot, start, ProfStep, label, start

### Community 129 - "MockHardwareState"
Cohesion: 0.29
Nodes (3): main(), MockHardwareState, simulate()

### Community 131 - "Env"
Cohesion: 0.25
Nodes (8): Env, burningBox, cactus, fallLanded, headInWater, inLava, insideBlock, inWater

### Community 132 - "T"
Cohesion: 0.24
Nodes (12): addWirePos(), anySideNormal(), cartTouchSink(), doorPower(), maxStrength(), neighborChanged(), neighborDo(), normal() (+4 more)

### Community 134 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 135 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 136 - "IpcLoadStatus"
Cohesion: 0.25
Nodes (7): IpcLoadStatus, IPC_STATUS_ERROR, IPC_STATUS_IDLE, IPC_STATUS_READING, IPC_STATUS_READY, IPC_STATUS_REQUESTED, IPC_STATUS_TIMEOUT

### Community 137 - "Group"
Cohesion: 0.25
Nodes (8): Group, G_GRASS, G_GRAVEL, G_SAND, G_SNOW, G_STONE, G_WOOD, Sound::groupOf()

### Community 138 - "SaveTask"
Cohesion: 0.29
Nodes (6): SaveTask, data, dataSize, inUse, _pad, path

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
Cohesion: 0.44
Nodes (5): bodyBox(), boxInWater(), moveEntity(), rayHit(), tick()

### Community 143 - "AnimalManager Module"
Cohesion: 0.33
Nodes (6): Drop, count, type, x, y, z

### Community 146 - "Drop"
Cohesion: 0.29
Nodes (7): Drop, count, durability, type, x, y, z

### Community 147 - "Redstone.cpp"
Cohesion: 0.19
Nodes (15): bounds(), burnedOut(), canProvidePower(), dropItem(), gettingPowered(), indirectlyGettingPowered(), indirectPowerAt(), indirectProvidingPowerTo() (+7 more)

### Community 148 - "AnimItems.cpp"
Cohesion: 0.08
Nodes (9): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, AnimItems::init(), AnimItems::tick(), setFrame() (+1 more)

### Community 149 - "chunkOf"
Cohesion: 0.29
Nodes (6): chunkOf(), floorDivi(), lightOre(), put(), removeBlock(), setTM()

### Community 150 - ".loadHostileAtlases"
Cohesion: 0.33
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 152 - "Drop"
Cohesion: 0.22
Nodes (9): Drop, durability, type, vx, vy, vz, x, y (+1 more)

### Community 153 - ".hashInt"
Cohesion: 0.19
Nodes (9): Chunk::Chunk(), getPatchAt(), terrainHeightCached(), terrainHeightFrom(), findLandChunkOffset(), hash2D(), Noise, randomGridValue() (+1 more)

### Community 154 - "HostileManager Module"
Cohesion: 0.29
Nodes (7): SavedWolf, health, sitting, x, y, yaw, z

### Community 155 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 157 - "RenderInput"
Cohesion: 0.20
Nodes (9): RenderInput, bodyLight, dimension, eyeLight, partialTicks, pitch, posX, posZ (+1 more)

### Community 158 - "Redstone Logic (Redstone)"
Cohesion: 0.29
Nodes (7): Tick, due, seq, t, x, y, z

### Community 160 - "Drop"
Cohesion: 0.33
Nodes (6): Drop, count, type, x, y, z

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "Dispenser::dispense"
Cohesion: 0.50
Nodes (4): dispenserFrontDir(), Dispenser::dispense(), gauss(), typeAtGrid()

### Community 163 - "ColorMaps & ColorMapData"
Cohesion: 0.48
Nodes (3): ColorMaps::foliage(), ColorMaps::grass(), lookup()

### Community 164 - "M"
Cohesion: 0.26
Nodes (16): isPlateBlock(), detectorCheck(), faceCode(), freeCell(), M(), plateBox(), plateCheck(), randomTick() (+8 more)

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

### Community 171 - "HudQuad"
Cohesion: 0.20
Nodes (8): HealthHud::draw(), build(), HudQuad, layer, u, v, x, y

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 173 - "os"
Cohesion: 0.08
Nodes (6): verify_structural(), verify_structural(), main(), verify_structural(), verify_structural(), verify_all()

### Community 174 - ".continueDisplayListRebuild"
Cohesion: 0.50
Nodes (3): callListFast(), flushList(), DSI_Log()

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

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
Cohesion: 0.10
Nodes (11): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math(), compute(), exposure(), lineClear(), Sky::draw() (+3 more)

### Community 189 - "Falling"
Cohesion: 0.22
Nodes (9): Falling, active, fallTime, prevY, type, vy, x, y (+1 more)

### Community 204 - "PlayerPos"
Cohesion: 0.40
Nodes (5): PlayerPos, valid, x, y, z

### Community 205 - "debug_single_run.py"
Cohesion: 0.36
Nodes (4): get_elf_sym(), get_target_ds_addr(), main(), MEMORY_BASIC_INFORMATION

### Community 208 - "ctypes"
Cohesion: 0.10
Nodes (22): enum_child_proc(), inspect_desmume(), inspect(), MEMORY_BASIC_INFORMATION, simulate_old_printrow(), click_coords(), run_test(), capture_window() (+14 more)

### Community 209 - "ArrowHurtCtx"
Cohesion: 0.67
Nodes (3): ArrowHurtCtx, hs, player

### Community 210 - "Liquid.cpp"
Cohesion: 0.25
Nodes (3): isHell(), popDue(), pushTick()

### Community 212 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 222 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

### Community 224 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

## Knowledge Gaps
- **1492 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1487 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2038 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **47 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `T`, `HandAnimations.cpp`, `Group`, `Block and Item Types`, `PaintingManager.cpp`, `SheepManager Module`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `Crafting Recipes`, `NetherGen.h`, `Drop`, `BlockType.h`, `Redstone.cpp`, `Inventory`, `Entity AI (HostileAI)`, `.hashInt`, `Drop`, `Furnace.cpp`, `isRedstoneComponent`, `Drop`, `ChunkManager`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Drop`, `Dispenser::dispense`, `M`, `AnimalManager Module`, `ChunkManager Module`, `Block and Item Types`, `RailLogic Module`, `Redstone Logic (Redstone)`, `isLiquidBlock`, `Block and Item Types`, `SheepManager.cpp`, `HostileManager Module`, `MinecartManager.cpp`, `notify`, `NetherTerrain`, `Falling`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `Vehicle Entity (MinecartModel)`, `HotbarIcons.cpp`, `BoatManager.cpp`, `Chunk.cpp`, `Maps Module`, `DebugChests.h`, `SteveModel.cpp`, `NoteBlocks.cpp`, `Sim`, `CartWorld`, `rand`, `Liquid.cpp`, `.floodFillSkyLight`, `InventoryScreen.cpp`, `FishingHook.cpp`, `HostileManager Module`, `Projectiles.cpp`, `BlockFace`, `BigTree`, `Recipe`, `VoxelColumnRLE`, `TntManager.cpp`, `chunkOf`, `Sound.cpp`, `Sphere`, `7. World engine in detail`, `TickInput`, `PendingDrops.h`?**
  _High betweenness centrality (0.221) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1492 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007751937984496124 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `main` to `Crafting Recipes`, `GameplayHotbar.cpp`, `BlockType.h`, `.loadHostileAtlases`, `Inventory`, `Entity AI (HostileAI)`, `.hashInt`, `AsyncSaveManager`, `isRedstoneComponent`, `WorldSave Module`, `main.cpp`, `Pistons.cpp`, `Texture & PaintingTex`, `M`, `GameOverScreen.cpp`, `isLiquidBlock`, `Block and Item Types`, `.continueDisplayListRebuild`, `DebugLogger`, `.update`, `NewWorldMenu.cpp`, `WorldSelectMenu Module`, `HotbarIcons.cpp`, `GameState`, `SteveModel.cpp`, `.reloadEntityTextures`, `Sim`, `rand`, `InventoryScreen.cpp`, `FishingHook.cpp`, `SubScreenMenu.cpp`, `BlockFace`, `Hardware`, `Recipe`, `TopScreenMenu & Renderer`, `.sqrtf`, `PendingDrops.h`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 90 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 90 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020559680182752713 - nodes in this community are weakly interconnected._