# Ayudantía 6 - Planificación agregada y MRP

**Pontificia Universidad Católica de Chile**  
**Escuela de Ingeniería**  
**Departamento de Ingeniería Industrial y de Sistemas**  
**ICS3213: Gestión de Operaciones**  
*Profesores: Alejandro Mac Cawley - Rodrigo Carrasco*  
*Semestre: Primer Semestre 2026*  
*Ayudantes: Franco Menares (fmenaresf@estudiante.uc.cl) - Juan Pablo García (jagrca@uc.cl)*  

---

## Repaso Planificación Agregada

La planificación agregada es el proceso de traducir la estrategia de una empresa en acciones concretas, actuando como un puente entre la estrategia competitiva y las operaciones diarias.

*   **Nivel de Decisión:** Nivel táctico con impacto operativo. Se sitúa en el horizonte de planificación de mediano plazo, entre la planeación estratégica (largo plazo) y la programación diaria (corto plazo).
*   **El Concepto de "Agregación":** 
    *   Los pronósticos por producto individual (SKU) suelen ser difíciles y tienen un alto nivel de error.
    *   Se busca agregar la información para ganar precisión (ley de los grandes números: al consolidar la demanda de múltiples productos, los errores individuales tienden a compensarse).
    *   Se utilizan "unidades equivalentes" que agrupan productos similares.
*   **Objetivo Principal:** Igualar la demanda prevista con la capacidad productiva, tomando decisiones sobre niveles de producción, subcontratación, niveles de inventario y fuerza laboral.

### Estrategias para abordar la demanda:

1.  **Estrategia de Persecución (Chase):**
    *   Ajusta la capacidad productiva para seguir la demanda período a período.
    *   *Palancas típicas:* Contratar/despedir trabajadores, usar horas extra o subcontratación.
    *   *Ventaja:* Inventario mínimo.
    *   *Desventaja:* Costos altos de contratación/despido y posible impacto en la moral del personal.
2.  **Estrategia de Nivelación (Level):**
    *   Mantiene una tasa de producción constante independiente de las fluctuaciones de demanda.
    *   El desajuste se absorbe con inventario (cuando hay exceso) o faltantes (cuando hay escasez).
    *   *Ventaja:* Fuerza laboral estable, sin costos de rotación.
    *   *Desventaja:* Costos de inventario o pérdida de ventas.
3.  **Estrategia Mixta:**
    *   En la práctica, casi ninguna empresa usa una estrategia pura.
    *   Se combinan elementos de las estrategias según la temporada, el costo y las restricciones laborales.

---

## Repaso MRP

### ¿Cómo pasamos de lo agregado a lo desagregado?
$$\text{Planificación Agregada} \rightarrow \text{Plan Maestro de Producción (MPS)} \rightarrow \text{Planificación de Requerimientos de Materiales (MRP)} \rightarrow \text{Programación diaria}$$

*   **MPS (Master Production Schedule):** Traduce el plan agregado en productos específicos, en cantidades específicas, en períodos específicos. Responde a: *¿Cuántas unidades del producto X debo producir en la semana Y?* No detalla qué materiales y componentes se necesitan para lograrlo.
*   **MRP (Material Requirements Planning):** Explota la demanda hacia atrás en el tiempo, considerando los tiempos de entrega (lead times), para determinar cuándo lanzar órdenes de producción o compra. Responde a: *¿Qué materiales necesito, en qué cantidad y en qué momento, para cumplir el MPS?* El resultado son órdenes de producción para componentes internos y órdenes de compra para materiales externos.

### ¿Cómo definimos el tamaño del lote a ordenar?
Buscamos equilibrar dos costos: **Costo de ordenar (Setup)** y **Costo de mantener inventario**.

*   **Lote a Lote ($L \times L$):**
    *   Produces/ordenas exactamente lo que se necesita cada período.
    *   *Ventaja:* Cero inventario, ideal para ítems caros o perecederos.
    *   *Desventaja:* Muchos setups si la demanda es frecuente.
*   **Cantidad Fija de Pedido:**
    *   Siempre se ordena la misma cantidad predefinida.
    *   *Ventaja:* Simple de gestionar.
    *   *Desventaja:* Puede generar inventario innecesario o ser insuficiente.
*   **Período Fijo de Pedido:**
    *   Se ordena cada $N$ períodos, cubriendo la demanda de ese intervalo.
    *   *Ventaja:* Simple, reduce frecuencia de órdenes.
    *   *Desventaja:* Puede generar inventario variable e impredecible.
*   **EOQ (Economic Order Quantity):**
    *   Se calcula una cantidad fija óptima basada en la demanda promedio.
    *   *Limitación:* Asume demanda constante, lo que rara vez ocurre en MRP.
*   **Costo Total Mínimo (LTC):**
    *   Ajusta el tamaño de lote período a período buscando igualar el costo de ordenar con el costo de inventario acumulado. Más dinámico que EOQ.
*   **Costo Unitario Mínimo (LUC):**
    *   Similar al Costo Total Mínimo, pero divide el costo total entre las unidades del lote.
*   **Wagner-Whitin:**
    *   Método óptimo matemáticamente: minimiza el costo total exacto.
    *   *Desventaja:* Computacionalmente más costoso, menos intuitivo.

---

## Repaso PERT

En planificación y programación de proyectos, se estima que la duración esperada de una actividad es una variable aleatoria con distribución Beta unimodal de parámetros $(a, m, b)$:
*   $a = \text{tiempo optimista}$
*   $m = \text{tiempo más probable}$
*   $b = \text{tiempo pesimista}$

El valor esperado ($t_e$ o $\mu$) y la desviación estándar $\sigma$ se calculan como:
$$t_e = \frac{a + 4m + b}{6}$$
$$\sigma = \frac{b - a}{6}$$

Una vez obtenidos $t_e$ y $\sigma^2$, se determinan los tiempos de calendario:
*   **ES (Earliest Start):** Tiempo de inicio más temprano. En nodos iniciales, $ES = 0$. Si una actividad tiene varios predecesores, $ES$ es el máximo de los $EF$ de estos, dado que no puede comenzar hasta que todos sus predecesores hayan terminado.
*   **EF (Earliest Finish):** Tiempo de término más temprano:
    $$EF = ES + t_e$$
    La duración esperada del proyecto, $T$, es el mayor $EF$ de todas las actividades que desembocan en el nodo final.
*   **LF (Latest Finish):** Tiempo de término más tardío. Para una actividad, $LF$ es el mínimo de los $LS$ de todas las actividades sucesoras. En el nodo final, $LF = T$.
*   **LS (Latest Start):** Tiempo de inicio más tardío:
    $$LS = LF - t_e$$
*   **Holgura ($H$):** Margen de retraso que se puede permitir en una actividad sin afectar la fecha de fin del proyecto:
    $$H = LF - EF \quad \text{o bien} \quad H = LS - ES$$

*   **Actividades Críticas:** Aquellas con holgura $H = 0$. Cualquier retraso en ellas retrasa el proyecto en la misma cantidad.
*   **Ruta Crítica:** Camino ininterrumpido desde el nodo inicial al final, compuesto exclusivamente por actividades críticas. Siempre existe al menos una.
*   **Varianza del Proyecto ($\sigma_T^2$):** Por el Teorema Central del Límite, la duración total $T$ del proyecto se aproxima a una distribución normal. Su varianza es la suma de las varianzas de las actividades en la ruta crítica:
    $$\sigma_T^2 = \sum_{i \in \text{ruta crítica}} \sigma_i^2$$
*   **Probabilidades:** Se calcula usando la normal estándar:
    $$P(T \le t_0) = P(Z \le z_0) \quad \text{donde} \quad z_0 = \frac{t_0 - T}{\sigma_T}$$

---

## Problema 1 (Tarea II 2024)

Como sabemos, la región de Valparaíso y el sur del país han vivido una situación muy compleja debido a los incendios forestales. Es por esto que la ONG *Desafíos Levantemos Chile* se ha propuesto entregar a las municipalidades afectadas cajas de ayuda con suministros básicos a lo largo de todo el año.

La ONG contrata a todo su equipo para realizar la planificación agregada de los 12 periodos (meses) de la planificación anual de la planta productiva. Para comenzar, se consideran los siguientes datos:
1.  La demanda de cajas de suministro en cada periodo $t$ es de $d_t$. Se permite tener demanda insatisfecha, la cual no puede superar las $l_{so}$ unidades por periodo. El costo de penalización es de $\$c_{so}$ por cada caja de suministros no entregada a tiempo.
2.  Durante los primeros 3 meses, por abundancia de voluntarios, el costo de producir una caja es de $0.7 \cdot c_p$, y en los meses restantes es de $\$c_p$.
3.  Se permite subcontratar la producción con un costo de $\$c_{su}$ por unidad y un límite máximo de $l_{su}$ unidades subcontratadas por periodo.
4.  Se cuenta con un inventario inicial de $i_0$ cajas. El costo de mantener una caja en inventario por periodo es $\$c_i$.
5.  La planta cuenta con una cantidad inicial y final de $w_0$ trabajadores. En cada periodo se puede contratar o despedir trabajadores con un costo de $\$c_c$ y $\$c_d$ respectivamente.
6.  Existe un solo turno de $h$ horas y se trabajan $n_t$ días en el mes $t$. El salario es de $\$c_{sn}$ por hora normal, y se permite un máximo de $l_{he}$ horas extra al mes por trabajador, con un salario de $\$c_{se}$ por hora extra.
7.  Hay dos categorías de trabajadores:
    *   **Experimentados:** Contratados hace más de un periodo, con productividad base. Producen $p_{hn}$ cajas en 1 hora normal de trabajo y $p_{he}$ en 1 hora extra. La fuerza laboral inicial $w_0$ se considera experta.
    *   **Novatos:** Contratados dentro del mismo periodo $t$, con un factor de productividad $\alpha$ ($0 \le \alpha \le 1$) respecto a los experimentados.

### Preguntas
1.  Modele el problema mediante programación lineal entera. Defina conjuntos, parámetros, variables de decisión, función objetivo y restricciones utilizadas.
2.  Debido a un cambio en las políticas, el espacio de almacenamiento disponible en la planta es limitado y solo alcanza para un total de 50 cajas. ¿Qué cambios se deben realizar al modelo?
3.  Debido a problemas con la empresa externa, ya no se permite subcontratación. ¿Qué cambios se deben realizar al modelo?

---

## Problema 2 (I2 2024)

Una empresa química elabora un preparado en envases de $500\text{ ml}$. Cada envase viene con su tapa. Los compuestos de la crema por envase son: $300\text{ ml}$ de compuesto A y $200\text{ ml}$ de compuesto B. A su vez, el compuesto B consta de $100\text{ ml}$ de compuesto C y $100\text{ ml}$ de compuesto D.

Los plazos de entrega de los proveedores (Lead Time) son:

| Componente | Plazo |
| :--- | :---: |
| Envase (con tapa) | 3 semanas |
| Compuesto A | 1 semana |
| Compuesto C | 2 semanas |
| Compuesto D | 1 semana |

*   La fabricación de la mezcla de los compuestos C y D demora 1 semana.
*   La mezcla de los compuestos A y B, junto con su envasado, demora 1 semana.
*   El inventario disponible y las órdenes en tránsito son:

| Componente | Inventario Actual | Orden en Tránsito | Plazo de Llegada |
| :--- | :---: | :---: | :---: |
| Producto Final | 500 unidades | - | - |
| Envase (pomo y tapa) | 300 unidades | 400 unidades | Semana 2 |
| Compuesto A | 0 litros | - | - |
| Compuesto B | 50 litros | - | - |
| Compuesto C | 50 litros | - | - |
| Compuesto D | 0 litros | - | - |

*   La demanda pronosticada para las próximas 6 semanas es:

| Semana | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Demanda** | 300 | 200 | 300 | 400 | 300 | 200 |

### Preguntas
1.  Dibuje un árbol que represente la lista de materiales (BOM: Bill Of Materials) del producto final.
2.  Construya las tablas de MRP para cada uno de los componentes.
3.  El compuesto C requiere estar en un ambiente controlado. Para transportar este producto hay que ocupar equipamiento especial, con un costo de traslado por orden de $10$. Además, mantenerlo en bodega cuesta $1$ por litro por semana. Utilice un algoritmo de loteo para determinar los lotes de fabricación del compuesto C. ¿Es mejor agrupar lotes? Indique el beneficio o costo económico de la agrupación.

---

## Problema 3

Usted dispone de la siguiente información sobre un proyecto:

| Actividad | Antecesores | $t_e$ | $t_o$ | $\sigma$ | Costo Normal |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | — | 5 | 4 | 0.9 | \$5.0 |
| **B** | — | 3 | 2 | 1.2 | \$4.0 |
| **C** | A, B | 4 | 3 | 1.0 | \$3.5 |
| **D** | C | 3 | 2 | 1.5 | \$2.0 |
| **E** | C | 5 | 3 | 1.1 | \$6.0 |
| **F** | D, E | 4 | 2 | 0.8 | \$5.0 |

### Preguntas
1.  **Diagrama, ES, EF, LS, LF y ruta crítica:** Desarrolle el diagrama del proyecto, determine los ES, EF, LS, LF y la ruta crítica. Calcule la duración esperada y la desviación estándar de la ruta crítica.
2.  **Duración con probabilidad:** Calcule la duración del proyecto de tal manera que sea el doble de probable que el proyecto se exceda del plazo a que no se exceda.
3.  **Contrato con bono y penalización:** Si le ofrecen un contrato con un bono de $\$200$ por terminar en o antes de 15 semanas y una penalización de $\$80$ por terminar en o después de 20 semanas, ¿aceptaría o rechazaría el contrato? ¿Cuál es el plazo máximo para ofrecer el bono de modo que aún convenga aceptar?
4.  **Reducción con costo mínimo:** Ahora tiene la posibilidad de que la duración esperada de una actividad sea su tiempo optimista en vez del esperado, pagando el doble de su costo normal. Calcule el costo mínimo para que la duración esperada de la ruta crítica sea 3 semanas menor que la inicial.

---

## Plantillas MRP para Desarrollo

### Producto Final (Unidad)
| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Req. Bruto** | | | | | | | |
| **Inv. Final** | | | | | | | |
| **Req. Neto** | | | | | | | |
| **Lote** | | | | | | | |
| **Orden Prog.** | | | | | | | |

### Componente: Envase (Unidad)
| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Req. Bruto** | | | | | | | |
| **Inv. Final** | | | | | | | |
| **Req. Neto** | | | | | | | |
| **Lote** | | | | | | | |
| **Orden Prog.** | | | | | | | |

### Componente: A (Litros)
| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Req. Bruto** | | | | | | | |
| **Inv. Final** | | | | | | | |
| **Req. Neto** | | | | | | | |
| **Lote** | | | | | | | |
| **Orden Prog.** | | | | | | | |

### Componente: B (Litros)
| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Req. Bruto** | | | | | | | |
| **Inv. Final** | | | | | | | |
| **Req. Neto** | | | | | | | |
| **Lote** | | | | | | | |
| **Orden Prog.** | | | | | | | |

### Componente: C (Litros)
| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Req. Bruto** | | | | | | | |
| **Inv. Final** | | | | | | | |
| **Req. Neto** | | | | | | | |
| **Lote** | | | | | | | |
| **Orden Prog.** | | | | | | | |
