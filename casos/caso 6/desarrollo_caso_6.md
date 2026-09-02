# ANÁLISIS DE CASO 6: ZARA (INDITEX) - MODA RÁPIDA
**Curso:** Gestión de Operaciones (ICS3213)  
**Integrantes del Grupo:** César Meneses, Fabián Ortega  
**Fecha:** 28 de Junio de 2026

*Nota: Dado que el archivo de preguntas original se encontraba vacío, este documento ha sido estructurado para responder analítica y rigurosamente las interrogantes fundamentales del caso Zara, aplicando los lineamientos y métricas del curso (Quick Response, Tiempos de Ciclo y Cadena de Suministro).*

---

## Pregunta 1 (3 puntos)

### 1.1. Flujograma de la Cadena de Suministro de Zara vs. Modelo Tradicional

El sistema de operaciones de Zara rompe con el esquema tradicional de producción de ropa empujado por pronósticos a largo plazo (push), sustituyéndolo por un modelo híbrido impulsado fuertemente por la demanda real (pull).

```mermaid
graph TD
    subgraph Modelo Tradicional de Ropa
    A1[Diseño y Bosquejos] -->|6 Meses| B1[Obtención de Materiales y Manufactura Externa]
    B1 --> C1[Distribución y Ventas en Tienda]
    C1 --> D1[Altos Descuentos Fin de Temporada]
    end

    subgraph Modelo de Respuesta Rápida - Zara
    A2[Información Diaria de Tiendas] --> B2[Diseño Ágil y Pequeños Lotes]
    B2 -->|4-5 Semanas Nuevo / 2 Sem. Reabastecimiento| C2[Manufactura Interna/Local JIT]
    C2 --> D2[Distribución Centralizada Arteixo]
    D2 --> E2[Remesas a Tiendas 2 veces/sem]
    E2 --> F2[Escasez Artificial y Baja Tasa de Descuentos]
    F2 -->|Feedback Directo| A2
    end
```

#### ¿Dónde radica la principal diferencia y ventaja competitiva?
1. **Integración Vertical hacia Atrás:** A diferencia de competidores como H&M y The Gap, que subcontratan toda su producción en Asia buscando minimizar el costo de mano de obra, Zara sacrifica costos laborales bajos (produciendo un 40% internamente y gran parte en la península ibérica) a cambio de **velocidad y flexibilidad**.
2. **Distribución Centralizada y Ágil:** Toda la mercancía, sea interna o externa, fluye hacia un único centro de distribución principal en Arteixo. Los productos rara vez pasan más de tres días en el almacén, el cual opera como una instalación de clasificación dinámica más que como una bodega de almacenamiento estático.

---

### 1.2. Problemas del modelo tradicional, métricas de Zara y gestión de variabilidad

#### Problemas del sistema tradicional (3 señalados):
1. **Altos errores de pronóstico:** Al tener que diseñar y comprometer la producción con 6 meses de anticipación, las empresas tradicionales se enfrentan a una altísima variabilidad e incertidumbre en la demanda real de la moda.
2. **Exceso de inventario y obsolescencia:** Los errores de pronóstico generan altos niveles de inventario sobrante que deben ser rematados al final de la temporada, destruyendo el margen comercial.
3. **Cadenas de suministro rígidas:** Ante la aparición de una nueva tendencia inesperada a mitad de temporada, los competidores carecen de la agilidad para diseñar, producir y distribuir a tiempo debido a sus extensos tiempos de entrega (lead times) desde Asia.

#### Métricas en que Zara destaca (3 señaladas):
1. **Tiempo de Ciclo (Lead Time):** Zara requiere de **4 a 5 semanas** para un diseño completamente nuevo, y **2 semanas** para reabastecimiento o modificaciones, frente a los 6 meses de la industria.
2. **Porcentaje de Ventas con Descuento (Markdowns):** Zara genera sólo entre un **15% y 20%** de sus ventas con precios de descuento, comparado con el **30% al 40%** de sus principales competidores europeos y estadounidenses.
3. **Frecuencia de Visitas de Clientes:** Un comprador típico visita Zara **17 veces al año**, comparado con el promedio de 3 a 4 veces para el resto del sector.

#### Cómo absorbe Zara la variabilidad:
Zara gestiona la variabilidad intrínseca del mundo de la moda mediante **compromisos postergados**. Al comenzar una temporada, Zara ha comprometido sólo el 15% de su producción (frente al 60% tradicional). Esto significa que absorbe la incertidumbre esperando a recibir información real del mercado desde los gerentes de tienda. La variabilidad es mitigada a través de un **sistema Just-in-Time (JIT)** y sobrecapacidad de manufactura, lo que les permite adaptarse ágilmente sin el látigo estadístico (*bullwhip effect*) de la demanda a largo plazo.

---

## Pregunta 2 (3 puntos)

### 2.1. Determinación de la Estructura de Costos y Penalización por Logística

Uno de los principales análisis operacionales reside en justificar por qué Zara acepta costos de producción y envíos más altos a cambio de menores tiempos de ciclo. 

#### Datos del Caso (Anexo 3 - Costo en Tierra de una Camisa):
- **Fabricación en Europa (España):** $42.24 (Costos de manufactura, mano de obra e insumos).
- **Fabricación en Asia:** $29.09 (Menor costo base, pero largos tiempos de ciclo).
- **Diferencial de Costo Directo:** Producir en Europa es un **45.2% más caro** en términos puramente fabriles ($\sim \$13.15$ de diferencia).

#### Justificación Económica Global:
Si evaluáramos el sistema mediante un modelo de Lote Económico (EOQ) clásico ignorando la obsolescencia, Asia ganaría. Sin embargo, aplicando un enfoque de **Modelo del Vendedor de Periódicos (Newsvendor)** adaptado, donde los productos de moda tienen un ciclo de vida ultra corto:

1. **Costo de Obsolescencia y Markdowns:** El diferencial de costo logístico se recupera con creces al evitar los descuentos. Un producto importado desde Asia requiere lotes grandes (economías de escala en transporte). Si falla la moda, se asume un 30-40% de liquidación sobre precios plenos.
2. **Costo de Oportunidad (Ventas Perdidas):** Zara reabastece productos exitosos en 2 semanas. Esto minimiza las ventas perdidas por quiebre de stock frente a un competidor atado a importaciones asiáticas que no puede reaccionar.
3. **Publicidad Orgánica:** Zara gasta sólo un **0.3%** en publicidad versus el **3-4%** de la industria, financiando indirectamente su extra costo logístico (como envíos aéreos globales) con este ahorro.

---

### 2.2. Opciones Estratégicas y Riesgos de Expansión

La dirección de Inditex enfrenta grandes interrogantes sobre la expansión, particularmente por el temor a **antieconomías de escala** en su sistema centralizado.

#### Propuesta Operacional de Crecimiento:
1. **Descentralización Modular (El modelo Zaragoza):** El modelo de Arteixo (con capacidad para manejar 45,000 prendas/hora y 130,000 m²) demostró saturación frente al incremento masivo de la red de tiendas. La apertura del centro de distribución en Zaragoza es la decisión operacional correcta. Replican su infraestructura JIT en un nodo con fácil acceso ferroviario y vial, permitiendo particionar geográficamente los despachos sin perder la política de distribución bi-semanal centralizada.
2. **"Mancha de Petróleo" (Estrategia de Localización):** En expansión internacional, Zara minimiza costos logísticos abriendo una tienda insignia (Flagship) y rodeándola progresivamente de tiendas menores. Esto satura las rutas de distribución y prorratea los costos de administración y bodegaje logístico, en contraste con abrir tiendas de forma dispersa, lo que encarecería gravemente las expediciones.

#### Conclusión Final:
Zara demuestra matemáticamente que la rentabilidad en la industria de la moda no proviene del mínimo costo unitario de manufactura (óptimo local), sino de la agilidad global del sistema para **igualar la oferta con la demanda real en tiempos mínimos** (óptimo global del sistema productivo). Su utilización eficiente de tecnología de información y despachos en lotes pequeños asegura márgenes netos sostenidos cercanos al 10%, liderando la industria.
