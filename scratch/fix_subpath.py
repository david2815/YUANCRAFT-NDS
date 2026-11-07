with open("source/WorldSelectMenu.cpp", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("char subPath[96];", "char subPath[290];")

with open("source/WorldSelectMenu.cpp", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated subPath buffer to 290")

