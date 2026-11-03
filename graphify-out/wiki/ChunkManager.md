# ChunkManager

> God node · 95 connections · `source/ChunkManager.h`

**Community:** [ChunkManager Module](ChunkManager_Module.md)

## Connections by Relation

### contains
- ChunkManager.h `EXTRACTED`
- LightNode `EXTRACTED`

### defines
- CAP_CHUNKS `EXTRACTED`
- lastUsedChunkX `EXTRACTED`
- lastUsedChunkZ `EXTRACTED`
- lastLightChunk `EXTRACTED`
- lastLightChunkX `EXTRACTED`
- lastLightChunkZ `EXTRACTED`
- LIGHT_QUEUE_CAPACITY `EXTRACTED`
- MAX_FLOOD_STEPS_PER_CALL `EXTRACTED`
- POOL_SPARE `EXTRACTED`
- SKY_FLOOD_STEPS_PER_CALL `EXTRACTED`
- skyPending `EXTRACTED`
- skyPendingCount `EXTRACTED`
- lightQueue `EXTRACTED`
- relightSeeds `EXTRACTED`
- skylightSubtract `EXTRACTED`
- pool `EXTRACTED`
- poolInUse `EXTRACTED`
- poolCount `EXTRACTED`
- poolSize `EXTRACTED`
- maxChunks `EXTRACTED`
- *…and 21 more `defines` connection(s) not listed (lowest-degree first to go)*

### method
- .getChunkAt() `EXTRACTED`
- .floodFillSkyLight() `EXTRACTED`
- .getChunkByChunkCoord() `EXTRACTED`
- .floodFillBlockLight() `EXTRACTED`
- .update() `EXTRACTED`
- .propagateSkyColumn() `EXTRACTED`
- .relightNewAirCell() `EXTRACTED`
- .tickLiquids() `EXTRACTED`
- .bucketTakeSource() `EXTRACTED`
- .bucketPlaceSource() `EXTRACTED`
- .isInsideOfMaterial() `EXTRACTED`
- .continueSkyFlood() `EXTRACTED`
- .removeBlockLight() `EXTRACTED`
- .removeSkyLightAt() `EXTRACTED`
- .findOrCreateSlot() `EXTRACTED`
- .acquireChunk() `EXTRACTED`
- .releaseChunk() `EXTRACTED`
- .flushOnePendingSave() `EXTRACTED`
- .getBlockTypeAt() `EXTRACTED`
- .propagateBlockLight() `EXTRACTED`
- *…and 31 more `method` connection(s) not listed (lowest-degree first to go)*

### references
- [Chunk](Chunk.md) `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*