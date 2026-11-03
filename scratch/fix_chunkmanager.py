import os

path = r"source/ChunkManager.cpp"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = """    // --- Frustum Culling en Punto Fijo (sin FPU de CPU ARM9) ---
    const int eyeX16 = (int)(playerX * 16.0f);
    const int eyeZ16 = (int)(playerZ * 16.0f);
    const int dirX256 = (int)(lookDirX * 256.0f);
    const int dirZ256 = (int)(lookDirZ * 256.0f);
    const int horizMagSq = (dirX256 * dirX256 + dirZ256 * dirZ256) >> 8;
    const bool canCullFrustum = (horizMagSq >= 32); // Desactivar solo si mira vertical extremo

    // Cono horizontal de 60° (medio angulo = 60°: cos=128, sin=222 en escala 256) con margen seguro
    const int FRUSTUM_CONE_COS = 128;
    const int FRUSTUM_CONE_SIN = 222;
    const int CHUNK_RADIUS_16 = 100; // ~6.25 bloques en escala 16

    for (int i = 0; i < maxChunks; i++) {
        if (!slotUsed[i]) continue;
        if (!chunks[i]->isGenerationComplete()) continue;
        if (chunks[i]->isCacheRecalcPending() && !chunks[i]->hasBuiltDisplayList()) continue;

        // Frustum Culling optimizado en punto fijo entero
        if (canCullFrustum) {
            int chunkCenterX16 = (chunkPosX[i] * WorldConfig::SIZE_X + WorldConfig::SIZE_X / 2) * 16;
            int chunkCenterZ16 = (chunkPosZ[i] * WorldConfig::SIZE_Z + WorldConfig::SIZE_Z / 2) * 16;
            int vx = chunkCenterX16 - eyeX16;
            int vz = chunkCenterZ16 - eyeZ16;
            int v2 = vx * vx + vz * vz;

            if (v2 > CHUNK_RADIUS_16 * CHUNK_RADIUS_16) {
                int d = (vx * dirX256 + vz * dirZ256) >> 8;
                if (d < -CHUNK_RADIUS_16) {
                    continue; // CULL: Detras del plano de la camara
                }
                int e2 = v2 - d * d;
                if (e2 > 0) {
                    int e = sqrt32(e2);
                    if (((e * FRUSTUM_CONE_COS - d * FRUSTUM_CONE_SIN) >> 8) > CHUNK_RADIUS_16) {
                        continue; // CULL: Fuera del cono visual del frustum
                    }
                }
            }
        }"""

replacement = """    // --- Frustum Culling en Punto Fijo (sin FPU de CPU ARM9) ---
    const int eyeX16 = (int)(playerX * 16.0f);
    const int eyeZ16 = (int)(playerZ * 16.0f);
    const int dirX256 = (int)(lookDirX * 256.0f);
    const int dirZ256 = (int)(lookDirZ * 256.0f);
    const int horizMagSq = dirX256 * dirX256 + dirZ256 * dirZ256;
    const int horizLen = sqrt32(horizMagSq);
    const bool canCullFrustum = (horizLen >= 48); // Si mira casi vertical no descartar horizontalmente

    int normDirX = 0, normDirZ = 0;
    if (canCullFrustum) {
        normDirX = (dirX256 << 8) / horizLen;
        normDirZ = (dirZ256 << 8) / horizLen;
    }

    // Cono horizontal conservador de 60° (medio angulo = 60°: cos=128, sin=222 en escala 256)
    const int FRUSTUM_CONE_COS = 128;
    const int FRUSTUM_CONE_SIN = 222;
    // Radio envolvente del chunk: diagonal de 16x16 es ~22.6 bloques -> radio ~11.3 bloques -> 181 en escala 16
    // Con margen de seguridad usamos 200 (~12.5 bloques) para cero pop-in
    const int CHUNK_RADIUS_16 = 200;
    const int CHUNK_NEAR_LIMIT_SQ = (32 * 16) * (32 * 16); // Chunks a menos de 32 bloques nunca se descartan

    for (int i = 0; i < maxChunks; i++) {
        if (!slotUsed[i]) continue;
        if (!chunks[i]->isGenerationComplete()) continue;
        if (chunks[i]->isCacheRecalcPending() && !chunks[i]->hasBuiltDisplayList()) continue;

        // Frustum Culling optimizado en punto fijo entero
        if (canCullFrustum) {
            int chunkCenterX16 = (chunkPosX[i] * WorldConfig::SIZE_X + WorldConfig::SIZE_X / 2) * 16;
            int chunkCenterZ16 = (chunkPosZ[i] * WorldConfig::SIZE_Z + WorldConfig::SIZE_Z / 2) * 16;
            int vx = chunkCenterX16 - eyeX16;
            int vz = chunkCenterZ16 - eyeZ16;
            int v2 = vx * vx + vz * vz;

            // Chunks inmediatos al jugador nunca se descartan
            if (v2 > CHUNK_NEAR_LIMIT_SQ) {
                int d = (vx * normDirX + vz * normDirZ) >> 8;
                if (d < -CHUNK_RADIUS_16) {
                    continue; // CULL: Detras del plano de la camara
                }
                int e2 = v2 - d * d;
                if (e2 > 0) {
                    int e = sqrt32(e2);
                    if (((e * FRUSTUM_CONE_COS - d * FRUSTUM_CONE_SIN) >> 8) > CHUNK_RADIUS_16) {
                        continue; // CULL: Fuera del cono visual del frustum
                    }
                }
            }
        }"""

if target in content:
    content = content.replace(target, replacement, 1)
    print("Frustum culling fix applied.")
else:
    print("Target not found in ChunkManager.cpp!")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

