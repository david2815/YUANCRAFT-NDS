with open("source/HandAnimations.cpp", "r", encoding="utf-8") as f:
    c = f.read()

target1 = "mapQuad(x0 * P, y0 * P, x1 * P, y1 * P, 0.0f, cr * sc / 255, cg * sc / 255, cb * sc / 255);"
replacement1 = "mapQuad(x0 * P, y0 * P, x1 * P, y1 * P, 0.0f, (cr * sc * 257) >> 16, (cg * sc * 257) >> 16, (cb * sc * 257) >> 16);"
assert target1 in c, "target1 not found"
c = c.replace(target1, replacement1)

target2 = "mapQuad((float)(i * k) * P, (float)(j * k) * P, (float)((i + run) * k) * P, (float)((j + 1) * k) * P, -0.008f, r * sc / 255, g * sc / 255, bl * sc / 255);"
replacement2 = "mapQuad((float)(i * k) * P, (float)(j * k) * P, (float)((i + run) * k) * P, (float)((j + 1) * k) * P, -0.008f, (r * sc * 257) >> 16, (g * sc * 257) >> 16, (bl * sc * 257) >> 16);"
assert target2 in c, "target2 not found"
c = c.replace(target2, replacement2)

with open("source/HandAnimations.cpp", "w", encoding="utf-8") as f:
    f.write(c)
print("Replaced divisions in HandAnimations.cpp successfully")

