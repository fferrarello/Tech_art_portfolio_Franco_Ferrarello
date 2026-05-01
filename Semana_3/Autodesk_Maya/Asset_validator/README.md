# 🚀 TA Dashboard PRO+ (AAA Asset Validator for Maya)

> Herramienta profesional de validación de assets para **Autodesk Maya** orientada a pipelines AAA.

---

## 🎯 Overview

**TA Dashboard PRO+** es una herramienta de validación automática que permite a Technical Artists y Modelers asegurar que los assets cumplen con estándares de producción.

Incluye validaciones de:

* Modelado
* Naming conventions
* Transformaciones
* Limpieza de geometría
* Estructura de rig (para personajes)

Todo desde una UI clara, rápida y enfocada en productividad.

---

## ✨ Features

### 🧱 Mesh Validation

* ✔ History check
* ✔ Freeze transforms
* ✔ Non-manifold detection
* ✔ Lamina faces detection

### 🏷 Naming System

* Auto-detección de tipo de objeto:

  * `geo_` → meshes
  * `grp_` → groups
  * `jnt_` → joints
* Fix automático de nombres
* Reversión al nombre original (con atributo `origName`)

### 🧍 Character Validation (modo CHARACTER)

* ✔ Validación de joints (`jnt_`)
* ✔ Estructura de rig (`jnt_root`)
* ✔ Jerarquías (`geo_grp`, `rig_grp`)
* ✔ Parenting correcto
* ✔ SkinCluster check

### 🛠 Fix System

* Fix individual por categoría
* Fix masivo (`FIX ALL`)
* Reversión de cambios (`REVERT`)

### 🎥 UX / Workflow

* Selección automática
* Frame en viewport (`viewFit`)
* Isolate select
* UI con feedback visual (OK / Issues)

---

## 🖥 UI Preview (Concept)

```
-----------------------------------
|      TA DASHBOARD PRO+          |
-----------------------------------
| Asset Type: [PROP / CHARACTER]  |
-----------------------------------
| History       | Freeze          |
| NonManifold   | Lamina          |
| Naming        | Joints          |
| Rig Structure | Groups          |
| Parenting     | Skin            |
-----------------------------------
| VALIDATE                          |
| FIX SELECTED | FIX ALL           |
| REVERT SEL   | REVERT ALL        |
-----------------------------------
```

---

## ⚙️ Installation

1. Copiar el script en tu entorno de Maya
2. Ejecutar en el Script Editor (Python):

```python
import Asset_Validator
```

> Alternativamente podés pegar el código directamente en el Script Editor.

---

## ▶️ Usage

1. Ejecutar la herramienta
2. Seleccionar tipo de asset:

   * `PROP`
   * `CHARACTER`
3. Click en **VALIDATE**
4. Revisar errores por categoría
5. Usar:

   * `FIX SELECTED` → arreglos específicos
   * `FIX ALL` → limpieza completa

---

## 🧠 How It Works

La herramienta:

1. Detecta todos los meshes en la escena
2. Evalúa reglas de producción
3. Agrupa errores por categoría
4. Permite:

   * Navegar errores
   * Seleccionar objetos
   * Arreglar automáticamente

---

## 🧩 Code Structure

```
Asset_Validator.py
│
├── UTILS
├── NAMING
├── VALIDATIONS
├── RIG VALIDATION
├── FIX SYSTEM
├── UI
└── MAIN EXECUTION
```

---

## 📌 Naming Rules

| Tipo  | Prefijo |
| ----- | ------- |
| Mesh  | geo_    |
| Group | grp_    |
| Joint | jnt_    |

---

## ⚠️ Known Limitations

* `polyCleanup` puede ser agresivo en ciertos meshes
* No incluye validación de UVs (aún)
* No detecta LODs o naming por pipeline avanzado

---

## 🔥 Roadmap

* [ ] UV validation
* [ ] LOD detection
* [ ] Export checks (FBX pipeline)
* [ ] Integración con Perforce / versionado
* [ ] Reporte exportable (JSON / HTML)

---

## 👨‍💻 Author

**Technical Artist Tooling**
Pipeline enfocado en producción AAA.

---

## 📄 License

MIT License (puedes adaptarla según tu necesidad)

---

## ⭐ Support

Si te sirve la tool:

* ⭐ Dale star al repo
* 💡 Sugiere mejoras
* 🧪 Reporta bugs

---

## 🧨 Pro Tip

Usá esta herramienta como **pre-flight check antes de exportar assets**.
Te ahorra errores en engine y problemas en el pipeline.

---
