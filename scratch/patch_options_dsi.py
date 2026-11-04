with open('source/Options.cpp', 'r', encoding='utf-8') as f:
    text = f.read()

if '#include "Hardware.h"' not in text:
    text = '#include "Hardware.h"\n' + text

text = text.replace('isDSiMode()', 'g_isDSi')

with open('source/Options.cpp', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated source/Options.cpp to use g_isDSi')

