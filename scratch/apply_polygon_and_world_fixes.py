import os, sys

def apply_fixes():
    # 1. Patch source/WorldSelectMenu.h
    wsm_h_path = "source/WorldSelectMenu.h"
    with open(wsm_h_path, "r", encoding="utf-8") as f:
        wsm_h = f.read()

    wsm_h_target = """    // Arma la lista de mundos existentes (huecos incluidos) y dibuja
    // el fondo correspondiente (con o sin mundos) + el nombre inicial.
    static void init();

    // Llamar después de Create/Delete — rearma la lista y el fondo
    // (puede cambiar entre "hay mundos"/"no hay mundos").
    static void refresh();"""

    wsm_h_replacement = """    // Arma la lista de mundos existentes (huecos incluidos) y dibuja
    // el fondo correspondiente (con o sin mundos) + el nombre inicial.
    static void init();

    // Reconstruye de forma segura la lista dinámica de mundos escaneando /mcdsefiles/worlds/
    static void refreshWorldList();

    // Llamar después de Create/Delete — rearma la lista y el fondo
    // (puede cambiar entre "hay mundos"/"no hay mundos").
    static void refresh();"""

    assert wsm_h_target in wsm_h, "WorldSelectMenu.h target mismatch"
    wsm_h = wsm_h.replace(wsm_h_target, wsm_h_replacement)
    with open(wsm_h_path, "w", encoding="utf-8") as f:
        f.write(wsm_h)
    print("Patched source/WorldSelectMenu.h")

    # 2. Patch source/WorldSelectMenu.cpp
    wsm_cpp_path = "source/WorldSelectMenu.cpp"
    new_wsm_cpp = """#include "WorldSelectMenu.h"
#include "WorldSave.h"
#include <nds.h>
#include <string.h>
#include "selectWorld.h"
#include "selectWorldNoWorld.h"
#include "MenuFont.h"
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>

static int bgId = -1;
static int worldList[100];
static int worldCount = 0;
static int selectedIndex = 0;

// Recuadro negro donde va el nombre, medido sobre la imagen real
static const int LABEL_X0 = 65, LABEL_X1 = 191;
static const int LABEL_Y0 = 108, LABEL_Y1 = 145;

static void clearLabelZone(u16* fb) {
    if (!fb) return;
    u16 black = RGB15(0, 0, 0) | BIT(15);
    for (int y = LABEL_Y0; y <= LABEL_Y1; y++) {
        for (int x = LABEL_X0; x <= LABEL_X1; x++) {
            fb[y * 256 + x] = black;
        }
    }
}

static void drawWorldName(int worldNum) {
    if (bgId < 0) return;
    u16* fb = (u16*)bgGetGfxPtr(bgId);
    if (!fb) return;

    clearLabelZone(fb);
    if (worldNum <= 0) return; // sin mundos: recuadro completamente limpio

    // Nombre propio del mundo (name.dat) o "World N". Hasta 12 letras al tamano de siempre
    char name[24];
    if (!WorldSave::readWorldName(worldNum, name, sizeof(name))) {
        snprintf(name, sizeof(name), "World %d", worldNum);
    }

    const int scale = MenuFont::scaleFor((int)strlen(name));
    const int textWidth = MenuFont::width(name, scale);
    const int startX = LABEL_X0 + ((LABEL_X1 - LABEL_X0 + 1) - textWidth) / 2;
    const int startY = LABEL_Y0 + ((LABEL_Y1 - LABEL_Y0 + 1) - 6 * scale) / 2;
    MenuFont::draw16(fb, name, startX, startY, scale, RGB15(31, 31, 31) | BIT(15));
}

void WorldSelectMenu::refreshWorldList() {
    // 1. Limpiar completamente los arrays y contadores antiguos
    memset(worldList, 0, sizeof(worldList));
    worldCount = 0;
    selectedIndex = 0;

    // 2. Abrir e inspeccionar la ruta /mcdsefiles/worlds/
    DIR* dir = opendir("/mcdsefiles/worlds");
    if (!dir) {
        mkdir("/mcdsefiles", 0777);
        mkdir("/mcdsefiles/worlds", 0777);
        dir = opendir("/mcdsefiles/worlds");
    }

    if (dir) {
        struct dirent* entry = nullptr;
        while ((entry = readdir(dir)) != nullptr && worldCount < 100) {
            if (entry->d_name[0] == '.') continue;

            // Comprobar patrón "world<N>"
            if (strncmp(entry->d_name, "world", 5) == 0) {
                int worldNum = atoi(entry->d_name + 5);
                if (worldNum > 0 && worldNum <= 100) {
                    char subPath[96];
                    snprintf(subPath, sizeof(subPath), "/mcdsefiles/worlds/%s", entry->d_name);
                    DIR* subDir = opendir(subPath);
                    if (subDir) {
                        bool hasValidFiles = false;
                        struct dirent* subEntry = nullptr;
                        while ((subEntry = readdir(subDir)) != nullptr) {
                            if (subEntry->d_name[0] == '.') continue;
                            // Si contiene un archivo de datos .dat se considera mundo válido
                            if (strstr(subEntry->d_name, ".dat") != nullptr) {
                                hasValidFiles = true;
                                break;
                            }
                        }
                        closedir(subDir);
                        if (hasValidFiles) {
                            worldList[worldCount++] = worldNum;
                        }
                    }
                }
            }
        }
        closedir(dir);
    }

    // Ordenar de forma ascendente los slots de mundos encontrados
    for (int i = 0; i < worldCount - 1; i++) {
        for (int j = i + 1; j < worldCount; j++) {
            if (worldList[i] > worldList[j]) {
                int tmp = worldList[i];
                worldList[i] = worldList[j];
                worldList[j] = tmp;
            }
        }
    }

    if (worldCount == 0) {
        selectedIndex = 0;
    } else if (selectedIndex >= worldCount) {
        selectedIndex = worldCount - 1;
    }
}

void WorldSelectMenu::init() {
    videoSetModeSub(MODE_5_2D | DISPLAY_BG3_ACTIVE);
    vramSetBankC(VRAM_C_SUB_BG);
    bgId = bgInitSub(3, BgType_Bmp16, BgSize_B16_256x256, 0, 0);

    refreshWorldList();

    // Si worldCount == 0, se carga selectWorldNoWorldBitmap (sin botones de jugar ni borrar)
    const void* bitmap = (worldCount > 0) ? (const void*)selectWorldBitmap : (const void*)selectWorldNoWorldBitmap;
    decompress(bitmap, bgGetGfxPtr(bgId), LZ77Vram);

    u16* pixels = (u16*)bgGetGfxPtr(bgId);
    for (int i = 0; i < 256 * 192; i++) {
        pixels[i] |= BIT(15);
    }

    if (worldCount > 0) {
        drawWorldName(worldList[selectedIndex]);
    } else {
        clearLabelZone(pixels);
    }
}

void WorldSelectMenu::refresh() {
    init();
}

void WorldSelectMenu::selectPrevious() {
    if (worldCount <= 0) return;
    selectedIndex = (selectedIndex - 1 + worldCount) % worldCount;
    drawWorldName(worldList[selectedIndex]);
}

void WorldSelectMenu::selectNext() {
    if (worldCount <= 0) return;
    selectedIndex = (selectedIndex + 1) % worldCount;
    drawWorldName(worldList[selectedIndex]);
}

int WorldSelectMenu::getSelectedWorldNum() {
    if (worldCount <= 0 || selectedIndex < 0 || selectedIndex >= worldCount) return -1;
    return worldList[selectedIndex];
}

int WorldSelectMenu::getWorldCount() {
    return worldCount;
}

bool WorldSelectMenu::isCreateTouched(int touchX, int touchY) {
    return touchX >= 0 && touchX <= 62 && touchY >= 162 && touchY <= 190;
}

bool WorldSelectMenu::isDeleteTouched(int touchX, int touchY) {
    if (worldCount <= 0) return false;
    return touchX >= 66 && touchX <= 125 && touchY >= 162 && touchY <= 190;
}

bool WorldSelectMenu::isPlayTouched(int touchX, int touchY) {
    if (worldCount <= 0) return false;
    return touchX >= 130 && touchX <= 189 && touchY >= 162 && touchY <= 190;
}

bool WorldSelectMenu::isBackTouched(int touchX, int touchY) {
    return touchX >= 194 && touchX <= 253 && touchY >= 162 && touchY <= 190;
}

bool WorldSelectMenu::isLeftArrowTouched(int touchX, int touchY) {
    if (worldCount <= 1) return false;
    return touchX >= 0 && touchX <= 64 && touchY >= 51 && touchY <= 113;
}

bool WorldSelectMenu::isRightArrowTouched(int touchX, int touchY) {
    if (worldCount <= 1) return false;
    return touchX >= 192 && touchX <= 255 && touchY >= 51 && touchY <= 113;
}
"""
    with open(wsm_cpp_path, "w", encoding="utf-8") as f:
        f.write(new_wsm_cpp)
    print("Patched source/WorldSelectMenu.cpp")

    # 3. Patch source/WorldSave.cpp
    ws_cpp_path = "source/WorldSave.cpp"
    with open(ws_cpp_path, "r", encoding="utf-8") as f:
        ws_cpp = f.read()

    # Include WorldSelectMenu.h in WorldSave.cpp
    if '#include "WorldSelectMenu.h"' not in ws_cpp:
        ws_cpp = '#include "WorldSelectMenu.h"\n' + ws_cpp

    del_old = """void WorldSave::deleteWorld(const char* path) {
    clearFolderContents(path);
    rmdir(path);
}"""

    del_new = """void WorldSave::deleteWorld(const char* path) {
    clearFolderContents(path);
    rmdir(path);
    // Reconstruir inmediatamente la lista dinámica de mundos y reindexar
    WorldSelectMenu::refreshWorldList();
}"""

    assert del_old in ws_cpp, "WorldSave.cpp deleteWorld mismatch"
    ws_cpp = ws_cpp.replace(del_old, del_new)

    # clearFolderContents unlink
    cf_old = """        struct stat st;
        if (stat(fullPath, &st) == 0 && S_ISDIR(st.st_mode)) {
            clearFolderContents(fullPath);
            rmdir(fullPath);
        } else {
            remove(fullPath);
        }"""

    cf_new = """        struct stat st;
        if (stat(fullPath, &st) == 0 && S_ISDIR(st.st_mode)) {
            clearFolderContents(fullPath);
            rmdir(fullPath);
        } else {
            unlink(fullPath);
            remove(fullPath);
        }"""

    assert cf_old in ws_cpp, "WorldSave.cpp clearFolderContents mismatch"
    ws_cpp = ws_cpp.replace(cf_old, cf_new)

    with open(ws_cpp_path, "w", encoding="utf-8") as f:
        f.write(ws_cpp)
    print("Patched source/WorldSave.cpp")

    # 4. Patch source/HwMath.h
    hw_math_path = "source/HwMath.h"
    with open(hw_math_path, "r", encoding="utf-8") as f:
        hw_math = f.read()

    sync_old = """    // Inicia división entera 32 / 32
    static inline void startDiv32(int32_t numer, int32_t denom) {"""

    sync_new = """    // Sincronización completa de los registros matemáticos de hardware
    static inline void sync() {
        while (REG_DIVCNT & DIV_BUSY);
        while (REG_SQRTCNT & SQRT_BUSY);
    }

    // Inicia división entera 32 / 32
    static inline void startDiv32(int32_t numer, int32_t denom) {
        while (REG_DIVCNT & DIV_BUSY);"""

    assert sync_old in hw_math, "HwMath.h startDiv32 mismatch"
    hw_math = hw_math.replace(sync_old, sync_new)

    hw_math = hw_math.replace("static inline void startDiv64_32(int64_t numer, int32_t denom) {",
                              "static inline void startDiv64_32(int64_t numer, int32_t denom) {\n        while (REG_DIVCNT & DIV_BUSY);")
    hw_math = hw_math.replace("static inline void startDivFixed20_12(int32_t numFixed, int32_t denFixed) {",
                              "static inline void startDivFixed20_12(int32_t numFixed, int32_t denFixed) {\n        while (REG_DIVCNT & DIV_BUSY);")
    hw_math = hw_math.replace("static inline void startSqrt32(uint32_t param) {",
                              "static inline void startSqrt32(uint32_t param) {\n        while (REG_SQRTCNT & SQRT_BUSY);")
    hw_math = hw_math.replace("static inline void startSqrt64(int64_t param) {",
                              "static inline void startSqrt64(int64_t param) {\n        while (REG_SQRTCNT & SQRT_BUSY);")
    hw_math = hw_math.replace("static inline void startSqrtFixed20_12(int32_t valFixed) {",
                              "static inline void startSqrtFixed20_12(int32_t valFixed) {\n        while (REG_SQRTCNT & SQRT_BUSY);")

    with open(hw_math_path, "w", encoding="utf-8") as f:
        f.write(hw_math)
    print("Patched source/HwMath.h")

    # 5. Patch source/ChunkManager.cpp
    cm_path = "source/ChunkManager.cpp"
    with open(cm_path, "r", encoding="utf-8") as f:
        cm_cpp = f.read()

    cm_old = """    int vertBudget = Options::get().renderQuality == 2 ? 7000 : (Options::get().renderQuality == 1 ? 11000 : 15000); // deja margen para brazo/mirilla/overlay/ítems tirados
    int rebuildBandBudget = Governor::skipHeavy() ? 0 : 64; // 64 ya no limita en la práctica: manda el presupuesto de tiempo; 0 = Governor salta las listas este cuadro
    Chunk::beginRebuildFrame();

    for (int k = 0; k < drawCount; k++) {
        int i = drawOrder[k];
        chunks[i]->draw(playerX, playerY, playerZ, lookDirX, lookDirY, lookDirZ, this, &vertBudget, &rebuildBandBudget);
    }"""

    cm_new = """    // Límite estricto de polígonos por frame: máximo 2000 polígonos para evitar saturación de la GPU a 1 FPS
    int polyBudget = (Options::get().renderQuality == 2) ? 1400 : ((Options::get().renderQuality == 1) ? 1700 : 2000);
    // Cada quad aporta 2 polígonos y 4 vértices (máximo 4000 vértices para el terreno)
    int vertBudget = polyBudget * 2;
    int rebuildBandBudget = Governor::skipHeavy() ? 0 : 64;
    Chunk::beginRebuildFrame();

    for (int k = 0; k < drawCount; k++) {
        if (vertBudget <= 0 || (GFX_CONTROL & GL_POLY_OVERFLOW)) {
            // Descarte inmediato si se satura el presupuesto de 2000 polígonos o la GPU señala overflow
            break;
        }
        int i = drawOrder[k];
        chunks[i]->draw(playerX, playerY, playerZ, lookDirX, lookDirY, lookDirZ, this, &vertBudget, &rebuildBandBudget);
    }"""

    assert cm_old in cm_cpp, "ChunkManager.cpp vertBudget mismatch"
    cm_cpp = cm_cpp.replace(cm_old, cm_new)
    with open(cm_path, "w", encoding="utf-8") as f:
        f.write(cm_cpp)
    print("Patched source/ChunkManager.cpp")

    # 6. Patch source/Chunk.cpp
    chunk_path = "source/Chunk.cpp"
    with open(chunk_path, "r", encoding="utf-8") as f:
        chk_cpp = f.read()

    chk_draw_old = """        const int bandVerts = dlBandVertCount[band] + dlBandVertCount2[band];
        if (vertBudget && bandVerts > *vertBudget) continue;"""

    chk_draw_new = """        // Comprobación de desbordamiento de polígonos por hardware en la GPU
        if (GFX_CONTROL & GL_POLY_OVERFLOW) {
            if (vertBudget) *vertBudget = 0;
            break;
        }

        const int bandVerts = dlBandVertCount[band] + dlBandVertCount2[band];
        if (vertBudget && bandVerts > *vertBudget) continue;"""

    assert chk_draw_old in chk_cpp, "Chunk.cpp draw overflow check mismatch"
    chk_cpp = chk_cpp.replace(chk_draw_old, chk_draw_new)
    with open(chunk_path, "w", encoding="utf-8") as f:
        f.write(chk_cpp)
    print("Patched source/Chunk.cpp")

    # 7. Patch source/main.cpp
    main_path = "source/main.cpp"
    with open(main_path, "r", encoding="utf-8") as f:
        main_cpp = f.read()

    if '#include "HwMath.h"' not in main_cpp:
        main_cpp = '#include "HwMath.h"\n' + main_cpp

    rend_start_old = """	if (shouldRender) {
            // La mano va PRIMERO — así nunca se pierde aunque el terreno"""

    rend_start_new = """	if (shouldRender) {
            // Sincronizar registros matemáticos y tubería de geometría antes de cada renderizado
            HwMath::sync();
            while ((DMA_CR(0) | DMA_CR(3)) & DMA_BUSY);
            while (GFX_BUSY);
            glMatrixMode(GL_MODELVIEW);
            glLoadIdentity();

            // La mano va PRIMERO — así nunca se pierde aunque el terreno"""

    assert rend_start_old in main_cpp, "main.cpp shouldRender start mismatch"
    main_cpp = main_cpp.replace(rend_start_old, rend_start_new)

    with open(main_path, "w", encoding="utf-8") as f:
        f.write(main_cpp)
    print("Patched source/main.cpp")

    # 8. Patch source/Sky.cpp (move math outside glBegin)
    sky_path = "source/Sky.cpp"
    with open(sky_path, "r", encoding="utf-8") as f:
        sky_cpp = f.read()

    sky_old = """        glBegin(GL_TRIANGLES);
        float px[17], py[17], pz[17];
        for (int i = 0; i <= 16; i++) {
            const float t = (float)i * PI_F * 2.0f / 16.0f, s = sinf(t), co = cosf(t);
            px[i] = s * 120.0f; py[i] = co * 120.0f; pz[i] = -co * 40.0f * a;
        }"""

    sky_new = """        float px[17], py[17], pz[17];
        for (int i = 0; i <= 16; i++) {
            const float t = (float)i * PI_F * 2.0f / 16.0f, s = sinf(t), co = cosf(t);
            px[i] = s * 120.0f; py[i] = co * 120.0f; pz[i] = -co * 40.0f * a;
        }
        glBegin(GL_TRIANGLES);"""

    assert sky_old in sky_cpp, "Sky.cpp math inside glBegin mismatch"
    sky_cpp = sky_cpp.replace(sky_old, sky_new)
    with open(sky_path, "w", encoding="utf-8") as f:
        f.write(sky_cpp)
    print("Patched source/Sky.cpp")

    # 9. Patch source/SteveModel.cpp (eliminate division inside glBegin)
    sm_path = "source/SteveModel.cpp"
    with open(sm_path, "r", encoding="utf-8") as f:
        sm_cpp = f.read()

    sm_old = """        glBegin(GL_QUADS);
        for (int i = 0; i < n; i++) {
            const int s = v * FACE_SHADE[q[i].face] / 255;
            glColor3b((u8)(c.r * s / 255), (u8)(c.g * s / 255 * gb), (u8)(c.b * s / 255 * gb));
            for (int k = 0; k < 4; k++) glVertex3v16(q[i].x[k], q[i].y[k], q[i].z[k]);
        }
        glEnd();"""

    sm_new = """        glBegin(GL_QUADS);
        for (int i = 0; i < n; i++) {
            const int s = (v * FACE_SHADE[q[i].face] * 257) >> 16;
            const int cr = (c.r * s * 257) >> 16;
            const int cg = (int)(((c.g * s * 257) >> 16) * gb);
            const int cb = (int)(((c.b * s * 257) >> 16) * gb);
            glColor3b((u8)cr, (u8)cg, (u8)cb);
            for (int k = 0; k < 4; k++) glVertex3v16(q[i].x[k], q[i].y[k], q[i].z[k]);
        }
        glEnd();"""

    assert sm_old in sm_cpp, "SteveModel.cpp division inside glBegin mismatch"
    sm_cpp = sm_cpp.replace(sm_old, sm_new)
    with open(sm_path, "w", encoding="utf-8") as f:
        f.write(sm_cpp)
    print("Patched source/SteveModel.cpp")

    # 10. Patch source/AnimalModel.cpp (eliminate division inside glBegin)
    am_path = "source/AnimalModel.cpp"
    with open(am_path, "r", encoding="utf-8") as f:
        am_cpp = f.read()

    am_old = """        glBegin(GL_QUADS);
        for (int f = 0; f < 6; f++) {
            const int s = v * SHADE[f] / 255;
            glColor3b((u8)(r * s / 255), (u8)(g * s / 255 * gb), (u8)(b * s / 255 * gb));
            for (int k = 0; k < 4; k++) glVertex3v16(p.quads[f].px[k], p.quads[f].py[k], p.quads[f].pz[k]);
        }
        glEnd();"""

    am_new = """        glBegin(GL_QUADS);
        for (int f = 0; f < 6; f++) {
            const int s = (v * SHADE[f] * 257) >> 16;
            const int cr = (r * s * 257) >> 16;
            const int cg = (int)(((g * s * 257) >> 16) * gb);
            const int cb = (int)(((b * s * 257) >> 16) * gb);
            glColor3b((u8)cr, (u8)cg, (u8)cb);
            for (int k = 0; k < 4; k++) glVertex3v16(p.quads[f].px[k], p.quads[f].py[k], p.quads[f].pz[k]);
        }
        glEnd();"""

    assert am_old in am_cpp, "AnimalModel.cpp division inside glBegin mismatch"
    am_cpp = am_cpp.replace(am_old, am_new)
    with open(am_path, "w", encoding="utf-8") as f:
        f.write(am_cpp)
    print("Patched source/AnimalModel.cpp")

    # 11. Patch source/HealthHud.cpp (precompute quad coordinates before glBegin)
    hh_path = "source/HealthHud.cpp"
    with open(hh_path, "r", encoding="utf-8") as f:
        hh_cpp = f.read()

    hh_old = """    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
        glLoadIdentity();
        glTranslatef(0.0f, 0.0f, -(float)Z0 / 4096.0f);
        glBegin(GL_QUADS);
        for (int i = 0; i < count; i++) {
            const HudQuad& q = quads[i];
            const int dist = Z0 - LAYER_STEP * q.layer;  // la capa más cercana se achica para seguir cayendo en el mismo píxel
            const int z = LAYER_STEP * q.layer;

            // píxel de pantalla -> unidades de cámara (x a la derecha, y hacia arriba, centro de la pantalla en (128, 96))
            int px[2] = { q.x, q.x + HealthHudLayout::ICON - EDGE_INSET };
            int py[2] = { q.y, q.y + HealthHudLayout::ICON - EDGE_INSET };
            short cx[2], cy[2];
            for (int k = 0; k < 2; k++) {
                int a = (px[k] - 128) * UNITS_PER_PIXEL * dist;
                int b = (96 - py[k]) * UNITS_PER_PIXEL * dist;
                cx[k] = (short)((a + (a >= 0 ? Z0 / 2 : -Z0 / 2)) / Z0);
                cy[k] = (short)((b + (b >= 0 ? Z0 / 2 : -Z0 / 2)) / Z0);
            }

            // coordenadas de textura en 12.4: el borde lejano queda 1/16 de texel antes del final del ícono, para no tomar el texel de al lado
            const int u0 = q.u << 4, v0 = q.v << 4, u1 = ((q.u + 9) << 4) - 1, v1 = ((q.v + 9) << 4) - 1;
            GFX_TEX_COORD = TEXTURE_PACK(u0, v1); glVertex3v16(cx[0], cy[1], z);
            GFX_TEX_COORD = TEXTURE_PACK(u1, v1); glVertex3v16(cx[1], cy[1], z);
            GFX_TEX_COORD = TEXTURE_PACK(u1, v0); glVertex3v16(cx[1], cy[0], z);
            GFX_TEX_COORD = TEXTURE_PACK(u0, v0); glVertex3v16(cx[0], cy[0], z);
        }
        glEnd();
    glPopMatrix(1);"""

    hh_new = """    // Precalcular todas las divisiones y coordenadas ANTES de glBegin para no perturbar el FIFO de vértices
    struct PrecomputedQuad {
        short cx[2];
        short cy[2];
        int z;
        int u0, v0, u1, v1;
    };
    PrecomputedQuad pq[HealthHudLayout::MAX_QUADS];
    for (int i = 0; i < count; i++) {
        const HudQuad& q = quads[i];
        const int dist = Z0 - LAYER_STEP * q.layer;
        pq[i].z = LAYER_STEP * q.layer;

        int px[2] = { q.x, q.x + HealthHudLayout::ICON - EDGE_INSET };
        int py[2] = { q.y, q.y + HealthHudLayout::ICON - EDGE_INSET };
        for (int k = 0; k < 2; k++) {
            int a = (px[k] - 128) * UNITS_PER_PIXEL * dist;
            int b = (96 - py[k]) * UNITS_PER_PIXEL * dist;
            pq[i].cx[k] = (short)((a + (a >= 0 ? Z0 / 2 : -Z0 / 2)) / Z0);
            pq[i].cy[k] = (short)((b + (b >= 0 ? Z0 / 2 : -Z0 / 2)) / Z0);
        }

        pq[i].u0 = q.u << 4;
        pq[i].v0 = q.v << 4;
        pq[i].u1 = ((q.u + 9) << 4) - 1;
        pq[i].v1 = ((q.v + 9) << 4) - 1;
    }

    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
        glLoadIdentity();
        glTranslatef(0.0f, 0.0f, -(float)Z0 / 4096.0f);
        glBegin(GL_QUADS);
        for (int i = 0; i < count; i++) {
            GFX_TEX_COORD = TEXTURE_PACK(pq[i].u0, pq[i].v1); glVertex3v16(pq[i].cx[0], pq[i].cy[1], pq[i].z);
            GFX_TEX_COORD = TEXTURE_PACK(pq[i].u1, pq[i].v1); glVertex3v16(pq[i].cx[1], pq[i].cy[1], pq[i].z);
            GFX_TEX_COORD = TEXTURE_PACK(pq[i].u1, pq[i].v0); glVertex3v16(pq[i].cx[1], pq[i].cy[0], pq[i].z);
            GFX_TEX_COORD = TEXTURE_PACK(pq[i].u0, pq[i].v0); glVertex3v16(pq[i].cx[0], pq[i].cy[0], pq[i].z);
        }
        glEnd();
    glPopMatrix(1);"""

    assert hh_old in hh_cpp, "HealthHud.cpp mismatch"
    hh_cpp = hh_cpp.replace(hh_old, hh_new)
    with open(hh_path, "w", encoding="utf-8") as f:
        f.write(hh_cpp)
    print("Patched source/HealthHud.cpp")

    # 12. Patch source/HandAnimations.cpp (move arm normal sqrtf/division outside glBegin)
    ha_path = "source/HandAnimations.cpp"
    with open(ha_path, "r", encoding="utf-8") as f:
        ha_cpp = f.read()

    ha_old = """    glBindTexture(0, Texture::skinTextureID);
    glBegin(GL_QUADS);
    for (int f = 0; f < 6; f++) {
        const Face& q = faces[f];

        // TexturedQuad.draw: normal = (v1 - v2) x (v1 - v0)
        float ax = q.v[1].x - q.v[2].x, ay = q.v[1].y - q.v[2].y, az = q.v[1].z - q.v[2].z;
        float bx = q.v[1].x - q.v[0].x, by = q.v[1].y - q.v[0].y, bz = q.v[1].z - q.v[0].z;
        float nx = ay * bz - az * by, ny = az * bx - ax * bz, nz = ax * by - ay * bx;
        float nl = sqrtf(nx * nx + ny * ny + nz * nz);
        if (nl > 0.0f) { nx /= nl; ny /= nl; nz /= nl; }
        nrm(nx, ny, nz);

        // TexturedQuad: v0=(u2,v1) v1=(u1,v1) v2=(u1,v2) v3=(u2,v2), con un margen de 0,1 texel
        const float m = 0.1f;
        const float uv[4][2] = {
            {q.u2 - m, q.vv1 + m}, {q.u1 + m, q.vv1 + m},
            {q.u1 + m, q.vv2 - m}, {q.u2 - m, q.vv2 - m},
        };
        for (int k = 0; k < 4; k++) {
            tex(uv[k][0], uv[k][1]);
            vtx(q.v[k].x * S, q.v[k].y * S, q.v[k].z * S);
        }
    }
    glEnd();"""

    ha_new = """    // Precalcular normales y sqrtf ANTES de glBegin
    float armNormals[6][3];
    for (int f = 0; f < 6; f++) {
        const Face& q = faces[f];
        float ax = q.v[1].x - q.v[2].x, ay = q.v[1].y - q.v[2].y, az = q.v[1].z - q.v[2].z;
        float bx = q.v[1].x - q.v[0].x, by = q.v[1].y - q.v[0].y, bz = q.v[1].z - q.v[0].z;
        float nx = ay * bz - az * by, ny = az * bx - ax * bz, nz = ax * by - ay * bx;
        float nl = sqrtf(nx * nx + ny * ny + nz * nz);
        if (nl > 0.0f) { float inv = 1.0f / nl; nx *= inv; ny *= inv; nz *= inv; }
        armNormals[f][0] = nx; armNormals[f][1] = ny; armNormals[f][2] = nz;
    }

    glBindTexture(0, Texture::skinTextureID);
    glBegin(GL_QUADS);
    for (int f = 0; f < 6; f++) {
        const Face& q = faces[f];
        nrm(armNormals[f][0], armNormals[f][1], armNormals[f][2]);

        // TexturedQuad: v0=(u2,v1) v1=(u1,v1) v2=(u1,v2) v3=(u2,v2), con un margen de 0,1 texel
        const float m = 0.1f;
        const float uv[4][2] = {
            {q.u2 - m, q.vv1 + m}, {q.u1 + m, q.vv1 + m},
            {q.u1 + m, q.vv2 - m}, {q.u2 - m, q.vv2 - m},
        };
        for (int k = 0; k < 4; k++) {
            tex(uv[k][0], uv[k][1]);
            vtx(q.v[k].x * S, q.v[k].y * S, q.v[k].z * S);
        }
    }
    glEnd();"""

    assert ha_old in ha_cpp, "HandAnimations.cpp mismatch"
    ha_cpp = ha_cpp.replace(ha_old, ha_new)
    with open(ha_path, "w", encoding="utf-8") as f:
        f.write(ha_cpp)
    print("Patched source/HandAnimations.cpp")

    print("\nALL 12 PATCHES FOR GRAPHICS AND WORLD SELECT APPLIED SUCCESSFULLY!")

if __name__ == "__main__":
    apply_fixes()
