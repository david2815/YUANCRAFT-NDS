# Graph Report - YUANCRAFT NDS PORT  (2026-11-03)

## Corpus Check
- 209 files · ~335,219 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 53 file(s) not represented in the graph (top: .grit 49, (none) 3, .exe 1)

## Summary
- 4223 nodes · 9484 edges · 188 communities (170 shown, 18 thin omitted)
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
- main
- Entity AI (HostileAI)
- Furnace.cpp
- .updateFaceCache
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
- DroppedItem.cpp
- BoatManager.cpp
- Texture and Image Decoding
- PartialBlocks.h
- BoatWorld
- Maps Module
- Crafting Recipes
- nds
- NoteBlocks.cpp
- Minecraft: Nintendo DS Edition
- HostileModel.cpp
- CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)
- FishingHook.cpp
- Options Module
- WorldSave Module
- Biome & Chunk
- Block and Item Types
- Caves Module
- Cube Module
- Hook
- HostileManager Module
- Projectiles Module
- Vehicle Entity (BoatModel)
- TickInput
- MobCull & Caves
- bigTreeComputeBranches
- AnimItems.cpp
- TextKeyboard Module
- Player.cpp
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
- TntManager.cpp
- Caves Module
- PerlinNoise
- Lakes Module
- 7. World engine in detail
- Projectiles Module
- Lat
- World
- Kind
- PauseScreen Module
- Bolt
- 12. Rendering, textures and models
- HostileManager Module
- FallingBlocks.cpp
- FlatQuad
- Climate Module
- HostileManager Module
- .isDSi
- Drop
- LoadingScreen Module
- AnimalManager Module
- Catch
- Clouds & CloudsData
- Part
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
- 14. Persistence
- chunkOf
- Redstone Logic (Redstone)
- Sound.h
- RedstoneEntityCtx
- Caves Module
- Redstone.cpp
- ColorMaps & ColorMapData
- Kind
- HostileManager Module
- Redstone Logic (Redstone)
- ArrowHurtCtx
- WorldConfig.h
- W
- Weather::tick
- Quad
- Redstone Logic (Redstone)
- Quad
- Rng
- T
- Sky.cpp
- topOf
- Col
- bump
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

## Communities (188 total, 18 thin omitted)

### Community 0 - "Block and Item Types"
Cohesion: 0.01
Nodes (257): BlockType, AIR, APPLE, ARROW, BED_BLOCK, BED_ITEM, BEDROCK, BIRCH_LEAVES (+249 more)

### Community 1 - "Chunk Meshing and Bands"
Cohesion: 0.02
Nodes (87): 7.5 Meshing and drawing, BandFlags, v, Chunk, bandDirty, biomeColumn, blocks, borderRefreshCursor (+79 more)

### Community 2 - "PartialBlocks.cpp"
Cohesion: 0.22
Nodes (31): 9.3 Liquids, particles, partial blocks, doubleOfSlab(), chunkOf(), cropCanStay(), cropsTick(), dropAt(), dropCrop(), eatCake() (+23 more)

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

### Community 9 - "Block and Item Types"
Cohesion: 0.05
Nodes (37): fireEncourage(), isFlowingLiquid(), isLavaBlock(), isMaterialSolid(), liquidFlowingOf(), liquidMaterial(), liquidStillOf(), isHell() (+29 more)

### Community 10 - "Chunk.cpp"
Cohesion: 0.06
Nodes (11): chunkFloorDiv(), fillDungeonChest(), oreFloorInt(), OreRng, s, oreVeinBlob(), shiftDown1(), shiftUp1() (+3 more)

### Community 11 - "Block and Item Types"
Cohesion: 0.06
Nodes (44): getGrassTint(), alloc(), baseMotion(), brightnessOf(), move(), P, active, age (+36 more)

### Community 12 - "Painting and Art Types"
Cohesion: 0.05
Nodes (44): Art, ox, oy, sx, sy, title, brightnessOf(), ChunkManager (+36 more)

### Community 13 - "Weather.cpp"
Cohesion: 0.17
Nodes (6): ChunkManager, drawBolt(), drawPrecip(), hash2(), quad4(), Weather::draw()

### Community 14 - "Dropped Item Physics"
Cohesion: 0.04
Nodes (42): DroppedItem, active, ageTicks, BOB_MAX, BOB_MIN, BOB_SPEED, bobPhase, count (+34 more)

### Community 15 - "ChunkManager Module"
Cohesion: 0.04
Nodes (42): ChunkManager, awaitingLoad, borderRefreshPending, CAP_CHUNKS, centerIndex, chunkPosX, chunkPosZ, chunks (+34 more)

### Community 16 - "Block and Item Types"
Cohesion: 0.13
Nodes (23): furnaceIsLit(), getBlockTextures(), isPumpkinBlock(), woolCell(), applyLight(), brighterRaw(), drawCenteredCrossQuad(), drawCrossQuad() (+15 more)

### Community 17 - "AnimalModel.cpp"
Cohesion: 0.19
Nodes (15): AnimalModel::draw(), AnimalModel::init(), brightnessOf(), drawChicken(), drawCow(), drawFlat(), drawPart(), drawPig() (+7 more)

### Community 18 - "Crafting Recipes"
Cohesion: 0.09
Nodes (19): iconShapeVisible(), CraftingScreen, bgId, visibleCount, visibleRecipeIndices, drawCountAt(), drawDigit(), drawDurabilityBarAt() (+11 more)

### Community 19 - "NetherGen.h"
Cohesion: 0.12
Nodes (15): baseType(), Col, ceilBottom, floorTop, pillar, surface, computeColumn(), firePatch() (+7 more)

### Community 20 - "GameplayHotbar.cpp"
Cohesion: 0.25
Nodes (3): GameplayHotbar, bgId, isInButtonRow()

### Community 21 - "Block and Item Types"
Cohesion: 0.08
Nodes (48): 8. Blocks and items, armorMaterial(), armorMaxDurability(), armorPiece(), armorReduceAmount(), armorRenderIndex(), blockHardness(), canHarvestBlock() (+40 more)

### Community 22 - "Sound.cpp"
Cohesion: 0.14
Nodes (24): 13. Audio, at(), cellToWorld(), digBase(), mobClip(), pick(), playClip(), raw() (+16 more)

### Community 23 - "main"
Cohesion: 0.07
Nodes (47): 4.1 Entry point and states (`main.cpp`, ~3300 lines), 4.2 Timing, 4.3 Profiler and debug screen (`Profiler.h/.cpp`), 4. Runtime architecture, 9.7 Inventory and crafting UI internals, getToolMaxDurability(), hasDurability(), isArmor() (+39 more)

### Community 24 - "Entity AI (HostileAI)"
Cohesion: 0.14
Nodes (32): 9.1 AI headers (`SheepAI.h`, `AnimalAI.h`, `HostileAI.h`), arrowTick(), attackBlocked(), attackEntity(), boxClear(), brightnessAt(), canSee(), canSpawnHere() (+24 more)

### Community 25 - "Furnace.cpp"
Cohesion: 0.08
Nodes (33): furnaceFrontDir(), canSmelt(), clearEntry(), clearSlot(), floorDivInt(), Furnace::clearAll(), Furnace::find(), Furnace::findOrCreate() (+25 more)

### Community 26 - ".updateFaceCache"
Cohesion: 0.21
Nodes (6): getPatchAt(), findLandChunkOffset(), hash2D(), Noise, randomGridValue(), smoothstep()

### Community 27 - "DisplayListBuilder Module"
Cohesion: 0.13
Nodes (11): DisplayListBuilder, capacity, cmdCount, cmdQueue, DisplayListBuilder::DisplayListBuilder(), out, overflow, paramCount (+3 more)

### Community 28 - "Spawners & Particles"
Cohesion: 0.17
Nodes (18): chunkAt(), ChunkManager, cx(), cy(), cz(), Entry, delay, gx (+10 more)

### Community 29 - "WorldSave Module"
Cohesion: 0.13
Nodes (11): 9.8 More internals (Nether, sky, saves, menus, chests, notes), Weather::load(), Weather::save(), clearFolderContents(), folderExists(), WorldSave, s_activeBasePath, s_activeWorldNum (+3 more)

### Community 30 - "ChunkManager"
Cohesion: 0.16
Nodes (6): isLightOpaque(), isLiquidBlock(), isWaterBlock(), torchFromMeta(), hidesLiquidFace(), placementTargetFree()

### Community 31 - "string"
Cohesion: 0.17
Nodes (4): draw(), OptionsMenu::open(), OptionsMenu::update(), printRow()

### Community 32 - "Pistons.cpp"
Cohesion: 0.07
Nodes (64): 5.2 Blocks, items, inventory, crafting, isPistonBase(), addMoving(), baseAdded(), baseNeighborChanged(), bounds(), box(), canExtend() (+56 more)

### Community 33 - "Texture & PaintingTex"
Cohesion: 0.07
Nodes (3): loadHostile(), loadSignFont(), loadSky16()

### Community 34 - "Controls & ItemOrder"
Cohesion: 0.06
Nodes (39): Action, BACK, BREAK, COUNT, FORWARD, JUMP, LOOK_DOWN, LOOK_LEFT (+31 more)

### Community 35 - "Texture and Image Decoding"
Cohesion: 0.10
Nodes (29): load_jpeg_image(), resample_row_1(), stbi__blinn_8x8(), stbi__cleanup_jpeg(), stbi__compute_y(), stbi__compute_y_16(), stbi__convert_16_to_8(), stbi__convert_8_to_16() (+21 more)

### Community 37 - "AnimalManager Module"
Cohesion: 0.09
Nodes (12): AnimalManager::attack(), AnimalManager::draw(), AnimalManager::explosionDamage(), AnimalManager::lightning(), AnimalManager::popDrop(), AnimalManager::spawnChicken(), AnimalManager::tick(), collectDeath() (+4 more)

### Community 38 - "isTorchBlock"
Cohesion: 0.21
Nodes (9): blockLightEmission(), getDropType(), isCrossPlant(), isJackBlock(), isTorchBlock(), torchMeta(), callListFast(), flushList() (+1 more)

### Community 40 - "RailLogic Module"
Cohesion: 0.12
Nodes (18): 9.4 Minecarts, boats, TNT, adjacentCount(), chainEnd(), chainPowered(), hasPower(), isRailAt(), Logic, c (+10 more)

### Community 41 - "Texture and Image Decoding"
Cohesion: 0.18
Nodes (28): stbi__addints_valid(), stbi__build_fast_ac(), stbi__build_huffman(), stbi__cpuid3(), stbi__decode_jpeg_header(), stbi__decode_jpeg_image(), stbi__err(), stbi__extend_receive() (+20 more)

### Community 42 - "Container Logic (ChestStore)"
Cohesion: 0.09
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
Cohesion: 0.09
Nodes (31): isNormalCube(), airSpawnSpot(), waterSpawnSpot(), autoMeta(), boundsForMeta(), Box, x0, x1 (+23 more)

### Community 48 - "Vehicle Entity (MinecartManager)"
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
Cohesion: 0.18
Nodes (7): ms10(), Prof::add(), Prof::endFrame(), Prof::now(), Prof::print(), Prof::step(), recordSpike()

### Community 53 - "Profiler Module"
Cohesion: 0.13
Nodes (15): Slot, DL_CALL, DL_CULL, DL_LOD, DL_REBUILD, DRAW_ALL, ENTS, FACES (+7 more)

### Community 54 - "M"
Cohesion: 0.26
Nodes (16): isPlateBlock(), detectorCheck(), faceCode(), freeCell(), M(), plateBox(), plateCheck(), randomTick() (+8 more)

### Community 55 - "InventoryScreen.cpp"
Cohesion: 0.07
Nodes (21): ChestView, FurnaceData, ChunkManager, drawDigit(), drawDurabilityBar(), drawSelectionBox(), drawSlotCount(), drawSlotIcon() (+13 more)

### Community 56 - "notify"
Cohesion: 0.20
Nodes (16): activate(), blockChanged(), blockRemoved(), buttonRelease(), drainDeferred(), drainRemoved(), flushWireSet(), handleRemoved() (+8 more)

### Community 57 - "NewWorldMenu.cpp"
Cohesion: 0.15
Nodes (10): drawField(), nearestIndex(), NewWorldMenu, MAX_NAME_LEN, MAX_SEED_DIGITS, Result, RES_CANCEL, RES_CREATE (+2 more)

### Community 58 - "Caves & CaveSinTable"
Cohesion: 0.18
Nodes (14): allocBlock(), cellRng(), emit(), floorD(), floorDiv(), freeCellBlocks(), jcos(), jsin() (+6 more)

### Community 59 - "Health Module"
Cohesion: 0.09
Nodes (30): applyArmor(), attack(), deathCameraRoll(), deathFovFactor(), heal(), HealthState, air, armorPoints (+22 more)

### Community 60 - "HostileManager Module"
Cohesion: 0.17
Nodes (17): addMob(), categoryCount(), countAlive(), halfCap(), HostileManager::count(), HostileManager::draw(), HostileManager::sleepSpawn(), HostileManager::spawnerSpawn() (+9 more)

### Community 61 - "Vehicle Entity (MinecartModel)"
Cohesion: 0.12
Nodes (20): addBox(), brightnessOf(), cubeFace(), drawBlock(), drawPart(), MinecartModel::draw(), MinecartModel::init(), Part (+12 more)

### Community 62 - "isLeavesBlock"
Cohesion: 0.18
Nodes (16): 9.5 World-generation pieces, 9. Entities and physics notes, isLeavesBlock(), isSapling(), beginFrame(), ChunkManager, freeOrLeaves(), genRound() (+8 more)

### Community 63 - "Texture and Image Decoding"
Cohesion: 0.16
Nodes (20): stbi__addsizes_valid(), stbi__check_png_header(), stbi__compute_transparency(), stbi__compute_transparency16(), stbi__create_png_alpha_expand8(), stbi__create_png_image(), stbi__create_png_image_raw(), stbi__de_iphone() (+12 more)

### Community 64 - "WorldSelectMenu Module"
Cohesion: 0.15
Nodes (4): clearLabelZone(), drawWorldName(), rebuildWorldList(), WorldSelectMenu

### Community 65 - "AnimalAI.h"
Cohesion: 0.06
Nodes (75): 12.7 Mob managers (how data, AI and model connect), anyIn(), blocking(), bodyBox(), Box, x0, x1, y0 (+67 more)

### Community 66 - "BigTree"
Cohesion: 0.13
Nodes (13): BigTree, AX, basePos, branchSlope, height, heightAttenuation, heightLimit, heightLimitLimit (+5 more)

### Community 67 - "Chunk.h"
Cohesion: 0.08
Nodes (28): BlockFace, BOTTOM, EAST, NONE, NORTH, SOUTH, TOP, WEST (+20 more)

### Community 69 - "BoatManager.cpp"
Cohesion: 0.14
Nodes (11): BoatManager::attack(), BoatManager::dismount(), BoatManager::loadFromFile(), BoatManager::popDrop(), BoatManager::saveToFile(), breakBoat(), dismountIndex(), forceDismount() (+3 more)

### Community 70 - "Texture and Image Decoding"
Cohesion: 0.26
Nodes (17): stbi__bit_reverse(), stbi__bitreverse16(), stbi__clamp(), stbi__compute_huffman_codes(), stbi__fill_bits(), stbi__idct_block(), stbi__parse_huffman_block(), stbi__parse_uncompressed_block() (+9 more)

### Community 71 - "PartialBlocks.h"
Cohesion: 0.12
Nodes (29): 9.6 Audio internals (`Sound.cpp`), isDoorBlock(), isPartialBlock(), isPistonBlock(), isRedstoneComponent(), isRepeaterBlock(), isSignBlock(), isStairsBlock() (+21 more)

### Community 72 - "BoatWorld"
Cohesion: 0.18
Nodes (9): BoatManager::draw(), BoatManager::spawnFromRay(), BoatManager::tick(), BoatWorld, cacheChunk, cacheCx, cacheCz, cacheReady (+1 more)

### Community 73 - "Maps Module"
Cohesion: 0.12
Nodes (23): ChunkManager, find(), freeSlot(), load(), mapColorOf(), Maps::colorOf(), Maps::create(), Maps::flush() (+15 more)

### Community 74 - "Crafting Recipes"
Cohesion: 0.14
Nodes (20): canCraft(), countMatchingIngredient(), countPatternCells(), doCraft(), ingredientMatches(), Recipe, altA, altB (+12 more)

### Community 75 - "nds"
Cohesion: 0.13
Nodes (15): ChunkManager, addBox(), brightnessOf(), buildFlat(), drawFlatPart(), drawPart(), Flat, b (+7 more)

### Community 76 - "NoteBlocks.cpp"
Cohesion: 0.12
Nodes (17): ChunkManager, Entry, gx, gy, gz, note, prev, used (+9 more)

### Community 77 - "Minecraft: Nintendo DS Edition"
Cohesion: 0.10
Nodes (19): About, Building, Contributing, Controls, Credits, Eaglercraft Beta 1.7.3 — Nintendo DS Port, Features, Installing and running (+11 more)

### Community 78 - "HostileModel.cpp"
Cohesion: 0.08
Nodes (40): brightnessOf(), drawBiped(), drawBody(), drawCreeper(), drawFireOverlay(), drawGhast(), drawPart(), drawPartAt() (+32 more)

### Community 79 - "CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)"
Cohesion: 0.09
Nodes (17): 10. UI and screen programming, 11. Performance playbook (lessons learned — follow them), 15. Recipes for common tasks, 16. Known differences from Beta 1.7.3 (deliberate), 17. Debugging checklist, 18. Credits and license, 1. What this project is, 2. Rules for an AI assistant modifying this project (read carefully) (+9 more)

### Community 80 - "FishingHook.cpp"
Cohesion: 0.23
Nodes (13): cellY(), FishingHook::cast(), FishingHook::clear(), FishingHook::draw(), gaussian(), handPos(), nextFloat(), nextInt() (+5 more)

### Community 81 - "Options Module"
Cohesion: 0.11
Nodes (19): Data, autoJump, chunkMode, clockCompassInvUpdate, controlMode, customSeed, customSeedSet, debugCoordsOnly (+11 more)

### Community 82 - "WorldSave Module"
Cohesion: 0.11
Nodes (18): WorldMetadata, armorDurability, armorType, formatVersion, gameTimeTicks, hotbarCount, hotbarDurability, hotbarType (+10 more)

### Community 83 - "Biome & Chunk"
Cohesion: 0.13
Nodes (15): BiomeType, DESERT, FOREST, GENERIC, OCEAN, PLAINS, RAINFOREST, SAVANNA (+7 more)

### Community 84 - "Block and Item Types"
Cohesion: 0.23
Nodes (6): lightDim(), LightNode, bx, by, bz, level

### Community 85 - "Caves Module"
Cohesion: 0.12
Nodes (17): Job, active, cx, cz, fill, nOrigins, originIdx, ox (+9 more)

### Community 86 - "Cube Module"
Cohesion: 0.16
Nodes (11): sameFaces(), Cube, drawBox(), FaceMask, bottom, east, north, south (+3 more)

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

### Community 91 - "TickInput"
Cohesion: 0.13
Nodes (16): clickAttack(), HandAnimations::tick(), swingItem(), TickInput, attackHeld, heldDurability, heldSlot, heldType (+8 more)

### Community 92 - "MobCull & Caves"
Cohesion: 0.13
Nodes (12): state, set(), State, lx, ly, lz, maxDist2, valid (+4 more)

### Community 93 - "bigTreeComputeBranches"
Cohesion: 0.12
Nodes (17): BigTreeBranch, trunkY, x, y, z, bigTreeCheckClearance(), bigTreeClearance(), bigTreeComputeBranches() (+9 more)

### Community 94 - "AnimItems.cpp"
Cohesion: 0.20
Nodes (3): AnimItems::init(), AnimItems::tick(), setFrame()

### Community 95 - "TextKeyboard Module"
Cohesion: 0.23
Nodes (14): addKey(), build(), drawAll(), drawKey(), drawText(), finish(), Key, ch (+6 more)

### Community 97 - "Caves Module"
Cohesion: 0.24
Nodes (6): advanceOrigin(), initTunnel(), JRandom, seed, pushTunnel(), reset()

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
Cohesion: 0.21
Nodes (11): rand, blocked(), brightnessOf(), ChunkManager, drawCube(), moveAxis(), spawn(), TntManager::draw() (+3 more)

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

### Community 112 - "TntManager.cpp"
Cohesion: 0.15
Nodes (13): Tnt, active, fuse, mx, my, mz, onGround, prevX (+5 more)

### Community 113 - "Caves Module"
Cohesion: 0.13
Nodes (13): CarveCursor, cell, sphere, carveSphere(), carveStep(), floorF(), isDecoration(), Sphere (+5 more)

### Community 114 - "PerlinNoise"
Cohesion: 0.28
Nodes (5): fieldNoise(), PerlinNoise, initialized, OCTAVE_COUNT, permutations

### Community 115 - "Lakes Module"
Cohesion: 0.26
Nodes (11): apply(), build(), cellIndex(), isShell(), Result, lake, stone, valid (+3 more)

### Community 116 - "7. World engine in detail"
Cohesion: 0.20
Nodes (7): 7.1 Chunk modes (`Options::chunkMode`, `WorldConfig`), 7.1b `ChunkManager::update` order (every main-loop iteration), 7.1c `tickLiquids` (20 Hz) and random ticks, 7.2 Memory model, 7.4 Lighting, 7.6 Saving, 7. World engine in detail

### Community 117 - "Projectiles Module"
Cohesion: 0.18
Nodes (11): ChunkManager, Kind, ARROW, EGG, SNOWBALL, PlayerHurtFn, PlayerTarget, box (+3 more)

### Community 118 - "Lat"
Cohesion: 0.18
Nodes (11): Lat, a, b, n1, n2, n3, LatCache, ready (+3 more)

### Community 119 - "World"
Cohesion: 0.19
Nodes (6): FishingHook::tick(), World, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 120 - "Kind"
Cohesion: 0.15
Nodes (12): ChunkManager, Kind, BUBBLE, DIG, EXPLODE, FLAME, HEART, LAVA (+4 more)

### Community 121 - "PauseScreen Module"
Cohesion: 0.20
Nodes (7): Button, BTN_BACK, BTN_NONE, BTN_OPTIONS, BTN_QUIT, BTN_SAVE, PauseScreen::touched()

### Community 122 - "Bolt"
Cohesion: 0.15
Nodes (13): Bolt, active, flashes, gx, gy, gz, life, seed (+5 more)

### Community 123 - "12. Rendering, textures and models"
Cohesion: 0.20
Nodes (7): 12.1 Projection, fog, VRAM banks (`Renderer.cpp`), 12.2 Texture loading (`Texture.h/.cpp`), 12.3 Texture coordinates, 12.4 Texture animation (`TextureAnim.*`, `AnimItems.*`), 12.5 Graphics conversion (`graphics/*.grit`, Makefile), 12. Rendering, textures and models, buildMap()

### Community 125 - "FallingBlocks.cpp"
Cohesion: 0.22
Nodes (6): ChunkManager, FallingBlocks::draw(), FallingBlocks::spawn(), FallingBlocks::update(), placeable(), texCoordCell()

### Community 126 - "FlatQuad"
Cohesion: 0.17
Nodes (11): FlatQuad, face, x, y, z, Quad, px, py (+3 more)

### Community 127 - "Climate Module"
Cohesion: 0.24
Nodes (7): biomeFor(), Lattice, h, t, x0, z0, raw()

### Community 128 - "HostileManager Module"
Cohesion: 0.11
Nodes (18): ChunkManager, Drop, count, type, x, y, z, ExplosionListener (+10 more)

### Community 130 - "Drop"
Cohesion: 0.11
Nodes (15): dispenserFrontDir(), ChunkManager, Dispenser::dispense(), Dispenser::popDrop(), Drop, durability, type, vx (+7 more)

### Community 131 - "LoadingScreen Module"
Cohesion: 0.43
Nodes (3): copyBitmapAndForceOpaque(), decompressTopOpaque(), LoadingScreen

### Community 132 - "AnimalManager Module"
Cohesion: 0.22
Nodes (5): CMWorld, cacheChunk, cacheCx, cacheCz, cacheReady

### Community 133 - "Catch"
Cohesion: 0.17
Nodes (11): Catch, damage, fish, vx, vy, vz, x, y (+3 more)

### Community 134 - "Clouds & CloudsData"
Cohesion: 0.31
Nodes (4): cloudAt(), Clouds::draw(), quad(), shade()

### Community 135 - "Part"
Cohesion: 0.17
Nodes (12): Part, faceMask, pointX, pointY, pointZ, px, py, pz (+4 more)

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

### Community 145 - "PendingDrops.h"
Cohesion: 0.24
Nodes (8): PendingDrop, type, x, y, z, PendingDrops, count, queue

### Community 146 - "HealthHudLayout Module"
Cohesion: 0.29
Nodes (7): build(), HudQuad, layer, u, v, x, y

### Community 148 - "RenderInput"
Cohesion: 0.20
Nodes (9): RenderInput, bodyLight, dimension, eyeLight, partialTicks, pitch, posX, posZ (+1 more)

### Community 151 - "Falling"
Cohesion: 0.22
Nodes (9): Falling, active, fallTime, prevY, type, vy, x, y (+1 more)

### Community 152 - "Pose"
Cohesion: 0.33
Nodes (6): Pose, pitchDeg, x, y, yawDeg, z

### Community 154 - "HostileManager Module"
Cohesion: 0.29
Nodes (7): SavedWolf, health, sitting, x, y, yaw, z

### Community 155 - "Drop"
Cohesion: 0.22
Nodes (8): ChunkManager, Drop, count, durability, type, x, y, z

### Community 156 - "14. Persistence"
Cohesion: 0.50
Nodes (4): 14. Persistence, `options.dat` layout (23 bytes; older files are shorter and missing fields keep defaults), SD card layout, Settings UI map (`SettingsMenu.cpp`)

### Community 157 - "chunkOf"
Cohesion: 0.29
Nodes (6): chunkOf(), floorDivi(), lightOre(), put(), removeBlock(), setTM()

### Community 158 - "Redstone Logic (Redstone)"
Cohesion: 0.29
Nodes (7): Tick, due, seq, t, x, y, z

### Community 159 - "Sound.h"
Cohesion: 0.22
Nodes (8): Group, G_GRASS, G_GRAVEL, G_SAND, G_SNOW, G_STONE, G_WOOD, Sound::groupOf()

### Community 160 - "RedstoneEntityCtx"
Cohesion: 0.50
Nodes (4): RedstoneEntityCtx, itemCount, items, player

### Community 161 - "Caves Module"
Cohesion: 0.33
Nodes (6): CellState, EMPTY, PENDING, READY, SIMULATING, UNKNOWN

### Community 162 - "Redstone.cpp"
Cohesion: 0.19
Nodes (15): bounds(), burnedOut(), canProvidePower(), dropItem(), gettingPowered(), indirectlyGettingPowered(), indirectPowerAt(), indirectProvidingPowerTo() (+7 more)

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

### Community 167 - "ArrowHurtCtx"
Cohesion: 0.67
Nodes (3): ArrowHurtCtx, hs, player

### Community 170 - "Weather::tick"
Cohesion: 0.46
Nodes (7): fireAt(), nextInt(), rnd(), spawnBolt(), tickBolt(), updateWeather(), Weather::tick()

### Community 171 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 172 - "Redstone Logic (Redstone)"
Cohesion: 0.40
Nodes (5): Burn, time, x, y, z

### Community 174 - "Quad"
Cohesion: 0.29
Nodes (6): Quad, px, py, pz, tu, tv

### Community 178 - "T"
Cohesion: 0.24
Nodes (12): addWirePos(), anySideNormal(), cartTouchSink(), doorPower(), maxStrength(), neighborChanged(), neighborDo(), normal() (+4 more)

### Community 179 - "Sky.cpp"
Cohesion: 0.53
Nodes (4): Sky::draw(), uv(), v(), vert()

### Community 180 - "topOf"
Cohesion: 0.60
Nodes (5): chunkAtGrid(), kindOf(), refresh(), topOf(), Weather::canRainAtGrid()

### Community 181 - "Col"
Cohesion: 0.33
Nodes (6): Col, gx, gz, kind, top, valid

### Community 182 - "bump"
Cohesion: 0.50
Nodes (3): BoatManager::riderEye(), bump(), eyeOf()

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
- **1439 isolated node(s):** `s`, `x`, `y`, `z`, `valid` (+1434 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1865 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BlockType` connect `Block and Item Types` to `HostileManager Module`, `Chunk Meshing and Bands`, `Drop`, `PartialBlocks.cpp`, `AnimalManager Module`, `HandAnimations.cpp`, `Block and Item Types`, `Chunk.cpp`, `Block and Item Types`, `Vehicle Entity (MinecartManager)`, `Painting and Art Types`, `Dropped Item Physics`, `AnimalManager Module`, `Block and Item Types`, `PendingDrops.h`, `Crafting Recipes`, `NetherGen.h`, `SheepManager Module`, `Block and Item Types`, `Sound.cpp`, `main`, `Falling`, `Furnace.cpp`, `.updateFaceCache`, `Drop`, `chunkOf`, `ChunkManager`, `Redstone Logic (Redstone)`, `Pistons.cpp`, `Sound.h`, `Controls & ItemOrder`, `Redstone.cpp`, `ChunkManager Module`, `AnimalManager Module`, `isTorchBlock`, `Block and Item Types`, `RailLogic Module`, `Redstone Logic (Redstone)`, `W`, `Block and Item Types`, `Block and Item Types`, `HostileManager Module`, `Torch Module`, `Vehicle Entity (MinecartManager)`, `T`, `M`, `InventoryScreen.cpp`, `notify`, `NetherTerrain`, `Vehicle Entity (MinecartModel)`, `isLeavesBlock`, `BigTree`, `Chunk.h`, `DroppedItem.cpp`, `BoatManager.cpp`, `PartialBlocks.h`, `BoatWorld`, `Maps Module`, `Crafting Recipes`, `nds`, `NoteBlocks.cpp`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `Block and Item Types`, `HostileManager Module`, `TickInput`, `bigTreeComputeBranches`, `Vehicle Entity (MinecartManager)`, `TntManager.cpp`, `VoxelColumnRLE`, `Projectiles Module`, `SheepManager Module`, `Caves Module`, `7. World engine in detail`, `World`, `FallingBlocks.cpp`?**
  _High betweenness centrality (0.268) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BlockType` (e.g. with `2. Rules for an AI assistant modifying this project (read carefully)` and `7.2 Memory model`) actually correct?**
  _`BlockType` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `s`, `x`, `y` to the rest of the system?**
  _1439 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Block and Item Types` be split into smaller, more focused modules?**
  _Cohesion score 0.007782101167315175 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `main` to `.isDSi`, `LoadingScreen Module`, `Player Module`, `Catch`, `Block and Item Types`, `Block and Item Types`, `PendingDrops.h`, `Crafting Recipes`, `GameplayHotbar.cpp`, `Block and Item Types`, `SubScreenMenu Module`, `.updateFaceCache`, `WorldSave Module`, `ChunkManager`, `Pistons.cpp`, `Texture & PaintingTex`, `isTorchBlock`, `Texture Module`, `Block and Item Types`, `Torch Module`, `.physicsTick`, `M`, `InventoryScreen.cpp`, `NewWorldMenu.cpp`, `isLeavesBlock`, `WorldSelectMenu Module`, `Chunk.h`, `PartialBlocks.h`, `Crafting Recipes`, `CLAUDE.md — Technical guide to *Minecraft: Nintendo DS Edition* (Eaglercraft Beta 1.7.3 — Nintendo DS Port)`, `WorldSave Module`, `Player.cpp`, `TopScreenMenu & Renderer`, `TntManager.cpp`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 87 inferred relationships involving `main()` (e.g. with `armorMaterial()` and `canHarvestBlock()`) actually correct?**
  _`main()` has 87 INFERRED edges - model-reasoned connections that need verification._
- **Should `Chunk Meshing and Bands` be split into smaller, more focused modules?**
  _Cohesion score 0.020475020475020474 - nodes in this community are weakly interconnected._