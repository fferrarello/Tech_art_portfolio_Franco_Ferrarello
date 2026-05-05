# 🎮 Pixel Art Style Guide

### Isométrico 3/4 · 32x32 · Oficina / Coworking Creativo (Production Ready)

---

## 📌 Overview

Este documento define las reglas visuales para la creación de sprites dentro de un entorno de **oficina moderna / coworking creativo**, con foco en claridad visual, coherencia sistémica y escalabilidad en producción.

El objetivo es garantizar:

* Consistencia visual
* Legibilidad en baja resolución
* Producción escalable
* Integración correcta en engine

---

## 🎯 Dirección Artística

### 🏢 Contexto

* Espacios de coworking
* Oficinas modernas abiertas
* Ambientes híbridos (trabajo + social)

### 🎨 Identidad visual

* Base neutra (grises cálidos, beige, madera)
* Acentos vibrantes (UI, branding, tecnología)
* Iluminación cálida + pantallas frías

### 🧩 Materialidad

* Madera (mesas)
* Metal (estructuras)
* Plástico (sillas)
* Vidrio (pantallas, ventanas)

### 🚫 Evitar

* Fantasía medieval
* Armaduras / armas
* FX mágicos irreales
* Saturación extrema constante

---

## 🎥 Cámara y Perspectiva

### 📐 Configuración

* Isométrica modificada (2:1)
* Rotación Y: 45°
* Rotación X: ~30°–35°

### 👁️ Vistas requeridas

* 3/4 Frente
* 3/4 Espalda

### 📌 Regla crítica

Todos los assets deben respetar la misma proyección → evitar ruptura espacial

---

## 📦 Resolución y Grid

* Resolución base: **32x32 px**
* Grid: 1px (pixel perfect)
* Snap obligatorio
* Sin anti-aliasing

### 📏 Uso del espacio

* Altura personaje: 24–28 px
* Margen superior controlado
* Base consistente entre assets

---

## 🧱 Punto de Anclaje (Grounding)

* Anchor pixel: centro inferior
* Todos los sprites apoyan en misma línea Y

### 🚫 Evitar

* Personajes flotando
* Desfase con sombras
* Inconsistencia en colisiones

---

## 🧍 Proporciones del Personaje

| Parte   | Proporción |
| ------- | ---------- |
| Cabeza  | 25–30%     |
| Torso   | 30–35%     |
| Piernas | 35–40%     |

### 📌 Regla

Proporciones constantes entre todos los personajes

---

## ⚖️ Peso Visual

Distribución de detalle:

1. Cabeza → máxima prioridad (expresión, identidad)
2. Torso → secundaria (ropa, postura)
3. Props → acento (laptop, café, celular)
4. Piernas → mínimo detalle

### 🎯 Reglas

* 60% del detalle en mitad superior
* Reducir ruido en zona inferior
* Priorizar lectura en movimiento

---

## 🎨 Paleta de Color

### 📊 Scope

* 12–16 colores por personaje
* 8–12 por sprite

### 📊 Distribución

* 40% tonos base
* 30% sombras
* 20% highlights
* 10% acentos

### 🌈 Valores y saturación

* Sombras → más frías, menos saturadas
* Highlights → más cálidos, ligeramente más saturados
* Midtones → dominantes

### 🚫 Evitar

* Negro puro (#000)
* Blanco puro (#FFF)

---

## 📌 Value Separation

Estructura mínima:

* Base
* Mid shadow
* Core shadow
* Highlight

### 📊 Diferencias recomendadas

* Base → mid: -15%
* Mid → core: -20–25%
* Base → highlight: +15%

### 🎯 Objetivo

Lectura clara en 1 segundo

---

## 💡 Iluminación

### ☀️ Luz principal

* Arriba-izquierda (global)

### 🌗 Luz secundaria

* Pantallas
* UI
* Elementos interactivos

### 🧠 Reglas avanzadas

#### Subsurface (pixel-friendly)

* Aplicar en piel
* 1px cálido en bordes

#### Materiales

* Pantalla:

  * Glow suave
  * Tonos fríos

* Metal:

  * Alto contraste
  * Highlights definidos

* Tela:

  * Transición suave

* Madera:

  * Midtones dominantes
  * Bajo contraste

---

## 🌈 Contraste

* Alto en silueta externa
* Bajo en detalles internos

---

## ✨ SFX Visuales (Oficina Adaptado)

### ✔ Permitidos

* Glow de pantallas
* Notificaciones
* Indicadores UI
* Vapor de café
* Feedback de interacción

### 🎨 Reglas

* 2–4 colores adicionales máximo
* Sin blur excesivo
* Dithering en vez de gradiente

### 💡 Integración

* Puede actuar como luz secundaria
* Solo afecta bordes cercanos

---

## ✏️ Lineart

### 📏 Base

* 1px

### 🎯 Adaptativo

* Reducir contraste en zonas pequeñas
* Eliminar líneas internas si es necesario

### 🎨 Color

* No negro puro
* Usar tonos oscuros del mismo color

### 📌 Jerarquía

* Contorno externo → más oscuro
* Interno → más suave

---

## 🧩 Volumen y Sombreado

### 📐 Técnica

Cel shading estructurado

### Niveles

* Base
* Mid shadow
* Core shadow
* Highlight
* (Opcional) bounce light

### 📌 Regla

Evitar banding → variar clusters

---

## 🧭 Orientación (3/4)

### Frente

* Cara parcial visible
* Interacción con props

### Espalda

* Mochila / hoodie
* Elementos de contexto laboral

### 🔄 Consistencia

* Mantener volumen entre vistas

---

## 🚶 Animación

### 🎬 Acciones

* Caminar
* Escribir en laptop
* Revisar celular
* Tomar café
* Conversar

### ⏱️ Timing

* No linear

#### Distribución (6 frames):

1 → Contact (hold)
2
3 → Passing (rápido)
4
5 → Contact (hold)
6

### 📈 Easing

* Micro ease in/out
* Evitar spacing uniforme

---

## 🎞️ Estabilidad de Volumen

* Mantener masa consistente
* No cambiar tamaño frame a frame
* Mantener anchor fijo

---

## 🧱 Tiles y Entorno

### Elementos base

* Escritorios
* Sillas
* PCs / laptops
* Plantas
* Pizarras

### 📌 Reglas

* Misma perspectiva
* Misma altura base
* Grid consistente

---

## 📁 Naming Convention

char_<role>*<action>*<direction>_<frame>.png

### Ejemplos

* char_dev_walk_front_01.png
* char_designer_idle_back_02.png
* char_manager_talk_front_03.png

---

## 🧪 Checklist de Calidad

Antes de exportar:

* Silueta clara (zoom 1x)
* Sin píxeles sueltos
* Luz consistente
* Anchor correcto
* Paleta válida
* Lectura en movimiento

---

## 🖥️ Validación en Engine

### Tests obligatorios

* Fondo claro y oscuro
* Sobre tiles complejos
* En movimiento
* Escala 1x

### Regla

Si no se entiende → simplificar

---

## 📤 Export

* PNG
* Fondo transparente
* 1x recomendado

### Si 2x:

* Nearest neighbor
* Cleanup manual obligatorio

---

## ⚙️ Pipeline

1. Silueta
2. Base
3. Sombra
4. Highlight
5. Polish

---

## 🚫 Errores Comunes

* Overdetail en 32x32
* Mezclar perspectivas
* Luz inconsistente
* Anti-aliasing
* Colores lavados

---

## 🎯 Filosofía

"Menos píxeles, más intención"
"Claridad > Realismo"
"Función > Decoración"
