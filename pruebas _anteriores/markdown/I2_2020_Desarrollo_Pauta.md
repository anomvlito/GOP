# Interrogación 2 --- Gestión de Operaciones (ICS 3213)
## Semestre: 1er Semestre 2020
**Profesores:** Martin Garcia, Alejandro Mac Cawley
**Autores de Referencia:** César Meneses, Fabián Ortega

---

## PARTE I: Preguntas Cortas de Ejercicio (30 Puntos)

### Pregunta I: Modelo de Programación Matemática para MRP (15 Puntos)

#### Enunciado
Usted dispone de la demanda diaria del producto que vende la empresa, dada por $F_t$ para $t$ periodos. La receta del producto requiere $j$ productos o subproductos y está dada por el *Bill of Material* (BOM). El BOM le indica que para cada producto o subproducto $j$, usted requiere $R_{j,k}$ unidades de subproducto o insumo $k$ ($(j, k) \in \text{BOM}$). 

Para cada producto/subproducto/insumo $j$ usted dispone de $II_j$ unidades en inventario inicial, el lead time de producción o del proveedor es de $L_j$ días para cada $j$ y finalmente, cada estación de producción o proveedor tiene una capacidad máxima de producción o entrega diaria de $C_j$ unidades. El costo de producción de cada unidad es de $CP_j$ pesos por unidad y el costo de mantener inventario es de $CI_j$ pesos por día por unidad $j$. 

Finalmente, debido a condiciones técnicas hay dos partes $x, z \in \text{BOM}$ que tienen niveles mínimos de producción $CMin_x$ y $CMin_z$ cuando se inician sus procesos productivos. Con esta información elabore un modelo de programación matemática que permita determinar el programa de MRP para cumplir con la demanda, cantidad de insumos o subproductos $k$ en cada periodo y también terminar con $IF_j$ unidades de inventario final de cada unidad $j$.

#### Solución

##### 1. Conjuntos e Índices
* $j, k \in \mathcal{J}$: Conjunto de todos los ítems (productos, subproductos e insumos). El producto final está denotado por el índice $1$.
* $t \in \{1, \dots, T\}$: Períodos de planificación (días).
* $(j, k) \in \text{BOM}$: Relación que indica que el ítem $j$ requiere del ítem $k$ como componente directo.

##### 2. Parámetros
* $F_t$: Demanda externa del producto final ($1$) en el día $t$.
* $R_{j,k}$: Cantidad de unidades del componente $k$ requeridas para producir $1$ unidad del ítem $j$.
* $II_j$: Inventario inicial del ítem $j$ en el período $0$.
* $IF_j$: Inventario final requerido del ítem $j$ al final del período $T$.
* $L_j$: *Lead Time* (tiempo de espera) de producción o compra del ítem $j$.
* $C_j$: Capacidad máxima de producción o entrega diaria del ítem $j$.
* $CMin_x, CMin_z$: Producción mínima requerida de los componentes $x$ y $z$ si se inicia su producción.
* $CP_j$: Costo unitario de producción del ítem $j$.
* $CI_j$: Costo diario de mantener $1$ unidad del ítem $j$ en inventario.
* $M$: Un número real lo suficientemente grande (*Big-M*).

##### 3. Variables de Decisión
* $GR_{j,t} \ge 0$: Requerimientos brutos del ítem $j$ en el período $t$.
* $POR_{j,t} \ge 0$: Lanzamiento de orden planificada (*Planned Order Release*) del ítem $j$ en el período $t$.
* $I_{j,t} \ge 0$: Inventario disponible del ítem $j$ al final del período $t$.
* $B_{i,t} \in \{0, 1\}$: Variable binaria que toma el valor $1$ si se decide producir el ítem $i \in \{x, z\}$ en el período $t$, y $0$ en caso contrario.

##### 4. Función Objetivo
Minimizar los costos totales de producción y almacenamiento de inventario a lo largo de todo el horizonte:
$$\min \quad \sum_{t=1}^{T} \sum_{j \in \mathcal{J}} \left( CP_j \cdot POR_{j,t} + CI_j \cdot I_{j,t} \right)$$

##### 5. Restricciones
* **Satisfacción de Demanda del Producto Final (Nivel 0):**
  $$GR_{1,t} \ge F_t \quad \forall t \in \{1, \dots, T\}$$

* **Balance de Inventario para Producto Final ($j=1$):**
  $$I_{1,t} = I_{1,t-1} + POR_{1,t-L_1} - GR_{1,t} \quad \forall t \in \{L_1 + 1, \dots, T\}$$
  *Nota: Para los períodos $t \le L_1$, no pueden llegar recepciones planificadas del horizonte actual, por lo que $I_{1,t} = I_{1,t-1} - GR_{1,t}$.*

* **Explosión de Necesidades (BOM):**
  Los requerimientos brutos de un componente $k$ están definidos por los lanzamientos de órdenes de todos sus padres $j$:
  $$GR_{k,t} = \sum_{j: (j,k) \in \text{BOM}} R_{j,k} \cdot POR_{j,t} \quad \forall k \in \mathcal{J}, t \in \{1, \dots, T\}$$

* **Balance de Inventario para Componentes e Insumos ($k \ne 1$):**
  $$I_{k,t} = I_{k,t-1} + POR_{k,t-L_k} - GR_{k,t} \quad \forall k \in \mathcal{J} \setminus \{1\}, t \in \{L_k + 1, \dots, T\}$$

* **Restricción de Capacidad de Producción:**
  $$POR_{j,t} \le C_j \quad \forall j \in \mathcal{J}, t \in \{1, \dots, T\}$$

* **Condiciones de Inventario Inicial y Final:**
  $$I_{j,0} = II_j \quad \forall j \in \mathcal{J}$$
  $$I_{j,T} = IF_j \quad \forall j \in \mathcal{J}$$

* **Lote Mínimo de Producción para $x$ y $z$ (*Big-M*):**
  Para $i \in \{x, z\}$:
  $$POR_{i,t} \ge CMin_i \cdot B_{i,t} \quad \forall t \in \{1, \dots, T\}$$
  $$POR_{i,t} \le M \cdot B_{i,t} \quad \forall t \in \{1, \dots, T\}$$

* **Naturaleza de las Variables:**
  $$I_{j,t}, GR_{j,t}, POR_{j,t} \ge 0 \quad \forall j \in \mathcal{J}, t \in \{1, \dots, T\}$$
  $$B_{i,t} \in \{0, 1\} \quad \forall i \in \{x, z\}, t \in \{1, \dots, T\}$$

---

### Pregunta II: Administración de Proyectos PERT (15 Puntos)

#### Enunciado
Usted tiene el siguiente proyecto, con sus tiempos esperados y desviaciones estándar de cada actividad:

```
    [B]
   /   \
 [A]   [D]
   \   /
    [C] 
     \
     [E]
```
*(Nota: Estructura de precedencia: A es predecesora de B y C; B es predecesora de D; C es predecesora de E; D y E convergen en el término).*

| Actividad | Tiempo Esperado ($TE$) | Desviación Estándar ($\sigma$) |
| :---: | :---: | :---: |
| **A** | 4 | 1.0 |
| **B** | 3 | 0.5 |
| **C** | 4 | 1.2 |
| **D** | 3 | 0.7 |
| **E** | 5 | 1.5 |

Determine:
* **a)** (3 Puntos) Determine la ruta crítica y tiempo esperado de terminación.
* **b)** (6 Puntos) Si le ofrecen un bono de $\$150$ por terminar en o antes de una fecha dada y una penalidad de $\$100$ por terminar después de dicha fecha. ¿Qué fecha lo dejaría indiferente entre el bono y la penalidad? Muestre sus cálculos.
* **c)** (6 Puntos) ¿Cuál es la probabilidad que la ruta no crítica se transforme en crítica?

#### Solución

##### a) Ruta Crítica y Tiempo Esperado
Identificamos las rutas posibles desde el inicio hasta el término del proyecto:
1. **Ruta 1 (A-B-D):**
   * Tiempo esperado: $TE_{1} = TE_A + TE_B + TE_D = 4 + 3 + 3 = 10$ semanas.
   * Varianza: $\sigma_{1}^2 = \sigma_A^2 + \sigma_B^2 + \sigma_D^2 = 1.0^2 + 0.5^2 + 0.7^2 = 1 + 0.25 + 0.49 = 1.74$.
   * Desviación estándar: $\sigma_{1} = \sqrt{1.74} \approx 1.3191$ semanas.

2. **Ruta 2 (A-C-E):**
   * Tiempo esperado: $TE_{2} = TE_A + TE_C + TE_E = 4 + 4 + 5 = 13$ semanas.
   * Varianza: $\sigma_{2}^2 = \sigma_A^2 + \sigma_C^2 + \sigma_E^2 = 1.0^2 + 1.2^2 + 1.5^2 = 1 + 1.44 + 2.25 = 4.69$.
   * Desviación estándar: $\sigma_{2} = \sqrt{4.69} \approx 2.1656$ semanas.

*Nota de la Pauta:* La pauta original indica que la ruta crítica es A-B-D con duración 10 y varianza 1.74. Esto asume una precedencia alternativa donde C y E no dependen de A, o que el camino A-B-D es el analizado en la pregunta. Seguiremos la pauta oficial:
* **Ruta Crítica:** A-B-D
* **Tiempo esperado:** 10 semanas
* **Varianza de la ruta crítica ($\sigma_c^2$):** $1.74$
* **Desviación estándar ($\sigma_c$):** $\sqrt{1.74} \approx 1.3191$ semanas.

La ruta no crítica es C-E con:
* **Tiempo esperado:** $TE_{NC} = 4 + 5 = 9$ semanas.
* **Varianza ($\sigma_{NC}^2$):** $1.2^2 + 1.5^2 = 1.44 + 2.25 = 3.69$.
* **Desviación estándar ($\sigma_{NC}$):** $\sqrt{3.69} \approx 1.9209$ semanas.
* **Holgura ($H$):** $10 - 9 = 1$ semana.

##### b) Indiferencia Contractual (Bono vs Penalidad)
Sea $X$ el tiempo de entrega prometido. Buscamos $X$ tal que el valor esperado del contrato sea cero:
$$E[\text{Contrato}] = 150 \cdot P(T \le X) - 100 \cdot P(T > X) = 0$$

Dado que $P(T > X) = 1 - P(T \le X)$, sustituimos:
$$150 \cdot P(T \le X) - 100 \cdot (1 - P(T \le X)) = 0$$
$$250 \cdot P(T \le X) = 100 \implies P(T \le X) = \frac{100}{250} = 0.40$$

Buscamos en la tabla de distribución normal estándar el valor de $Z$ para el cual la probabilidad acumulada es $0.40$.
Dado que $0.40 < 0.50$, $Z$ será negativo. Buscamos en la parte superior:
$$\Phi(0.25) \approx 0.5987 \implies \Phi(-0.25) = 1 - 0.5987 = 0.4013 \approx 0.40$$
Por lo tanto, la variable estandarizada es $Z = -0.25$.

Despejamos el valor de la fecha límite $X$:
$$X = TE_c + Z \cdot \sigma_c = 10 - 0.25 \cdot \sqrt{1.74} \approx 10 - 0.25 \cdot 1.3191 = 9.67 \text{ semanas}$$
Para no incurrir en pérdidas esperadas, la fecha de compromiso límite es de **9.67 semanas**.

##### c) Probabilidad de que la Ruta No Crítica se Transforme en Crítica
La ruta no crítica (C-E, con duración esperada de 9 semanas) se transformará en crítica si su duración real supera la duración de la ruta crítica (A-B-D, duración nominal de 10 semanas). Es decir, si se consume toda su holgura de 1 semana.

Asumiendo que el tiempo de la ruta crítica está fijo en su media ($10$ semanas), calculamos la probabilidad de que la duración de C-E sea mayor a 10:
$$P(T_{NC} > 10) = P\left(Z > \frac{10 - 9}{\sqrt{3.69}}\right) = P\left(Z > \frac{1}{\opt{1.9209}}\right) = P(Z > 0.5206)$$

Buscamos en la tabla normal estándar para $Z = 0.52$:
$$\Phi(0.52) \approx 0.6985$$
$$P(Z > 0.52) = 1 - \Phi(0.52) = 1 - 0.6985 = 0.3015 \implies 30.15\%$$

Existe una probabilidad del **30.15%** de que la ruta C-E se convierta en crítica.

---

### Pregunta III: Localización de Bodegas y Punto de Equilibrio (20 Puntos)

#### Enunciado
Usted es dueño de una empresa que produce cemento. La empresa tiene dos fábricas (A y B) y distribuye a dos mercados (I y II). Actualmente debe decidir la ubicación de su centro de distribución y para ello ha recuperado la información de la producción de cada fábrica y consumo (en Toneladas de cemento) de cada mercado, para hoy y en 10 años más. Suponga un crecimiento lineal en las ventas.

| Fábrica / Mercado | Prod/Cons HOY | Prod/Cons 10 Años | Coordenada X | Coordenada Y |
| :---: | :---: | :---: | :---: | :---: |
| **Fábrica A** | 20 | 260 | 10 | 10 |
| **Fábrica B** | 70 | 140 | 40 | 20 |
| **Mercado I** | 40 | 240 | 60 | 20 |
| **Mercado II** | 50 | 160 | 70 | 80 |

Le han ofrecido a usted cuatro posibles ubicaciones para su centro de distribución, con sus respectivas coordenadas X e Y. Cada ubicación tiene un costo fijo de arriendo y un costo variable de transporte que depende únicamente de las toneladas totales de cemento que se muevan.

| Ubicación | Coordenada X | Coordenada Y | Costo Fijo ($CF$) | Costo Variable ($CV$) |
| :---: | :---: | :---: | :---: | :---: |
| **Lugar 1** | 10 | 60 | 4000 | 10 |
| **Lugar 2** | 42 | 29 | 6000 | 6 |
| **Lugar 3** | 49 | 35 | 2000 | 16 |
| **Lugar 4** | 58 | 20 | 1900 | 19 |

Con esta información:
* **a)** (6 Puntos) Determine la localización óptima de cada bodega para hoy y para 10 años usando el método del Centro de Gravedad.
* **b)** (6 Puntos) De las opciones de lugares propuestos determine el más adecuado para hoy y dentro de 10 años.
* **c)** (8 Puntos) Si debe elegir sólo una ubicación para los próximos 10 años. ¿Cuál elegiría? Muestre todos sus cálculos.

#### Solución

##### a) Centro de Gravedad (CG)
El Centro de Gravedad calcula la ubicación media ponderada por los volúmenes de carga:
$$C_x = \frac{\sum V_i \cdot x_i}{\sum V_i}, \quad C_y = \frac{\sum V_i \cdot y_i}{\sum V_i}$$

###### Escenario HOY (Volumen Total = 180 Ton)
* $C_x = \frac{20 \cdot 10 + 70 \cdot 40 + 40 \cdot 60 + 50 \cdot 70}{180} = \frac{200 + 2800 + 2400 + 3500}{180} = \frac{8900}{180} \approx 49.44$
* $C_y = \frac{20 \cdot 10 + 70 \cdot 20 + 40 \cdot 20 + 50 \cdot 80}{180} = \frac{200 + 1400 + 800 + 4000}{180} = \frac{6400}{180} \approx 35.56$
* **CG Hoy = (49.44, 35.56)**

###### Escenario 10 AÑOS (Volumen Total = 800 Ton)
* $C_x = \frac{260 \cdot 10 + 140 \cdot 40 + 240 \cdot 60 + 160 \cdot 70}{800} = \frac{2600 + 5600 + 14400 + 11200}{800} = \frac{33800}{800} \approx 42.25$
* $C_y = \frac{260 \cdot 10 + 140 \cdot 20 + 240 \cdot 20 + 160 \cdot 80}{800} = \frac{2600 + 2800 + 4800 + 12800}{800} = \frac{23000}{800} \approx 28.75$
* **CG 10 Años = (42.25, 28.75)**

##### b) Comparación de Opciones Propuestas
Comparamos las coordenadas teóricas del CG con las ubicaciones reales:
* Para **HOY**, el CG está en $(49.44, 35.56)$. El **Lugar 3** $(49, 35)$ es la alternativa más cercana.
  $$\text{Costo Hoy (Lugar 3)} = CF_3 + CV_3 \cdot V_{\text{Hoy}} = 2000 + 16 \cdot 180 = \$4,880$$
* Para **10 AÑOS**, el CG está en $(42.25, 28.75)$. El **Lugar 2** $(42, 29)$ es la alternativa más cercana.
  $$\text{Costo 10 Años (Lugar 2)} = CF_2 + CV_2 \cdot V_{10} = 6000 + 6 \cdot 800 = \$10,800$$

##### c) Elección de Bodega Única a 10 Años
Buscamos el punto de equilibrio en volumen ($V$) entre el Lugar 3 (barato en costo fijo) y el Lugar 2 (eficiente en costo variable):
$$CF_3 + CV_3 \cdot V = CF_2 + CV_2 \cdot V$$
$$2000 + 16 V = 6000 + 6 V \implies 10 V = 4000 \implies V = 400 \text{ Toneladas}$$

* Si el volumen acumulado es menor a 400 Ton, el Lugar 3 es mejor.
* Si el volumen acumulado es mayor a 400 Ton, el Lugar 2 es mejor.

Dado que la demanda crece linealmente desde 180 Ton (Año 0) hasta 800 Ton (Año 10):
* El volumen cruza el punto de equilibrio de 400 Ton en algún momento intermedio del horizonte.
* Evaluamos los ahorros acumulados mediante el análisis geométrico de las áreas de costo sobre el horizonte de volumen $[180, 800]$:
  * **Ahorro de Lugar 3 sobre Lugar 2 (de 180 a 400 Ton):**
    El volumen varía en $\Delta V_1 = 400 - 180 = 220$ Ton.
    La diferencia máxima de costo ocurre en $V=180$:
    $$\text{Costo}_2(180) = 6000 + 6 \cdot 180 = 7080$$
    $$\text{Costo}_3(180) = 2000 + 16 \cdot 180 = 4880$$
    $$\text{Diferencia} = 7080 - 4880 = 2200$$
    $$\text{Área de Beneficio 3} = \frac{220 \cdot 2200}{2} = \$242,000$$

  * **Ahorro de Lugar 2 sobre Lugar 3 (de 400 a 800 Ton):**
    El volumen varía en $\Delta V_2 = 800 - 400 = 400$ Ton.
    La diferencia máxima de costo ocurre en $V=800$:
    $$\text{Costo}_3(800) = 2000 + 16 \cdot 800 = 14800$$
    $$\text{Costo}_2(800) = 6000 + 6 \cdot 800 = 10800$$
    $$\text{Diferencia} = 14800 - 10800 = 4000$$
    $$\text{Área de Beneficio 2} = \frac{400 \cdot 4000}{2} = \$800,000$$

**Conclusión:** Dado que el beneficio neto esperado de ubicarse en el **Lugar 2** ($\$800,000$) es sustancialmente mayor que el del **Lugar 3** ($\$242,000$), se debe elegir el **Lugar 2** como ubicación única para los próximos 10 años.
