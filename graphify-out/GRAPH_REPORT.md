# Graph Report - YUANCRAFT NDS PORT  (2026-11-03)

## Corpus Check
- 249 files · ~357,229 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 55 file(s) not represented in the graph (top: .grit 49, (none) 4, .ini 1)

## Summary
- 4401 nodes · 9785 edges · 208 communities (172 shown, 36 thin omitted)
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
- stbi_uc
- ChunkManager Module
- AnimalManager Module
- rand
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
- MenuFont.cpp
- CMWorld
- Maps Module
- DebugChests.h
- nds
- NoteBlocks.cpp
- Minecraft: Nintendo DS Edition
- BigTree
- GameOverScreen.cpp
- CartWorld
- Options Module
- RaycastHit
- Biome & Chunk
- .floodFillSkyLight
- Caves Module
- Cube Module
- Hook
- HostileManager Module
- Projectiles Module
- Vehicle Entity (BoatModel)
- getDropType
- MobCull & Caves
- .update
- W
- TextKeyboard Module
- Hardware
- re
- Caves Module
- RailLogic.h
- SettingsMenu Module
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
- PNode
- Lakes Module
- 7. World engine in detail
- Projectiles Module
- Env
- build.sh
- FishingHook.cpp
- PauseScreen Module
- TickInput
- PendingDrops.h
- HostileManager Module
- World
- .computeColumnFacesBitwise
- Climate.h
- HostileManager Module
- sys
- stdlib
- CMWorld
- M
- MockAsyncSaveManager
- Clouds & CloudsData
- Catch
- Texture.h
- Dispenser.cpp
- Redstone Logic (Redstone)
- Redstone Logic (Redstone)
- SheepManager Module
- Entity AI (BoatAI)
- AnimalManager Module
- Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)
- HealthHudLayout Module
- Health.h
- FlatQuad
- StartupSplash Module
- PlayerHit
- Chunk.h
- Pose
- Chunk Module
- HostileManager Module
- Drop
- RenderInput
- Redstone Logic (Redstone)
- ModelBox.h
- Caves Module
- Redstone.cpp
- ColorMaps & ColorMapData
- Kind
- HostileManager Module
- Redstone Logic (Redstone)
- verify_simulation
- Cell
- JRandom
- explode
- Redstone Logic (Redstone)
- BlockFace
- SaveTask
- verify_occupancy_simulation.py
- MobCull.h
- State
- wireCompute
- Box
- verify_ui_logic_sim.py
- packSpot
- math
- test_print_row_safety.py
- NetherTerrain
- P
- ExplosionDamage.h
- Rng
- .reloadEntityTextures
- P3
- RedstoneEntityCtx
- Rng
- ctypes
- ArrowHurtCtx
- PlayerPos
- isLiquidBlock

## God Nodes (most connected - your core abstractions)
1. `BlockType` - 556 edges
2. `Chunk` - 212 edges
3. `main()` - 194 edges
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

## Communities (208 total, 36 thin omitted)

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
Nodes (72): anyIn(), blocking(), bodyBox(), Box, x0, x1, y0, y1 (+64 more)

### Community 4 - "Player Module"
Cohesion: 0.03
Nodes (60): dyeDamage(), getDamageVsEntity(), makeDispenserBlock(), main(), Player, AIR_ACCELERATION, AIR_FRICTION, bobPhase (+52 more)

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
Cohesion: 0.05
Nodes (37): findSpawn(), fireEncourage(), isFlowingLiquid(), isLavaBlock(), isMaterialSolid(), liquidMaterial(), isHell(), percentAir() (+29 more)

### Community 10 - "Chunk.cpp"
Cohesion: 0.06
Nodes (23): BigTreeBranch, trunkY, x, y, z, bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches() (+15 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.07
Nodes (43): alloc(), baseMotion(), brightnessOf(), move(), P, active, age, b (+35 more)

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
Cohesion: 0.16
Nodes (19): torchMeta(), applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad(), drawLodTopQuad(), emitCenteredCrossQuad(), emitCrossQuad() (+11 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.13
Nodes (21): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+13 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.08
Nodes (20): getToolMaxDurability(), ChestView, CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit() (+12 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.06
Nodes (31): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), fieldNoise() (+23 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.11
Nodes (10): GameplayHotbar, bgId, isInButtonRow(), drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), getItemsPixelIndex() (+2 more)

### Community 21 - "BlockType.h"
Cohesion: 0.10
Nodes (46): armorMaterial(), armorRenderIndex(), blockHardness(), canHarvestBlock(), fireCatch(), getBlockStrength(), getBlockTextures(), getGrassTint() (+38 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.05
Nodes (51): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 13. Audio, 14. Persistence, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is (+43 more)

### Community 23 - "Inventory"
Cohesion: 0.08
Nodes (43): 9.7 Inventory and crafting UI internals, armorMaxDurability(), armorPiece(), armorReduceAmount(), hasDurability(), isArmor(), maxStackFor(), ChestStore::transferWithInventory() (+35 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.06
Nodes (63): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), arrowTick(), attackBlocked(), attackEntity(), boxClear(), brightnessAt(), canSee(), canSpawnHere() (+55 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.09
Nodes (31): canSmelt(), ChunkManager, clearEntry(), clearSlot(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate(), Furnace::fuelBurnTime() (+23 more)

### Community 26 - "AsyncSaveManager"
Cohesion: 0.10
Nodes (13): AsyncSaveManager, MAX_BUFFER_SIZE, QUEUE_CAPACITY, s_allEnqueued, s_completedTasks, s_head, s_initialized, s_pendingCount (+5 more)

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "Spawners & Particles"
Cohesion: 0.09
Nodes (30): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+22 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.07
Nodes (30): 9.6 Audio internals (`Sound.cpp`), 9.8 More internals (Nether, sky, saves, menus, chests, notes), 9. Entities and physics notes, SD card layout, clearFolderContents(), folderExists(), WorldMetadata, armorDurability (+22 more)

### Community 31 - "string"
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
Nodes (26): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+18 more)

### Community 35 - "stbi_uc"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.10
Nodes (10): AnimalManager::attack(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath(), countKind(), halfCap() (+2 more)

### Community 38 - "rand"
Cohesion: 0.24
Nodes (11): isSapling(), rand, cropDrops(), ChunkManager, isLog(), markLeaf(), Trees::grow(), Trees::leafTick() (+3 more)

### Community 39 - "Block and Item Types"
Cohesion: 0.10
Nodes (7): 7.1c `tickLiquids` (20 Hz) and random ticks, isWaterBlock(), liquidFlowingOf(), liquidStillOf(), LiquidWorld, m, waterSpawnSpot()

### Community 40 - "RailLogic Module"
Cohesion: 0.18
Nodes (9): adjacentCount(), isRailAt(), Logic, c, n, powered, tx, ty (+1 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - "isNormalCube"
Cohesion: 0.09
Nodes (30): isNormalCube(), airSpawnSpot(), autoMeta(), boundsForMeta(), Box, x0, x1, y0 (+22 more)

### Community 43 - "Texture Module"
Cohesion: 0.07
Nodes (29): Texture, boatTextureID, cartTextureID, chickenTextureID, cowTextureID, creeperTextureID, ghastfireTextureID, ghastTextureID (+21 more)

### Community 44 - "Block and Item Types"
Cohesion: 0.15
Nodes (24): bodyBox(), Box, maxX, maxY, maxZ, minX, minY, minZ (+16 more)

### Community 45 - "Block and Item Types"
Cohesion: 0.09
Nodes (13): woolType(), collectDeath(), collideAll(), gatherBodies(), pushDrop(), SheepManager::attack(), SheepManager::interact(), SheepManager::lightning() (+5 more)

### Community 46 - "HostileManager Module"
Cohesion: 0.10
Nodes (3): HostileManager::interact(), HostileManager::popDrop(), rf01()

### Community 47 - "PartialBlocks.h"
Cohesion: 0.11
Nodes (25): isDoorBlock(), isPistonBlock(), isRedstoneComponent(), isRedstoneTorch(), isRepeaterBlock(), isSignBlock(), isStairsBlock(), bedCell() (+17 more)

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

### Community 54 - "M"
Cohesion: 0.25
Nodes (16): gettingPowered(), indirectlyGettingPowered(), indirectProvidingPowerTo(), isIndirectlyPoweringTo(), isPoweringTo(), M(), providingPowerTo(), randomTick() (+8 more)

### Community 55 - "LoadingScreen.cpp"
Cohesion: 0.20
Nodes (4): copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen, SubScreenMenu

### Community 56 - "notify"
Cohesion: 0.24
Nodes (18): activate(), blockChanged(), buttonRelease(), detectorCheck(), drainRemoved(), flushWireSet(), handleRemoved(), notify() (+10 more)

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

### Community 62 - "InventoryScreen.cpp"
Cohesion: 0.20
Nodes (9): drawCountAt(), drawDigit(), drawDurabilityBar(), drawSelectionBoxAt(), getItemsPixelIndex(), getSlotPosition(), getTerrainPixelIndex(), InventoryScreen (+1 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

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
Cohesion: 0.09
Nodes (8): 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, AnimItems::init(), AnimItems::tick(), setFrame(), buildMap()

### Community 68 - "main.cpp"
Cohesion: 0.10
Nodes (24): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, computeCelestialAngle(), computeNightFactor(), computeSkyBrightness(), computeSkylightSubtract() (+16 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.06
Nodes (31): BoatManager::attack(), BoatManager::dismount(), BoatManager::draw(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::riderEye(), BoatManager::saveToFile(), BoatManager::spawnFromRay() (+23 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "MenuFont.cpp"
Cohesion: 0.21
Nodes (11): find(), Glyph, c, rows, MenuFont::draw16(), MenuFont::draw8(), MenuFont::fill16(), MenuFont::fill8() (+3 more)

### Community 72 - "CMWorld"
Cohesion: 0.17
Nodes (7): AnimalManager::draw(), AnimalManager::explosionDamage(), CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 73 - "Maps Module"
Cohesion: 0.13
Nodes (22): find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush(), Maps::pixels() (+14 more)

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

### Community 80 - "CartWorld"
Cohesion: 0.15
Nodes (9): CartWorld, cacheChunk, cacheCx, cacheCz, cacheReady, MinecartManager::draw(), MinecartManager::spawn(), MinecartManager::tick() (+1 more)

### Community 81 - "Options Module"
Cohesion: 0.10
Nodes (20): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+12 more)

### Community 82 - "RaycastHit"
Cohesion: 0.15
Nodes (13): Chunk, ChunkManager, Raycaster, RaycastHit, blockXi, blockYi, blockZi, chunk (+5 more)

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

### Community 87 - "Hook"
Cohesion: 0.12
Nodes (17): Hook, active, hooked, inGround, mobIndex, mx, my, mz (+9 more)

### Community 88 - "HostileManager Module"
Cohesion: 0.18
Nodes (6): exposure(), HWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 89 - "Projectiles Module"
Cohesion: 0.22
Nodes (15): brightnessOf(), cellY(), chunkOf(), eggBreak(), gaussian(), nextFloat(), nextInt(), nextU() (+7 more)

### Community 90 - "Vehicle Entity (BoatModel)"
Cohesion: 0.11
Nodes (18): addBox(), BoatModel::draw(), BoatModel::init(), brightnessOf(), drawPart(), Part, pointX, pointY (+10 more)

### Community 91 - "getDropType"
Cohesion: 0.19
Nodes (12): furnaceFrontDir(), furnaceIsLit(), getDropType(), isFurnaceBlock(), isJackBlock(), isPumpkinBlock(), makeFurnaceBlock(), slabOfDouble() (+4 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.22
Nodes (9): State, lx, ly, lz, maxDist2, valid, x, y (+1 more)

### Community 93 - ".update"
Cohesion: 0.12
Nodes (8): getPatchAt(), terrainHeightCached(), terrainHeightFrom(), findLandChunkOffset(), hash2D(), Noise, randomGridValue(), smoothstep()

### Community 94 - "W"
Cohesion: 0.23
Nodes (6): 9.5 World-generation pieces, beginFrame(), freeOrLeaves(), genRound(), genSpruce(), W

### Community 95 - "TextKeyboard Module"
Cohesion: 0.23
Nodes (14): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+6 more)

### Community 98 - "Caves Module"
Cohesion: 0.13
Nodes (15): Tunnel, branchStep, isRoom, length, pitch, pitchVel, r, radiusScale (+7 more)

### Community 99 - "RailLogic.h"
Cohesion: 0.22
Nodes (9): 9.4 Minecarts, boats, TNT, chainEnd(), chainPowered(), hasPower(), Pos, x, y, z (+1 more)

### Community 100 - "SettingsMenu Module"
Cohesion: 0.27
Nodes (15): draw(), drawControls(), drawDebug(), drawPopUp(), getRowCount(), openControls(), openDebug(), printControlsRow() (+7 more)

### Community 101 - "JRandom"
Cohesion: 0.24
Nodes (6): advanceOrigin(), initTunnel(), JRandom, seed, pushTunnel(), reset()

### Community 102 - "MobBody & AnimalManager"
Cohesion: 0.18
Nodes (12): AnimalManager::collectBodies(), HostileManager::collectBodies(), collide(), MobBody, h, mx, mz, w (+4 more)

### Community 103 - "TopScreenMenu & Renderer"
Cohesion: 0.20
Nodes (4): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), Renderer, startPanorama(), TopScreenMenu

### Community 104 - "TntManager.cpp"
Cohesion: 0.10
Nodes (23): blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn(), Tnt, active (+15 more)

### Community 105 - "Simplex"
Cohesion: 0.18
Nodes (8): initIfSeedChanged(), Octaves, gen, Simplex, perm, xo, yo, zo

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
Cohesion: 0.18
Nodes (10): ChunkManager, Drop, durability, type, vx, vy, vz, x (+2 more)

### Community 113 - "Caves.h"
Cohesion: 0.13
Nodes (13): CarveCursor, cell, sphere, carveSphere(), carveStep(), floorF(), isDecoration(), Sphere (+5 more)

### Community 114 - "PNode"
Cohesion: 0.20
Nodes (10): PNode, closed, heapIndex, prev, toNext, total, toTarget, x (+2 more)

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.17
Nodes (9): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), 7.1b `ChunkManager::update` order (every main-loop iteration), 7.2 Memory model, 7.3 Generation pipeline (`Chunk::update`, spread across many frames), 7.4 Lighting, 7.5 Meshing and drawing, 7.6 Saving, 7. World engine in detail (+1 more)

### Community 117 - "Projectiles Module"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 118 - "Env"
Cohesion: 0.25
Nodes (8): Env, burningBox, cactus, fallLanded, headInWater, inLava, insideBlock, inWater

### Community 119 - "build.sh"
Cohesion: 0.40
Nodes (4): DEVKITARM, DEVKITPRO, PATH, build.sh script

### Community 120 - "FishingHook.cpp"
Cohesion: 0.23
Nodes (13): cellY(), FishingHook::cast(), FishingHook::clear(), FishingHook::draw(), gaussian(), handPos(), nextFloat(), nextInt() (+5 more)

### Community 121 - "PauseScreen Module"
Cohesion: 0.11
Nodes (11): ChunkManager, Button, BTN_BACK, BTN_CONTINUE, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE (+3 more)

### Community 122 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 123 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 125 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 126 - ".computeColumnFacesBitwise"
Cohesion: 0.27
Nodes (3): sameFaces(), shiftDown1(), shiftUp1()

### Community 127 - "Climate.h"
Cohesion: 0.24
Nodes (7): biomeFor(), Lattice, h, t, x0, z0, raw()

### Community 128 - "HostileManager Module"
Cohesion: 0.20
Nodes (9): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+1 more)

### Community 131 - "CMWorld"
Cohesion: 0.17
Nodes (7): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady, SheepManager::draw(), SheepManager::explosionDamage()

### Community 132 - "M"
Cohesion: 0.18
Nodes (13): anySideNormal(), canProvidePower(), cartTouchSink(), doorPower(), dropItem(), isPowerProviderOrWire(), neighborChanged(), neighborDo() (+5 more)

### Community 134 - "Clouds & CloudsData"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 135 - "Catch"
Cohesion: 0.17
Nodes (11): Catch, damage, fish, vx, vy, vz, x, y (+3 more)

### Community 136 - "Texture.h"
Cohesion: 0.18
Nodes (7): HealthHud::draw(), MenuBackground, texCoordCell(), Sky::draw(), uv(), v(), vert()

### Community 137 - "Dispenser.cpp"
Cohesion: 0.31
Nodes (5): dispenserFrontDir(), Dispenser::dispense(), Dispenser::popDrop(), gauss(), typeAtGrid()

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
Cohesion: 0.29
Nodes (7): build(), HudQuad, layer, u, v, x, y

### Community 147 - "Health.h"
Cohesion: 0.31
Nodes (8): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), hurtCameraRoll(), randomBit(), tick()

### Community 148 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 150 - "PlayerHit"
Cohesion: 0.22
Nodes (9): HostileManager::popPlayerHit(), PlayerHit, amount, explosion, kx, ky, kz, srcX (+1 more)

### Community 151 - "Chunk.h"
Cohesion: 0.08
Nodes (16): DisplayListBuilder, ChunkManager, Falling, active, fallTime, prevY, type, vy (+8 more)

### Community 152 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

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

### Community 160 - "ModelBox.h"
Cohesion: 0.24
Nodes (9): build(), Face, v, Vertex, u, v, x, y (+1 more)

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "Redstone.cpp"
Cohesion: 0.16
Nodes (13): blockRemoved(), bounds(), burnedOut(), chunkOf(), faceCode(), floorDivi(), freeCell(), indirectPowerAt() (+5 more)

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

### Community 171 - "explode"
Cohesion: 0.33
Nodes (7): 9.2 Managers: spawning, caps, explosions, collectDeath(), explode(), HostileManager::attack(), HostileManager::lightning(), pushDrop(), resistanceOf()

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 174 - "BlockFace"
Cohesion: 0.17
Nodes (14): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+6 more)

### Community 175 - "SaveTask"
Cohesion: 0.29
Nodes (6): SaveTask, data, dataSize, inUse, _pad, path

### Community 176 - "verify_occupancy_simulation.py"
Cohesion: 0.47
Nodes (3): isNormalCube_BUGGY(), isSolidGrid(), simulate_column()

### Community 177 - "MobCull.h"
Cohesion: 0.33
Nodes (3): state, set(), visible()

### Community 178 - "State"
Cohesion: 0.33
Nodes (6): State, detail, humidity, ready, seed, temperature

### Community 179 - "wireCompute"
Cohesion: 0.33
Nodes (5): addWirePos(), drainDeferred(), maxStrength(), Top, wireCompute()

### Community 180 - "Box"
Cohesion: 0.29
Nodes (7): Box, x0, x1, y0, y1, z0, z1

### Community 181 - "verify_ui_logic_sim.py"
Cohesion: 0.38
Nodes (3): MockOptions, test_ds_original_menu_logic(), test_dsi_profile_and_fps_target()

### Community 182 - "packSpot"
Cohesion: 0.50
Nodes (4): 12.7 Mob managers (how data, AI and model connect), chunkOf(), packSpot(), shouldDespawn()

### Community 183 - "math"
Cohesion: 0.20
Nodes (4): simulate_hw_divf(), simulate_hw_sqrtf(), test_math_accuracy(), test_frustum_sorting_math()

### Community 184 - "test_print_row_safety.py"
Cohesion: 1.00
Nodes (3): print_row_sim(), test_all_options(), visual_length()

### Community 187 - "P"
Cohesion: 0.50
Nodes (4): P, x, y, z

### Community 188 - "ExplosionDamage.h"
Cohesion: 0.83
Nodes (3): compute(), exposure(), lineClear()

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

### Community 212 - "isLiquidBlock"
Cohesion: 0.12
Nodes (13): isCrossPlant(), isLightOpaque(), isLiquidBlock(), isPartialBlock(), isTorchBlock(), cellOfIndex(), sideIndex(), callListFast() (+5 more)

## Knowledge Gaps
- **1462 isolated node(s):** `DEVKITPRO`, `DEVKITARM`, `PATH`, `s`, `x` (+1457 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1946 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **36 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `HostileManager Module`, `Chunk Meshing and Bands`, `PartialBlocks.cpp`, `stdlib`, `Player Module`, `M`, `CMWorld`, `HandAnimations.cpp`, `Dispenser.cpp`, `Sim`, `Chunk.cpp`, `Painting and Art Types`, `Block and Item Types`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `SheepManager Module`, `Crafting Recipes`, `NetherGen.h`, `BlockType.h`, `Sound.cpp`, `Inventory`, `Chunk.h`, `Furnace.cpp`, `Drop`, `.setBlockDirect`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Controls & ItemOrder`, `Redstone.cpp`, `ChunkManager Module`, `AnimalManager Module`, `rand`, `Block and Item Types`, `Redstone Logic (Redstone)`, `isNormalCube`, `explode`, `Block and Item Types`, `BlockFace`, `PartialBlocks.h`, `MinecartManager.cpp`, `M`, `notify`, `NetherTerrain`, `Vehicle Entity (MinecartModel)`, `BoatManager.cpp`, `CMWorld`, `Maps Module`, `DebugChests.h`, `nds`, `NoteBlocks.cpp`, `BigTree`, `CartWorld`, `isLiquidBlock`, `.floodFillSkyLight`, `HostileManager Module`, `getDropType`, `.update`, `W`, `RailLogic.h`, `TntManager.cpp`, `VoxelColumnRLE`, `Projectiles Module`, `Drop`, `Caves.h`, `7. World engine in detail`, `TickInput`, `PendingDrops.h`, `World`?**
  _High betweenness centrality (0.262) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DEVKITPRO`, `DEVKITARM`, `PATH` to the rest of the system?**
  _1462 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Player Module` to `PartialBlocks.cpp`, `Catch`, `Sim`, `Crafting Recipes`, `GameplayHotbar.cpp`, `BlockType.h`, `Inventory`, `AsyncSaveManager`, `WorldSave Module`, `Pistons.cpp`, `Texture & PaintingTex`, `rand`, `isNormalCube`, `BlockFace`, `PartialBlocks.h`, `LoadingScreen.cpp`, `NewWorldMenu.cpp`, `InventoryScreen.cpp`, `WorldSelectMenu Module`, `main.cpp`, `.reloadEntityTextures`, `GameOverScreen.cpp`, `isLiquidBlock`, `getDropType`, `.update`, `Hardware`, `TopScreenMenu & Renderer`, `.sqrtf`, `PendingDrops.h`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 88 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 88 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020941502249913466 - nodes in this community are weakly interconnected._