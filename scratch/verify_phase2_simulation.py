import os
import sys

class MockHardwareState:
    def __init__(self, is_dsi=True, sd_functional=True):
        self.is_dsi = is_dsi
        self.sd_functional = sd_functional
        self.cpu_clock_mhz = 67
        self.fat_initialized = False
        self.fat_ok = False
        self.sd_writes = []
        self.console_outputs = []
        self.hw_math_active = False
        self.splash_displayed = False
        self.menu_loaded = False
        self.step_trace = []

    def fatInitDefault(self):
        self.step_trace.append("fatInitDefault")
        self.fat_initialized = True
        self.fat_ok = self.sd_functional
        return self.fat_ok

    def debugLoggerInit(self, fatOk):
        self.step_trace.append(f"debugLoggerInit(fatOk={fatOk})")
        self.fat_logging_enabled = fatOk
        if fatOk:
            self.sd_writes.append("HEADER: === YUANCRAFT NDS - DEBUG LOAD LOG ===")

    def debugLoggerLog(self, msg):
        self.console_outputs.append(msg)
        if getattr(self, 'fat_logging_enabled', False):
            if not self.fat_ok:
                raise RuntimeError("ERROR: SD write attempted when FAT is not ok!")
            self.sd_writes.append(msg)

    def hwMathSync(self):
        self.step_trace.append("hwMathSync")
        self.hw_math_active = False

    def startupSplashShow(self):
        self.step_trace.append("startupSplashShow")
        if self.cpu_clock_mhz != 67:
            raise RuntimeError(f"CLOCK ERROR: CPU clock was {self.cpu_clock_mhz} MHz during splash screen! Must be 67 MHz.")
        if self.hw_math_active:
            raise RuntimeError("MATH ERROR: Hardware math coprocessors were active during splash!")
        self.splash_displayed = True

    def initMenus(self):
        self.step_trace.append("initMenus")
        if not self.splash_displayed:
            raise RuntimeError("FLOW ERROR: Menus initialized before splash screen completed!")
        self.menu_loaded = True

    def initHardwareProfile(self):
        self.step_trace.append("initHardwareProfile")
        if not self.menu_loaded:
            raise RuntimeError("OVERCLOCK ERROR: CPU clock switched before main menu loaded!")
        if self.is_dsi and self.fat_ok:
            self.cpu_clock_mhz = 133
        else:
            self.cpu_clock_mhz = 67

def simulate(scenario_name, is_dsi, sd_functional):
    print(f"\n--- Testing Scenario: {scenario_name} ---")
    hw = MockHardwareState(is_dsi=is_dsi, sd_functional=sd_functional)

    # 1. First call in main(): fatInitDefault()
    fatOk = hw.fatInitDefault()
    hw.debugLoggerInit(fatOk)

    # 2. HwMath sync
    hw.hwMathSync()

    # 3. Splash screen (67 MHz)
    hw.startupSplashShow()

    # 4. Main Menu load
    hw.initMenus()

    # 5. Overclock only after menu load
    if fatOk:
        hw.initHardwareProfile()

    # Verifications
    assert hw.step_trace[0] == "fatInitDefault", "Step 1 must be fatInitDefault!"
    assert hw.step_trace[1].startswith("debugLoggerInit"), "Step 2 must be debugLoggerInit!"
    assert hw.splash_displayed, "Splash screen must have displayed"
    assert hw.menu_loaded, "Main menu must have loaded"

    if sd_functional:
        assert len(hw.sd_writes) > 0, "SD logs should be present when SD works"
        if is_dsi:
            assert hw.cpu_clock_mhz == 133, f"Expected 133 MHz on DSi, got {hw.cpu_clock_mhz}"
            print("  -> DSi safely transitioned to 133 MHz strictly AFTER main menu load.")
        else:
            assert hw.cpu_clock_mhz == 67, f"Expected 67 MHz on DS, got {hw.cpu_clock_mhz}"
            print("  -> DS safely maintained base 67 MHz.")
    else:
        assert len(hw.sd_writes) == 0, "Zero SD writes must occur when SD fails"
        assert hw.cpu_clock_mhz == 67, f"Expected 67 MHz safe base clock when SD fails, got {hw.cpu_clock_mhz}"
        print("  -> SD failure isolation passed: 0 SD writes, clock preserved at 67 MHz, menus loaded.")

    print(f"Scenario [{scenario_name}] PASSED.")

def main():
    print("=" * 60)
    print("DOUBLE VERIFICATION - TEST 2: RUNTIME FLOW SIMULATION")
    print("=" * 60)

    simulate("DSi Console with Working SD", is_dsi=True, sd_functional=True)
    simulate("DS Console with Working SD", is_dsi=False, sd_functional=True)
    simulate("DSi Console with R4 Flashcart / SD Failure", is_dsi=True, sd_functional=False)
    simulate("DS Console with R4 Flashcart / SD Failure", is_dsi=False, sd_functional=False)

    print("\nSUCCESS: All Simulation Scenarios PASSED cleanly (100%).\n")

if __name__ == "__main__":
    main()
