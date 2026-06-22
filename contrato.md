# [ CONTEXTO Y ROL ]
Actúa como un Desarrollador Web Geoespacial Experto. Tu objetivo es construir el cascarón arquitectónico (UI) para un dashboard de análisis territorial interactivo. 

# [ RESTRICCIONES TÉCNICAS (Protocolo KISS) ]
El principio KISS lo aplicaremos estrictamente para la programación; el rigor lo dejaremos exclusivamente para la gestión territorial y los datos. Por lo tanto:
1. Genera un único archivo `index.html`. Nada de múltiples archivos.
2. Prohibido usar frameworks de JS (ni React, ni Vue). Usa exclusivamente Vanilla JS.
3. Prohibido escribir código CSS personalizado o usar etiquetas `<style>`. Utiliza estrictamente clases de Tailwind CSS importado vía CDN.
4. Importa MapLibre GL JS vía CDN en el `<head>`.

# [ ARQUITECTURA VISUAL (Cyberpunk / High-Contrast UI) ]
La interfaz debe tener una estética Dark Sci-Fi / Synthwave para evitar la fatiga visual al analizar datos espaciales densos:
1. **Layout General:** Pantalla completa (`h-screen w-full`), sin scroll, usando flexbox.
2. **Lienzo Base:** Fondo oscuro profundo (`bg-slate-950`) y texto principal en gris claro (`text-slate-300`). Tipografía de sistema sin remates.
3. **Estructura de Paneles:**
   - **Panel Lateral (Izquierda):** Ocupa exactamente el 25% del ancho (`w-1/4`). Aplica un efecto 'Glassmorphism' intenso (`backdrop-blur-md bg-white/5`). Añade un borde derecho con un resplandor neón magenta o cyan (ej. `border-r border-cyan-500/50 shadow-[4px_0_15px_#06b6d4]`).
   - **Contenedor Principal (Derecha):** Ocupa el 75% restante (`w-3/4`). Este es el lienzo para el motor espacial.
4. **Tipografía de Datos:** Usa una fuente Monospace (`font-mono`) de color vibrante (ej. texto neón cyan o magenta) exclusivamente para los títulos y números clave del panel, simulando una terminal de datos.

# [ LÓGICA ESPACIAL Y DATOS (QUÉ HACER) ]
1. En el contenedor principal (derecha), crea un `<div id="map">` que ocupe el 100% de su contenedor padre (`h-full w-full`).
2. En el panel lateral, incluye:
   - Un título principal en la parte superior: "SISTEMA DE MONITOREO TERRITORIAL".
   - Una sección debajo llamada "Control de Capas".
   - Un botón de acción con estilo Neobrutalista/Cyberpunk (fondo transparente, borde grueso cyan, texto cyan que brille al hacer hover) con el texto: "INICIALIZAR MAPLIBRE".
3. No agregues la lógica de inicialización del mapa todavía. Solo deja la estructura del DOM lista y perfecta.