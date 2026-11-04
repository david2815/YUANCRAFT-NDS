import sys

with open('source/main.cpp', 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize to LF
norm = content.replace('\r\n', '\n')

old_entry = """int main(void) {
    // 1. Registro e inicializacion prioritaria de interrupciones de hardware (IRQ VBLANK)
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

new_entry = """int main(void) {
    // 1. Inicializacion sincrona inmediata del sistema de archivos FAT
    // Debe ser lo primero que se ejecute de forma sincrona en el punto de entrada
    bool fatOk = fatInitDefault();

    // Deshabilitacion condicional absoluta de lectura/escritura de logs en SD si FAT falla
    // El juego prioriza arrancar los menus por encima de la depuracion
    DebugLogger::init(fatOk);

    // 2. Registro e inicializacion prioritaria de interrupciones de hardware
    irqInit();
    irqEnable(IRQ_VBLANK);

    // 3. Inicializacion de la consola nativa de texto en pantalla inferior
    consoleDemoInit();

    // 4. Deteccion basica de plataforma sin alterar reloj ni registros TWL (67 MHz NTR base)
    g_isDSi = isDSiMode();

    if (!fatOk) {
        iprintf("[DEBUG] AVISO: SD no disponible / libfat fallo. Modo seguro en pantalla.\\n");
        DebugLogger::log("[DEBUG] AVISO: Modo seguro activado. Tarjeta SD no disponible.");
    } else {
        iprintf("[DEBUG] libfat inicializado correctamente.\\n");
        DebugLogger::log("[DEBUG] Sistema de archivos FAT inicializado correctamente.");
    }

    // Sincronizacion y purga de coprocesadores matematicos (REG_DIV / REG_SQRT inactivos)
    HwMath::sync();

    // 5. Inicializacion del subsistema grafico 3D en pantalla superior
    Renderer renderer;
    renderer.init();
    renderer.setupProjection();

    // 6. Retraso de seguridad de hardware de 30 frames inmediatamente despues de inicializar
    // la pantalla superior para permitir la estabilizacion fisica de los bancos de VRAM y el bus SD
    for (int i = 0; i < 30; i++) {
        swiWaitForVBlank();
    }

    // 7. Pantallas de inicio (logos de Eagtek y Mojang) a reloj base seguro (67 MHz)
    // Sin hilos de fondo ni solicitudes IPC, usando unicamente bucles simples con swiWaitForVBlank()
    StartupSplash::show();"""

assert old_entry in norm, "old_entry not found in main.cpp!"
norm = norm.replace(old_entry, new_entry, 1)

old_menu = """    StartupSplash::finish();   // todo cargado: la pantalla de abajo vuelve a la normalidad y el menu toma las dos pantallas
    SubScreenMenu::init(fatOk ? WorldSave::worldSlotExists(1) : false);
    TopScreenMenu::init();

    GameState state = STATE_MENU;"""

new_menu = """    StartupSplash::finish();   // todo cargado: la pantalla de abajo vuelve a la normalidad y el menu toma las dos pantallas
    SubScreenMenu::init(fatOk ? WorldSave::worldSlotExists(1) : false);
    TopScreenMenu::init();

    // Conmutacion de reloj a 133 MHz SOLO tras pasar la pantalla del logo y cargar el menu principal
    if (fatOk) {
        Hardware::initHardwareProfile();
        Hardware::printHardwareInfo();
        DebugLogger::log("[DEBUG] Perfil de hardware: %s @ %d MHz", Hardware::getDeviceName(), Hardware::getCpuFrequencyMHz());
        AsyncSaveManager::init();
    }

    GameState state = STATE_MENU;"""

assert old_menu in norm, "old_menu not found in main.cpp!"
norm = norm.replace(old_menu, new_menu, 1)

with open('source/main.cpp', 'w', encoding='utf-8', newline='\n') as f:
    f.write(norm)

print("SUCCESS: patch_main_safe_seq.py applied successfully!")
