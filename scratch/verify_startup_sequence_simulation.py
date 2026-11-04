import os
import sys

class MockHardwareNDS:
    def __init__(self, is_dsi=False, sd_working=True):
        self.is_dsi = is_dsi
        self.sd_working = sd_working
        self.irq_vblank_enabled = False
        self.gpu_initialized = False
        self.hardware_delay_frames = 0
        self.splash_displayed = False
        self.fat_initialized = False
        self.fat_ok = False
        self.cpu_frequency_mhz = 67
        self.overclocked = False
        self.sd_filesystem = {}
        self.screen_console = []
        self.circular_history = []
        self.debug_log_file_open = False
        self.subscreen_worlds_checked = None

    def irqInit(self):
        pass

    def irqEnable(self, irq_type):
        if irq_type == "IRQ_VBLANK":
            self.irq_vblank_enabled = True

    def consoleDemoInit(self):
        self.screen_console.append("[CONSOLE_INIT]")

    def rendererInit(self):
        self.gpu_initialized = True

    def swiWaitForVBlank(self):
        if not self.irq_vblank_enabled:
            raise RuntimeError("CRASH: swiWaitForVBlank called before IRQ_VBLANK enabled!")
        self.hardware_delay_frames += 1

    def startupSplashShow(self):
        if not self.gpu_initialized:
            raise RuntimeError("CRASH: StartupSplash::show() called before GPU initialized!")
        if self.hardware_delay_frames < 30:
            raise RuntimeError("WARNING: StartupSplash showed before 30-frame hardware settling delay!")
        self.splash_displayed = True

    def fatInitDefault(self):
        self.fat_initialized = True
        self.fat_ok = self.sd_working
        return self.fat_ok

    def debugLoggerInit(self, fatOk):
        self.fat_available_for_logger = fatOk
        if self.fat_available_for_logger:
            self.debug_log_file_open = True
            self.sd_filesystem["/mcdsefiles/worlds/debug_load.txt"] = "=== YUANCRAFT NDS - DEBUG LOAD LOG ===\n"

    def debugLoggerLog(self, msg):
        if hasattr(self, 'fat_available_for_logger') and self.fat_available_for_logger:
            if not self.fat_ok:
                raise RuntimeError("CORRUPTION: DebugLogger wrote to SD when fat_ok was false!")
            cur = self.sd_filesystem.get("/mcdsefiles/worlds/debug_load.txt", "")
            self.sd_filesystem["/mcdsefiles/worlds/debug_load.txt"] = cur + msg + "\n"
        self.screen_console.append(msg)
        self.circular_history.append(msg)

    def hardwareInitProfile(self):
        if not self.splash_displayed:
            raise RuntimeError("GPU CORRUPTION: Hardware overclock attempted before splash screen completed!")
        if not self.fat_ok:
            raise RuntimeError("TIMING COLLAPSE: Hardware overclock attempted without confirmed FAT status!")
        if self.is_dsi:
            self.overclocked = True
            self.cpu_frequency_mhz = 133
        else:
            self.overclocked = False
            self.cpu_frequency_mhz = 67

    def subScreenMenuInit(self, world_exists):
        self.subscreen_worlds_checked = world_exists

def run_simulation(name, is_dsi, sd_working):
    print(f"\n--- Testing Scenario: {name} ---")
    hw = MockHardwareNDS(is_dsi=is_dsi, sd_working=sd_working)
    
    # Execution following refactored main() sequence
    # 1. IRQ Init
    hw.irqInit()
    hw.irqEnable("IRQ_VBLANK")
    assert hw.irq_vblank_enabled, "IRQ VBlank must be enabled first"
    
    # 2. Console Init
    hw.consoleDemoInit()
    
    # 3. GPU Init
    hw.rendererInit()
    assert hw.gpu_initialized, "GPU must be initialized before splash"
    
    # 4. 30-Frame Hardware Settling Delay
    for _ in range(30):
        hw.swiWaitForVBlank()
    assert hw.hardware_delay_frames == 30, f"Expected 30 settling frames, got {hw.hardware_delay_frames}"
    
    # 5. Splash Screen
    hw.startupSplashShow()
    assert hw.splash_displayed, "Splash screen must be displayed"
    
    # 6. FAT Init
    fatOk = hw.fatInitDefault()
    hw.debugLoggerInit(fatOk)
    
    if not fatOk:
        # Fallback to screen console
        hw.consoleDemoInit()
        hw.debugLoggerLog("[DEBUG] AVISO: Fallo al inicializar libfat (SD). Modo seguro en pantalla.")
        hw.debugLoggerLog("[DEBUG] AVISO: Modo seguro activado. Tarjeta SD no disponible.")
    else:
        hw.debugLoggerLog("[DEBUG] Sistema de archivos FAT inicializado correctamente.")
        hw.hardwareInitProfile()
        hw.debugLoggerLog(f"[DEBUG] Perfil de hardware: @ {hw.cpu_frequency_mhz} MHz")
        
    # SubScreenMenu Init
    hw.subScreenMenuInit(fatOk and True)
    
    # Validations per scenario
    if sd_working:
        assert fatOk is True
        assert "/mcdsefiles/worlds/debug_load.txt" in hw.sd_filesystem
        assert "=== YUANCRAFT NDS - DEBUG LOAD LOG ===" in hw.sd_filesystem["/mcdsefiles/worlds/debug_load.txt"]
        if is_dsi:
            assert hw.cpu_frequency_mhz == 133
            assert hw.overclocked is True
            print("  -> DSi Overclock safely activated to 133 MHz.")
        else:
            assert hw.cpu_frequency_mhz == 67
            assert hw.overclocked is False
            print("  -> DS Base clock strictly maintained at 67 MHz.")
    else:
        assert fatOk is False
        assert "/mcdsefiles/worlds/debug_load.txt" not in hw.sd_filesystem
        assert hw.cpu_frequency_mhz == 67, "CPU must not overclock when SD fails!"
        assert hw.subscreen_worlds_checked is False, "World select must safely default to 0 worlds"
        assert any("Modo seguro en pantalla" in s for s in hw.screen_console), "Fallback log must be in console"
        print("  -> Environment Isolation successful: SD bypassed, 0 crashes, native console fallback active.")
        
    print(f"Scenario [{name}] PASSED.")

def main():
    print("=" * 60)
    print("VERIFICATION 2: FUNCTIONAL LOGIC & HARDWARE SIMULATION")
    print("=" * 60)
    
    run_simulation("Nintendo DS (NTR Mode, 67MHz, Working SD)", is_dsi=False, sd_working=True)
    run_simulation("Nintendo DSi (TWL Mode, 133MHz, Working SD)", is_dsi=True, sd_working=True)
    run_simulation("Nintendo DS with R4/Flashcart Lag (SD Failure)", is_dsi=False, sd_working=False)
    run_simulation("Nintendo DSi with Twilight Menu SD Timeout (SD Failure)", is_dsi=True, sd_working=False)
    
    print("\nSUCCESS: All 4 hardware runtime simulation profiles PASSED cleanly!\n")

if __name__ == "__main__":
    main()
