<div align="center">

# 🛰️ Sistema de Monitoreo Territorial

### Dashboard Geoespacial Interactivo — Humedales Urbanos + SINADER

![MapLibre GL JS](https://img.shields.io/badge/MapLibre_GL_JS-4.x-06b6d4?style=for-the-badge&logo=maplibre)
![Chart.js](https://img.shields.io/badge/Chart.js-4.x-d946ef?style=for-the-badge&logo=chartdotjs)
![Turf.js](https://img.shields.io/badge/Turf.js-6.x-22d55e?style=for-the-badge&logo=leaflet)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-06b6d4?style=for-the-badge&logo=tailwindcss)
![Vanilla JS](https://img.shields.io/badge/Vanilla_JS-ES6+-f7df1e?style=for-the-badge&logo=javascript)

---

[🚀 Demo en vivo](https://alexandraffuentes-star.github.io/analisis-humedales-urbanos) •
[📋 Descripción](#-descripción) •
[🗺️ Funcionalidades](#️-funcionalidades) •
[📂 Estructura](#-estructura) •
[⚡ Inicio rápido](#-inicio-rápido)

</div>

---

## 📋 Descripción

Sistema interactivo de visualización y análisis geoespacial enfocado en **Humedales Urbanos de Chile** y datos del **SINADER** (Sistema Nacional de Información Ambiental y de Recursos Naturales). Combina un mapa base oscuro con capas temáticas, filtros dinámicos y herramientas GIS directamente en el navegador, todo con estética cyberpunk.

---

## 🗺️ Funcionalidades

| Funcionalidad | Descripción |
|---|---|
| **🗺️ Mapa Interactivo** | Visualización de humedales urbanos y establecimientos SINADER sobre mapa oscuro CartoDB |
| **🔍 Filtros Dinámicos** | Filtrado por región, comuna, nombre, proceso (Municipal / de Oficio) y rango de hectáreas |
| **📊 Panel de Gráficos** | Estadísticas de hectáreas por región, distribución por proceso, top rubros SINADER |
| **📏 Herramienta Buffer** | Generación de zonas de influencia con descarga en GeoJSON y Shapefile |
| **🔵 Clustering SINADER** | Agrupación inteligente de puntos con zoom expansivo |
| **🎨 Leyenda Temática** | Mapa de colores por rubro industrial SINADER |
| **🌙 Interfaz Cyberpunk** | Diseño oscuro con neón cyan y fucsia, glassmorphism |

---

## 📂 Estructura

```
📦 analisis-humedales-urbanos
├── 📄 index.html              → Dashboard principal con gráficos
├── 📄 index_chips.html         → Dashboard versión chips de filtros
├── 📄 analyze.py               → Script de análisis exploratorio de datos
├── 📄 Humedales_Urbanos.geojson    → Dataset de humedales urbanos
├── 📄 sinader_puntos.geojson       → Dataset de puntos SINADER
├── 📄 gi-sinader-2024-ckan.xlsx    → Datos SINADER en Excel
├── 📄 plan_implementacion.md       → Plan de evolución del proyecto
├── 📄 contrato.md                  → Documento contractual
└── 📄 .gitignore
```

---

## ⚡ Inicio rápido

```bash
# Clonar el repositorio
git clone https://github.com/alexandraffuentes-star/analisis-humedales-urbanos.git
cd analisis-humedales-urbanos

# Servir con Python (para evitar CORS)
python -m http.server 8000

# Abrir en el navegador
# http://localhost:8000
```

> **Nota**: El proyecto usa Vanilla JS (sin compilador ni bundler). Solo necesitas un servidor HTTP estático.

---

## 🛠️ Stack Tecnológico

- **[MapLibre GL JS](https://maplibre.org/)** — Motor de mapas vectoriales
- **[Chart.js](https://www.chartjs.org/)** — Visualización de gráficos
- **[Turf.js](https://turfjs.org/)** — Análisis geoespacial en el navegador
- **[Tailwind CSS](https://tailwindcss.com/)** — Estilos utilitarios
- **[shp-write](https://github.com/mapbox/shp-write)** — Exportación a Shapefile

---

## 📊 Datos

- **Humedales Urbanos**: Polígonos de humedales reconocidos por el Ministerio del Medio Ambiente de Chile, con atributos como nombre, comuna, región, hectáreas y proceso de reconocimiento.
- **SINADER**: Puntos de establecimientos industriales y de servicios registrados en el Sistema Nacional de Información Ambiental y de Recursos Naturales, clasificados por rubro.

---

<div align="center">

**Desarrollado con 💜 para la gestión territorial y ambiental**

[Reportar un problema](https://github.com/alexandraffuentes-star/analisis-humedales-urbanos/issues) •
[Sugerir mejora](https://github.com/alexandraffuentes-star/analisis-humedales-urbanos/issues)

</div>
