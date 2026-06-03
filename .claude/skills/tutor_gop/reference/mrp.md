# Planificación de Corto Plazo y MRP

El Plan de Requerimiento de Materiales (MRP) es la técnica por excelencia para la gestión de inventarios con demanda dependiente. Traduce el Plan Maestro de Producción (MPS) en las necesidades netas de componentes, insumos y materias primas a lo largo del tiempo, coordinando las órdenes de compra y producción bajo desfases de tiempo (*Lead Time*).

## 1. Estructura de la Matriz MRP
Para cada ítem, la matriz se completa período a período siguiendo las siguientes ecuaciones matemáticas:

* **Requerimiento Bruto ($GR_t$):** Representa la demanda total del componente.
  * Para el producto terminado (Nivel 0): proviene del MPS o de la demanda de clientes.
  * Para componentes dependientes (Nivel $>0$): es la suma de los lanzamientos planificados de todos sus padres directos multiplicados por el coeficiente de uso del BOM:
    $$GR_{componente, t} = \sum_{padre} \text{Coeficiente} \cdot PORelease_{padre, t}$$
* **Inventario Disponible Proyectado ($I_t$):**
  $$I_t = I_{t-1} + SR_t + POR_t - GR_t$$
  *Donde $SR_t$ es la orden en tránsito (Scheduled Receipt), $POR_t$ es la recepción planificada de la orden (Planned Order Receipt), e $I_0$ es el stock inicial (On-Hand).*
* **Requerimiento Neto ($NR_t$):**
  $$NR_t = \max\left(0, GR_t - I_{t-1} - SR_t\right)$$
* **Recepción Planificada ($POR_t$):** Cantidad total que debe ingresar en el período $t$. Su tamaño depende de la heurística de loteo aplicada.
* **Lanzamiento Planificado ($PORelease_t$):** La orden debe liberarse con un desfase igual al Lead Time ($L$):
  $$PORelease_{t - L} = POR_t$$

## 2. Heurísticas y Algoritmos de Loteo (Lot-Sizing)

### A. Lote a Lote (L4L)
* **Regla:** Se ordena exactamente lo que se necesita en cada período ($POR_t = NR_t$).
* **Propiedades:** Minimiza el inventario almacenado a cero, pero maximiza el número de setups. Adecuado cuando el costo de almacenamiento es prohibitivo o el costo de setup es nulo.

### B. Heurística de Silver-Meal (SM)
Busca minimizar el costo promedio por período de un lote que cubre la demanda de los próximos $k$ períodos.
* **Fórmula de Costo Promedio $C(k)$:**
  $$C(k) = \frac{S + H \cdot \sum_{j=1}^{k} (j-1) \cdot D_{t+j-1}}{k}$$
  *Donde $S$ es el costo de setup, $H$ es el costo de inventario unitario por período, y $D$ es la demanda.*
* **Algoritmo:**
  1. Para un período $t$ con requerimiento neto positivo, calcula $C(1) = S$.
  2. Incrementa $k$ y calcula $C(2), C(3), \dots$
  3. Detén el cálculo en el período $k^*$ donde el costo promedio comience a subir por primera vez:
     $$C(k^* + 1) > C(k^*)$$
  4. Programa una orden de tamaño $\sum_{j=1}^{k^*} D_{t+j-1}$ en el período $t$.
  5. Reinicia el algoritmo en el período $t + k^*$.

### C. Algoritmo Wagner-Whitin (Programación Dinámica)
Garantiza la obtención del óptimo global exacto de costo.
* **Ecuación de Recurrencia:**
  Sea $f(t)$ el costo mínimo acumulado de satisfacer las demandas desde el período 1 hasta el período $t$.
  $$f(t) = \min_{1 \le j \le t} \left\{ f(j-1) + S + \sum_{r=j}^{t} H \cdot (r - j) \cdot D_r \right\}$$
  Se evalúan todas las alternativas de producción en el período $j$ para cubrir la demanda hasta $t$.
* **Propiedades:** Satisface la propiedad de inventario cero (solo se produce en un período si el inventario disponible al inicio del período es cero).
