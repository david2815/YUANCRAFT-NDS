import sys

with open('source/main.cpp', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace block 1
block1_old = """    consoleDemoInit();

    // Verificacion y deteccion dinamica de hardware en arranque
    g_isDSi = isDSiMode();
    Hardware::initHardwareProfile();
    Hardware::printHardwareInfo();
    AsyncSaveManager::init();

    Renderer renderer;
    renderer.init();
    renderer.setupProjection();

    StartupSplash::show();   // logos de Eagtek y Mojang (1 s cada uno) al arrancar, antes de cargar nada"""

block1_new = """    // 1. Registro e inicializacion prioritaria de interrupciones de hardware (IRQ VBLANK)
    irqInit();
    irqEnable(IRQ_VBLANK);

    // 2. Inicializacion de la consola nativa de texto en pantalla inferior
    consoleDemoInit();

    // 3. Deteccion basica y segura de plataforma sin conmutar relojes de hardware prematuramente
    g_isDSi = isDSiMode();

    // 4. Inicializacion del subsistema grafico 3D en pantalla superior
    Renderer renderer;
    renderer.init();
    renderer.setupProjection();

    // 5. Retraso de seguridad de hardware de 30 frames inmediatamente despues de inicializar
    // la pantalla superior para permitir la estabilizacion fisica de los bancos de VRAM y el bus SD
    for (int i = 0; i < 30; i++) {
        swiWaitForVBlank();
    }

    // 6. Despliegue completo de las pantallas de presentacion (logos de Eagtek y Mojang)
    StartupSplash::show();   // logos de Eagtek y Mojang (1 s cada uno) al arrancar, antes de cargar nada

    // 7. Inicializacion segura del sistema de archivos FAT y aislamiento de entorno
    bool fatOk = fatInitDefault();
    DebugLogger::init(fatOk);

    if (!fatOk) {
        // Aislamiento de entorno: Si la SD fisica falla o tarda en responder (R4 / Twilight Menu),
        // omitir logs en la SD y redirigir la depuracion exclusivamente a la salida de texto nativa
        consoleDemoInit();
        iprintf("[DEBUG] AVISO: Fallo al inicializar libfat (SD). Modo seguro en pantalla.\\n");
        DebugLogger::log("[DEBUG] AVISO: Modo seguro activado. Tarjeta SD no disponible.");
    } else {
        DebugLogger::log("[DEBUG] Sistema de archivos FAT inicializado correctamente.");
        // Conmutacion segura a frecuencia DSi (133 MHz) SOLO tras confirmar FAT (TRUE) y con logo desplegado
        Hardware::initHardwareProfile();
        Hardware::printHardwareInfo();
        DebugLogger::log("[DEBUG] Perfil de hardware: %s @ %d MHz", Hardware::getDeviceName(), Hardware::getCpuFrequencyMHz());
        AsyncSaveManager::init();
    }"""

# Normalize CRLF/LF for matching
norm_content = content.replace('\r\n', '\n')
assert block1_old in norm_content, "Block 1 old not found!"

norm_content = norm_content.replace(block1_old, block1_new, 1)

# Replace block 2 (the old IRQ, DebugLogger, fatInitDefault block)
block2_old = """    // Registro y activaci\xc3\xb3n estricta de interrupciones de hardware
    irqInit();
    irqEnable(IRQ_VBLANK);

    // Inyecci\xc3\xb3n obligatoria de mensajes de depuraci\xc3\xb3n en arranque
    DebugLogger::init();
    DebugLogger::log("[DEBUG] Inicializando sistema de archivos FAT...");

    if (!fatInitDefault()) {
        iprintf("ERROR: libfat init failed\\n");
        DebugLogger::log("[DEBUG] ERROR: Fallo al inicializar libfat.");
    } else {
        iprintf("libfat initialized\\n");
        DebugLogger::log("[DEBUG] Sistema de archivos FAT inicializado correctamente.");
    }
    Prof::init();
    WorldSave::ensureDirectoryStructure();
    Options::load();
    Sound::init();   // los menus tambien suenan
    Controls::load();   // perfiles de controles (controlsprofile.dat)
    autoJumpEnabled = Options::get().autoJump;
    controlMode = Options::get().controlMode;
    WorldSave::recoverInterruptedSession();"""

# Also handle if the comment has non-utf8 or whatever character
if block2_old not in norm_content:
    # let's find the lines from Prof::init() backwards
    idx_prof = norm_content.find("Prof::init();")
    assert idx_prof != -1, "Prof::init() not found!"
    # find where "selectedSlotChangedByTouch = false;" is
    idx_start = norm_content.find("selectedSlotChangedByTouch = false;\n", 0, idx_prof)
    assert idx_start != -1, "selectedSlotChangedByTouch not found!"
    idx_start += len("selectedSlotChangedByTouch = false;\n\n")
    # find where "WorldSave::recoverInterruptedSession();" ends
    idx_end = norm_content.find("WorldSave::recoverInterruptedSession();", idx_prof) + len("WorldSave::recoverInterruptedSession();")
    
    old_slice = norm_content[idx_start:idx_end]
    print("Found old slice to replace:")
    print(repr(old_slice))
    
    block2_new = """    Prof::init();
    if (fatOk) {
        WorldSave::ensureDirectoryStructure();
        Options::load();
        Controls::load();   // perfiles de controles (controlsprofile.dat)
        WorldSave::recoverInterruptedSession();
    }
    Sound::init();   // los menus tambien suenan
    autoJumpEnabled = Options::get().autoJump;
    controlMode = Options::get().controlMode;"""
    
    norm_content = norm_content[:idx_start] + block2_new + norm_content[idx_end:]
else:
    block2_new = """    Prof::init();
    if (fatOk) {
        WorldSave::ensureDirectoryStructure();
        Options::load();
        Controls::load();   // perfiles de controles (controlsprofile.dat)
        WorldSave::recoverInterruptedSession();
    }
    Sound::init();   // los menus tambien suenan
    autoJumpEnabled = Options::get().autoJump;
    controlMode = Options::get().controlMode;"""
    norm_content = norm_content.replace(block2_old, block2_new, 1)

# Block 3: SubScreenMenu::init
block3_old = "SubScreenMenu::init(WorldSave::worldSlotExists(1));"
block3_new = "SubScreenMenu::init(fatOk ? WorldSave::worldSlotExists(1) : false);"
assert block3_old in norm_content, "Block 3 old not found!"
norm_content = norm_content.replace(block3_old, block3_new, 1)

# Write back preserving CRLF
with open('source/main.cpp', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(norm_content.replace('\n', '\r\n'))

print("Patch applied successfully to source/main.cpp!")
