# Planificación Agregada de la Producción

La Planificación Agregada traduce los planes estratégicos de largo plazo de la corporación en decisiones tácticas de producción de mediano plazo (típicamente de 3 a 18 meses). Su propósito principal es coordinar la capacidad operativa para satisfacer la demanda agregada de familias de productos, equilibrando costos laborales, de inventario y de capacidad.

## 1. Estrategias Puras y Mixtas
* **Persecución (Chase):** Ajusta la capacidad productiva de manera dinámica para seguir la demanda período a período. 
  * *Herramientas:* Contratación y despido de personal, horas extra, subcontratación.
  * *Efecto:* Minimiza el costo de mantener inventario a expensas de la estabilidad laboral y la moral de la fuerza de trabajo.
* **Nivelación (Level):** Mantiene una tasa de producción y una fuerza laboral constante durante todo el horizonte.
  * *Herramientas:* Acumulación de inventario (en períodos de baja demanda) y faltantes o entregas pendientes (en períodos de alta demanda).
  * *Efecto:* Asegura una fuerza de trabajo estable y procesos controlados, pero eleva los costos de almacenamiento o arriesga penalizaciones por quiebres de stock.
* **Mixta:** Combina elementos de persecución y nivelación en proporciones óptimas calculadas mediante programación lineal.

## 2. Formulación Matemática General (MILP)

### Índices y Conjuntos
* $n \in \mathcal{N}$: Plantas productivas o centros de trabajo.
* $i \in \mathcal{I}$: Clientes o mercados de destino.
* $t \in \mathcal{T}$: Períodos de planificación (semanas, meses).

### Parámetros
* $D_{it}$: Demanda del cliente $i$ en el período $t$ [unidades].
* $PR_n$: Productividad de un trabajador en la planta $n$ [unidades/hora].
* $HN_n$: Horas normales disponibles por trabajador a la semana en la planta $n$.
* $HE_n$: Límite máximo de horas extra permitidas por trabajador a la semana en la planta $n$.
* $CP_n$: Costo de producción unitario en la planta $n$ [$/unidad].
* $H_n$: Costo de almacenamiento unitario por período en la planta $n$ [$/unidad-período].
* $CT_n$: Costo laboral normal de un trabajador en la planta $n$ [$/período].
* $CE_n$: Costo de hora extra en la planta $n$ [$/hora].
* $CC_n$: Costo de contratación de un trabajador en la planta $n$ [$/trabajador].
* $CD_n$: Costo de despido de un trabajador en la planta $n$ [$/trabajador].
* $C_{in}$: Costo de transporte unitario desde la planta $n$ al cliente $i$ [$/unidad].
* $A_n$: Costo fijo de activación de la planta $n$ [$/activación].

### Variables de Decisión
* $P_{n,t} \ge 0$: Cantidad producida en la planta $n$ en el período $t$.
* $I_{n,t} \ge 0$: Inventario acumulado en la planta $n$ al final del período $t$.
* $S_{n,i,t} \ge 0$: Cantidad enviada desde la planta $n$ al cliente $i$ en el período $t$.
* $TA_{n,t} \ge 0$: Fuerza laboral activa en la planta $n$ durante el período $t$ [trabajadores].
* $TCA_{n,t} \ge 0$: Trabajadores contratados en la planta $n$ en el período $t$.
* $TDA_{n,t} \ge 0$: Trabajadores despedidos en la planta $n$ en el período $t$.
* $H_{n,t} \ge 0$: Horas extra totales programadas en la planta $n$ en el período $t$.
* $X_{n,t} \in \{0, 1\}$: $1$ si la planta $n$ opera en el período $t$, $0$ si no.
* $Y_{n,t} \in \{0, 1\}$: $1$ si la planta $n$ se activa al inicio del período $t$, $0$ si no.

### Formulación del Modelo de Costo Mínimo
$$\min \quad \sum_{t \in \mathcal{T}} \sum_{n \in \mathcal{N}} \left( CP_n \cdot P_{n,t} + H_n \cdot I_{n,t} + CT_n \cdot TA_{n,t} + CE_n \cdot H_{n,t} + CC_n \cdot TCA_{n,t} + CD_n \cdot TDA_{n,t} + A_n \cdot Y_{n,t} + \sum_{i \in \mathcal{I}} C_{in} \cdot S_{n,i,t} \right)$$

### Sujeto a
* **Balance de Demanda en Mercados:**
  $$\sum_{n \in \mathcal{N}} S_{n,i,t} \ge D_{it} \quad \forall i, t$$
* **Balance de Inventario en Bodegas de Plantas:**
  $$I_{n,t} = I_{n,t-1} + P_{n,t} - \sum_{i \in \mathcal{I}} S_{n,i,t} \quad \forall n, t$$
* **Dinámica de Fuerza Laboral (Flujo de Trabajadores):**
  $$TA_{n,t} = TA_{n,t-1} + TCA_{n,t} - TDA_{n,t} \quad \forall n, t$$
* **Restricción de Capacidad de Producción:**
  La producción total no puede exceder las horas de trabajo disponibles multiplicadas por la productividad:
  $$P_{n,t} \le PR_n \cdot \left( HN_n \cdot TA_{n,t} + H_{n,t} \right) \quad \forall n, t$$
* **Límite de Horas Extra:**
  $$H_{n,t} \le HE_n \cdot TA_{n,t} \quad \forall n, t$$
* **Lógica de Activación y Consecutividad de Planta:**
  $$P_{n,t} \le M \cdot X_{n,t} \quad \forall n, t \quad \text{(M grande)}$$
  $$Y_{n,t} \ge X_{n,t} - X_{n,t-1} \quad \forall n, t$$
* **Condiciones de Borde:**
  $$I_{n,0} = I_{n,0}^{\text{inicial}}, \quad I_{n,T} = I_{n,T}^{\text{final}} \quad \forall n$$
  $$TA_{n,0} = T_n^{\text{inicial}}, \quad TA_{n,T} = T_n^{\text{final}} \quad \forall n$$
