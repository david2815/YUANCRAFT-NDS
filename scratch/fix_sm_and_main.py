# 1. Fix SettingsMenu.cpp
with open('source/SettingsMenu.cpp', 'r', encoding='utf-8') as f:
    sm_text = f.read()

sm_text = sm_text.replace(
    'static int s_view = 0;\n    s_showingPopUp = false;              // 0 = lista de opciones',
    'static int s_view = 0;              // 0 = lista de opciones'
)

# In SettingsMenu::open():
if 's_showingPopUp = false;' not in sm_text.split('void SettingsMenu::open()')[1]:
    sm_text = sm_text.replace(
        'void SettingsMenu::open() {\n    s_selected = 0;\n    s_top = 0;\n    s_view = 0;',
        'void SettingsMenu::open() {\n    s_selected = 0;\n    s_top = 0;\n    s_view = 0;\n    s_showingPopUp = false;'
    )

with open('source/SettingsMenu.cpp', 'w', encoding='utf-8') as f:
    f.write(sm_text)
print('Fixed source/SettingsMenu.cpp')

# 2. Fix main.cpp keyscan
with open('source/main.cpp', 'r', encoding='utf-8') as f:
    m_text = f.read()

old_keys = """        scanKeys();
        u32 keys_down = keysDown();
        u32 keys_held = keysHeld();"""

new_keys = """        scanKeys();
        u32 keys_down = keysDown();
        u32 keys_held = keysHeld();
        if (saveLocked) {
            keys_down = 0;
            keys_held = 0;
        }"""

if old_keys in m_text:
    m_text = m_text.replace(old_keys, new_keys, 1)
    print('Fixed main.cpp keyscan with saveLocked')
else:
    print('Warning: old_keys not found in main.cpp')

with open('source/main.cpp', 'w', encoding='utf-8') as f:
    f.write(m_text)
print('Fixed source/main.cpp')

