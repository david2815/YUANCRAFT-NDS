# Reglas del Proyecto: YUANCRAFT-NDS (Minecraft DS Port)

## REGLA ESTRICTA Y OBLIGATORIA: FLUJO DE TRABAJO CON GRAPHIFY
Como este es un proyecto colaborativo que requiere máximo orden y consistencia entre compañeros de equipo:

1. **ANTES de realizar cualquier cambio, responder consultas de arquitectura o implementar funciones:**
   - Consultar obligatoriamente el grafo de conocimiento en `graphify-out/`:
     - `graphify query "<pregunta o concepto>"` para búsquedas contextuales de dependencias.
     - `graphify path "<nodoA>" "<nodoB>"` para entender cómo se relacionan componentes.
     - `graphify explain "<concepto o función>"` para inspeccionar un nodo y sus llamadas.
     - Si existe `graphify-out/wiki/index.md`, revisar la documentación antes de leer archivos dispersos.
   - Respetar la arquitectura existente y verificar los vínculos entre módulos.

2. **DESPUÉS de realizar cualquier modificación en el código o archivos del proyecto:**
   - Ejecutar obligatoriamente la actualización del grafo:
     ```sh
     graphify update .
     ```
   - Esto sincroniza el AST y las relaciones sin costo de API, manteniendo el grafo listo para los demás colaboradores.

3. **Restricciones técnicas del hardware (Nintendo DS):**
   - ARM946E-S @ 67 MHz, **sin FPU** (evitar `float`/`double` en bucles críticos; usar enteros / punto fijo).
   - **4 MB de RAM principal** casi al límite: no agregar buffers o tablas estáticas grandes sin evaluar su impacto.
   - Límite de geometría: ~2048 polígonos / ~6144 vértices por frame.
   - Texturas en paletas de 16 o 256 colores vía VRAM.
   - Mantener fidelidad a la versión original de referencia (Minecraft Beta 1.7.3).

