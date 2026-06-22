# Evolución del Sistema de Monitoreo Territorial (Dashboard Geoespacial)

Este plan de implementación propone las siguientes fases para evolucionar el cascarón actual hacia un **Dashboard Analítico Completo**. El objetivo es mantener el rendimiento alto, la arquitectura basada en Vanilla JS, y el protocolo visual (Cyberpunk/Dark Sci-Fi).

## User Review Required

> [!IMPORTANT]
> El proyecto ha alcanzado un estado funcional base. Necesito tu validación sobre qué área debemos priorizar ahora. Por favor revisa las fases propuestas a continuación y dime cuál deseas ejecutar primero, o si tienes un rumbo diferente en mente.

## Fases Propuestas

A continuación se dividen las posibles funcionalidades en módulos arquitectónicos lógicos:

---

### Fase 1: Filtros Avanzados y Lógica de Datos
Actualmente, el filtro comprueba si el atributo "existe" en la base de datos.
- **Implementación**: Crear un panel de filtros dependientes. Cuando se hace clic en un "Chip" (ej. Comuna), se despliega un sub-menú dinámico con los valores únicos de esa propiedad (ej. "Santiago", "Lo Barnechea", etc.).
- **Técnica**: Extraer valores únicos recorriendo el objeto GeoJSON con Vanilla JS y generar controles interactivos secundarios, aplicando `map.setFilter()` con expresiones de equivalencia `['==', ['get', 'comuna'], valor]`.

### Fase 2: Panel Analítico (Gráficos Interactivos)
Integrar un panel de estadísticas que reaccione al contexto del mapa.
- **Implementación**: Agregar un panel flotante o extender el panel izquierdo inferior para mostrar gráficos de resumen (ej. Total de Hectáreas por Comuna, Distribución de procesos de reconocimiento).
- **Técnica**: Integrar **Chart.js** (vía CDN) manteniendo el tema visual con gráficos de barras/anillos en colores Neón (Cyan y Fuchsia), los cuales se actualizarán en tiempo real cuando el mapa cambie de vista o se aplique un filtro.

### Fase 3: Herramientas GIS Básicas en UI
Añadir capacidades de análisis espacial directo para el analista de datos.
- **Implementación**: Herramientas de "Medición de distancias", "Cálculo de Área de Polígonos", y "Búsqueda por dirección".
- **Técnica**: Integrar **Turf.js** (vía CDN) para la lógica espacial nativa en el navegador, creando botones de herramientas en el lienzo del mapa.

### Fase 4: Leyenda Dinámica y Capas Base
Darle al usuario contexto sobre lo que está viendo y permitirle alternar vistas.
- **Implementación**: Crear un componente de leyenda auto-generada basado en la visualización actual (ej. escala de colores por Hectáreas).
- **Técnica**: Manipular el DOM para crear una leyenda que lea la estructura de `paint` de MapLibre y permitir alternar el estilo base (ej. cambiar entre mapa base oscuro y satélite).

---

## Open Questions

> [!WARNING]
> Para continuar, por favor responde a lo siguiente:
> 1. ¿Cuál de las fases anteriores (1, 2, 3 o 4) prefieres que abordemos como siguiente paso?
> 2. Si eliges avanzar con análisis de datos o gráficos (Fase 2), ¿te parece bien usar *Chart.js*, o prefieres *D3.js* para visualizaciones más personalizadas?
> 3. ¿Deseas mantener solo `index_chips.html` como versión definitiva, o continuaremos desarrollando en paralelo el clásico `index.html`?
