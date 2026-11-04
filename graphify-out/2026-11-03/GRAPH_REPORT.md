# Graph Report - YUANCRAFT NDS PORT  (2026-11-03)

## Corpus Check
- 244 files · ~352,600 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 55 file(s) not represented in the graph (top: .grit 49, (none) 4, .ini 1)

## Summary
- 4380 nodes · 9757 edges · 217 communities (184 shown, 33 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1127 edges (avg confidence: 0.86)
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
- stb_image.h
- AnimalManager Module
- isLeavesBlock
- Block and Item Types
- RailLogic Module
- Texture and Image Decoding
- Torch.h
- Texture Module
- Block and Item Types
- Block and Item Types
- HostileManager Module
- Recipe
- Vehicle Entity (MinecartManager)
- Projectiles Module
- SignManager Module
- Noise.cpp
- Profiler Module
- Profiler Module
- updateTick
- WorldMetadata
- notify
- NewWorldMenu.cpp
- Caves & CaveSinTable
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
- MenuFont.cpp
- CMWorld
- Maps Module
- DebugChests.h
- nds
- NoteBlocks.cpp
- Minecraft: Nintendo DS Edition
- BigTree
- GameOverScreen.cpp
- Teleporter.h
- Options Module
- BoatWorld
- Biome & Chunk
- .floodFillSkyLight
- Caves Module
- Cube Module
- Hook
- HostileManager Module
- Projectiles Module
- Vehicle Entity (BoatModel)
- ChunkManager
- MobCull & Caves
- .generateColumn
- Tnt
- TextKeyboard Module
- Hardware
- Caves Module
- Caves Module
- Vehicle Entity (MinecartManager)
- SettingsMenu Module
- bigTreeComputeBranches
- MobBody & AnimalManager
- TopScreenMenu & Renderer
- TntManager.cpp
- Climate Module
- VoxelColumnRLE
- Projectiles Module
- Part
- ChestStore.cpp
- .sqrtf
- SheepModel Module
- Drop
- Caves Module
- HostileModel.cpp
- Lakes Module
- 7. World engine in detail
- Projectiles Module
- nds
- build.sh
- FishingHook.cpp
- PauseScreen Module
- TickInput
- PendingDrops.h
- HostileManager Module
- World
- HotbarIcons.cpp
- Climate Module
- HostileManager Module
- .update
- stdlib
- CMWorld
- M
- MockAsyncSaveManager
- Clouds & CloudsData
- Catch
- Texture.h
- State
- Vehicle Entity (MinecartManager)
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Caves Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- HealthHudLayout Module
- Lakes Module
- FlatQuad
- StartupSplash Module
- SubScreenMenu Module
- Falling
- Pose
- Chunk Module
- HostileManager Module
- PNode
- RenderInput
- Redstone Logic (Redstone)
- BlockFace
- ModelBox.h
- Caves Module
- Redstone.cpp
- ColorMaps & ColorMapData
- Kind
- HostileManager Module
- Redstone Logic (Redstone)
- Raycaster.cpp
- 12. Rendering, textures and models
- Chunk.h
- Profiler.h
- Redstone Logic (Redstone)
- os
- RaycastHit
- Spike
- verify_occupancy_simulation.py
- Drop
- T
- Box
- Box
- verify_ui_logic_sim.py
- Quad
- math
- 9. Entities and physics notes
- NetherTerrain
- Quad
- P
- ExplosionDamage.h
- Quad
- Vtx
- Sky.cpp
- Rng
- RayHit
- bump
- P3
- RedstoneEntityCtx
- Rng
- ctypes
- ArrowHurtCtx
- PlayerPos
- packSpot
- Chest.h
- HostileModel::drawArrow

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 212 edges
3. `main()` - 193 edges
4. `ChunkManager` - 96 edges
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

## Communities (217 total, 33 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (86): BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor, CACHE_RECALC_BATCH (+78 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.22
Nodes (32): 9.3 Liquids, particles, partial blocks, activate(), boxHit(), chunkOf(), cropCanStay(), cropsTick(), dropAt(), dropCrop() (+24 more)

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

### Community 9 - "Sim"
Cohesion: 0.06
Nodes (24): fireCatch(), fireEncourage(), isFlowingLiquid(), isLavaBlock(), liquidMaterial(), liquidStillOf(), isHell(), percentAir() (+16 more)

### Community 10 - "Chunk.cpp"
Cohesion: 0.06
Nodes (14): callListFast(), chunkFloorDiv(), flushList(), oreFloorInt(), OreRng, s, oreVeinBlob(), packTexCoordCell() (+6 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.06
Nodes (44): getGrassTint(), alloc(), baseMotion(), brightnessOf(), move(), P, active, age (+36 more)

### Community 12 - "Painting and Art Types"
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
Cohesion: 0.11
Nodes (30): 7.5 Meshing and drawing, blockLightEmission(), furnaceIsLit(), getBlockTextures(), getDropType(), isDispenserBlock(), isFurnaceBlock(), isJackBlock() (+22 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.13
Nodes (21): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+13 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.09
Nodes (17): CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt(), drawPageIndicator() (+9 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.06
Nodes (31): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+23 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.24
Nodes (3): GameplayHotbar, bgId, isInButtonRow()

### Community 21 - "BlockType.h"
Cohesion: 0.07
Nodes (48): 8. Blocks and items, armorMaterial(), armorMaxDurability(), armorPiece(), armorReduceAmount(), armorRenderIndex(), blockHardness(), canHarvestBlock() (+40 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.06
Nodes (50): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 13. Audio, 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is (+42 more)

### Community 23 - "Inventory"
Cohesion: 0.13
Nodes (23): 9.7 Inventory and crafting UI internals, hasDurability(), isArmor(), isRecord(), maxStackFor(), ChestStore::transferWithInventory(), Furnace::transferWithInventory(), Inventory (+15 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.14
Nodes (32): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), airSpawnSpot(), arrowTick(), attackBlocked(), attackEntity(), brightnessAt(), canSee(), canSpawnHere() (+24 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.08
Nodes (35): furnaceFrontDir(), makeFurnaceBlock(), canSmelt(), ChunkManager, clearEntry(), clearSlot(), floorDivInt(), Furnace::clearAll() (+27 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.08
Nodes (18): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+10 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "Spawners & Particles"
Cohesion: 0.09
Nodes (30): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+22 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.10
Nodes (13): 9.8 More internals (Nether, sky, saves, menus, chests, notes), SD card layout, copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen, clearFolderContents(), folderExists(), WorldSave (+5 more)

### Community 30 - ".setBlockDirect"
Cohesion: 0.18
Nodes (6): isCrossPlant(), isSapling(), isTorchBlock(), torchFromMeta(), torchMeta(), lodSkipTop()

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

### Community 35 - "stb_image.h"
Cohesion: 0.06
Nodes (61): load_jpeg_image(), resample_row_1(), stbi__bitcount(), stbi__blinn_8x8(), stbi__clamp(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16() (+53 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.10
Nodes (11): AnimalManager::attack(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath(), countKind() (+3 more)

### Community 38 - "isLeavesBlock"
Cohesion: 0.21
Nodes (12): isLeavesBlock(), freeOrLeaves(), genRound(), genSpruce(), isLog(), markLeaf(), Trees::grow(), Trees::leafTick() (+4 more)

### Community 39 - "Block and Item Types"
Cohesion: 0.11
Nodes (5): isWaterBlock(), liquidFlowingOf(), LiquidWorld, m, waterSpawnSpot()

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.19
Nodes (23): stbi__addints_valid(), stbi__bitreverse16(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__extend_receive(), stbi__get_marker() (+15 more)

### Community 42 - "Torch.h"
Cohesion: 0.46
Nodes (7): autoMeta(), canPlaceAt(), floorSupport(), intermediate(), metaForPlacement(), mustDrop(), rayVsBox()

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.14
Nodes (25): isRailBlock(), bodyBox(), Box, maxX, maxY, maxZ, minX, minY (+17 more)

### Community 45 - "Block and Item Types"
Cohesion: 0.08
Nodes (15): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::draw(), SheepManager::explosionDamage() (+7 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.09
Nodes (11): 9.2 Managers: spawning, caps, explosions, collectDeath(), explode(), HostileManager::attack(), HostileManager::interact(), HostileManager::lightning(), HostileManager::popDrop(), pushDrop() (+3 more)

### Community 47 - "Recipe"
Cohesion: 0.13
Nodes (19): getToolMaxDurability(), canCraft(), countPatternCells(), doCraft(), Recipe, altA, altB, altC (+11 more)

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
Cohesion: 0.13
Nodes (10): Chunk::Chunk(), HeightCache, h, tx, tz, NetherColCache, c, tx (+2 more)

### Community 52 - "Profiler Module"
Cohesion: 0.17
Nodes (7): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike()

### Community 53 - "Profiler Module"
Cohesion: 0.13
Nodes (15): Slot, DL_CALL, DL_CULL, DL_LOD, DL_REBUILD, DRAW_ALL, ENTS, FACES (+7 more)

### Community 54 - "updateTick"
Cohesion: 0.52
Nodes (7): detectorCheck(), plateBox(), plateCheck(), repeaterTick(), schedule(), tick(), updateTick()

### Community 55 - "WorldMetadata"
Cohesion: 0.11
Nodes (18): WorldMetadata, armorDurability, armorType, formatVersion, gameTimeTicks, hotbarCount, hotbarDurability, hotbarType (+10 more)

### Community 56 - "notify"
Cohesion: 0.23
Nodes (15): activate(), blockChanged(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved(), neighborChanged() (+7 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves & CaveSinTable"
Cohesion: 0.19
Nodes (11): allocBlock(), carveSphere(), emit(), floorD(), floorF(), freeCellBlocks(), isDecoration(), jcos() (+3 more)

### Community 59 - "Health Module"
Cohesion: 0.07
Nodes (38): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), Env, burningBox, cactus, fallLanded (+30 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.17
Nodes (17): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::count(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn() (+9 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.18
Nodes (14): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+6 more)

### Community 62 - "InventoryScreen.cpp"
Cohesion: 0.21
Nodes (10): drawCountAt(), drawDigit(), drawDurabilityBar(), drawIconAt(), drawSelectionBoxAt(), getItemsPixelIndex(), getSlotPosition(), getTerrainPixelIndex() (+2 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.14
Nodes (23): stbi__addsizes_valid(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone(), stbi__do_png() (+15 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.18
Nodes (4): clearLabelZone(), drawWorldName(), rebuildWorldList(), WorldSelectMenu

### Community 65 - "AnimalAI.h"
Cohesion: 0.20
Nodes (28): anyIn(), blocking(), bodyBox(), calcX(), calcY(), calcZ(), cellBox(), cellY() (+20 more)

### Community 66 - "PathWork"
Cohesion: 0.19
Nodes (18): findPath(), heapAdd(), heapChange(), heapDequeue(), heapSortBack(), heapSortForward(), openPoint(), pathHash() (+10 more)

### Community 67 - "AnimItems.cpp"
Cohesion: 0.12
Nodes (3): AnimItems::init(), AnimItems::tick(), setFrame()

### Community 68 - "main.cpp"
Cohesion: 0.09
Nodes (24): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, computeCelestialAngle(), computeNightFactor(), computeSkyBrightness(), computeSkylightSubtract() (+16 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.14
Nodes (11): BoatManager::attack(), BoatManager::dismount(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::saveToFile(), breakBoat(), dismountIndex(), forceDismount() (+3 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.34
Nodes (15): stbi__bit_reverse(), stbi__compute_huffman_codes(), stbi__err(), stbi__fill_bits(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block(), stbi__parse_zlib(), stbi__parse_zlib_header() (+7 more)

### Community 71 - "MenuFont.cpp"
Cohesion: 0.21
Nodes (11): find(), Glyph, c, rows, MenuFont::draw16(), MenuFont::draw8(), MenuFont::fill16(), MenuFont::fill8() (+3 more)

### Community 72 - "CMWorld"
Cohesion: 0.18
Nodes (6): AnimalManager::draw(), CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 73 - "Maps Module"
Cohesion: 0.12
Nodes (23): ChunkManager, find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush() (+15 more)

### Community 74 - "DebugChests.h"
Cohesion: 0.17
Nodes (13): buildItemList(), findSite(), groundHeight(), isGivenItem(), isReplaceable(), isSkippable(), Site, alongX (+5 more)

### Community 75 - "nds"
Cohesion: 0.09
Nodes (26): addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b, g (+18 more)

### Community 76 - "NoteBlocks.cpp"
Cohesion: 0.12
Nodes (17): ChunkManager, Entry, gx, gy, gz, note, prev, used (+9 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (20): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+12 more)

### Community 78 - "BigTree"
Cohesion: 0.13
Nodes (13): BigTree, AX, basePos, branchSlope, height, heightAttenuation, heightLimit, heightLimitLimit (+5 more)

### Community 80 - "Teleporter.h"
Cohesion: 0.23
Nodes (12): Bounds, x0, x1, z0, z1, createPortal(), findPortal(), placeInPortal() (+4 more)

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "BoatWorld"
Cohesion: 0.18
Nodes (9): BoatManager::draw(), BoatManager::spawnFromRay(), BoatManager::tick(), BoatWorld, cacheChunk, cacheCx, cacheCz, cacheReady (+1 more)

### Community 83 - "Biome & Chunk"
Cohesion: 0.13
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

### Community 87 - "Hook"
Cohesion: 0.12
Nodes (17): Hook, active, hooked, inGround, mobIndex, mx, my, mz (+9 more)

### Community 88 - "HostileManager Module"
Cohesion: 0.17
Nodes (6): exposure(), HWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 89 - "Projectiles Module"
Cohesion: 0.22
Nodes (15): brightnessOf(), cellY(), chunkOf(), eggBreak(), gaussian(), nextFloat(), nextInt(), nextU() (+7 more)

### Community 90 - "Vehicle Entity (BoatModel)"
Cohesion: 0.17
Nodes (12): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+4 more)

### Community 91 - "ChunkManager"
Cohesion: 0.16
Nodes (8): isLightOpaque(), bigTreeCheckClearance(), bigTreeClearance(), bigTreeDrawLine(), bigTreeLeafLayerRadius(), bigTreePlaceLeafCluster(), bigTreePlaceSphereLayer(), fillDungeonChest()

### Community 92 - "MobCull & Caves"
Cohesion: 0.13
Nodes (12): state, set(), State, lx, ly, lz, maxDist2, valid (+4 more)

### Community 93 - ".generateColumn"
Cohesion: 0.14
Nodes (13): findSpawn(), isLiquidBlock(), isMaterialSolid(), getPatchAt(), hidesLiquidFace(), placementTargetFree(), boxClear(), findLandChunkOffset() (+5 more)

### Community 94 - "Tnt"
Cohesion: 0.15
Nodes (13): Tnt, active, fuse, mx, my, mz, onGround, prevX (+5 more)

### Community 95 - "TextKeyboard Module"
Cohesion: 0.23
Nodes (14): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+6 more)

### Community 97 - "Caves Module"
Cohesion: 0.18
Nodes (11): advanceOrigin(), cellRng(), initTunnel(), JRandom, seed, prepare(), probeOrigins(), pushTunnel() (+3 more)

### Community 98 - "Caves Module"
Cohesion: 0.13
Nodes (15): Tunnel, branchStep, isRoom, length, pitch, pitchVel, r, radiusScale (+7 more)

### Community 99 - "Vehicle Entity (MinecartManager)"
Cohesion: 0.17
Nodes (7): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn()

### Community 100 - "SettingsMenu Module"
Cohesion: 0.27
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 101 - "bigTreeComputeBranches"
Cohesion: 0.17
Nodes (11): BigTreeBranch, trunkY, x, y, z, bigTreeComputeBranches(), bigTreeEnvelope(), BigTreeRng (+3 more)

### Community 102 - "MobBody & AnimalManager"
Cohesion: 0.18
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.22
Nodes (3): Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.21
Nodes (11): rand, blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn(), TntManager::draw() (+3 more)

### Community 105 - "Climate Module"
Cohesion: 0.18
Nodes (8): initIfSeedChanged(), Octaves, gen, Simplex, perm, xo, yo, zo

### Community 106 - "VoxelColumnRLE"
Cohesion: 0.15
Nodes (7): RLERun, length, type, VoxelColumnRLE, MAX_RUNS, runCount, runs

### Community 107 - "Projectiles Module"
Cohesion: 0.18
Nodes (7): drawSprite(), Projectiles::draw(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 108 - "Part"
Cohesion: 0.24
Nodes (11): drawPartAt(), drawPartRot(), drawWolf(), emitQuads(), HostileModel::init(), make(), Part, pointX (+3 more)

### Community 109 - "ChestStore.cpp"
Cohesion: 0.10
Nodes (24): ChestData, gx, gy, gz, slot, used, ChestSlot, count (+16 more)

### Community 111 - "SheepModel Module"
Cohesion: 0.13
Nodes (17): addBox(), brightnessOf(), drawModel(), drawPart(), Part, pointX, pointY, pointZ (+9 more)

### Community 112 - "Drop"
Cohesion: 0.18
Nodes (10): ChunkManager, Drop, durability, type, vx, vy, vz, x (+2 more)

### Community 113 - "Caves Module"
Cohesion: 0.25
Nodes (6): Sphere, flat, r16, x8, y8, z8

### Community 114 - "HostileModel.cpp"
Cohesion: 0.28
Nodes (13): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawSpider() (+5 more)

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.22
Nodes (6): 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.6 Saving, 7. World engine in detail

### Community 117 - "Projectiles Module"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 118 - "nds"
Cohesion: 0.12
Nodes (28): 9.6 Audio internals (`Sound.cpp`), isDoorBlock(), isNormalCube(), isPartialBlock(), isPistonBlock(), isRedstoneComponent(), isRepeaterBlock(), isSignBlock() (+20 more)

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 120 - "FishingHook.cpp"
Cohesion: 0.23
Nodes (13): cellY(), FishingHook::cast(), FishingHook::clear(), FishingHook::draw(), gaussian(), handPos(), nextFloat(), nextInt() (+5 more)

### Community 121 - "PauseScreen Module"
Cohesion: 0.15
Nodes (9): Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched() (+1 more)

### Community 122 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 123 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 125 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 126 - "HotbarIcons.cpp"
Cohesion: 0.18
Nodes (10): ChestView, FurnaceData, drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon(), getItemsPixelIndex() (+2 more)

### Community 127 - "Climate Module"
Cohesion: 0.24
Nodes (7): biomeFor(), Lattice, h, t, x0, z0, raw()

### Community 128 - "HostileManager Module"
Cohesion: 0.11
Nodes (18): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+10 more)

### Community 129 - ".update"
Cohesion: 0.31
Nodes (3): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), cellInWindow(), ChunkManager::ChunkManager()

### Community 131 - "CMWorld"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 132 - "M"
Cohesion: 0.24
Nodes (14): burnedOut(), canProvidePower(), gettingPowered(), indirectProvidingPowerTo(), isIndirectlyPoweringTo(), isPoweringTo(), isPowerProviderOrWire(), M() (+6 more)

### Community 134 - "Clouds & CloudsData"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 135 - "Catch"
Cohesion: 0.17
Nodes (11): Catch, damage, fish, vx, vy, vz, x, y (+3 more)

### Community 136 - "Texture.h"
Cohesion: 0.28
Nodes (3): HealthHud::draw(), MenuBackground, texCoordCell()

### Community 137 - "State"
Cohesion: 0.33
Nodes (6): State, detail, humidity, ready, seed, temperature

### Community 138 - "Vehicle Entity (MinecartManager)"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

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

### Community 144 - "Caves Module"
Cohesion: 0.25
Nodes (8): Cell, count, cx, cz, first, lastUse, nblocks, pad

### Community 146 - "HealthHudLayout Module"
Cohesion: 0.29
Nodes (7): build(), HudQuad, layer, u, v, x, y

### Community 148 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 151 - "Falling"
Cohesion: 0.12
Nodes (15): ChunkManager, Falling, active, fallTime, prevY, type, vy, x (+7 more)

### Community 152 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 154 - "HostileManager Module"
Cohesion: 0.29
Nodes (7): SavedWolf, health, sitting, x, y, yaw, z

### Community 155 - "PNode"
Cohesion: 0.20
Nodes (10): PNode, closed, heapIndex, prev, toNext, total, toTarget, x (+2 more)

### Community 157 - "RenderInput"
Cohesion: 0.17
Nodes (10): ChunkManager, RenderInput, bodyLight, dimension, eyeLight, partialTicks, pitch, posX (+2 more)

### Community 158 - "Redstone Logic (Redstone)"
Cohesion: 0.29
Nodes (7): Tick, due, seq, t, x, y, z

### Community 159 - "BlockFace"
Cohesion: 0.20
Nodes (10): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+2 more)

### Community 160 - "ModelBox.h"
Cohesion: 0.24
Nodes (9): build(), Face, v, Vertex, u, v, x, y (+1 more)

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "Redstone.cpp"
Cohesion: 0.17
Nodes (14): blockRemoved(), bounds(), chunkOf(), faceCode(), floorDivi(), freeCell(), indirectPowerAt(), lightOre() (+6 more)

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

### Community 168 - "Raycaster.cpp"
Cohesion: 0.50
Nodes (4): cellPresent(), faceFromCode(), partialBoxHit(), torchBoxHit()

### Community 169 - "12. Rendering, textures and models"
Cohesion: 0.20
Nodes (7): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), 12.2 Texture loading (`Texture.h/.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 170 - "Chunk.h"
Cohesion: 0.13
Nodes (8): 7.3 Generation pipeline (`Chunk::update`, spread across many frames), dispenserFrontDir(), DisplayListBuilder, Dispenser::dispense(), Dispenser::popDrop(), gauss(), typeAtGrid(), genColsPerFrame()

### Community 171 - "Profiler.h"
Cohesion: 0.22
Nodes (6): ProfScope, slot, start, ProfStep, label, start

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 173 - "os"
Cohesion: 0.06
Nodes (4): print_row_sim(), test_all_options(), visual_length(), test_deadlock_and_hw_cache()

### Community 174 - "RaycastHit"
Cohesion: 0.15
Nodes (13): Chunk, ChunkManager, Raycaster, RaycastHit, blockXi, blockYi, blockZi, chunk (+5 more)

### Community 175 - "Spike"
Cohesion: 0.20
Nodes (10): Spike, dim, frame, label, part, stepMs10, total, x (+2 more)

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

### Community 177 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 178 - "T"
Cohesion: 0.20
Nodes (14): addWirePos(), anySideNormal(), cartTouchSink(), doorPower(), dropItem(), indirectlyGettingPowered(), maxStrength(), neighborDo() (+6 more)

### Community 179 - "Box"
Cohesion: 0.25
Nodes (8): boundsForMeta(), Box, x0, x1, y0, y1, z0, z1

### Community 180 - "Box"
Cohesion: 0.29
Nodes (7): Box, x0, x1, y0, y1, z0, z1

### Community 181 - "verify_ui_logic_sim.py"
Cohesion: 0.38
Nodes (3): MockOptions, test_ds_original_menu_logic(), test_dsi_profile_and_fps_target()

### Community 182 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 183 - "math"
Cohesion: 0.43
Nodes (4): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math()

### Community 184 - "9. Entities and physics notes"
Cohesion: 0.22
Nodes (8): 9.5 World-generation pieces, 9. Entities and physics notes, beginFrame(), CarveCursor, cell, sphere, carveStep(), floorDiv()

### Community 186 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 187 - "P"
Cohesion: 0.50
Nodes (4): P, x, y, z

### Community 188 - "ExplosionDamage.h"
Cohesion: 0.83
Nodes (3): compute(), exposure(), lineClear()

### Community 189 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 191 - "Vtx"
Cohesion: 0.29
Nodes (7): buildModel(), Vtx, u, v, x, y, z

### Community 200 - "Sky.cpp"
Cohesion: 0.53
Nodes (4): Sky::draw(), uv(), v(), vert()

### Community 202 - "RayHit"
Cohesion: 0.33
Nodes (6): RayHit, face, hit, x, y, z

### Community 204 - "bump"
Cohesion: 0.50
Nodes (3): BoatManager::riderEye(), bump(), eyeOf()

### Community 205 - "P3"
Cohesion: 0.50
Nodes (4): P3, x, y, z

### Community 206 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

### Community 209 - "ArrowHurtCtx"
Cohesion: 0.67
Nodes (3): ArrowHurtCtx, hs, player

### Community 210 - "PlayerPos"
Cohesion: 0.40
Nodes (5): PlayerPos, valid, x, y, z

### Community 211 - "packSpot"
Cohesion: 0.50
Nodes (4): 12.7 Mob managers (how data, AI and model connect), chunkOf(), packSpot(), shouldDespawn()

## Knowledge Gaps
- **1460 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1455 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1937 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `HostileManager Module`, `Chunk Meshing and Bands`, `stdlib`, `PartialBlocks.cpp`, `M`, `CMWorld`, `HandAnimations.cpp`, `Sim`, `Chunk.cpp`, `Block and Item Types`, `Vehicle Entity (MinecartManager)`, `Painting and Art Types`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `SheepManager Module`, `NetherGen.h`, `BlockType.h`, `Sound.cpp`, `Inventory`, `Falling`, `Furnace.cpp`, `.setBlockDirect`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Controls & ItemOrder`, `Redstone.cpp`, `ChunkManager Module`, `AnimalManager Module`, `isLeavesBlock`, `Block and Item Types`, `RailLogic Module`, `Raycaster.cpp`, `Chunk.h`, `Redstone Logic (Redstone)`, `Block and Item Types`, `Block and Item Types`, `HostileManager Module`, `Recipe`, `Vehicle Entity (MinecartManager)`, `Drop`, `T`, `updateTick`, `9. Entities and physics notes`, `NetherTerrain`, `Caves & CaveSinTable`, `notify`, `Vehicle Entity (MinecartModel)`, `InventoryScreen.cpp`, `BoatManager.cpp`, `CMWorld`, `Maps Module`, `DebugChests.h`, `nds`, `NoteBlocks.cpp`, `BigTree`, `BoatWorld`, `.floodFillSkyLight`, `HostileManager Module`, `ChunkManager`, `.generateColumn`, `Vehicle Entity (MinecartManager)`, `TntManager.cpp`, `VoxelColumnRLE`, `Projectiles Module`, `Drop`, `7. World engine in detail`, `nds`, `TickInput`, `PendingDrops.h`, `World`, `HotbarIcons.cpp`?**
  _High betweenness centrality (0.267) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1460 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Player Module` to `Catch`, `Block and Item Types`, `Crafting Recipes`, `GameplayHotbar.cpp`, `BlockType.h`, `SubScreenMenu Module`, `Inventory`, `Furnace.cpp`, `AsyncSaveManager`, `WorldSave Module`, `.setBlockDirect`, `BlockFace`, `Pistons.cpp`, `Texture & PaintingTex`, `isLeavesBlock`, `Raycaster.cpp`, `Block and Item Types`, `Recipe`, `NewWorldMenu.cpp`, `InventoryScreen.cpp`, `WorldSelectMenu Module`, `main.cpp`, `.reloadEntityTextures`, `GameOverScreen.cpp`, `.generateColumn`, `Hardware`, `TopScreenMenu & Renderer`, `TntManager.cpp`, `.sqrtf`, `nds`, `PendingDrops.h`, `HotbarIcons.cpp`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 88 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 88 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020941502249913466 - nodes in this community are weakly interconnected._