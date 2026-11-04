import os, sys, re

def verify_structural():
    print("=== VERIFICATION 1: STRUCTURAL AST & STATIC CODE CHECK ===")
    errors = []

    # 1. ChunkManager.cpp
    with open("source/ChunkManager.cpp", "r", encoding="utf-8") as f:
        cm = f.read()
    if "polyBudget = (Options::get().renderQuality == 2) ? 1400 : ((Options::get().renderQuality == 1) ? 1700 : 2000)" not in cm:
        errors.append("ChunkManager.cpp: polyBudget not strictly capped to 2000")
    if "vertBudget = polyBudget * 2;" not in cm:
        errors.append("ChunkManager.cpp: vertBudget not set to polyBudget * 2")
    if "if (vertBudget <= 0 || (GFX_CONTROL & GL_POLY_OVERFLOW))" not in cm:
        errors.append("ChunkManager.cpp: overflow and vertBudget check missing before draw loop")

    # 2. Chunk.cpp
    with open("source/Chunk.cpp", "r", encoding="utf-8") as f:
        chk = f.read()
    if "if (GFX_CONTROL & GL_POLY_OVERFLOW)" not in chk:
        errors.append("Chunk.cpp: GFX_CONTROL & GL_POLY_OVERFLOW check missing in Chunk::draw")

    # 3. main.cpp
    with open("source/main.cpp", "r", encoding="utf-8") as f:
        main_c = f.read()
    if "HwMath::sync();" not in main_c:
        errors.append("main.cpp: HwMath::sync() missing at shouldRender start")
    if "glMatrixMode(GL_MODELVIEW);" not in main_c or "glLoadIdentity();" not in main_c:
        errors.append("main.cpp: glMatrixMode(GL_MODELVIEW) and glLoadIdentity() missing at shouldRender start")

    # 4. HwMath.h
    with open("source/HwMath.h", "r", encoding="utf-8") as f:
        hw = f.read()
    if "static inline void sync()" not in hw:
        errors.append("HwMath.h: HwMath::sync() not defined")
    if "while (REG_DIVCNT & DIV_BUSY);" not in hw or "while (REG_SQRTCNT & SQRT_BUSY);" not in hw:
        errors.append("HwMath.h: sync() doesn't wait for both DIV_BUSY and SQRT_BUSY")

    # 5. Math inside glBegin/glEnd check
    files_to_check = [
        "source/Sky.cpp",
        "source/SteveModel.cpp",
        "source/AnimalModel.cpp",
        "source/HealthHud.cpp",
        "source/HandAnimations.cpp"
    ]
    for filepath in files_to_check:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        in_gl = False
        for idx, line in enumerate(lines):
            l = line.strip()
            if "glBegin" in l and not l.startswith("//"):
                in_gl = True
            elif "glEnd" in l and not l.startswith("//"):
                in_gl = False
            elif in_gl:
                # Check for active hardware/software division or sqrt
                if not l.startswith("//"):
                    if "sqrtf(" in l:
                        errors.append(f"{filepath}:{idx+1}: sqrtf called inside glBegin block!")
                    if "/ Z0" in l:
                        errors.append(f"{filepath}:{idx+1}: division by Z0 inside glBegin block!")
                    if "/ 255" in l:
                        errors.append(f"{filepath}:{idx+1}: division / 255 inside glBegin block!")

    # 6. WorldSelectMenu
    with open("source/WorldSelectMenu.h", "r", encoding="utf-8") as f:
        wsm_h = f.read()
    if "static void refreshWorldList();" not in wsm_h:
        errors.append("WorldSelectMenu.h: refreshWorldList() declaration missing")

    with open("source/WorldSelectMenu.cpp", "r", encoding="utf-8") as f:
        wsm_cpp = f.read()
    if "void WorldSelectMenu::refreshWorldList()" not in wsm_cpp:
        errors.append("WorldSelectMenu.cpp: refreshWorldList() definition missing")
    if "memset(worldList, 0, sizeof(worldList));" not in wsm_cpp:
        errors.append("WorldSelectMenu.cpp: memset(worldList, 0, ...) missing")
    if "opendir(\"/mcdsefiles/worlds\")" not in wsm_cpp:
        errors.append("WorldSelectMenu.cpp: opendir(/mcdsefiles/worlds) missing")
    if "selectWorldNoWorldBitmap" not in wsm_cpp:
        errors.append("WorldSelectMenu.cpp: selectWorldNoWorldBitmap missing for empty worlds")
    if "clearLabelZone" not in wsm_cpp:
        errors.append("WorldSelectMenu.cpp: clearLabelZone missing")
    if "if (worldCount <= 0) return false;" not in wsm_cpp:
        errors.append("WorldSelectMenu.cpp: touch guard for worldCount <= 0 missing in delete/play")

    # 7. WorldSave.cpp
    with open("source/WorldSave.cpp", "r", encoding="utf-8") as f:
        ws_cpp = f.read()
    if "WorldSelectMenu::refreshWorldList();" not in ws_cpp:
        errors.append("WorldSave.cpp: WorldSelectMenu::refreshWorldList() not called in deleteWorld")
    if "unlink(fullPath);" not in ws_cpp:
        errors.append("WorldSave.cpp: unlink(fullPath) missing in clearFolderContents")

    if errors:
        print("[FAIL] Verification 1 encountered errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("[PASS] Verification 1 PASSED: All structural rules and hardware constraints verified!")

if __name__ == "__main__":
    verify_structural()
