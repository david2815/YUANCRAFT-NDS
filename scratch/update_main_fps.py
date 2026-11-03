import os

path = r"source/main.cpp"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add #include "MenuFont.h"
target_inc = '#include "Governor.h"'
replacement_inc = '#include "Governor.h"\n#include "MenuFont.h"'

if target_inc in content:
    content = content.replace(target_inc, replacement_inc, 1)
    print("MenuFont.h included.")
else:
    print("target_inc not found!")

# 2. Add FPS tracking and display in main loop
target_loop = """        Prof::add(Prof::FRAME, Prof::now() - frameStartTicks);
        Governor::onFrameEnd(Prof::now() - frameStartTicks);
        Prof::setContext((int)floorf(player->x), (int)floorf(player->y), (int)floorf(player->z), currentDimension);
        Prof::endFrame();
        static int profPrintCounter = 0;
        if (consoleVisible && !paused && ++profPrintCounter >= 30) {   // never over the pause menu
            profPrintCounter = 0;
            if (Options::get().debugCoordsOnly) {
                iprintf("\\x1b[2J");   // solo coordenadas: sin rendimiento ni memoria
            } else {
                Prof::print();
                iprintf("underflow %d\\noverflow  %d\\nRDLINES min %d\\n",
                        gfxUnderflowCount, gfxOverflowCount, rdLinesMin);
                int dlKB0 = Chunk::getDisplayListBytes() / 1024;
                if (dlKB0 > dlMaxKB) dlMaxKB = dlKB0;
                iprintf("DL %d KB (max %d)\\nChunks %dx%dK=%dK\\n", dlKB0, dlMaxKB, chunkManager->chunkCount(), (int)(sizeof(Chunk) / 1024), chunkManager->poolKB());
                iprintf("Health %d/20  damage %s (X) night (B)\\n", healthState.health, healthDamageEnabled ? "ON" : "OFF");
            }"""

replacement_loop = """        Prof::add(Prof::FRAME, Prof::now() - frameStartTicks);
        Governor::onFrameEnd(Prof::now() - frameStartTicks);
        Prof::setContext((int)floorf(player->x), (int)floorf(player->y), (int)floorf(player->z), currentDimension);
        Prof::endFrame();

        // --- Medicion y visualizacion de FPS en tiempo real (cero costo CPU) ---
        static u32 s_fpsLastTime = 0;
        static int s_fpsFrameAccum = 0;
        static int s_fpsCurrent = 0;
        static bool s_fpsWasDrawn = false;

        s_fpsFrameAccum++;
        u32 curTicks = Prof::now();
        if (curTicks - s_fpsLastTime >= 33513982) { // 1 segundo exacto de reloj bus NDS
            s_fpsCurrent = s_fpsFrameAccum;
            s_fpsFrameAccum = 0;
            s_fpsLastTime = curTicks;
        }

        if (Options::get().showFps) {
            static int s_fpsDrawCounter = 0;
            if (!consoleVisible && !paused && GameplayHotbar::getBgId() != -1 && ++s_fpsDrawCounter >= 15) {
                s_fpsDrawCounter = 0;
                u16* fb = (u16*)bgGetGfxPtr(GameplayHotbar::getBgId());
                char fpsBuf[12];
                snprintf(fpsBuf, sizeof(fpsBuf), "FPS %d", s_fpsCurrent);
                MenuFont::fill16(fb, 200, 30, 252, 42, RGB15(0, 0, 0) | BIT(15));
                MenuFont::draw16(fb, fpsBuf, 202, 32, 1, RGB15(31, 31, 0) | BIT(15));
                s_fpsWasDrawn = true;
            }
        } else if (s_fpsWasDrawn) {
            if (!consoleVisible && !paused && GameplayHotbar::getBgId() != -1) {
                u16* fb = (u16*)bgGetGfxPtr(GameplayHotbar::getBgId());
                MenuFont::fill16(fb, 200, 30, 252, 42, RGB15(0, 0, 0) | BIT(15));
            }
            s_fpsWasDrawn = false;
        }

        static int profPrintCounter = 0;
        if (consoleVisible && !paused && ++profPrintCounter >= 30) {   // never over the pause menu
            profPrintCounter = 0;
            if (Options::get().debugCoordsOnly) {
                iprintf("\\x1b[2J");   // solo coordenadas: sin rendimiento ni memoria
            } else {
                Prof::print();
                iprintf("underflow %d\\noverflow  %d\\nRDLINES min %d\\n",
                        gfxUnderflowCount, gfxOverflowCount, rdLinesMin);
                int dlKB0 = Chunk::getDisplayListBytes() / 1024;
                if (dlKB0 > dlMaxKB) dlMaxKB = dlKB0;
                iprintf("DL %d KB (max %d)\\nChunks %dx%dK=%dK\\n", dlKB0, dlMaxKB, chunkManager->chunkCount(), (int)(sizeof(Chunk) / 1024), chunkManager->poolKB());
                iprintf("Health %d/20  damage %s (X) night (B)\\n", healthState.health, healthDamageEnabled ? "ON" : "OFF");
            }
            if (Options::get().showFps) {
                iprintf("FPS %d\\n", s_fpsCurrent);
            }"""

if target_loop in content:
    content = content.replace(target_loop, replacement_loop, 1)
    print("Loop updated with FPS counter.")
else:
    print("target_loop not found!")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("main.cpp written.")

