import os, re

def patch_file(path, search_regex, replacement):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if not re.search(search_regex, content):
        print(f"FAILED TO FIND PATTERN IN {path}")
        return False
    new_content = re.sub(search_regex, replacement, content, count=1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Patched {path} successfully!")
    return True

# 1. Patch source/VoxelRLE.h
voxel_rle_path = "source/VoxelRLE.h"
with open(voxel_rle_path, "r", encoding="utf-8") as f:
    rle_content = f.read()

rle_old = """struct RLERun {
    BlockType type; // 1 byte: tipo de bloque
    u8 length;      // 1 byte: longitud del tramo (1..128)
};

class VoxelColumnRLE {
public:
    // 24 tramos x 2 bytes = 48 bytes por columna (cabe perfectamente en 2 líneas de caché de 32B)
    static constexpr int MAX_RUNS = 24;

    u8 runCount;
    RLERun runs[MAX_RUNS];

    inline void initEmpty() {
        runCount = 1;
        runs[0].type = BlockType::AIR;
        runs[0].length = (u8)WorldConfig::SIZE_Y; // 128 bloques de aire
    }"""

rle_new = """// Verificación de protección estricta de memoria para VRAM de la GPU
static inline bool isVramPointer(const void* ptr) {
    uintptr_t addr = (uintptr_t)ptr;
    return (addr >= 0x06000000 && addr < 0x07000000);
}

struct __attribute__((aligned(2))) RLERun {
    BlockType type; // 1 byte: tipo de bloque
    u8 length;      // 1 byte: longitud del tramo (1..128)
};

// Alineación estricta de 32 bits (4 bytes) para evitar desfasamientos de memoria en GPU/DMA
class __attribute__((aligned(4))) VoxelColumnRLE {
public:
    // 24 tramos x 2 bytes = 48 bytes por columna
    static constexpr int MAX_RUNS = 24;

    u8 runCount;
    u8 _pad[3]; // Relleno explícito a 32 bits: sizeof(VoxelColumnRLE) = 52 bytes (múltiplo de 4)
    RLERun runs[MAX_RUNS];

    inline void initEmpty() {
        runCount = 1;
        _pad[0] = _pad[1] = _pad[2] = 0;
        runs[0].type = BlockType::AIR;
        runs[0].length = (u8)WorldConfig::SIZE_Y; // 128 bloques de aire
    }"""

assert rle_old in rle_content, "VoxelRLE target mismatch!"
with open(voxel_rle_path, "w", encoding="utf-8") as f:
    f.write(rle_content.replace(rle_old, rle_new))
print("Patched source/VoxelRLE.h")

# 2. Patch source/AsyncSaveManager.h
asm_h_path = "source/AsyncSaveManager.h"
with open(asm_h_path, "r", encoding="utf-8") as f:
    asm_h = f.read()

asm_h_old = """    struct SaveTask {
        char path[96];
        int dataSize;
        u8 data[MAX_BUFFER_SIZE];
        volatile bool inUse;
    };"""

asm_h_new = """    // Estructura estrictamente alineada a 32 bits para DMA y coprocesador
    struct __attribute__((aligned(4))) SaveTask {
        char path[96];
        int dataSize;
        u8 data[MAX_BUFFER_SIZE] __attribute__((aligned(4)));
        volatile bool inUse;
        u8 _pad[3];
    };"""

assert asm_h_old in asm_h, "AsyncSaveManager.h SaveTask target mismatch!"
asm_h = asm_h.replace(asm_h_old, asm_h_new)

asm_h_q_old = "    static SaveTask s_queue[QUEUE_CAPACITY];"
asm_h_q_new = "    static SaveTask s_queue[QUEUE_CAPACITY] __attribute__((aligned(4)));"
assert asm_h_q_old in asm_h, "AsyncSaveManager.h s_queue target mismatch!"
asm_h = asm_h.replace(asm_h_q_old, asm_h_q_new)

with open(asm_h_path, "w", encoding="utf-8") as f:
    f.write(asm_h)
print("Patched source/AsyncSaveManager.h")

# 3. Patch source/AsyncSaveManager.cpp
asm_cpp_path = "source/AsyncSaveManager.cpp"
with open(asm_cpp_path, "r", encoding="utf-8") as f:
    asm_cpp = f.read()

asm_cpp_def_old = "AsyncSaveManager::SaveTask AsyncSaveManager::s_queue[AsyncSaveManager::QUEUE_CAPACITY] = {};"
asm_cpp_def_new = "AsyncSaveManager::SaveTask AsyncSaveManager::s_queue[AsyncSaveManager::QUEUE_CAPACITY] __attribute__((aligned(4))) = {};"
assert asm_cpp_def_old in asm_cpp, "AsyncSaveManager.cpp definition mismatch!"
asm_cpp = asm_cpp.replace(asm_cpp_def_old, asm_cpp_def_new)

asm_cpp_enq_old = """bool AsyncSaveManager::enqueueSave(const char* path, const u8* compData, int compSize) {
    if (!s_initialized) init();
    if (!path || !compData || compSize <= 0) return false;
    if (compSize > MAX_BUFFER_SIZE) return false;"""

asm_cpp_enq_new = """bool AsyncSaveManager::enqueueSave(const char* path, const u8* compData, int compSize) {
    if (!s_initialized) init();
    if (!path || !compData || compSize <= 0) return false;
    if (compSize > MAX_BUFFER_SIZE) return false;

    // Protección absoluta de VRAM: rechazar punteros de bancos de video 3D (0x06000000..0x06FFFFFF)
    uintptr_t srcAddr = (uintptr_t)compData;
    if (srcAddr >= 0x06000000 && srcAddr < 0x07000000) return false;"""

assert asm_cpp_enq_old in asm_cpp, "AsyncSaveManager.cpp enqueueSave mismatch!"
asm_cpp = asm_cpp.replace(asm_cpp_enq_old, asm_cpp_enq_new)

with open(asm_cpp_path, "w", encoding="utf-8") as f:
    f.write(asm_cpp)
print("Patched source/AsyncSaveManager.cpp")

# 4. Patch source/ChunkCompression.h
cc_h_path = "source/ChunkCompression.h"
with open(cc_h_path, "r", encoding="utf-8") as f:
    cc_h = f.read()

cc_comp_old = """    static int compressLZ10(const u8* src, int srcLen, u8* dst, int maxDstLen) {
        if (!src || !dst || srcLen <= 0 || maxDstLen < 8) return 0;"""

cc_comp_new = """    static int compressLZ10(const u8* src, int srcLen, u8* dst, int maxDstLen) {
        if (!src || !dst || srcLen <= 0 || maxDstLen < 8) return 0;

        // Protección absoluta de VRAM: no comprimir desde ni hacia bancos VRAM de la GPU
        uintptr_t srcAddr = (uintptr_t)src;
        uintptr_t dstAddr = (uintptr_t)dst;
        if ((srcAddr >= 0x06000000 && srcAddr < 0x07000000) ||
            (dstAddr >= 0x06000000 && dstAddr < 0x07000000)) {
            return 0;
        }"""

assert cc_comp_old in cc_h, "ChunkCompression compressLZ10 mismatch!"
cc_h = cc_h.replace(cc_comp_old, cc_comp_new)

cc_decomp_old = """    // Descompresión por hardware/BIOS usando libnds
    static inline bool decompressBIOS(const void* src, void* dst) {
        if (!src || !dst) return false;
        const u8* p = (const u8*)src;
        if (p[0] != 0x10) return false; // Comprobación de cabecera LZ10

        // Llama a la rutina en ROM/BIOS a través de la SWI de libnds
        decompress(src, dst, LZ77);
        return true;
    }"""

cc_decomp_new = """    // Descompresión por hardware/BIOS usando libnds
    static inline bool decompressBIOS(const void* src, void* dst) {
        if (!src || !dst) return false;

        uintptr_t srcAddr = (uintptr_t)src;
        uintptr_t dstAddr = (uintptr_t)dst;

        // Protección absoluta de VRAM: no descompresión a bancos VRAM del motor 3D
        if ((srcAddr >= 0x06000000 && srcAddr < 0x07000000) ||
            (dstAddr >= 0x06000000 && dstAddr < 0x07000000)) {
            return false;
        }

        // Validación estricta de alineación de 32 bits requerida por la BIOS (SWI LZ77)
        if (((srcAddr | dstAddr) & 3) != 0) return false;

        const u8* p = (const u8*)src;
        if (p[0] != 0x10) return false; // Comprobación de cabecera LZ10

        // Llama a la rutina en ROM/BIOS a través de la SWI de libnds
        decompress(src, dst, LZ77);
        return true;
    }"""

assert cc_decomp_old in cc_h, "ChunkCompression decompressBIOS mismatch!"
cc_h = cc_h.replace(cc_decomp_old, cc_decomp_new)

with open(cc_h_path, "w", encoding="utf-8") as f:
    f.write(cc_h)
print("Patched source/ChunkCompression.h")

# 5. Patch source/Chunk.h
chunk_h_path = "source/Chunk.h"
with open(chunk_h_path, "r", encoding="utf-8") as f:
    chk_h = f.read()

chk_h_old = """    u32 canaryBeforeBlocks = 0xDEAD0001;
    BlockType blocks[WorldConfig::SIZE_X][WorldConfig::SIZE_Y][WorldConfig::SIZE_Z];
    VoxelColumnRLE rleCols[WorldConfig::SIZE_X][WorldConfig::SIZE_Z];
    u32 canaryAfterBlocks = 0xDEAD0002;
    u32 canaryBeforeFaceCache = 0xDEAD0003;
    FaceMask faceCache[WorldConfig::SIZE_X][WorldConfig::SIZE_Y][WorldConfig::SIZE_Z];
    u32 canaryAfterFaceCache = 0xDEAD0004;"""

chk_h_new = """    u32 canaryBeforeBlocks = 0xDEAD0001;
    BlockType blocks[WorldConfig::SIZE_X][WorldConfig::SIZE_Y][WorldConfig::SIZE_Z] __attribute__((aligned(4)));
    VoxelColumnRLE rleCols[WorldConfig::SIZE_X][WorldConfig::SIZE_Z] __attribute__((aligned(4)));
    u32 canaryAfterBlocks = 0xDEAD0002;
    u32 canaryBeforeFaceCache = 0xDEAD0003;
    FaceMask faceCache[WorldConfig::SIZE_X][WorldConfig::SIZE_Y][WorldConfig::SIZE_Z] __attribute__((aligned(4)));
    u32 canaryAfterFaceCache = 0xDEAD0004;"""

assert chk_h_old in chk_h, "Chunk.h blocks/rleCols mismatch!"
chk_h = chk_h.replace(chk_h_old, chk_h_new)

chk_occ_old = """    u32 canaryBeforeOccupancy = 0xDEAD0005;
    unsigned int occupancy[WorldConfig::SIZE_X][WorldConfig::SIZE_Z][4] = {};
    u32 canaryAfterOccupancy = 0xDEAD0006;"""

chk_occ_new = """    u32 canaryBeforeOccupancy = 0xDEAD0005;
    unsigned int occupancy[WorldConfig::SIZE_X][WorldConfig::SIZE_Z][4] __attribute__((aligned(4))) = {};
    u32 canaryAfterOccupancy = 0xDEAD0006;"""

assert chk_occ_old in chk_h, "Chunk.h occupancy mismatch!"
chk_h = chk_h.replace(chk_occ_old, chk_occ_new)

chk_liq_old = """    static constexpr int LIQUID_META_BYTES = WorldConfig::SIZE_X * WorldConfig::SIZE_Y * WorldConfig::SIZE_Z / 2;
    u8 liquidMeta[LIQUID_META_BYTES] = {};"""

chk_liq_new = """    static constexpr int LIQUID_META_BYTES = WorldConfig::SIZE_X * WorldConfig::SIZE_Y * WorldConfig::SIZE_Z / 2;
    u8 liquidMeta[LIQUID_META_BYTES] __attribute__((aligned(4))) = {};"""

assert chk_liq_old in chk_h, "Chunk.h liquidMeta mismatch!"
chk_h = chk_h.replace(chk_liq_old, chk_liq_new)

with open(chunk_h_path, "w", encoding="utf-8") as f:
    f.write(chk_h)
print("Patched source/Chunk.h")

# 6. Patch source/Chunk.cpp
chunk_cpp_path = "source/Chunk.cpp"
with open(chunk_cpp_path, "r", encoding="utf-8") as f:
    chk_cpp = f.read()

# callListFast vertex buffer sync
clf_old = """static inline void callListFast(const u32* list) {
    const u32 count = *list++;
    while ((DMA_CR(0) | DMA_CR(1) | DMA_CR(2) | DMA_CR(3)) & DMA_BUSY) {}
    DMA_SRC(0) = (uint32)list;
    DMA_DEST(0) = 0x4000400;
    DMA_CR(0) = DMA_FIFO | count;
    while (DMA_CR(0) & DMA_BUSY) {}
}"""

clf_new = """static inline void callListFast(const u32* list) {
    if (!list) return;
    const u32 count = *list++;
    if (count == 0) return;
    while ((DMA_CR(0) | DMA_CR(1) | DMA_CR(2) | DMA_CR(3)) & DMA_BUSY) {}
    while (GFX_BUSY) {} // Sincronización del bus de geometría para evitar desalineación de matrices
    DMA_SRC(0) = (uint32)list;
    DMA_DEST(0) = 0x4000400;
    DMA_CR(0) = DMA_FIFO | count;
    while (DMA_CR(0) & DMA_BUSY) {}
}"""

assert clf_old in chk_cpp, "Chunk.cpp callListFast mismatch!"
chk_cpp = chk_cpp.replace(clf_old, clf_new)

# scratch buffer alignment
scratch_old = """static const u32 DL_SCRATCH_WORDS = 6144;
static u32 s_dlScratch[DL_SCRATCH_WORDS + 1];"""

scratch_new = """static const u32 DL_SCRATCH_WORDS = 6144;
static u32 s_dlScratch[DL_SCRATCH_WORDS + 1] __attribute__((aligned(4)));"""

assert scratch_old in chk_cpp, "Chunk.cpp s_dlScratch mismatch!"
chk_cpp = chk_cpp.replace(scratch_old, scratch_new)

# save buffers alignment in saveToFileAsync
s_save_async_old = """bool Chunk::saveToFileAsync(const char* path) const {
    if (!generationComplete) return false;
    static u8 s_rawSaveBuf[sizeof(blocks) + sizeof(liquidMeta)];
    static u8 s_compSaveBuf[sizeof(s_rawSaveBuf) + 256];"""

s_save_async_new = """bool Chunk::saveToFileAsync(const char* path) const {
    if (!generationComplete) return false;
    static u8 s_rawSaveBuf[sizeof(blocks) + sizeof(liquidMeta)] __attribute__((aligned(4)));
    static u8 s_compSaveBuf[sizeof(s_rawSaveBuf) + 256] __attribute__((aligned(4)));"""

assert s_save_async_old in chk_cpp, "Chunk.cpp saveToFileAsync mismatch!"
chk_cpp = chk_cpp.replace(s_save_async_old, s_save_async_new)

# save buffers in saveToFile
s_save_old = """    // Buffer de ensamblado de bloques y metadatos de fluidos (12288 bytes)
    static u8 s_rawSaveBuf[sizeof(blocks) + sizeof(liquidMeta)];
    static u8 s_compSaveBuf[sizeof(s_rawSaveBuf) + 256];"""

s_save_new = """    // Buffer de ensamblado de bloques y metadatos de fluidos (12288 bytes)
    static u8 s_rawSaveBuf[sizeof(blocks) + sizeof(liquidMeta)] __attribute__((aligned(4)));
    static u8 s_compSaveBuf[sizeof(s_rawSaveBuf) + 256] __attribute__((aligned(4)));"""

assert s_save_old in chk_cpp, "Chunk.cpp saveToFile mismatch!"
chk_cpp = chk_cpp.replace(s_save_old, s_save_new)

# load buffers in loadFromFile
s_load_old = """    static u8 s_rawLoadBuf[sizeof(blocks) + sizeof(liquidMeta)];
    static u8 s_compLoadBuf[sizeof(s_rawLoadBuf) + 256];"""

s_load_new = """    static u8 s_rawLoadBuf[sizeof(blocks) + sizeof(liquidMeta)] __attribute__((aligned(4)));
    static u8 s_compLoadBuf[sizeof(s_rawLoadBuf) + 256] __attribute__((aligned(4)));"""

assert s_load_old in chk_cpp, "Chunk.cpp loadFromFile mismatch!"
chk_cpp = chk_cpp.replace(s_load_old, s_load_new)

with open(chunk_cpp_path, "w", encoding="utf-8") as f:
    f.write(chk_cpp)
print("Patched source/Chunk.cpp")

# 7. Patch source/Hardware.h
hw_h_path = "source/Hardware.h"
with open(hw_h_path, "r", encoding="utf-8") as f:
    hw_h = f.read()

hw_old = """        if (g_isDSi) {
            // Activar reloj a 133.12 MHz (TWL Mode) en CPU ARM9
            setCpuClock(true);

            // Verificación segura leyendo el registro SCFG_CLK (bit 0 = 133 MHz)
            // Solo se lee en DSi (en DS original causaría bus error de memoria)
            u16 clk = REG_SCFG_CLK;
            if ((clk & 1) != 0 || g_isDSi) {
                ocFlag() = true;
                cpuFreqRef() = 133;
            } else {
                ocFlag() = false;
                cpuFreqRef() = 67;
            }
        }"""

hw_new = """    // Conmutación segura de frecuencia ejecutada en ITCM conforme a las especificaciones GBATEK
    ITCM_CODE static void applyClockSafeTWL() {
        // Preservar configuración previa de EXMEMCNT (waitstates de bus de VRAM, ROM y SD)
        u16 oldExmem = REG_EXMEMCNT;

        // Conmutar CPU ARM9 a alta velocidad (134.06 MHz)
        setCpuClock(true);

        // Restaurar de forma estricta los waitstates de bus para que VRAM y SD no colapsen
        REG_EXMEMCNT = oldExmem;

        // Esperar ciclos de reloj en ITCM para que el bus y PLL se estabilicen
        for (volatile int i = 0; i < 128; i++) {
            __asm__ volatile("nop");
        }

        // Sincronizar memorias intermedias y cachés
        DC_FlushAll();
        IC_InvalidateAll();
    }

public:
    static inline void initHardwareProfile() {
        if (initedRef()) return;
        initedRef() = true;

        g_isDSi = isDSiMode();

        if (g_isDSi) {
            // Conmutación segura de reloj preservando waitstates de bus y VRAM
            applyClockSafeTWL();

            // Verificación segura leyendo el registro SCFG_CLK (bit 0 = 133 MHz)
            u16 clk = REG_SCFG_CLK;
            if ((clk & 1) != 0 || g_isDSi) {
                ocFlag() = true;
                cpuFreqRef() = 133;
            } else {
                ocFlag() = false;
                cpuFreqRef() = 67;
            }
        }"""

# Look at private section in Hardware.h
hw_section_old = """class Hardware {
private:
    static inline bool& ocFlag() { static bool o = false; return o; }
    static inline int& cpuFreqRef() { static int f = 67; return f; }
    static inline bool& initedRef() { static bool i = false; return i; }

public:
    static inline void initHardwareProfile() {
        if (initedRef()) return;
        initedRef() = true;

        g_isDSi = isDSiMode();

        if (g_isDSi) {
            // Activar reloj a 133.12 MHz (TWL Mode) en CPU ARM9
            setCpuClock(true);

            // Verificación segura leyendo el registro SCFG_CLK (bit 0 = 133 MHz)
            // Solo se lee en DSi (en DS original causaría bus error de memoria)
            u16 clk = REG_SCFG_CLK;
            if ((clk & 1) != 0 || g_isDSi) {
                ocFlag() = true;
                cpuFreqRef() = 133;
            } else {
                ocFlag() = false;
                cpuFreqRef() = 67;
            }
        }"""

hw_section_new = """class Hardware {
private:
    static inline bool& ocFlag() { static bool o = false; return o; }
    static inline int& cpuFreqRef() { static int f = 67; return f; }
    static inline bool& initedRef() { static bool i = false; return i; }

""" + hw_new

assert hw_section_old in hw_h, "Hardware.h initHardwareProfile mismatch!"
hw_h = hw_h.replace(hw_section_old, hw_section_new)

with open(hw_h_path, "w", encoding="utf-8") as f:
    f.write(hw_h)
print("Patched source/Hardware.h")

# 8. Patch source/Renderer.cpp
rend_path = "source/Renderer.cpp"
with open(rend_path, "r", encoding="utf-8") as f:
    rend_cpp = f.read()

rend_old = """    glFogColor(20, 20, 31, 31); // se sobreescribe cada frame en main.cpp según la hora
    glEnable(GL_FOG);
}"""

rend_new = """    glFogColor(20, 20, 31, 31); // se sobreescribe cada frame en main.cpp según la hora
    glEnable(GL_FOG);
    glMatrixMode(GL_MODELVIEW); // Restablecer siempre el modo de matrices a MODELVIEW para proteger la proyección
}"""

assert rend_old in rend_cpp, "Renderer.cpp setupProjection mismatch!"
rend_cpp = rend_cpp.replace(rend_old, rend_new)

with open(rend_path, "w", encoding="utf-8") as f:
    f.write(rend_cpp)
print("Patched source/Renderer.cpp")

# 9. Patch source/main.cpp
main_path = "source/main.cpp"
with open(main_path, "r", encoding="utf-8") as f:
    main_cpp = f.read()

# drawAll post-cull sanity
drawall_old = """            { PROF(Prof::DRAW_ALL); chunkManager->drawAll(player->x, player->y, player->z, lookDirX, lookDirY, lookDirZ); }
            const u32 entsStartTicks = Prof::now();   // lo que se dibuja despues del terreno (mobs, objetos, particulas, clima, HUD...)"""

drawall_new = """            glMatrixMode(GL_MODELVIEW);
            { PROF(Prof::DRAW_ALL); chunkManager->drawAll(player->x, player->y, player->z, lookDirX, lookDirY, lookDirZ); }

            // Saneamiento de bus DMA y GPU tras descarte/renderizado de chunks
            while ((DMA_CR(0) | DMA_CR(3)) & DMA_BUSY);
            while (GFX_BUSY);
            glMatrixMode(GL_MODELVIEW);

            // Verificación y saneamiento del stack de matrices ante posibles desbordamientos
            if (GFX_STATUS & BIT(15)) {
                glResetMatrixStack();
                renderer.setupProjection();
                glMatrixMode(GL_MODELVIEW);
                player->applyCamera(partialTick, 0.0f);
            }

            const u32 entsStartTicks = Prof::now();   // lo que se dibuja despues del terreno (mobs, objetos, particulas, clima, HUD...)"""

assert drawall_old in main_cpp, "main.cpp drawAll mismatch!"
main_cpp = main_cpp.replace(drawall_old, drawall_new)

# glFlush vertex buffer cleanup
flush_old = """            if (timeInPortal > 0.0f) drawPortalOverlay(timeInPortal);

            Prof::add(Prof::ENTS, Prof::now() - entsStartTicks);
            glFlush(0);"""

flush_new = """            if (timeInPortal > 0.0f) drawPortalOverlay(timeInPortal);

            // Saneamiento del búfer de vértices y aseguramiento de primitivas cerradas antes de glFlush
            glEnd();
            while (GFX_BUSY);
            glMatrixMode(GL_MODELVIEW);
            GFX_CONTROL |= GL_POLY_OVERFLOW | GL_COLOR_UNDERFLOW;

            Prof::add(Prof::ENTS, Prof::now() - entsStartTicks);
            glFlush(0);"""

assert flush_old in main_cpp, "main.cpp glFlush mismatch!"
main_cpp = main_cpp.replace(flush_old, flush_new)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(main_cpp)
print("Patched source/main.cpp")

print("ALL PATCHES APPLIED SUCCESSFULLY!")

