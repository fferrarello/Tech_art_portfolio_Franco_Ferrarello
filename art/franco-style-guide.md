📌 Overview



Este documento define las reglas visuales para la creación de sprites para el juego the Office.



El objetivo es garantizar:



Consistencia visual

Legibilidad en baja resolución

Producción escalable



🎥 Cámara y Perspectiva

📐 Tipo de cámara

Isométrica modificada (2:1 pixel ratio)

Ángulo aproximado:

Rotación Y: 45°

Rotación X: \~30°–35°

👁️ Vistas requeridas

3/4 Frente

3/4 Espalda

📊 Ejemplo conceptual

&#x20;      ↖ cámara

&#x20;        \\

&#x20;         \\   (personaje)

&#x20;          🧍

📦 Resolución y Grid

Tamaño base: 32x32 px

Grid: 1px exacto (pixel perfect)

No anti-aliasing automático

Snap siempre activado

📏 Uso del espacio

Personaje típico: 24–28 px de alto

Margen superior: evitar overflow

Base alineada al suelo (consistente entre assets)

🧍 Proporciones del Personaje

Parte	Proporción aproximada

Cabeza	25–30%

Torso	30–35%

Piernas	35–40%

📌 Reglas clave

Silueta clara > detalle interno

Evitar tangentes visuales

Priorizar lectura a distancia

🎨 Paleta de Color

🎯 Reglas

Máximo recomendado: 12–16 colores por sprite

Separar:

Base

Sombra

Highlight

💡 Iluminación

Luz principal: arriba-izquierda

Sombra: abajo-derecha

🌈 Contraste

Alto contraste en bordes exteriores

Bajo contraste en detalles internos

✏️ Lineart

Grosor: 1px

Color: no usar negro puro (#000000)

Preferido: tonos oscuros del mismo color base

Lineart selectivo (no encerrar todo)

🧩 Volumen y Sombreado

📐 Técnica

Cel shading simplificado

Máximo:

1 tono base

1 sombra

1 highlight



🧭 Orientación (3/4)

Frente

Se ven:

Cara parcial

Pecho

Parte frontal de piernas

Espalda

Se ven:

Espalda

Parte trasera de cabeza

Talones

🔄 Consistencia

Mantener volumen idéntico entre vistas

🚶 Animación
FPS recomendado
6–12 fps
Ciclos básicos
Idle
Walk (4–6 frames)
Run (6–8 frames)
📌 Regla clave
Movimiento claro > fluidez extrema

🧱 Tiles y Entorno

Misma perspectiva que personajes

Altura consistente

Bordes alineados a grid

📁 Naming Convention

char\_<tipo>\_<accion>\_<direccion>\_<frame>.png

Ejemplo:

char\_knight\_walk\_front\_01.png

char\_knight\_walk\_back\_03.png

🧪 Checklist de Calidad



Antes de exportar:



&#x20;Silueta clara a zoom 1x

&#x20;No hay pixels sueltos

&#x20;Consistencia de luz

&#x20;Alineación al grid

&#x20;Colores dentro de paleta

&#x20;Lectura correcta en 3/4

📤 Export

Formato: PNG

Fondo: transparente

Escala: 1x (no upscale)

Sin compresión con pérdida

⚙️ Pipeline Recomendado
Sketch (bloques básicos)
Silueta limpia
Color base
Sombra
Highlights
Polish (cleanup)

