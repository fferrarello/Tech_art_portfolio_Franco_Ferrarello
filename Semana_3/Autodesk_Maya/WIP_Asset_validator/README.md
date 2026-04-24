\# 🛠️ TA Dashboard PRO+



\### AAA Asset Validator for Autodesk Maya



<p align="center">

&#x20; <img src="https://img.shields.io/badge/Maya-2022%2B-blue?style=for-the-badge\&logo=autodesk" />

&#x20; <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge\&logo=python" />

&#x20; <img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge" />

&#x20; <img src="https://img.shields.io/badge/Tool-Type%20TA%20Pipeline-critical?style=for-the-badge" />

</p>



<p align="center">

&#x20; <b>Validación automática de assets 3D con estándares AAA</b><br>

&#x20; Optimizado para Technical Artists, Modelers y Riggers

</p>



\---



\## 🎬 Preview



<p align="center">

&#x20; <img src="https://via.placeholder.com/900x500.png?text=TA+Dashboard+UI+Preview" width="80%"/>

</p>



<p align="center">

&#x20; <img src="https://via.placeholder.com/900x400.png?text=Viewport+Highlight+System" width="80%"/>

</p>



\---



\## ⚡ Demo (GIF)



<p align="center">

&#x20; <img src="https://via.placeholder.com/800x400.gif?text=Validation+%2B+Auto+Fix+%2B+Highlight" width="80%"/>

</p>



\---



\## 🚀 Features



\### 🔍 Smart Validation System



\* Construction History check

\* Freeze Transform validation

\* Non-Manifold detection

\* Lamina Faces detection

\* Naming convention enforcement

\* Rig validation (Character mode)

\* Parenting \& hierarchy checks

\* SkinCluster verification



\---



\### 🎨 Visual Debug (Viewport Highlight)



| Error Type   | Color    |

| ------------ | -------- |

| History      | Verde    |

| Freeze       | Celeste  |

| Non-Manifold | Rojo     |

| Lamina       | Rosa     |

| Naming       | Azul     |

| Rig Issues   | Amarillo |



✔ Highlight automático por categoría

✔ Limpieza instantánea

✔ Identificación visual ultra rápida



\---



\### ⚡ Auto-Fix System



\* Fix individual por categoría

\* Fix masivo (`FIX ALL`)

\* Auto-renaming inteligente

\* Corrección de joints

\* Limpieza completa de escena



\---



\### 🧠 Adaptive Asset Intelligence



El sistema cambia automáticamente según el tipo de asset:



| Tipo      | Validaciones    |

| --------- | --------------- |

| PROP      | Básicas         |

| CHARACTER | Avanzadas + Rig |



\---



\### 🖥️ UI Dashboard (AAA Style)



\* Panel dividido tipo producción

\* Feedback visual (OK / Issues)

\* Listas interactivas

\* Doble click → Focus + Isolate

\* Highlight dinámico



\---



\## 📦 Instalación



\### Método rápido



1\. Abrir \*\*Script Editor\*\* en Maya

2\. Pegar el código

3\. Ejecutar



\---



\### Método recomendado (modular)



```python

\# guardar como ta\_dashboard\_pro.py

import ta\_dashboard\_pro

```



\---



\## ▶️ Uso



\### 1. Seleccionar tipo de asset



\* `PROP`

\* `CHARACTER`



\---



\### 2. Ejecutar validación



```

VALIDATE

```



\---



\### 3. Visualizar errores



```

HIGHLIGHT ALL ISSUES

```



\---



\### 4. Corregir



```

FIX SELECTED

FIX ALL

```



\---



\### 5. Revertir cambios



```

REVERT SELECTED

REVERT ALL

```



\---



\## 📁 Naming Convention



| Tipo  | Prefijo |

| ----- | ------- |

| Mesh  | `geo\_`  |

| Grupo | `grp\_`  |

| Joint | `jnt\_`  |



\---



\## 🧩 Estructura esperada (CHARACTER)



```

rig\_grp

&#x20;├── jnt\_root

&#x20;└── ...



geo\_grp

&#x20;└── meshes

```



\---



\## 🧪 Validaciones



| Categoría     | Descripción            |

| ------------- | ---------------------- |

| History       | History innecesario    |

| Freeze        | Transform no congelado |

| NonManifold   | Geometría inválida     |

| Lamina        | Caras duplicadas       |

| Naming        | Naming incorrecto      |

| Joints        | Prefijo incorrecto     |

| Rig Structure | Estructura faltante    |

| Groups        | Grupos obligatorios    |

| Parenting     | Jerarquía incorrecta   |

| Skin          | Falta de skinning      |



\---



\## ⚠️ Consideraciones



\* Usa `maya.cmds`

\* Algunos fixes son destructivos

\* Recomendado trabajar sobre copias

\* Pensado para pipelines AAA



\---



\## 🧠 Arquitectura



```

Core

&#x20;├── Validation Engine

&#x20;├── Fix Engine

&#x20;├── Highlight System

&#x20;└── UI System



State

&#x20;├── TA\_RESULTS

&#x20;├── ASSET\_TYPE

&#x20;└── HIGHLIGHTED

```



\---



\## 🔮 Roadmap



\* \[ ] Export Validator (FBX Ready)

\* \[ ] Unreal / Unity Integration

\* \[ ] Report Generator (JSON / HTML)

\* \[ ] Batch Processing

\* \[ ] PySide2 UI Upgrade

\* \[ ] Scene Scoring System (AAA rating)



\---



\## 👨‍💻 Autor



Desarrollado para optimizar workflows de producción en Maya.



\---



\## 📜 Licencia



MIT / Libre uso profesional y educativo



\---



\## 🔥 Bonus



> Este tipo de herramientas es estándar en estudios AAA para:



\* Control de calidad

\* Automatización de pipeline

\* Reducción de errores humanos

\* Preparación para engine (game-ready)



\---



<p align="center">

&#x20; <b>TA Dashboard PRO+ — Pipeline Ready 🚀</b>

</p>



