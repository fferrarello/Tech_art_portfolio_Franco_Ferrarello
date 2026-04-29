# 🛠️ TA Dashboard (AAA Asset Validator)

Herramienta avanzada para **Autodesk Maya** enfocada en validación automática de assets 3D bajo estándares AAA.

Diseñada para artistas técnicos (TA), modeladores y riggers que necesitan asegurar calidad, consistencia y limpieza en sus escenas.

---

## 🚀 Features

### 🔍 Validaciones automáticas

* ✔️ Construction History
* ✔️ Freeze Transforms
* ✔️ Non-Manifold Geometry
* ✔️ Lamina Faces
* ✔️ Naming Convention (geo_, grp_, jnt_)
* ✔️ Estructura de rig (CHARACTER)
* ✔️ Jerarquía de grupos (geo_grp / rig_grp)
* ✔️ Parenting correcto
* ✔️ SkinCluster check

---

### 🎨 Highlight visual en viewport

* Coloreado automático por tipo de error
* Identificación rápida de problemas en escena
* Limpieza de highlights con un click

---

### ⚡ Fixes automáticos

* Fix individual por categoría
* Fix masivo (`FIX ALL`)
* Renombrado inteligente basado en tipo de nodo
* Corrección de joints automáticamente

---

### 🧠 Inteligencia de Asset Type

* **PROP**
* **CHARACTER**

El sistema adapta validaciones automáticamente según el tipo de asset.

---

### 🖥️ UI Profesional

* Dashboard organizado por categorías
* Estados visuales (OK / Issues)
* Selección + focus automático en viewport
* Sistema de listas interactivas

---

## 📦 Instalación

1. Copiar el script en el Script Editor de Maya (Python)
2. Ejecutar el archivo

```python
import ta_dashboard_pro
```

O simplemente pegar el código y correrlo.

---

## ▶️ Uso

1. Abrir la herramienta (se ejecuta automáticamente)
2. Seleccionar tipo de asset:

   * `PROP`
   * `CHARACTER`
3. Presionar:

### 🔎 VALIDATE

Ejecuta todas las validaciones

### 🎨 HIGHLIGHT ALL ISSUES

Colorea todos los errores en viewport

### 🧹 CLEAR HIGHLIGHT

Limpia los colores

### 🔧 FIX SELECTED

Corrige elementos seleccionados

### ⚡ FIX ALL

Aplica correcciones globales:

* Borra history
* Freeze transforms
* Centra pivots
* Renombra correctamente

### 🔁 REVERT

Restaura nombres originales (si fueron modificados)

---

## 📁 Naming Convention

| Tipo  | Prefijo |
| ----- | ------- |
| Mesh  | `geo_`  |
| Grupo | `grp_`  |
| Joint | `jnt_`  |

---

## 🧩 Estructura esperada (CHARACTER)

```
rig_grp
 ├── jnt_root
 └── ...
 
geo_grp
 └── meshes
```

---

## ⚠️ Consideraciones

* La herramienta usa `maya.cmds`
* Pensada para pipelines AAA
* Algunos fixes pueden ser destructivos (ej: delete history)
* Se recomienda trabajar sobre copias de escena

---

## 🧪 Validaciones incluidas

| Categoría     | Descripción                              |
| ------------- | ---------------------------------------- |
| History       | Detecta construction history innecesario |
| Freeze        | Verifica transforms no congelados        |
| NonManifold   | Geometría inválida                       |
| Lamina        | Caras duplicadas                         |
| Naming        | Convenciones incorrectas                 |
| Joints        | Naming incorrecto                        |
| Rig Structure | Estructura faltante                      |
| Groups        | Grupos obligatorios                      |
| Parenting     | Jerarquía incorrecta                     |
| Skin          | Falta de skinning                        |

---

## 💡 Roadmap (ideas futuras)

* Export validator (FBX/engine-ready)
* Integración con Unreal / Unity
* Reportes automáticos (JSON / HTML)
* Batch validation
* UI con Qt / PySide2

---

## 👨‍💻 Autor

Herramienta desarrollada para optimizar workflows de producción 3D en Maya.

---

## 📜 Licencia

Libre para uso educativo y profesional.
Modificar bajo tu propio riesgo 😄

---

## 🔥 Preview

> UI tipo dashboard + validación en tiempo real + highlight por error

---

## ⭐ Si te sirve...

Dale una estrella al repo y compartilo 🚀
