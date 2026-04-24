\# 🎬 TAProSuite – Maya Technical Artist Toolkit



\*\*TAProSuite\*\* es un plugin modular para Autodesk Maya orientado a Technical Artists, que integra herramientas de \*\*pose management, animación procedural, validación de escenas y asistencia con IA\*\*.



Diseñado como un sistema escalable tipo \*\*pipeline de estudio\*\*, permite acelerar workflows de animación y debugging dentro de producción.



\---



\## 🚀 Features principales



\### 🤖 AI Pose System



\* Generación de poses a partir de texto (prompt-based)

\* Selección inteligente de poses desde librería

\* Sistema extensible para integrar modelos de IA reales



\---



\### 🎭 Pose Library (tipo Studio Library)



\* Guardado de poses en formato JSON

\* Organización por nombre y tags

\* Aplicación directa al rig

\* Sistema portable entre proyectos



\---



\### 🔀 Pose Blending



\* Mezcla entre poses (interpolación)

\* Ideal para crear transiciones naturales

\* Base para sistemas de animación más complejos



\---



\### 🎬 AI Blocking Animation



\* Generación automática de blocking desde texto

\* Creación de keyframes en timeline

\* Secuencias tipo:



&#x20; \* anticipation → action → recovery



\---



\### 📊 Pipeline Dashboard



\* Escaneo de escena

\* Conteo de:



&#x20; \* meshes

&#x20; \* joints

&#x20; \* cámaras

\* Información rápida del estado del asset



\---



\### 🐞 Debug Tool



\* Detección de:



&#x20; \* history innecesario

&#x20; \* constraints rotos

&#x20; \* nodos aislados

\* Base para validación de assets en pipeline



\---



\## 🏗️ Estructura del proyecto



```

TAProSuite/

│

├── plug-ins/

│   └── TAProSuite.py

│

├── scripts/

│   ├── main.py

│   ├── ui/

│   ├── core/

│   ├── pose\_library/

│   └── config/

│

├── icons/

│

└── TAProSuite.mod

```



\---



\## ⚙️ Instalación



\### 1. Copiar módulo



Mover el archivo `.mod` a:



```

C:/Users/<USER>/Documents/maya/modules/

```



\---



\### 2. Editar ruta



Dentro de `TAProSuite.mod`:



```

\+ TAProSuite 1.0 C:/ruta/a/TAProSuite

```



\---



\### 3. Activar plugin



En Maya:



\* Windows → Settings/Preferences → Plug-in Manager

\* Buscar: `TAProSuite.py`

\* Activar:



&#x20; \* ✔ Loaded

&#x20; \* ✔ Auto Load



\---



\### 4. Ejecutar



\* Botón en Shelf: \*\*TAPro\*\*

\* O comando:



```python

TAProSuite

```



\---



\## 🧪 Uso básico



\### 🎭 Guardar pose



1\. Seleccionar controles del rig

2\. Click en “Save Pose”

3\. Nombrar la pose



\---



\### 🤖 Aplicar pose con IA



1\. Click en “AI Pose”

2\. Escribir prompt:



```

"angry attack pose"

```



\---



\### 🎬 Generar animación



1\. Click en “AI Animate (Blocking)”

2\. Ejemplo:



```

"jump attack"

```



Se generan keyframes automáticamente en timeline.



\---



\## 🔧 Configuración



Archivo:



```

scripts/config/settings.json

```



Permite ajustar:



\* intensidad de poses

\* randomización

\* checks de debug



\---



\## 🔐 API Key (IA)



Se recomienda usar variable de entorno:



```bash

OPENAI\_API\_KEY=tu\_api\_key

```



Y acceder desde código:



```python

import os

API\_KEY = os.getenv("OPENAI\_API\_KEY")

```



\---



\## 🧠 Roadmap (futuro)



\* Auto-rig detection inteligente

\* Pose embeddings (búsqueda semántica real)

\* Animación secundaria automática

\* Integración con motores (Unity / Unreal)

\* UI avanzada con PySide2



\---



\## 💼 Uso en portfolio



Este proyecto demuestra:



\* Desarrollo de tools para Maya (Python API)

\* Diseño de pipeline modular

\* Integración de IA en DCC tools

\* Automatización de animación (blocking procedural)



\---



\## ⚠️ Disclaimer



Este sistema no reemplaza animadores, sino que acelera el proceso de blocking inicial.



\---



\## 👨‍💻 Autor



Desarrollado como herramienta de Technical Art orientada a producción.



\---



\## 📄 Licencia



Uso libre para fines educativos y de portfolio.



