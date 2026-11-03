import os

path = r"source/SettingsMenu.cpp"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target1 = "static const int ROW_COUNT = 13;"
replacement1 = "static const int ROW_COUNT = 14;"

target2 = """        case 12: printRow(sel, "inventoryMap", Options::get().inventoryMap ? "true" : "false"); break;
    }"""
replacement2 = """        case 12: printRow(sel, "inventoryMap", Options::get().inventoryMap ? "true" : "false"); break;
        case 13: printRow(sel, "fps counter", Options::get().showFps ? "on" : "off"); break;
    }"""

target3 = """        } else if (s_selected == 12) {
            Options::get().inventoryMap = !Options::get().inventoryMap;
            Options::save();
            draw();"""

replacement3 = """        } else if (s_selected == 12) {
            Options::get().inventoryMap = !Options::get().inventoryMap;
            Options::save();
            draw();
        } else if (s_selected == 13) {
            Options::get().showFps = !Options::get().showFps;
            Options::save();
            draw();"""

if target1 in content and target2 in content and target3 in content:
    content = content.replace(target1, replacement1, 1)
    content = content.replace(target2, replacement2, 1)
    content = content.replace(target3, replacement3, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SettingsMenu.cpp updated successfully.")
else:
    print("Could not match all targets in SettingsMenu.cpp!")

