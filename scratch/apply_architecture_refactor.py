import sys

# 1. Update source/main.cpp
with open("source/main.cpp", "r", encoding="utf-8") as f:
    main_src = f.read()

assert '#include "AsyncSaveManager.h"' not in main_src
main_src = '#include "AsyncSaveManager.h"\n' + main_src

main_target_init = """    // Verificacion y deteccion dinamica de hardware en arranque
    Hardware::printHardwareInfo();"""

main_repl_init = """    // Verificacion y deteccion dinamica de hardware en arranque
    Hardware::initHardwareProfile();
    Hardware::printHardwareInfo();
    AsyncSaveManager::init();"""

assert main_target_init in main_src, "main_target_init not found"
main_src = main_src.replace(main_target_init, main_repl_init, 1)

main_target_update = """        Governor::setEnabled(true);
        Chunk::setBudgetPercent(Governor::budgetPercent());   // si el cuadro anterior se pasó, los presupuestos se recortan
        { PROF(Prof::UPDATE); chunkManager->update(player->x, player->z); }"""

main_repl_update = """        Governor::setEnabled(true);
        Chunk::setBudgetPercent(Governor::budgetPercent());   // si el cuadro anterior se pasó, los presupuestos se recortan
        float ldx = 0.0f, ldy = 0.0f, ldz = 0.0f;
        player->getLookDirection(ldx, ldy, ldz);
        { PROF(Prof::UPDATE); chunkManager->update(player->x, player->z, ldx, ldz); }"""

assert main_target_update in main_src, "main_target_update not found"
main_src = main_src.replace(main_target_update, main_repl_update, 1)

with open("source/main.cpp", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(main_src)
print("source/main.cpp refactored successfully.")

# 2. Update source/Chunk.cpp
with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
    chunk_src = f.read()

chunk_src = '#include "AsyncSaveManager.h"\n' + chunk_src

chunk_target_update = """void Chunk::update(const ChunkManager* manager) {"""
chunk_repl_update = """void Chunk::update(const ChunkManager* manager, bool pauseSecondaryStructures) {"""
assert chunk_target_update in chunk_src, "chunk_target_update not found"
chunk_src = chunk_src.replace(chunk_target_update, chunk_repl_update, 1)

chunk_target_struct = """    PROF(Prof::GEN_STRUCT);
    if (!cavesDone) {
        PROFSTEP("caves");
        if (generateCaves(manager)) cavesDone = true;
        return; // un paso por cuadro; árboles, menas y cactus empiezan cuando terminan las cuevas
    }
    s_structureGenActive = true;
    // Terreno terminado — repartimos las estructuras en varios frames
    // separados, en vez de las 3 juntas de golpe
    switch (structureGenPhase) {
        case 0: {
            PROFSTEP("lakes");
            if (generateLakes(manager)) { structureGenPhase = 1; structureGenXi = 0; structureGenZi = 0; }
            break;
        }
        case 1: {
            PROFSTEP("trees");"""

chunk_repl_struct = """    PROF(Prof::GEN_STRUCT);
    if (!cavesDone) {
        if (pauseSecondaryStructures) return; // Pausa cuevas en chunks lejanos para mantener 30 FPS en DS
        PROFSTEP("caves");
        if (generateCaves(manager)) cavesDone = true;
        return;
    }
    s_structureGenActive = true;
    switch (structureGenPhase) {
        case 0: {
            if (pauseSecondaryStructures) { s_structureGenActive = false; return; }
            PROFSTEP("lakes");
            if (generateLakes(manager)) { structureGenPhase = 1; structureGenXi = 0; structureGenZi = 0; }
            break;
        }
        case 1: {
            if (pauseSecondaryStructures) { s_structureGenActive = false; return; }
            PROFSTEP("trees");"""

assert chunk_target_struct in chunk_src, "chunk_target_struct not found"
chunk_src = chunk_src.replace(chunk_target_struct, chunk_repl_struct, 1)

chunk_target_save = """bool Chunk::saveToFile(const char* path) const {"""
chunk_repl_save = """bool Chunk::saveToFileAsync(const char* path) const {
    if (!generationComplete) return false;
    static u8 s_rawSaveBuf[sizeof(blocks) + sizeof(liquidMeta)];
    static u8 s_compSaveBuf[sizeof(s_rawSaveBuf) + 256];

    const size_t rawSize = sizeof(blocks) + sizeof(liquidMeta);
    memcpy(s_rawSaveBuf, blocks, sizeof(blocks));
    memcpy(s_rawSaveBuf + sizeof(blocks), liquidMeta, sizeof(liquidMeta));

    int compSize = ChunkCompression::compressLZ10(s_rawSaveBuf, (int)rawSize, s_compSaveBuf, (int)sizeof(s_compSaveBuf));
    if (compSize > 0 && compSize < (int)rawSize) {
        if (AsyncSaveManager::enqueueSave(path, s_compSaveBuf, compSize)) {
            return true;
        }
    }
    return saveToFile(path);
}

bool Chunk::saveToFile(const char* path) const {"""

assert chunk_target_save in chunk_src, "chunk_target_save not found"
chunk_src = chunk_src.replace(chunk_target_save, chunk_repl_save, 1)

chunk_target_load = """    // Sincronizar hacia el almacenamiento RLE en RAM activa
    syncRLEFromBlocks();

    {   // archivo dañado (guardado incompleto de una version anterior): si la capa y=0 es toda aire se descarta y el chunk se regenera de la semilla
        bool any = false;
        for (int x = 0; x < SIZE_X && !any; x++)
            for (int z = 0; z < SIZE_Z; z++)
                if (blocks[x][0][z] != BlockType::AIR) { any = true; break; }
        if (!any) { remove(path); return false; }
    }

    loadStaging = true;      // el bioma y los colores se calculan despues, repartidos en varios cuadros
    loadBiomeIdx = 0;
    return true;"""

chunk_repl_load = """    // Sincronizar hacia el almacenamiento RLE en RAM activa
    syncRLEFromBlocks();

    {   // archivo dañado (guardado incompleto de una version anterior): si la capa y=0 es toda aire se descarta y el chunk se regenera de la semilla
        bool any = false;
        for (int x = 0; x < SIZE_X && !any; x++)
            for (int z = 0; z < SIZE_Z; z++)
                if (blocks[x][0][z] != BlockType::AIR) { any = true; break; }
        if (!any) { remove(path); return false; }
    }

    // CARGA INSTANTANEA (Volcado Directo RLE/LZSS):
    // Bypass del pipeline repartido para carga inmediata desde disco
    rebuildAllOccupancy();
    if (s_dimension == 0) {
        computeBiomeData();
    }
    loadStaging = false;
    generationComplete = true;
    beginFullFaceCacheRecalc();
    markDisplayListDirty();
    return true;"""

assert chunk_target_load in chunk_src, "chunk_target_load not found"
chunk_src = chunk_src.replace(chunk_target_load, chunk_repl_load, 1)

with open("source/Chunk.cpp", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(chunk_src)
print("source/Chunk.cpp refactored successfully.")

# 3. Update source/ChunkManager.cpp
with open("source/ChunkManager.cpp", "r", encoding="utf-8") as f:
    cm_src = f.read()

cm_src = '#include "AsyncSaveManager.h"\n' + cm_src

cm_target_update_sig = """void ChunkManager::update(float playerX, float playerZ) {"""
cm_repl_update_sig = """void ChunkManager::update(float playerX, float playerZ, float lookDirX, float lookDirZ) {"""
assert cm_target_update_sig in cm_src, "cm_target_update_sig not found"
cm_src = cm_src.replace(cm_target_update_sig, cm_repl_update_sig, 1)

cm_target_load = """            if (chunks[i]->loadFromFile(filename)) {   // etapa 1: abrir y leer. Bioma y colores se calculan despues, repartidos (abajo)
                loadingBiome[i] = true;                 // awaitingLoad sigue en true hasta que termine
            } else {
                awaitingLoad[i] = false;                // sin archivo: el chunk se genera de la semilla
            }"""

cm_repl_load = """            if (chunks[i]->loadFromFile(filename)) {
                // Carga instantanea: descompresion y volcado directo completados
                loadingBiome[i] = false;
                awaitingLoad[i] = false;
                chunks[i]->beginFullFaceCacheRecalc();
            } else {
                awaitingLoad[i] = false;
            }"""
assert cm_target_load in cm_src, "cm_target_load not found"
cm_src = cm_src.replace(cm_target_load, cm_repl_load, 1)

cm_target_heavy = """    // Streaming asíncrono dinámico: en DSi (133 MHz, 16 MB) se procesan hasta 5 chunks;
    // en DS tradicional (67 MHz, 4 MB) se restringe estrictamente a 2 chunks para streaming suave sin congelar la SD.
    const int MAX_CONCURRENT_HEAVY_CHUNKS = Hardware::isDSi() ? 5 : 2;

    int processedHeavy = 0;
    Chunk::beginHeavyFrame();
    Caves::beginFrame();

    // Un chunk recien leido del disco termina su bioma/colores en varios cuadros (el mas cercano primero); los demas esperan su turno
    if (!Governor::skipHeavy()) {
        const int ccx = centerIndex >= 0 ? chunkPosX[centerIndex] : 0;
        const int ccz = centerIndex >= 0 ? chunkPosZ[centerIndex] : 0;
        int best = -1, bestKey = 0x7FFFFFFF;
        for (int i = 0; i < maxChunks; i++) {
            if (!slotUsed[i] || !loadingBiome[i]) continue;
            const int ddx = chunkPosX[i] - ccx, ddz = chunkPosZ[i] - ccz;
            const int key = ddx * ddx + ddz * ddz;
            if (key < bestKey) { bestKey = key; best = i; }
        }
        if (best >= 0 && chunks[best]->continueLoad()) {
            loadingBiome[best] = false;
            awaitingLoad[best] = false;
            chunks[best]->beginFullFaceCacheRecalc();
        }
    }

    // Primero los chunks más cercanos al jugador: al llegar a terreno nuevo, el de debajo de los pies se completa antes que los del borde
    // de la ventana (antes se rotaba entre todos por igual y con 25 chunks el de los pies tardaba mucho)
    int heavyOrder[CAP_CHUNKS], heavyKey[CAP_CHUNKS], heavyCount = 0;
    {
        const int ccx = centerIndex >= 0 ? chunkPosX[centerIndex] : 0;
        const int ccz = centerIndex >= 0 ? chunkPosZ[centerIndex] : 0;
        for (int i = 0; i < maxChunks; i++) {
            if (!slotUsed[i] || !needsHeavyWork(i)) continue;
            const int ddx = chunkPosX[i] - ccx, ddz = chunkPosZ[i] - ccz;
            const int key = ddx * ddx + ddz * ddz;
            int p = heavyCount++;
            while (p > 0 && heavyKey[p - 1] > key) { heavyKey[p] = heavyKey[p - 1]; heavyOrder[p] = heavyOrder[p - 1]; p--; }
            heavyKey[p] = key; heavyOrder[p] = i;
        }
    }

    for (int k = 0; k < heavyCount; k++) {
        int i = heavyOrder[k];
        if (processedHeavy >= MAX_CONCURRENT_HEAVY_CHUNKS || Governor::skipHeavy()) continue;   // Governor: tras un cuadro lento se salta el trabajo pesado
        if (!Chunk::heavyBudgetLeft()) break;

        chunks[i]->update(this);
        processedHeavy++;"""

cm_repl_heavy = """    // Procesar cola de guardado asíncrono continua en segundo plano
    AsyncSaveManager::processQueue();

    // DSi (133 MHz): ráfaga (burst generation) de hasta 8 chunks simultáneos
    // DS original (67 MHz): restrictivo a 2 chunks para streaming suave a 30 FPS
    const int MAX_CONCURRENT_HEAVY_CHUNKS = Hardware::getMaxConcurrentHeavyChunks();

    const bool isDS = !Hardware::isDSi();
    const bool slowFrame = Governor::isSlowFrame();

    int processedHeavy = 0;
    Chunk::beginHeavyFrame();
    Caves::beginFrame();

    if (!Governor::skipHeavy()) {
        const int ccx = centerIndex >= 0 ? chunkPosX[centerIndex] : 0;
        const int ccz = centerIndex >= 0 ? chunkPosZ[centerIndex] : 0;
        int best = -1, bestKey = 0x7FFFFFFF;
        for (int i = 0; i < maxChunks; i++) {
            if (!slotUsed[i] || !loadingBiome[i]) continue;
            const int ddx = chunkPosX[i] - ccx, ddz = chunkPosZ[i] - ccz;
            const int key = ddx * ddx + ddz * ddz;
            if (key < bestKey) { bestKey = key; best = i; }
        }
        if (best >= 0 && chunks[best]->continueLoad()) {
            loadingBiome[best] = false;
            awaitingLoad[best] = false;
            chunks[best]->beginFullFaceCacheRecalc();
        }
    }

    // Cola en espiral ascendente priorizando el Frustum frontal en punto fijo 8.8
    int heavyOrder[CAP_CHUNKS], heavyKey[CAP_CHUNKS], heavyCount = 0;
    {
        const int ccx = centerIndex >= 0 ? chunkPosX[centerIndex] : 0;
        const int ccz = centerIndex >= 0 ? chunkPosZ[centerIndex] : 0;

        const int dirX8 = (int)(lookDirX * 256.0f);
        const int dirZ8 = (int)(lookDirZ * 256.0f);
        const bool hasDir = (dirX8 != 0 || dirZ8 != 0);

        for (int i = 0; i < maxChunks; i++) {
            if (!slotUsed[i] || !needsHeavyWork(i)) continue;
            const int ddx = chunkPosX[i] - ccx;
            const int ddz = chunkPosZ[i] - ccz;
            const int distSq = ddx * ddx + ddz * ddz;

            int key = distSq * 512;
            if (hasDir && distSq > 0) {
                int dot = ddx * dirX8 + ddz * dirZ8;
                key -= (dot * 2);
            }

            int p = heavyCount++;
            while (p > 0 && heavyKey[p - 1] > key) {
                heavyKey[p] = heavyKey[p - 1];
                heavyOrder[p] = heavyOrder[p - 1];
                p--;
            }
            heavyKey[p] = key;
            heavyOrder[p] = i;
        }
    }

    for (int k = 0; k < heavyCount; k++) {
        int i = heavyOrder[k];
        if (processedHeavy >= MAX_CONCURRENT_HEAVY_CHUNKS || Governor::skipHeavy()) continue;
        if (!Chunk::heavyBudgetLeft()) break;

        const int ccx = centerIndex >= 0 ? chunkPosX[centerIndex] : 0;
        const int ccz = centerIndex >= 0 ? chunkPosZ[centerIndex] : 0;
        const int ddx = chunkPosX[i] - ccx;
        const int ddz = chunkPosZ[i] - ccz;
        const int distSq = ddx * ddx + ddz * ddz;

        // Perfil DS (67 MHz): Si el cuadro supera 25ms, pausar estructuras secundarias en chunks lejanos
        bool pauseSecondary = isDS && slowFrame && (distSq > 4);

        chunks[i]->update(this, pauseSecondary);
        processedHeavy++;"""

assert cm_target_heavy in cm_src, "cm_target_heavy not found"
cm_src = cm_src.replace(cm_target_heavy, cm_repl_heavy, 1)

cm_target_flush = """void ChunkManager::flushOnePendingSave() {
    PROFSTEP("chunk save");
    if (pendingSaveCount <= 0) return;
    pendingSaveCount--;
    Chunk* toSave = pendingSaveChunks[pendingSaveCount];
    char oldFilename[96];
    toSave->getSaveFilename(oldFilename);
    toSave->saveToFile(oldFilename);
    releaseChunk(toSave);
}"""

cm_repl_flush = """void ChunkManager::flushOnePendingSave() {
    PROFSTEP("chunk save");
    if (pendingSaveCount <= 0) return;
    pendingSaveCount--;
    Chunk* toSave = pendingSaveChunks[pendingSaveCount];
    char oldFilename[96];
    toSave->getSaveFilename(oldFilename);
    toSave->saveToFileAsync(oldFilename);
    releaseChunk(toSave);
}"""

assert cm_target_flush in cm_src, "cm_target_flush not found"
cm_src = cm_src.replace(cm_target_flush, cm_repl_flush, 1)

cm_target_save_mod = """        if (chunks[i]->saveToFile(filename)) {"""
cm_repl_save_mod = """        if (chunks[i]->saveToFileAsync(filename)) {"""
assert cm_target_save_mod in cm_src, "cm_target_save_mod not found"
cm_src = cm_src.replace(cm_target_save_mod, cm_repl_save_mod, 1)

with open("source/ChunkManager.cpp", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(cm_src)
print("source/ChunkManager.cpp refactored successfully.")

print("All architecture refactorings applied successfully!")

