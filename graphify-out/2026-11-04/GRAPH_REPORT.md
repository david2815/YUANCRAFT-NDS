# Graph Report - YUANCRAFT NDS PORT  (2026-11-04)

## Corpus Check
- 293 files · ~382,354 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 70 file(s) not represented in the graph (top: .grit 49, (none) 8, .ini 3)

## Summary
- 4639 nodes · 10291 edges · 236 communities (193 shown, 43 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1185 edges (avg confidence: 0.86)
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
- PartialBlocks.h
- WorldSave Module
- ChunkManager
- nds
- Pistons.cpp
- Texture & PaintingTex
- Controls & ItemOrder
- stbi_uc
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
- isNormalCube
- LoadingScreen.cpp
- notify
- NewWorldMenu.cpp
- Caves.cpp
- Health Module
- HostileManager Module
- Vehicle Entity (MinecartModel)
- CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)
- Texture and Image Decoding
- WorldSelectMenu Module
- AnimalAI.h
- Painting
- HostileModel.cpp
- main.cpp
- BoatManager.cpp
- Texture and Image Decoding
- Chunk.cpp
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
- BlockFace
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
- TntManager.cpp
- ChestStore.cpp
- .sqrtf
- SheepModel Module
- ChunkManager.h
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
- RailLogic.h
- stdlib
- stbi__malloc
- MockHardwareState
- FishingHook.cpp
- CMWorld
- T
- MockAsyncSaveManager
- Teleporter.h
- FlatQuad
- .update
- RaycastHit
- Climate.h
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- Drop
- indirectProvidingPowerTo
- AnimItems.cpp
- StartupSplash Module
- World
- ChestStore.cpp
- Drop
- .hashInt
- HostileManager Module
- Drop
- RenderInput
- Redstone Logic (Redstone)
- Catch
- Drop
- Caves Module
- Redstone.cpp
- ColorMaps & ColorMapData
- M
- HostileManager Module
- Redstone Logic (Redstone)
- verify_simulation
- Cell
- JRandom
- HudQuad
- Redstone Logic (Redstone)
- os
- Falling
- test_emulator_run.py
- verify_occupancy_simulation.py
- Projectiles.h
- Quad
- Drop
- Quad
- verify_ui_logic_sim.py
- computeSkyBrightness
- Clouds.cpp
- test_print_row_safety.py
- NetherTerrain
- run_full_hardware_verification.py
- P
- math
- FallingBlocks.cpp
- ModelBox.h
- stbi__bmp_load
- State
- Art
- Part
- 12. Rendering, textures and models
- Sound.h
- debug_single_run.py
- ExplosionDamage.h
- Env
- ctypes
- ArrowHurtCtx
- Liquid.cpp
- Kind
- bigTreeComputeBranches
- bump
- SubScreenMenu.cpp
- RedstoneEntityCtx
- Quad
- Climate.h
- GameState
- Pose
- playClip

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 216 edges
3. `main()` - 199 edges
4. `ChunkManager` - 102 edges
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

## Communities (236 total, 43 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (86): BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor, CACHE_RECALC_BATCH (+78 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.20
Nodes (34): 9.3 Liquids, particles, partial blocks, doubleOfSlab(), isRecord(), activate(), boxHit(), chunkOf(), cropCanStay(), cropsTick() (+26 more)

### Community 3 - "Block and Item Types"
Cohesion: 0.06
Nodes (73): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+65 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (57): main(), Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase, bobStrength, buttonLookSpeedH, buttonLookSpeedV (+49 more)

### Community 5 - "Texture and Image Decoding"
Cohesion: 0.08
Nodes (46): main(), stbi__convert_8_to_16(), stbi_convert_iphone_png_to_rgb(), stbi_convert_iphone_png_to_rgb_thread(), stbi_convert_wchar_to_utf8(), stbi__do_zlib(), stbi_failure_reason(), stbi__fopen() (+38 more)

### Community 6 - "Texture and Image Decoding"
Cohesion: 0.14
Nodes (46): stbi__at_eof(), stbi__bmp_info(), stbi__bmp_test(), stbi__build_huffman(), stbi__check_png_header(), stbi__get16be(), stbi__get32be(), stbi__get8() (+38 more)

### Community 7 - "HandAnimations.cpp"
Cohesion: 0.11
Nodes (30): 12.6 Mob models (`ModelBox.h`, `*Model.cpp`), isSword(), applyViewBobbing(), blockRenderColor(), brightnessOf(), drawBlockInHand(), drawFirstPersonArm(), drawItem2D() (+22 more)

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
Cohesion: 0.11
Nodes (30): blockLightEmission(), furnaceIsLit(), getBlockTextures(), getDropType(), isDispenserBlock(), isFurnaceBlock(), isJackBlock(), isPumpkinBlock() (+22 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.26
Nodes (15): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+7 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.09
Nodes (17): CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt(), drawPageIndicator() (+9 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.06
Nodes (31): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+23 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.11
Nodes (13): ChestView, FurnaceData, GameplayHotbar, bgId, isInButtonRow(), drawDigit(), drawDurabilityBar(), drawSelectionBox() (+5 more)

### Community 21 - "BlockType.h"
Cohesion: 0.11
Nodes (36): 8. Blocks and items, armorMaterial(), armorRenderIndex(), blockHardness(), canHarvestBlock(), dyeDamage(), fireCatch(), getBlockStrength() (+28 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.17
Nodes (20): at(), cellToWorld(), digBase(), mobClip(), pick(), raw(), rnd(), Sound::blockBreak() (+12 more)

### Community 23 - "Inventory"
Cohesion: 0.07
Nodes (44): 9.7 Inventory and crafting UI internals, armorMaxDurability(), armorPiece(), armorReduceAmount(), getToolMaxDurability(), hasDurability(), isArmor(), maxStackFor() (+36 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.14
Nodes (32): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), arrowTick(), attackBlocked(), attackEntity(), boxClear(), brightnessAt(), canSee(), canSpawnHere() (+24 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.08
Nodes (35): furnaceFrontDir(), makeFurnaceBlock(), canSmelt(), ChunkManager, clearEntry(), clearSlot(), floorDivInt(), Furnace::clearAll() (+27 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.08
Nodes (19): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+11 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "PartialBlocks.h"
Cohesion: 0.10
Nodes (32): 9.6 Audio internals (`Sound.cpp`), iconShapeVisible(), isDoorBlock(), isPistonBlock(), isPlateBlock(), isRedstoneComponent(), isRedstoneTorch(), isRepeaterBlock() (+24 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.14
Nodes (10): 9.8 More internals (Nether, sky, saves, menus, chests, notes), SD card layout, clearFolderContents(), folderExists(), WorldSave, s_activeBasePath, s_activeWorldNum, s_dimension (+2 more)

### Community 31 - "nds"
Cohesion: 0.16
Nodes (4): draw(), OptionsMenu::open(), OptionsMenu::update(), printRow()

### Community 32 - "Pistons.cpp"
Cohesion: 0.07
Nodes (64): 5.2 Blocks, items, inventory, crafting, isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend() (+56 more)

### Community 33 - "Texture & PaintingTex"
Cohesion: 0.07
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.09
Nodes (25): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+17 more)

### Community 35 - "stbi_uc"
Cohesion: 0.10
Nodes (27): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__convert_16_to_8(), stbi__copyval(), stbi__float_postprocess() (+19 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.10
Nodes (10): AnimalManager::attack(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath(), countKind(), halfCap() (+2 more)

### Community 40 - "RailLogic Module"
Cohesion: 0.18
Nodes (9): adjacentCount(), isRailAt(), Logic, c, n, powered, tx, ty (+1 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.20
Nodes (22): stbi__addints_valid(), stbi__build_fast_ac(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__extend_receive(), stbi__get_marker(), stbi__grow_buffer_unsafe(), stbi__jpeg_decode_block() (+14 more)

### Community 42 - "isLiquidBlock"
Cohesion: 0.12
Nodes (15): isCrossPlant(), isLightOpaque(), isLiquidBlock(), isPartialBlock(), isSapling(), isTorchBlock(), torchMeta(), cellOfIndex() (+7 more)

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.14
Nodes (25): isRailBlock(), bodyBox(), Box, maxX, maxY, maxZ, minX, minY (+17 more)

### Community 45 - "Block and Item Types"
Cohesion: 0.09
Nodes (14): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::explosionDamage(), SheepManager::interact() (+6 more)

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
Cohesion: 0.08
Nodes (24): Box, q, brightnessOf(), buildBox(), ChunkManager, drawBox(), drawText(), find() (+16 more)

### Community 51 - "Noise.cpp"
Cohesion: 0.13
Nodes (10): Chunk::Chunk(), HeightCache, h, tx, tz, NetherColCache, c, tx (+2 more)

### Community 52 - "Profiler Module"
Cohesion: 0.10
Nodes (17): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike(), Spike (+9 more)

### Community 53 - "Profiler Module"
Cohesion: 0.08
Nodes (21): ProfScope, slot, start, ProfStep, label, start, Slot, DL_CALL (+13 more)

### Community 54 - "isNormalCube"
Cohesion: 0.09
Nodes (30): isNormalCube(), airSpawnSpot(), autoMeta(), boundsForMeta(), Box, x0, x1, y0 (+22 more)

### Community 55 - "LoadingScreen.cpp"
Cohesion: 0.43
Nodes (3): copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen

### Community 56 - "notify"
Cohesion: 0.19
Nodes (17): activate(), blockChanged(), blockRemoved(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved() (+9 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves.cpp"
Cohesion: 0.18
Nodes (13): carveSphere(), carveStep(), cellRng(), floorDiv(), floorF(), isDecoration(), jcos(), jsin() (+5 more)

### Community 59 - "Health Module"
Cohesion: 0.09
Nodes (30): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), HealthState, air, armorPoints (+22 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.17
Nodes (17): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::count(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn() (+9 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)"
Cohesion: 0.11
Nodes (18): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is, 2. Rules for an AI assistant modifying this project (read carefully) (+10 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.10
Nodes (34): stbi__addsizes_valid(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__convert_format(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+26 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.17
Nodes (3): clearLabelZone(), drawWorldName(), WorldSelectMenu

### Community 65 - "AnimalAI.h"
Cohesion: 0.06
Nodes (75): 12.7 Mob managers (how data, AI and model connect), anyIn(), blocking(), bodyBox(), Box, x0, x1, y0 (+67 more)

### Community 66 - "Painting"
Cohesion: 0.12
Nodes (17): Painting, active, art, dir, gx, gy, gz, maxX (+9 more)

### Community 67 - "HostileModel.cpp"
Cohesion: 0.20
Nodes (16): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawSpider() (+8 more)

### Community 68 - "main.cpp"
Cohesion: 0.07
Nodes (17): HealthHud::draw(), drawBreakingOverlay(), drawDeathOverlay(), drawPortalOverlay(), drawSleepOverlay(), furnaceFrontDirFromYaw(), redstoneEnumerateEntities(), redstoneEnumerateMinecarts() (+9 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.14
Nodes (11): BoatManager::attack(), BoatManager::dismount(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::saveToFile(), breakBoat(), dismountIndex(), forceDismount() (+3 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (18): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__err(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block() (+10 more)

### Community 71 - "Chunk.cpp"
Cohesion: 0.08
Nodes (8): chunkFloorDiv(), oreFloorInt(), OreRng, s, oreVeinBlob(), sameFaces(), shiftDown1(), shiftUp1()

### Community 72 - "CMWorld"
Cohesion: 0.17
Nodes (7): AnimalManager::draw(), AnimalManager::explosionDamage(), CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

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
Cohesion: 0.09
Nodes (16): fireEncourage(), isFlowingLiquid(), isLavaBlock(), isMaterialSolid(), isWaterBlock(), liquidFlowingOf(), liquidMaterial(), liquidStillOf() (+8 more)

### Community 79 - "IpcChunkLoader"
Cohesion: 0.06
Nodes (27): Chunk, ChunkManager, IpcChunkExchange, chunkX, chunkZ, compBuffer, dataSize, frameCounter (+19 more)

### Community 80 - "CartWorld"
Cohesion: 0.15
Nodes (9): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn(), MinecartManager::tick() (+1 more)

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "BigTree"
Cohesion: 0.05
Nodes (38): 9.5 World-generation pieces, isLeavesBlock(), beginFrame(), PendingDrop, type, x, y, z (+30 more)

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
Cohesion: 0.18
Nodes (6): exposure(), HWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 89 - "Projectiles.cpp"
Cohesion: 0.22
Nodes (15): brightnessOf(), cellY(), chunkOf(), eggBreak(), gaussian(), nextFloat(), nextInt(), nextU() (+7 more)

### Community 90 - "BoatModel.cpp"
Cohesion: 0.17
Nodes (12): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+4 more)

### Community 91 - "BlockFace"
Cohesion: 0.17
Nodes (14): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+6 more)

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
Cohesion: 0.23
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
Cohesion: 0.20
Nodes (4): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.15
Nodes (13): Tnt, active, fuse, mx, my, mz, onGround, prevX (+5 more)

### Community 105 - "FaceMask"
Cohesion: 0.17
Nodes (10): Cube, drawBox(), FaceMask, bottom, east, north, south, top (+2 more)

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.14
Nodes (10): isValidMainRamPointer(), isVramPointer(), RLERun, length, type, VoxelColumnRLE, MAX_RUNS, _pad (+2 more)

### Community 107 - "MockHardwareNDS"
Cohesion: 0.23
Nodes (3): main(), MockHardwareNDS, run_simulation()

### Community 108 - "TntManager.cpp"
Cohesion: 0.19
Nodes (12): rand, cropDrops(), blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn() (+4 more)

### Community 109 - "ChestStore.cpp"
Cohesion: 0.12
Nodes (15): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+7 more)

### Community 111 - "SheepModel Module"
Cohesion: 0.13
Nodes (17): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+9 more)

### Community 112 - "ChunkManager.h"
Cohesion: 0.31
Nodes (5): dispenserFrontDir(), Dispenser::dispense(), Dispenser::popDrop(), gauss(), typeAtGrid()

### Community 113 - "Sphere"
Cohesion: 0.10
Nodes (12): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), CarveCursor, cell, sphere, Sphere, flat, r16, x8 (+4 more)

### Community 114 - "verify_ipc_streaming_simulation.py"
Cohesion: 0.19
Nodes (8): main(), MockChunk, MockChunkManager, SimulatedIpcChunkLoader, test_async_streaming_flow(), test_corrupted_file_failsafe(), test_sd_timeout_failsafe(), test_ui_stability_and_vblank_loop()

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.20
Nodes (7): 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.5 Meshing and drawing, 7.6 Saving, 7. World engine in detail

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
Cohesion: 0.25
Nodes (5): Simplex, perm, xo, yo, zo

### Community 121 - "PauseScreen Module"
Cohesion: 0.15
Nodes (9): Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched() (+1 more)

### Community 122 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 123 - "World"
Cohesion: 0.18
Nodes (7): drawSprite(), Projectiles::draw(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 125 - "SettingsMenu.cpp"
Cohesion: 0.27
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 126 - "RailLogic.h"
Cohesion: 0.20
Nodes (10): 9.4 Minecarts, boats, TNT, 9. Entities and physics notes, chainEnd(), chainPowered(), hasPower(), Pos, x, y (+2 more)

### Community 128 - "stbi__malloc"
Cohesion: 0.18
Nodes (15): stbi__compute_y_16(), stbi__convert_format16(), stbi__cpuid3(), stbi__gif_header(), stbi__gif_load_next(), stbi__gif_parse_colortable(), stbi__jpeg_load(), stbi__load_gif_main() (+7 more)

### Community 129 - "MockHardwareState"
Cohesion: 0.29
Nodes (3): main(), MockHardwareState, simulate()

### Community 130 - "FishingHook.cpp"
Cohesion: 0.23
Nodes (13): cellY(), FishingHook::cast(), FishingHook::clear(), FishingHook::draw(), gaussian(), handPos(), nextFloat(), nextInt() (+5 more)

### Community 131 - "CMWorld"
Cohesion: 0.18
Nodes (6): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady, SheepManager::draw()

### Community 132 - "T"
Cohesion: 0.20
Nodes (14): addWirePos(), anySideNormal(), canProvidePower(), cartTouchSink(), doorPower(), dropItem(), isPowerProviderOrWire(), maxStrength() (+6 more)

### Community 134 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 135 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 136 - ".update"
Cohesion: 0.24
Nodes (3): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), cellInWindow(), ChunkManager::ChunkManager()

### Community 137 - "RaycastHit"
Cohesion: 0.15
Nodes (13): Chunk, ChunkManager, Raycaster, RaycastHit, blockXi, blockYi, blockZi, chunk (+5 more)

### Community 138 - "Climate.h"
Cohesion: 0.22
Nodes (6): Lattice, h, t, x0, z0, raw()

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

### Community 147 - "indirectProvidingPowerTo"
Cohesion: 0.32
Nodes (8): gettingPowered(), indirectlyGettingPowered(), indirectPowerAt(), indirectProvidingPowerTo(), isIndirectlyPoweringTo(), isPoweringTo(), providingPowerTo(), wirePoweringTo()

### Community 148 - "AnimItems.cpp"
Cohesion: 0.16
Nodes (3): AnimItems::init(), AnimItems::tick(), setFrame()

### Community 150 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 151 - "ChestStore.cpp"
Cohesion: 0.29
Nodes (9): ChestStore::clearAll(), ChestStore::findOrCreate(), ChestStore::loadFromFile(), ChestStore::remove(), ChestStore::saveToFile(), clearEntry(), clearSlot(), getI32() (+1 more)

### Community 152 - "Drop"
Cohesion: 0.18
Nodes (10): ChunkManager, Drop, durability, type, vx, vy, vz, x (+2 more)

### Community 153 - ".hashInt"
Cohesion: 0.14
Nodes (10): getPatchAt(), LakeTerrain, lava, terrainHeightCached(), terrainHeightFrom(), findLandChunkOffset(), hash2D(), Noise (+2 more)

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

### Community 164 - "M"
Cohesion: 0.36
Nodes (12): detectorCheck(), M(), plateBox(), plateCheck(), randomTick(), repeaterCheck(), repeaterInput(), repeaterTick() (+4 more)

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

### Community 171 - "HudQuad"
Cohesion: 0.29
Nodes (7): build(), HudQuad, layer, u, v, x, y

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 173 - "os"
Cohesion: 0.08
Nodes (6): verify_structural(), verify_structural(), main(), verify_structural(), verify_structural(), verify_all()

### Community 174 - "Falling"
Cohesion: 0.22
Nodes (9): Falling, active, fallTime, prevY, type, vy, x, y (+1 more)

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

### Community 177 - "Projectiles.h"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 178 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 179 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 180 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 181 - "verify_ui_logic_sim.py"
Cohesion: 0.38
Nodes (3): MockOptions, test_ds_original_menu_logic(), test_dsi_profile_and_fps_target()

### Community 182 - "computeSkyBrightness"
Cohesion: 0.31
Nodes (9): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, computeCelestialAngle(), computeNightFactor(), computeSkyBrightness(), computeSkylightSubtract() (+1 more)

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
Cohesion: 0.43
Nodes (4): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math()

### Community 189 - "FallingBlocks.cpp"
Cohesion: 0.24
Nodes (6): ChunkManager, FallingBlocks::draw(), FallingBlocks::spawn(), FallingBlocks::update(), placeable(), texCoordCell()

### Community 191 - "ModelBox.h"
Cohesion: 0.24
Nodes (9): build(), Face, v, Vertex, u, v, x, y (+1 more)

### Community 193 - "stbi__bmp_load"
Cohesion: 0.31
Nodes (9): stbi__bitcount(), stbi__bmp_load(), stbi__bmp_parse_header(), stbi__bmp_set_mask_defaults(), stbi__bmp_test_raw(), stbi__get16le(), stbi__get32le(), stbi__high_bit() (+1 more)

### Community 200 - "State"
Cohesion: 0.33
Nodes (6): State, detail, humidity, ready, seed, temperature

### Community 201 - "Art"
Cohesion: 0.33
Nodes (6): Art, ox, oy, sx, sy, title

### Community 202 - "Part"
Cohesion: 0.31
Nodes (9): drawPartAt(), drawPartRot(), drawWolf(), emitQuads(), Part, pointX, pointY, pointZ (+1 more)

### Community 203 - "12. Rendering, textures and models"
Cohesion: 0.29
Nodes (6): 12.2 Texture loading (`Texture.h/.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 204 - "Sound.h"
Cohesion: 0.22
Nodes (8): Group, G_GRASS, G_GRAVEL, G_SAND, G_SNOW, G_STONE, G_WOOD, Sound::groupOf()

### Community 205 - "debug_single_run.py"
Cohesion: 0.36
Nodes (4): get_elf_sym(), get_target_ds_addr(), main(), MEMORY_BASIC_INFORMATION

### Community 206 - "ExplosionDamage.h"
Cohesion: 0.83
Nodes (3): compute(), exposure(), lineClear()

### Community 207 - "Env"
Cohesion: 0.25
Nodes (8): Env, burningBox, cactus, fallLanded, headInWater, inLava, insideBlock, inWater

### Community 208 - "ctypes"
Cohesion: 0.10
Nodes (22): enum_child_proc(), inspect_desmume(), inspect(), MEMORY_BASIC_INFORMATION, simulate_old_printrow(), click_coords(), run_test(), capture_window() (+14 more)

### Community 209 - "ArrowHurtCtx"
Cohesion: 0.67
Nodes (3): ArrowHurtCtx, hs, player

### Community 210 - "Liquid.cpp"
Cohesion: 0.25
Nodes (3): isHell(), popDue(), pushTick()

### Community 211 - "Kind"
Cohesion: 0.25
Nodes (8): Kind, K_BACK, K_CANCEL, K_CHAR, K_CLEAR, K_OK, K_SHIFT, K_SPACE

### Community 212 - "bigTreeComputeBranches"
Cohesion: 0.13
Nodes (16): BigTreeBranch, trunkY, x, y, z, bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches() (+8 more)

### Community 213 - "bump"
Cohesion: 0.50
Nodes (3): BoatManager::riderEye(), bump(), eyeOf()

### Community 222 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

### Community 224 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 225 - "Climate.h"
Cohesion: 0.33
Nodes (4): biomeFor(), initIfSeedChanged(), Octaves, gen

### Community 227 - "GameState"
Cohesion: 0.29
Nodes (7): GameState, STATE_CREATE_WORLD, STATE_LOADING, STATE_MENU, STATE_OPTIONS, STATE_PLAYING, STATE_WORLD_SELECT

### Community 229 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 230 - "playClip"
Cohesion: 0.40
Nodes (4): 13. Audio, playClip(), Sound::note(), Sound::rain()

## Knowledge Gaps
- **1492 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1487 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2026 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **43 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `CMWorld`, `T`, `HandAnimations.cpp`, `Block and Item Types`, `PaintingManager.cpp`, `SheepManager Module`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `Drop`, `NetherGen.h`, `GameplayHotbar.cpp`, `BlockType.h`, `World`, `Inventory`, `Drop`, `Furnace.cpp`, `.hashInt`, `Drop`, `PartialBlocks.h`, `Sound.cpp`, `ChunkManager`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Drop`, `Redstone.cpp`, `ChunkManager Module`, `AnimalManager Module`, `M`, `Block and Item Types`, `Redstone Logic (Redstone)`, `isLiquidBlock`, `Block and Item Types`, `Block and Item Types`, `Falling`, `HostileManager Module`, `MinecartManager.cpp`, `Drop`, `isNormalCube`, `notify`, `NetherTerrain`, `Caves.cpp`, `FallingBlocks.cpp`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `Vehicle Entity (MinecartModel)`, `BoatManager.cpp`, `Chunk.cpp`, `CMWorld`, `Maps Module`, `DebugChests.h`, `SteveModel.cpp`, `NoteBlocks.cpp`, `Sound.h`, `Sim`, `CartWorld`, `BigTree`, `Liquid.cpp`, `.floodFillSkyLight`, `bigTreeComputeBranches`, `InventoryScreen.cpp`, `HostileManager Module`, `BlockFace`, `indirectProvidingPowerTo`, `VoxelColumnRLE`, `TntManager.cpp`, `ChunkManager.h`, `7. World engine in detail`, `BoatWorld`, `TickInput`, `World`, `RailLogic.h`, `stdlib`?**
  _High betweenness centrality (0.225) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1492 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Player Module` to `PartialBlocks.cpp`, `HandAnimations.cpp`, `Block and Item Types`, `Crafting Recipes`, `GameplayHotbar.cpp`, `BlockType.h`, `Inventory`, `Furnace.cpp`, `AsyncSaveManager`, `.hashInt`, `PartialBlocks.h`, `WorldSave Module`, `Catch`, `Pistons.cpp`, `Texture & PaintingTex`, `GameOverScreen.cpp`, `isLiquidBlock`, `Block and Item Types`, `DebugLogger`, `isNormalCube`, `LoadingScreen.cpp`, `computeSkyBrightness`, `NewWorldMenu.cpp`, `WorldSelectMenu Module`, `main.cpp`, `Sim`, `IpcChunkLoader`, `BigTree`, `InventoryScreen.cpp`, `SubScreenMenu.cpp`, `BlockFace`, `Hardware`, `TopScreenMenu & Renderer`, `TntManager.cpp`, `.sqrtf`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 88 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 88 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020844564240790654 - nodes in this community are weakly interconnected._