# Update SteveModel.cpp
with open("source/SteveModel.cpp", "r", encoding="utf-8") as f:
    sm = f.read()

sm_old = """            const int s = (v * FACE_SHADE[q[i].face] * 257) >> 16;
            const int cr = (c.r * s * 257) >> 16;
            const int cg = (int)(((c.g * s * 257) >> 16) * gb);
            const int cb = (int)(((c.b * s * 257) >> 16) * gb);"""

sm_new = """            const int s = ((v * FACE_SHADE[q[i].face] + 1) * 257) >> 16;
            const int cr = ((c.r * s + 1) * 257) >> 16;
            const int cg = (int)((((c.g * s + 1) * 257) >> 16) * gb);
            const int cb = (int)((((c.b * s + 1) * 257) >> 16) * gb);"""

assert sm_old in sm, "sm_old mismatch"
sm = sm.replace(sm_old, sm_new)
with open("source/SteveModel.cpp", "w", encoding="utf-8") as f:
    f.write(sm)
print("Updated SteveModel.cpp")

# Update AnimalModel.cpp
with open("source/AnimalModel.cpp", "r", encoding="utf-8") as f:
    am = f.read()

am_old = """            const int s = (v * SHADE[f] * 257) >> 16;
            const int cr = (r * s * 257) >> 16;
            const int cg = (int)(((g * s * 257) >> 16) * gb);
            const int cb = (int)(((b * s * 257) >> 16) * gb);"""

am_new = """            const int s = ((v * SHADE[f] + 1) * 257) >> 16;
            const int cr = ((r * s + 1) * 257) >> 16;
            const int cg = (int)((((g * s + 1) * 257) >> 16) * gb);
            const int cb = (int)((((b * s + 1) * 257) >> 16) * gb);"""

assert am_old in am, "am_old mismatch"
am = am.replace(am_old, am_new)
with open("source/AnimalModel.cpp", "w", encoding="utf-8") as f:
    f.write(am)
print("Updated AnimalModel.cpp")

# Update HandAnimations.cpp
with open("source/HandAnimations.cpp", "r", encoding="utf-8") as f:
    ha = f.read()

ha_old1 = "mapQuad(x0 * P, y0 * P, x1 * P, y1 * P, 0.0f, (cr * sc * 257) >> 16, (cg * sc * 257) >> 16, (cb * sc * 257) >> 16);"
ha_new1 = "mapQuad(x0 * P, y0 * P, x1 * P, y1 * P, 0.0f, ((cr * sc + 1) * 257) >> 16, ((cg * sc + 1) * 257) >> 16, ((cb * sc + 1) * 257) >> 16);"
assert ha_old1 in ha, "ha_old1 mismatch"
ha = ha.replace(ha_old1, ha_new1)

ha_old2 = "mapQuad((float)(i * k) * P, (float)(j * k) * P, (float)((i + run) * k) * P, (float)((j + 1) * k) * P, -0.008f, (r * sc * 257) >> 16, (g * sc * 257) >> 16, (bl * sc * 257) >> 16);"
ha_new2 = "mapQuad((float)(i * k) * P, (float)(j * k) * P, (float)((i + run) * k) * P, (float)((j + 1) * k) * P, -0.008f, ((r * sc + 1) * 257) >> 16, ((g * sc + 1) * 257) >> 16, ((bl * sc + 1) * 257) >> 16);"
assert ha_old2 in ha, "ha_old2 mismatch"
ha = ha.replace(ha_old2, ha_new2)

with open("source/HandAnimations.cpp", "w", encoding="utf-8") as f:
    f.write(ha)
print("Updated HandAnimations.cpp")

