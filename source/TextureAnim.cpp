#include "TextureAnim.h"
#include "TextureAnimCore.h"
#include "AnimData.h"
#include "Texture.h"
#include "terrain.h"
#include "AnimItems.h"
#include <nds.h>

namespace {
    unsigned char s_mapFire0[ANIM_COLORS];
    unsigned char s_mapFire1[ANIM_COLORS];
    unsigned char s_mapPortal[ANIM_COLORS];
    unsigned char* s_texture = nullptr;
    int s_vblanks = 0;
    int s_frame = 0;
}

void TextureAnim::init() {
    s_texture = nullptr;

    // El puntero a la textura tiene que caer en el banco de texturas A..D mapeado como LCD (0x06800000..0x06880000); si no, sin animación
    unsigned int addr = (unsigned int)glGetTexturePointer(Texture::textureID);
    if (addr < 0x06800000u || addr >= 0x06880000u) return;

    const unsigned short* pal = (const unsigned short*)terrainPal;
    TextureAnimCore::buildMap(FIRE0_COLORS, ANIM_COLORS, pal, s_mapFire0);
    TextureAnimCore::buildMap(FIRE1_COLORS, ANIM_COLORS, pal, s_mapFire1);
    TextureAnimCore::buildMap(PORTAL_COLORS, ANIM_COLORS, pal, s_mapPortal);

    s_texture = (unsigned char*)addr;
    s_vblanks = 0;
    s_frame = 0;
}

void TextureAnim::onVBlank() {
    // Protección Absoluta de la VRAM y Buffers de Pantalla (Regla 1 de GEMINI.md):
    // Prohíbe terminantemente compartir, modificar o alterar los punteros asignados
    // a los bancos de VRAM (Bancos A, B, C o D) utilizados por el motor 3D de libnds.
    // Alternar los bancos A y D entre LCD y TEXTURE en medio de la ejecución provoca
    // corrupción gráfica inmediata, pantallas negras y congelamiento total de la GPU.
    return;
}
