\# 🌍 Terrain Generator PRO para Maya 2027



\## 📌 Descripción General



\*\*Terrain Generator PRO\*\* es una herramienta de generación procedural de terrenos para Autodesk Maya 2027, pensada para Technical Artists y workflows de entornos.



Genera terrenos orgánicos utilizando una implementación propia de \*\*Perlin Noise\*\*, con soporte para biomas, suavizado y control de detalle.



La herramienta está enfocada en \*\*estabilidad, realismo y usabilidad\*\*, evitando problemas comunes como picos, roturas de malla y artefactos de ruido.



\---



\## 🚀 Características



\### 🧠 Generación Procedural



\* Implementación propia de \*\*Perlin Noise (sin dependencias externas)\*\*

\* Ruido multi-octava para variación natural

\* Generación basada en \*\*seed\*\* (reproducible)



\### 🌍 Modelado del Terreno



\* Terrenos suaves y orgánicos (sin picos)

\* Mezcla balanceada de \*\*base + detalle + ridge\*\*

\* Suavizado global usando `smoothstep`



\### 🏔️ Biomas



\* \*\*Montañas\*\* → mayor contraste y elevación

\* \*\*Llanuras\*\* → terreno más plano

\* \*\*Isla\*\* → caída radial desde el centro



\### 🎛️ Controles de Usuario



\* Tamaño del terreno

\* Resolución (subdivisiones)

\* Altura máxima

\* Escala de ruido (alta precisión)

\* Seed

\* Selección de bioma



\---



\## ⚙️ Instalación



1\. Abrí Autodesk Maya 2027

2\. Abrí el \*\*Script Editor\*\*

3\. Pegá el script en la pestaña de Python

4\. Ejecutá el script



La ventana de la herramienta aparecerá automáticamente.



\---



\## 🖥️ Uso



1\. Configurá los parámetros:



&#x20;  \* \*\*Size\*\* → tamaño del terreno

&#x20;  \* \*\*Resolution\*\* → densidad de la malla

&#x20;  \* \*\*Max Height\*\* → altura máxima

&#x20;  \* \*\*Noise Scale\*\* → frecuencia del terreno (\*\*MUY importante\*\*)

&#x20;  \* \*\*Seed\*\* → variación aleatoria

&#x20;  \* \*\*Biome\*\* → tipo de terreno



2\. Hacé clic en:



```

Generate Terrain PRO

```



3\. Se generará un nuevo terreno en la escena.



\---



\## 🎯 Configuraciones Recomendadas



| Escenario     | Noise Scale | Height | Resolution |

| ------------- | ----------- | ------ | ---------- |

| Terreno suave | 0.015       | 30     | 100        |

| Balanceado    | 0.03        | 40     | 120        |

| Detallado     | 0.05        | 50     | 150+       |



\---



\## 🧠 Cómo Funciona



\### Fórmula del Terreno



El terreno se genera combinando:



\* \*\*Base Noise\*\* → formas grandes

\* \*\*Detail Noise\*\* → variaciones pequeñas

\* \*\*Ridged Noise\*\* → definición de montañas

\* \*\*Masking\*\* → mezcla zonas planas y accidentadas

\* \*\*Smoothstep\*\* → elimina artefactos bruscos



Estructura final:



```

terrain = base \* 0.8 + detail \* 0.2

terrain += ridge \* mask \* 0.2

```



Luego se:



\* normaliza

\* limita (clamp)

\* suaviza

\* adapta según el bioma



\---



\## ⚠️ Problemas Comunes y Soluciones



\### ❌ Terreno con picos



\* Bajá el \*\*Noise Scale\*\*

\* Reducí el \*\*Max Height\*\*



\### ❌ Terreno muy plano



\* Subí el \*\*Noise Scale\*\*

\* Aumentá el \*\*Height\*\*



\### ❌ Artefactos raros



\* Revisá el seed

\* Asegurate de no tener el script duplicado



\---



\## 💡 Notas Técnicas



\* Usa desplazamiento de vértices solo en el eje \*\*Y\*\* (mantiene la malla limpia)

\* Incluye \*\*clamping\*\* para evitar errores matemáticos

\* Evita números complejos y resultados inestables

\* Aplica \*\*polySmooth\*\* para mejorar el acabado



\---



\## 🔥 Mejoras Futuras (Opcional)



\* 🌊 Sistema de erosión procedural

\* 🎨 Auto texturizado (por altura y pendiente)

\* 🌲 Scatter procedural (árboles, rocas)

\* 🗺️ Exportación/importación de heightmaps

\* ⚡ Aceleración por GPU



\---



\## 🧑‍💻 Notas del Autor



Esta herramienta está pensada como pieza de \*\*portfolio de Technical Artist\*\*, replicando workflows similares a:



\* Houdini Heightfields

\* Unreal Engine Landscape Tools

\* World Machine / Gaea



\---



\## 📄 Licencia



Uso libre para proyectos personales y portfolio.

Se puede modificar y extender libremente.



\---



\## 🚀 Conclusión



Esta herramienta es una base sólida para un pipeline de terrenos procedurales dentro de Maya.



Con erosión y texturizado, puede alcanzar calidad \*\*nivel AAA\*\*.



\---



