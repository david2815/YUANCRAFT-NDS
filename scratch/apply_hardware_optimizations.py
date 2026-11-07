import re

def patch_player():
    with open("source/Player.h", "rb") as f:
        content = f.read().decode("utf-8")
    
    if '#include "HwMath.h"' not in content:
        content = '#include "HwMath.h"\r\n' + content
    
    # Declare ITCM_CODE on critical methods
    content = content.replace(
        "void physicsTick(u32 keysHeld, const ChunkManager& chunkManager, bool autoJumpEnabled);",
        "ITCM_CODE void physicsTick(u32 keysHeld, const ChunkManager& chunkManager, bool autoJumpEnabled);"
    )
    content = content.replace(
        "bool collidesAt(const ChunkManager& chunkManager, float testX, float testY, float testZ) const;",
        "ITCM_CODE bool collidesAt(const ChunkManager& chunkManager, float testX, float testY, float testZ) const;"
    )
    
    with open("source/Player.h", "wb") as f:
        f.write(content.encode("utf-8"))
    print("Patched source/Player.h")

    with open("source/Player.cpp", "rb") as f:
        c_cpp = f.read().decode("utf-8")

    if '#include "HwMath.h"' not in c_cpp:
        c_cpp = '#include "HwMath.h"\r\n' + c_cpp

    # Replace sqrtf with HwMath::sqrtf
    c_cpp = c_cpp.replace("float inputMag = sqrtf(", "float inputMag = HwMath::sqrtf(")
    c_cpp = c_cpp.replace("float speed = sqrtf(", "float speed = HwMath::sqrtf(")
    c_cpp = c_cpp.replace("float moveSpeed = sqrtf(", "float moveSpeed = HwMath::sqrtf(")
    c_cpp = c_cpp.replace("float speed2 = sqrtf(", "float speed2 = HwMath::sqrtf(")
    c_cpp = c_cpp.replace("float d = sqrtf(", "float d = HwMath::sqrtf(")

    # Replace divisions in physics
    c_cpp = c_cpp.replace(
        "float k = accel / inputMag;",
        "float k = HwMath::divf(accel, inputMag);"
    )
    c_cpp = c_cpp.replace(
        "float scale = MAX_SPEED / speed;",
        "float scale = HwMath::divf(MAX_SPEED, speed);"
    )
    c_cpp = c_cpp.replace(
        "float dirX = velocityX / moveSpeed;",
        "float dirX = HwMath::divf(velocityX, moveSpeed);"
    )
    c_cpp = c_cpp.replace(
        "float dirZ = velocityZ / moveSpeed;",
        "float dirZ = HwMath::divf(velocityZ, moveSpeed);"
    )
    c_cpp = c_cpp.replace(
        "float t = (float)s / (float)(SAMPLES - 1);",
        "float t = HwMath::divf((float)s, (float)(SAMPLES - 1));"
    )
    c_cpp = c_cpp.replace(
        "velocityX -= dx / d * 0.4f;",
        "velocityX -= HwMath::divf(dx, d) * 0.4f;"
    )
    c_cpp = c_cpp.replace(
        "velocityZ -= dz / d * 0.4f;",
        "velocityZ -= HwMath::divf(dz, d) * 0.4f;"
    )

    # ITCM_CODE on implementation
    c_cpp = c_cpp.replace(
        "void Player::physicsTick(u32 keysHeld, const ChunkManager& chunkManager, bool autoJumpEnabled) {",
        "ITCM_CODE void Player::physicsTick(u32 keysHeld, const ChunkManager& chunkManager, bool autoJumpEnabled) {"
    )
    c_cpp = c_cpp.replace(
        "bool Player::collidesAt(const ChunkManager& chunkManager, float testX, float testY, float testZ) const {",
        "ITCM_CODE bool Player::collidesAt(const ChunkManager& chunkManager, float testX, float testY, float testZ) const {"
    )

    with open("source/Player.cpp", "wb") as f:
        f.write(c_cpp.encode("utf-8"))
    print("Patched source/Player.cpp")

def patch_raycaster():
    with open("source/Raycaster.cpp", "rb") as f:
        content = f.read().decode("utf-8")

    if '#include "HwMath.h"' not in content:
        content = '#include "HwMath.h"\r\n' + content

    old_dda = """        float tX = 999.0f, tY = 999.0f, tZ = 999.0f;
        if (activeX) tX = (boundX - px) / remainX;
        if (activeY) tY = (boundY - (py + Y_ALIGN_OFFSET)) / remainY;
        if (activeZ) tZ = (boundZ - pz) / remainZ;"""

    new_dda = """        float tX = 999.0f, tY = 999.0f, tZ = 999.0f;
        if (activeX) tX = HwMath::divf(boundX - px, remainX);
        if (activeY) tY = HwMath::divf(boundY - (py + Y_ALIGN_OFFSET), remainY);
        if (activeZ) tZ = HwMath::divf(boundZ - pz, remainZ);"""

    content = content.replace(old_dda, new_dda)

    with open("source/Raycaster.cpp", "wb") as f:
        f.write(content.encode("utf-8"))
    print("Patched source/Raycaster.cpp")

def patch_torch_and_partial():
    # Torch.h
    with open("source/Torch.h", "rb") as f:
        t_content = f.read().decode("utf-8")
    if '#include "HwMath.h"' not in t_content:
        t_content = '#include "HwMath.h"\r\n' + t_content
    t_content = t_content.replace(
        "float t = (v - a[axis]) / d;",
        "float t = HwMath::divf(v - a[axis], d);"
    )
    with open("source/Torch.h", "wb") as f:
        f.write(t_content.encode("utf-8"))
    print("Patched source/Torch.h")

    # PartialBlocks.cpp
    with open("source/PartialBlocks.cpp", "rb") as f:
        p_content = f.read().decode("utf-8")
    if '#include "HwMath.h"' not in p_content:
        p_content = '#include "HwMath.h"\r\n' + p_content
    p_content = p_content.replace(
        "float t1 = (bd[i] - s[i]) / d, t2 = (bd[i + 3] - s[i]) / d;",
        "float t1 = HwMath::divf(bd[i] - s[i], d), t2 = HwMath::divf(bd[i + 3] - s[i], d);"
    )
    with open("source/PartialBlocks.cpp", "wb") as f:
        f.write(p_content.encode("utf-8"))
    print("Patched source/PartialBlocks.cpp")

def patch_voxel_rle():
    with open("source/VoxelRLE.h", "rb") as f:
        content = f.read().decode("utf-8")
    
    # ITCM_CODE on unpack
    content = content.replace(
        "inline void unpack(BlockType* out128) const {",
        "ITCM_CODE void unpack(BlockType* out128) const {"
    )
    with open("source/VoxelRLE.h", "wb") as f:
        f.write(content.encode("utf-8"))
    print("Patched source/VoxelRLE.h")

def patch_chunk():
    with open("source/Chunk.h", "rb") as f:
        h_content = f.read().decode("utf-8")
    h_content = h_content.replace(
        "void rebuildColumnOccupancy(int xi, int zi);",
        "ITCM_CODE void rebuildColumnOccupancy(int xi, int zi);"
    )
    h_content = h_content.replace(
        "void computeColumnFacesBitwise(int xi, int zi, const class ChunkManager* manager);",
        "ITCM_CODE void computeColumnFacesBitwise(int xi, int zi, const class ChunkManager* manager);"
    )
    with open("source/Chunk.h", "wb") as f:
        f.write(h_content.encode("utf-8"))
    print("Patched source/Chunk.h")

    with open("source/Chunk.cpp", "rb") as f:
        c_content = f.read().decode("utf-8")

    # ITCM_CODE on implementations
    c_content = c_content.replace(
        "void Chunk::rebuildColumnOccupancy(int xi, int zi) {",
        "ITCM_CODE void Chunk::rebuildColumnOccupancy(int xi, int zi) {"
    )
    c_content = c_content.replace(
        "void Chunk::computeColumnFacesBitwise(int xi, int zi, const ChunkManager* manager) {",
        "ITCM_CODE void Chunk::computeColumnFacesBitwise(int xi, int zi, const ChunkManager* manager) {"
    )

    # Replace display list memcpy with dmaCopyWords
    old_band_copy = "memcpy(buf, s_dlScratch, (1 + bodyWords) * sizeof(u32)); // la palabra 0 ya trae el tamao"
    # check variations of comment
    idx1 = c_content.find("memcpy(buf, s_dlScratch, (1 + bodyWords) * sizeof(u32));")
    if idx1 != -1:
        # find end of line
        end_idx1 = c_content.find("\n", idx1)
        old_line1 = c_content[idx1:end_idx1].rstrip("\r")
        new_line1 = "dmaCopyWords(3, s_dlScratch, buf, (1 + bodyWords) * sizeof(u32));"
        c_content = c_content.replace(old_line1, new_line1, 1)
        print("Replaced band geometry memcpy with dmaCopyWords")
    else:
        print("Warning: band geometry memcpy not found")

    idx2 = c_content.find("memcpy(buf, s_dlScratch, (1 + words) * sizeof(u32));")
    if idx2 != -1:
        end_idx2 = c_content.find("\n", idx2)
        old_line2 = c_content[idx2:end_idx2].rstrip("\r")
        new_line2 = "dmaCopyWords(3, s_dlScratch, buf, (1 + words) * sizeof(u32));"
        c_content = c_content.replace(old_line2, new_line2, 1)
        print("Replaced lod geometry memcpy with dmaCopyWords")
    else:
        print("Warning: lod geometry memcpy not found")

    with open("source/Chunk.cpp", "wb") as f:
        f.write(c_content.encode("utf-8"))
    print("Patched source/Chunk.cpp")

def patch_main():
    with open("source/main.cpp", "rb") as f:
        content = f.read().decode("utf-8")

    # Add DTCM player and chunk pointers
    dtcm_defs = """// Fast Data Tightly Coupled Memory (DTCM) para acceso a latencia cero
static DTCM_BSS Player s_dtcmPlayer;
static DTCM_BSS Chunk* s_dtcmCurrentChunk = nullptr;
static DTCM_BSS Chunk* s_dtcmActiveChunks[9];
"""
    if "s_dtcmPlayer" not in content:
        content = content.replace("Player* player = nullptr;", "Player* player = nullptr;\r\n" + dtcm_defs, 1)

    # Change player = new Player(); to use s_dtcmPlayer
    # Line 701: player = new Player(); -> player = &s_dtcmPlayer; *player = Player();
    content = content.replace(
        "player = new Player();\r\n        inventoryOpen = false;",
        "player = &s_dtcmPlayer;\r\n        *player = Player();\r\n        s_dtcmCurrentChunk = nullptr;\r\n        inventoryOpen = false;"
    )

    # Line 930: delete player; player = new Player(); -> *player = Player();
    content = content.replace(
        "delete player;\r\n        player = new Player();       // cuerpo entero otra vez",
        "*player = Player();       // cuerpo entero en DTCM otra vez"
    )

    # Update s_dtcmCurrentChunk each frame right around chunkManager->update
    old_update = "AsyncSaveManager::processQueue();"
    new_update = "AsyncSaveManager::processQueue();\r\n        s_dtcmCurrentChunk = chunkManager ? chunkManager->getCenterChunk() : nullptr;"
    if "s_dtcmCurrentChunk = chunkManager" not in content:
        content = content.replace(old_update, new_update, 1)

    with open("source/main.cpp", "wb") as f:
        f.write(content.encode("utf-8"))
    print("Patched source/main.cpp")

def patch_renderer():
    with open("source/Renderer.cpp", "rb") as f:
        content = f.read().decode("utf-8")
    
    # Ensure glEnable(GL_FOG) is called in Renderer::init()
    if "glEnable(GL_FOG);" not in content.split("void Renderer::setupProjection")[0]:
        content = content.replace(
            "glViewport(0, 0, 255, 191);\r\n}",
            "glViewport(0, 0, 255, 191);\r\n    glEnable(GL_FOG);\r\n}"
        )
        print("Enabled GL_FOG in Renderer::init()")

    with open("source/Renderer.cpp", "wb") as f:
        f.write(content.encode("utf-8"))
    print("Patched source/Renderer.cpp")

if __name__ == "__main__":
    patch_player()
    patch_raycaster()
    patch_torch_and_partial()
    patch_voxel_rle()
    patch_chunk()
    patch_main()
    patch_renderer()
    print("All optimizations applied successfully!")

