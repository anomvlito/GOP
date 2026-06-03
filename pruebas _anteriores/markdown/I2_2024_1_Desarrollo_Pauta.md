# Interrogación 2 --- Gestión de Operaciones (ICS 3213)
## Semestre: 1er Semestre 2024
**Profesores:** Alejandro Mac Cawley, Rodrigo Carrasco
**Autores de Referencia:** César Meneses, Fabián Ortega

---

## PARTE DESARROLLO

### Pregunta 1: Planificación Agregada y Cadena de Suministro (20 Puntos)

#### Enunciado
Usted es el Gerente de Operaciones para una gran empresa que produce un producto y debe elaborar el plan de producción para las siguientes 52 semanas. Marketing le ha entregado la demanda de cada cliente $i$ para cada semana $t$, la cual es $D_{it}$. 

La producción puede ser hecha en cualquiera de las $N$ plantas de la empresa, pero para ello debe activar la planta, lo cual tiene un costo fijo de $A_n$. El costo de producción unitario es $CP_n$ por unidad en la planta $n$ y la producción debe ser despachada a cada cliente $i$ a un costo $C_{in}$ por cada unidad despachada al cliente $i$ de la planta $n$. La productividad de cada trabajador en la planta es de $PR_n$ unidades por hora de producción por trabajador y se trabajan turnos de 8 horas diarias en 5 días a la semana. El costo semanal de cada trabajador es $\$CT$, el costo de contratación es $\$CC$ y el de despido es $\$CDS$. Es posible trabajar un máximo de 2 horas extra por día a un costo de $CE$ pesos por hora extra trabajada. Actualmente (tiempo 0) usted dispone de $T_n$ trabajadores y mantiene $INVI_n$ unidades en inventario en cada planta. Al final del año debe dejar $TF_n$ trabajadores y $INVF_n$ unidades en inventario en cada planta $n$. El costo de mantener unidades en inventario es $H_n$ pesos por unidad por semana para cada planta $n$.

* **i.** (10 ptos) Con esta información construya un modelo de programación matemática que permita determinar la planificación de producción. Indique las variables de decisión, la función objetivo y las restricciones.
* **ii.** (5 ptos) Ahora usted debe planificar el aprovisionamiento de la planta de la materia prima para producir el producto. Usted sabe que para producir una unidad de producto final se requiere $R$ unidades de materia prima a un costo de $IN_t$ por unidad de materia prima en el tiempo $t$. Actualmente (tiempo 0) mantiene $MPI_n$ unidades en inventario de materia prima en cada planta, al final del año debe dejar $MPF_n$ unidades en inventario y el costo de mantener unidades en inventario es $MC_n$ para cada planta. Este insumo es provisto por $j$ proveedores distintos que tienen un *Lead-Time* de $L$ semanas, cada uno puede entregar como máximo $MAX_j$ unidades del insumo por semana y el costo de despacho entre cada proveedor y planta es de $CTP_{nj}$. Indique cómo cambia el modelo (nuevas variables, cambios en la función objetivo y nuevas restricciones).
* **iii.** (5 ptos) Usted determina que el flujo entre cada proveedor y planta es $F_{nj}$ unidades de cada proveedor $j$ a la planta $n$. Con esta información usted quiere determinar la ubicación de dos bodegas que permitan recibir los insumos de parte de los proveedores. Para ello usted georreferencia cada proveedor con una coordenada en X e Y, siendo $CPRX_j$ y $CPRY_j$ respectivamente para cada proveedor $j$, y lo mismo para cada planta, siendo $CPLX_n$ y $CPLY_n$ para cada planta $n$. Si usted quiere determinar la cota de peor caso y asume la distancia Manhattan, construya el modelo de programación matemática que permita determinar la ubicación de cada bodega y la asignación de las plantas y proveedores a cada bodega.

#### Solución

##### i. Modelo Base de Planificación Agregada (MILP)

###### 1. Variables de Decisión
* $P_{n,t} \ge 0$: Cantidad de producto final fabricado en la planta $n$ en la semana $t$.
* $I_{n,t} \ge 0$: Inventario de producto final en la planta $n$ al final de la semana $t$.
* $DE_{n,i,t} \ge 0$: Despacho de producto final de la planta $n$ al cliente $i$ en la semana $t$.
* $TA_{n,t} \ge 0$: Trabajadores disponibles en la planta $n$ en la semana $t$.
* $TCA_{n,t} \ge 0$: Trabajadores contratados en la planta $n$ al inicio de la semana $t$.
* $TDA_{n,t} \ge 0$: Trabajadores despedidos en la planta $n$ al inicio de la semana $t$.
* $HE_{n,t} \ge 0$: Horas extra totales trabajadas en la planta $n$ en la semana $t$.
* $B_{n,t} \in \{0, 1\}$: Variable binaria que toma el valor $1$ si la planta $n$ opera en la semana $t$, y $0$ en caso contrario.

###### 2. Función Objetivo
Minimizar los costos totales de producción, despacho, contratación, despido, sueldos normales, horas extra y activación de plantas:
$$\begin{aligned}
  \min \quad \sum_{t=1}^{52} \sum_{n=1}^{N} \Big( &CP_n \cdot P_{n,t} + H_n \cdot I_{n,t} + CT \cdot TA_{n,t} + CC \cdot TCA_{n,t} + CDS \cdot TDA_{n,t} \\
  &+ CE \cdot HE_{n,t} + A_n \cdot B_{n,t} + \sum_{i} C_{in} \cdot DE_{n,i,t} \Big)
\end{aligned}$$

###### 3. Restricciones
* **Satisfacción de la Demanda de los Clientes:**
  $$\sum_{n=1}^{N} DE_{n,i,t} \ge D_{it} \quad \forall i, t$$
* **Balance de Inventario en Plantas:**
  $$I_{n,t} = I_{n,t-1} + P_{n,t} - \sum_{i} DE_{n,i,t} \quad \forall n, t$$
* **Dinámica de la Fuerza Laboral:**
  $$TA_{n,t} = TA_{n,t-1} + TCA_{n,t} - TDA_{n,t} \quad \forall n, t$$
* **Restricción de Capacidad de Producción (basado en mano de obra):**
  $$P_{n,t} \le PR_n \cdot \left( TA_{n,t} \cdot 8 \cdot 5 + HE_{n,t} \right) \quad \forall n, t$$
* **Límite de Horas Extra:**
  $$HE_{n,t} \le TA_{n,t} \cdot 2 \cdot 5 \quad \forall n, t$$
* **Activación de Planta (Relación con producción):**
  $$P_{n,t} \le M \cdot B_{n,t} \quad \forall n, t$$
* **Condiciones de Borde:**
  $$I_{n,0} = INVI_n, \quad I_{n,52} = INVF_n \quad \forall n$$
  $$TA_{n,0} = T_n, \quad TA_{n,52} = TF_n \quad \forall n$$
  $$TA_{n,t}, TCA_{n,t}, TDA_{n,t}, P_{n,t}, I_{n,t}, HE_{n,t} \ge 0, \quad B_{n,t} \in \{0, 1\}$$

##### ii. Extensión para Aprovisionamiento de Materia Prima

###### 1. Nuevas Variables de Decisión
* $QSI_{n,j,t} \ge 0$: Cantidad de materia prima solicitada al proveedor $j$ para ser entregada en la planta $n$ en la semana $t$.
* $QUI_{n,t} \ge 0$: Cantidad de materia prima consumida en la planta $n$ en la semana $t$ para la producción de producto final.
* $IIN_{n,t} \ge 0$: Inventario de materia prima en la planta $n$ al final de la semana $t$.

###### 2. Modificaciones en la Función Objetivo (Costos Adicionales)
Se agregan los costos de adquisición de materia prima, transporte desde proveedores y almacenamiento:
$$\text{Costos MP} = \sum_{t=1}^{52} \sum_{n=1}^{N} \left( \sum_{j} IN_t \cdot QSI_{n,j,t} + \sum_{j} CTP_{nj} \cdot QSI_{n,j,t} + MC_n \cdot IIN_{n,t} \right)$$
Este término se suma a la función objetivo de minimización.

###### 3. Nuevas Restricciones
* **Consumo de Materia Prima:**
  $$QUI_{n,t} \ge R \cdot P_{n,t} \quad \forall n, t$$
* **Balance de Inventario de Materia Prima (con desfase por Lead-Time $L$):**
  $$IIN_{n,t} = IIN_{n,t-1} + \sum_{j} QSI_{n,j,t-L} - QUI_{n,t} \quad \forall n, t$$
* **Capacidad Máxima del Proveedor:**
  $$\sum_{n=1}^{N} QSI_{n,j,t} \le MAX_j \quad \forall j, t$$
* **Condiciones de Borde para Materia Prima:**
  $$IIN_{n,0} = MPI_n, \quad IIN_{n,52} = MPF_n \quad \forall n$$

##### iii. Modelo de Ubicación de dos Bodegas (Centro de Gravedad y Distancia Manhattan)
Queremos ubicar dos bodegas intermedias (bodegas $b \in \{1, 2\}$) que consoliden la materia prima de los proveedores y la entreguen a las plantas.

###### 1. Variables de Decisión
* $CX_b, CY_b$: Coordenadas X e Y de la bodega $b \in \{1, 2\}$.
* $B_{j,b} \in \{0, 1\}$: $1$ si el proveedor $j$ se asigna a la bodega $b$, $0$ si no.
* $B'_{n,b} \in \{0, 1\}$: $1$ si la planta $n$ se asigna a la bodega $b$, $0$ si no.
* $DX_{j,b}, DY_{j,b} \ge 0$: Desviaciones absolutas en coordenadas entre el proveedor $j$ y la bodega $b$.
* $DX'_{n,b}, DY'_{n,b} \ge 0$: Desviaciones absolutas en coordenadas entre la planta $n$ y la bodega $b$.

###### 2. Función Objetivo
Minimizar la distancia Manhattan total ponderada por los flujos de carga:
$$\min \quad \sum_{j} \sum_{b=1}^{2} F_{j} \left( DX_{j,b} + DY_{j,b} \right) + \sum_{n} \sum_{b=1}^{2} F_{n} \left( DX'_{n,b} + DY'_{n,b} \right)$$
*(Donde $F_j$ es la cantidad de insumo del proveedor $j$ y $F_n$ es el consumo de la planta $n$).*

###### 3. Restricciones
* **Asignación Única:**
  $$\sum_{b=1}^{2} B_{j,b} = 1 \quad \forall j, \quad \sum_{b=1}^{2} B'_{n,b} = 1 \quad \forall n$$
* **Distancia Manhattan Linealizada para Proveedores (con Big-M):**
  $$DX_{j,b} \ge CPRX_j - CX_b - M(1 - B_{j,b}) \quad \forall j, b$$
  $$DX_{j,b} \ge CX_b - CPRX_j - M(1 - B_{j,b}) \quad \forall j, b$$
  $$DY_{j,b} \ge CPRY_j - CY_b - M(1 - B_{j,b}) \quad \forall j, b$$
  $$DY_{j,b} \ge CY_b - CPRY_j - M(1 - B_{j,b}) \quad \forall j, b$$
* **Distancia Manhattan Linealizada para Plantas (con Big-M):**
  $$DX'_{n,b} \ge CPLX_n - CX_b - M(1 - B'_{n,b}) \quad \forall n, b$$
  $$DX'_{n,b} \ge CX_b - CPLX_n - M(1 - B'_{n,b}) \quad \forall n, b$$
  $$DY'_{n,b} \ge CPLY_n - CY_b - M(1 - B'_{n,b}) \quad \forall n, b$$
  $$DY'_{n,b} \ge CY_b - CPLY_n - M(1 - B'_{n,b}) \quad \forall n, b$$

---

### Pregunta 2: Planificación de Requerimiento de Materiales (MRP) (20 Puntos)

#### Enunciado
Una empresa química elabora un preparado en envases de $500\text{ ml}$. Cada envase viene con su tapa y los compuestos de la crema por envase son: $300\text{ ml}$ de compuesto A y $200\text{ ml}$ de compuesto B. A su vez, el compuesto B consta de $100\text{ ml}$ de compuesto C y $100\text{ ml}$ de compuesto D.

Los tiempos de fabricación/entrega son:
* Mezcla de compuestos C y D: demora 1 semana.
* Mezcla de compuestos A, B, C más envasado final: demora 1 semana.
* Demanda de envases por las próximas 6 semanas:
  * Semana 1: 300
  * Semana 2: 200
  * Semana 3: 300
  * Semana 4: 400
  * Semana 5: 300
  * Semana 6: 200

* **i.** (5 ptos) Dibuje un árbol que represente la lista de materiales (BOM).
* **ii.** (10 ptos) Construya las tablas de MRP para cada uno de los componentes, considerando inventarios iniciales nulos y lotificación Lote a Lote (L4L).
* **iii.** (5 ptos) El compuesto C requiere estar en un ambiente controlado lo que tiene un costo de setup de envío de $10$ por cada orden. Además, mantenerlo en bodega cuesta $1$ por semana por unidad. Utilice Silver-Meal para determinar los lotes de fabricación óptimos para C y comente el beneficio de agrupar.

#### Solución

##### i. Árbol BOM
```
                 [Crema Final (500 ml)]
               /        |         \       \
       Tapa (1)   Envase (1)   A(300 ml)  B(200 ml)
                                         /        \
                                     C(100 ml)   D(100 ml)
```

##### ii. Tablas de MRP (L4L)
*Nota: Dado que la demanda es de Crema Final (envases), y el envasado y mezcla final toma 1 semana, los requerimientos brutos de A y B ocurren 1 semana antes de la demanda. B a su vez toma 1 semana en mezclarse (C y D se mezclan para formar B).*
* $PORelease_{\text{Final}} = [300 \text{ en W0}, 200 \text{ en W1}, 300 \text{ en W2}, 400 \text{ en W3}, 300 \text{ en W4}, 200 \text{ en W5}]$.
* Compuesto B: Coeficiente = 200 ml por envase. $GR_B = 200 \cdot PORelease_{\text{Final}}$.
  * $GR_B = [60000, 40000, 60000, 80000, 60000, 40000]$.
  * Como la mezcla de B toma 1 semana $\implies$ Lanzamientos planificados de B ($PORelease_B$) ocurren con desfase de 1 semana.
* Compuestos C y D: Coeficiente = 100 ml por cada B (que representa 200 ml). Así, por cada 1 ml de B, se requiere 0.5 ml de C y 0.5 ml de D.
  * $GR_C = 0.5 \cdot PORelease_B$.

##### iii. Loteo de Compuesto C con Silver-Meal
Supongamos una demanda de requerimientos netos de C dada por:
$$D_C = [30, 20, 30, 40, 30, 20]$$
Con costo de setup $S = 10$ y costo de almacenamiento $H = 1$ por semana:
* **Lote en W1:**
  * $k=1: C(1) = 10/1 = 10$.
  * $k=2: C(2) = (10 + 1 \cdot 1 \cdot 20)/2 = 30/2 = 15$.
  * Como $C(2) > C(1)$ ($15 > 10$), paramos. El primer lote es de **30 unidades** en W1.
* **Lote en W2:**
  * $k=1: C(1) = 10/1 = 10$.
  * $k=2: C(2) = (10 + 1 \cdot 1 \cdot 30)/2 = 40/2 = 20$.
  * Paramos. Lote de **20 unidades** en W2.
* **Conclusión:** Bajo estas condiciones extremas de costo de almacenamiento alto ($H=1$) en relación al costo de setup ($S=10$), el algoritmo prefiere no agrupar lotes (se comporta como L4L) para evitar altos costos de almacenamiento.

---

### Pregunta 3: Administración de Proyectos PERT/CPM (20 Puntos)

#### Enunciado
Usted dispone de la siguiente información sobre un proyecto (tiempos en semanas):

| Actividad | Antecesores | Tiempo Esperado ($TE$) | Tiempo Optimista ($TO$) | Desviación Estándar ($\sigma$) | Costo Normal |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | - | 4 | 3 | 1.0 | 4 |
| **B** | - | 2 | 1 | 1.5 | 3 |
| **C** | A, B | 3 | 2 | 0.8 | 3 |
| **D** | C | 2 | 1 | 2.0 | 1.5 |
| **E** | C | 4 | 2 | 1.3 | 5 |
| **F** | D, E | 3 | 1 | 0.7 | 4 |

Conteste:
* **i.** (7 Puntos) Desarrolle el diagrama del proyecto, determine los tiempos ES, EF, LS, LF y la ruta crítica, con su duración y desviación estándar.
* **ii.** (2 Puntos) Calcule la duración del proyecto que sea el doble de probable de excederse que de no cumplirse.
* **iii.** (6 Puntos) Si le ofrecen un contrato con un bono de $\$200$ por terminar en o antes de 11 semanas y una penalización de $\$80$ por terminar en o después de 16 semanas. ¿Aceptaría o rechazaría el contrato? ¿Cuál es la cantidad de semanas máxima que debe ofrecer el bono para que quiera aceptar el contrato?
* **iv.** (5 Puntos) Ahora tiene la posibilidad de que la duración esperada de una actividad sea su tiempo optimista pagando el doble de su costo normal. Calcule el costo mínimo para que el tiempo esperado de la ruta crítica sea 3 semanas menos que el inicial. (*HINT: La ruta crítica puede variar o no*).

#### Solución

##### i. Diagrama de Tiempos y Ruta Crítica
Realizamos el cálculo de pasadas hacia adelante y hacia atrás:
* **A (TE=4):** $ES=0, EF=4$. $LS=0, LF=4$. Holgura = 0.
* **B (TE=2):** $ES=0, EF=2$. $LS=2, LF=4$. Holgura = 2.
* **C (TE=3):** $ES=\max(EF_A, EF_B) = 4, EF=7$. $LS=4, LF=7$. Holgura = 0.
* **D (TE=2):** $ES=7, EF=9$. $LS=9, LF=11$. Holgura = 2.
* **E (TE=4):** $ES=7, EF=11$. $LS=7, LF=11$. Holgura = 0.
* **F (TE=3):** $ES=\max(EF_D, EF_E) = 11, EF=14$. $LS=11, LF=14$. Holgura = 0.

* **Ruta Crítica:** A - C - E - F
* **Duración esperada ($\mu_p$):** $4 + 3 + 4 + 3 = 14$ semanas.
* **Varianza de la ruta crítica ($\sigma_p^2$):**
  $$\sigma_p^2 = \sigma_A^2 + \sigma_C^2 + \sigma_E^2 + \sigma_F^2 = 1.0^2 + 0.8^2 + 1.3^2 + 0.7^2 = 1.0 + 0.64 + 1.69 + 0.49 = 3.82$$
* **Desviación estándar ($\sigma_p$):** $\sqrt{3.82} \approx 1.9545$ semanas.

##### ii. Duración con Probabilidad Asimétrica (Doble de Probable Excederse)
Queremos buscar un tiempo $X$ tal que la probabilidad de excederse sea el doble de la de cumplir:
$$P(T > X) = 2 \cdot P(T \le X)$$
Dado que $P(T > X) + P(T \le X) = 1$:
$$2 \cdot P(T \le X) + P(T \le X) = 1 \implies 3 \cdot P(T \le X) = 1 \implies P(T \le X) = 0.3333$$

El valor de $Z$ para una probabilidad acumulada de $0.3333$ es $Z \approx -0.43$.
Despejamos la duración $X$:
$$X = \mu_p + Z \cdot \sigma_p = 14 - 0.43 \cdot 1.9545 = 13.16 \text{ semanas}$$
La duración buscada es de **13.16 semanas**.

##### iii. Evaluación del Contrato
* **Bono:** $\$200$ si $T \le 11$.
  $$Z_1 = \frac{11 - 14}{1.9545} = -1.53$$
  $$P(T \le 11) = 1 - \Phi(1.53) = 1 - 0.9370 = 0.0630$$
  $$VE_{\text{bono}} = 200 \cdot 0.0630 = \$12.60$$
* **Penalización:** $\$80$ si $T \ge 16$.
  $$Z_2 = \frac{16 - 14}{1.9545} = 1.02$$
  $$P(T \ge 16) = 1 - \Phi(1.02) = 1 - 0.8461 = 0.1539$$
  $$VE_{\text{pen}} = 80 \cdot 0.1539 = \$12.31$$
* **Valor Esperado:**
  $$VE_{\text{neto}} = 12.60 - 12.31 = +\$0.29$$
  Como el valor esperado es positivo ($+\$0.29$), el contrato **se acepta**.

Para que el bono no sea rentable (indiferencia $VE = 0$):
$$P(T \le X) \cdot 200 = 12.31 \implies P(T \le X) = \frac{12.31}{200} = 0.06155$$
Buscamos en la tabla normal: $\Phi(-Z) = 0.0616 \implies Z \approx 1.54$ (o $-1.54$).
$$X = 14 + 1.54 \cdot 1.9545 \approx 17.01 \text{ semanas}$$
La cantidad máxima de semanas que debe ofrecer el bono es de **17.01 semanas**.

##### iv. Crashing de Costo Mínimo (Reducción de 3 semanas)
Podemos reducir actividades de la ruta crítica (A, C, E, F) a su tiempo optimista pagando el doble de su costo normal (costo de crashing = costo normal).
* **Opciones de acortamiento de la ruta crítica:**
  * **A:** reduce de 4 a 3 (ahorro 1 sem), Costo Crashing = $\$4$.
  * **C:** reduce de 3 a 2 (ahorro 1 sem), Costo Crashing = $\$3$.
  * **E:** reduce de 4 a 2 (ahorro 2 sem), Costo Crashing = $\$5$.
  * **F:** reduce de 3 a 1 (ahorro 2 sem), Costo Crashing = $\$4$.

Queremos reducir 3 semanas en total:
1. **Paso 1:** Reducir **C** en 1 semana (Costo = $\$3$). Es el más barato. La duración del proyecto baja a 13.
2. **Paso 2:** Reducir **F** en 2 semanas (Costo = $\$4$). Es el siguiente más barato por unidad de tiempo. La duración del proyecto baja a 11.
*Nota de la Pauta:* La pauta indica que se reduce F en 2 semanas (costo $\$4$) y C en 1 semana (costo $\$3$).
El costo mínimo de reducción para lograr las 3 semanas de ahorro es:
$$\text{Costo Crashing} = \text{Costo C} + \text{Costo F} = 3 + 4 = \$7$$
El costo total del proyecto pasa a ser el costo normal más el costo de crashing:
$$\text{Costo Total} = \text{Costo Normal Total} + \text{Crashing} = (4+3+3+1.5+5+4) + 7 = 20.5 + 7 = \$27.5$$
El costo de crashing es de **$\$7$** (Costo total de **$\$27.5$**).
