# Interrogación 2 --- Gestión de Operaciones (ICS 3213)
## Semestre: 1er Semestre 2025
**Profesores:** Alejandro Mac Cawley, Rodrigo Carrasco
**Autores de Referencia:** César Meneses, Fabián Ortega

---

## PARTE DESARROLLO

### Pregunta 1: Planificación de la Producción de Varias Plantas (20 Puntos)

#### Enunciado
Usted es el Gerente de Operaciones de una empresa que fabrica un solo producto en varias plantas. Debe planificar la producción para las siguientes $T$ semanas. La demanda semanal de cada cliente $i$ para cada semana $t$ está dada por $D_{it}$. Esta demanda debe ser satisfecha o tendrá una penalización de $P_i$ por unidad insatisfecha.

La producción puede realizarse en cualquiera de las $N$ plantas, pero cada vez que una planta comienza a operar después de estar inactiva, incurre en un costo fijo de activación $A_n$. Si la planta se usa por semanas consecutivas, este costo sólo se paga una vez. Si se deja de operar por un periodo de tiempo y se vuelve a utilizar más adelante, el costo de activación se paga nuevamente. Cada planta tiene trabajadores con una capacidad de horas normales por semana $HN_n$, y puede utilizar hasta $HE_n$ horas extra por semana a un costo adicional $CE_n$ por cada hora adicional. Cada planta tiene una productividad de $PR_n$ unidades por hora. El costo de producción por unidad en la planta $n$ es $CP_n$.

Cada unidad producida debe enviarse a algún cliente $i$, y el costo de envío por unidad desde la planta $n$ al cliente $i$ es $C_{in}$. Se puede mantener inventario en cada planta con un costo de almacenamiento semanal $H_n$ por unidad. El inventario inicial es de $I_{n,0}$ y al final del periodo de planificación se debe terminar con $I_{n,T}$ en cada planta.

* **i)** (12 puntos) Con esta información construya un modelo de programación matemática que permita determinar la planificación de producción. Indique las variables de decisión, la función objetivo y las restricciones.
* **ii)** (5 puntos) Modifique el modelo anterior para que cumpla con las siguientes condiciones adicionales:
  * Si una planta se activa en una semana, debe operar al menos un turno completo (40 horas normales por semana).
  * La producción en una planta solo es rentable si se fabrican al menos $L_n$ unidades en esa semana.
  * La empresa solo permite que se deje sin entregar o insatisfecha a lo más el $A_i$ porcentaje de la demanda del cliente $i$ durante el horizonte de planificación $T$.
* **iii)** (3 puntos) Si $D_{it}$ es el pronóstico de ventas y usted dispone de un intervalo de confianza al 90% dado por $[DI_{it}, DS_{it}]$, ¿cómo incorporaría esta información en la planificación? Indique paso a paso cómo lo haría e incluya los conceptos de caso pesimista, esperado y optimista.

#### Solución

##### i. Modelo Base de Planificación Agregada (MILP)

###### 1. Variables de Decisión
* $P_{n,t} \ge 0$: Cantidad de producto final fabricado en la planta $n$ en la semana $t$.
* $I_{n,t} \ge 0$: Inventario en la planta $n$ al final de la semana $t$.
* $S_{n,i,t} \ge 0$: Cantidad despachada de la planta $n$ al cliente $i$ en la semana $t$.
* $NS_{i,t} \ge 0$: Demanda insatisfecha para el cliente $i$ en la semana $t$.
* $H_{n,t} \ge 0$: Horas extra utilizadas en la planta $n$ en la semana $t$.
* $X_{n,t} \in \{0, 1\}$: Variable binaria que indica si la planta $n$ está operando en la semana $t$.
* $Y_{n,t} \in \{0, 1\}$: Variable binaria que toma el valor $1$ si la planta $n$ se activa (inicia operación) en la semana $t$, habiendo estado inactiva en $t-1$.

###### 2. Función Objetivo
Minimizar los costos totales de producción, inventario, envío, penalizaciones y activaciones de plantas:
$$\begin{aligned}
  \min \quad \sum_{t=1}^{T} \sum_{n=1}^{N} \Big( &CP_n \cdot P_{n,t} + H_n \cdot I_{n,t} + A_n \cdot Y_{n,t} + CE_n \cdot H_{n,t} + \sum_{i} C_{in} \cdot S_{n,i,t} \Big) \\
  &+ \sum_{t=1}^{T} \sum_{i} P_i \cdot NS_{i,t}
\end{aligned}$$

###### 3. Restricciones
* **Satisfacción de Demanda y Ventas Perdidas:**
  $$\sum_{n=1}^{N} S_{n,i,t} + NS_{i,t} = D_{it} \quad \forall i, t$$
* **Balance de Inventario en Plantas:**
  $$I_{n,t} = I_{n,t-1} + P_{n,t} - \sum_{i} S_{n,i,t} \quad \forall n, t$$
* **Capacidad Máxima de Producción en Planta:**
  La producción máxima depende de las horas normales ($HN_n$) y extra ($H_{n,t}$) habilitadas por la variable binaria de operación:
  $$P_{n,t} \le PR_n \cdot \left( HN_n \cdot X_{n,t} + H_{n,t} \right) \quad \forall n, t$$
* **Límite de Horas Extra:**
  $$H_{n,t} \le HE_n \cdot X_{n,t} \quad \forall n, t$$
* **Dinámica de Activación de Plantas (Lógica de $Y_{n,t}$):**
  $$Y_{n,t} \ge X_{n,t} - X_{n,t-1} \quad \forall n, t$$
  $$Y_{n,t}, X_{n,t} \in \{0, 1\} \quad \forall n, t$$
* **Condiciones de Borde:**
  $$I_{n,0} = I_{n,0}^{\text{dato}}, \quad I_{n,T} = I_{n,T}^{\text{requerido}} \quad \forall n$$

##### ii. Condiciones Adicionales

* **Turno Mínimo Obligatorio:**
  Si la planta está operando ($X_{n,t}=1$), debe usarse al menos un turno de 40 horas normales:
  $$P_{n,t} \ge PR_n \cdot 40 \cdot X_{n,t} \quad \forall n, t$$

* **Producción Mínima por Rentabilidad:**
  Si se decide producir en la semana $t$, debe ser por lo menos $L_n$ unidades:
  $$P_{n,t} \ge L_n \cdot X_{n,t} \quad \forall n, t$$

* **Límite de Demanda Insatisfecha del Cliente:**
  El volumen insatisfecho acumulado del cliente $i$ no puede superar el porcentaje $A_i$ de su demanda total:
  $$\sum_{t=1}^{T} NS_{i,t} \le A_i \cdot \sum_{t=1}^{T} D_{it} \quad \forall i$$

##### iii. Análisis de Incertidumbre y Escenarios
El uso de un intervalo de confianza al 90% $[DI_{it}, DS_{it}]$ permite formular tres escenarios clave:
1. **Caso Esperado (Normal):** Se utiliza la demanda media $D_{it}$. Ofrece una planificación de costo promedio mínimo pero vulnerable a quiebres de stock.
2. **Caso Pesimista (Cota Superior):** Se planifica usando la demanda superior del intervalo $DS_{it}$. Obliga a sobreproducir, contratar más horas extra o acumular inventario. Protege el nivel de servicio ante picos de demanda.
3. **Caso Optimista (Cota Inferior):** Se planifica con la demanda inferior $DI_{it}$. Minimiza los costos operativos inmediatos pero arriesga penalizaciones masivas si la demanda real es mayor.

*Paso a paso para la toma de decisiones:*
* Resolver el modelo para cada uno de los tres escenarios.
* Realizar un análisis de robustez: evaluar el costo de aplicar la solución del caso esperado en el escenario pesimista.
* Determinar un stock de seguridad óptimo basado en la diferencia entre el caso pesimista y el esperado para balancear el costo de almacenamiento y el costo de penalización por quiebre de stock.

---

### Pregunta 2: Administración de Proyectos PERT/CPM (20 Puntos)

#### Enunciado
Usted está a cargo de un proyecto de 6 actividades. Se detalla:

| Actividad | Precedentes | Tiempo Esperado ($TE$) | Desviación Estándar ($\sigma$) |
| :---: | :---: | :---: | :---: |
| **A** | - | 13 | 0.5 |
| **B** | - | 12 | 1.0 |
| **C** | - | 9 | 1.0 |
| **D** | A, B | 14 | 2.0 |
| **E** | B, C | 12 | 1.0 |
| **F** | E | 6 | 0.4 |

Determine:
* **i.** Construya el diagrama de PERT del proyecto y determine la ruta crítica.
* **ii.** Construya un intervalo de confianza para el tiempo de término del proyecto al 95%.
* **iii.** Su contraparte le ofrece un bono de $\$150$ si termina en o antes de 28 días y una penalidad de $\$50$ si en o después de 31 días. ¿Acepta o no el contrato? ¿Qué fecha (días) en la penalidad lo deja indiferente?
* **iv.** Determine todos los caminos alternativos y su probabilidad de que excedan los 30 días, transformándose en rutas críticas.

#### Solución

##### i. Tiempos de Actividades y Ruta Crítica
* **A (TE=13):** $ES=0, EF=13$. $LS=3, LF=16$. Holgura = 3.
* **B (TE=12):** $ES=0, EF=12$. $LS=0, LF=12$. Holgura = 0.
* **C (TE=9):** $ES=0, EF=9$. $LS=3, LF=12$. Holgura = 3.
* **D (TE=14):** $ES=\max(13, 12) = 13, EF=27$. $LS=16, LF=30$. Holgura = 3.
* **E (TE=12):** $ES=\max(12, 9) = 12, EF=24$. $LS=12, LF=24$. Holgura = 0.
* **F (TE=6):** $ES=24, EF=30$. $LS=24, LF=30$. Holgura = 0.

* **Ruta Crítica:** B - E - F
* **Duración esperada ($\mu_p$):** $12 + 12 + 6 = 30$ días.
* **Varianza de la ruta crítica ($\sigma_p^2$):**
  $$\sigma_p^2 = \sigma_B^2 + \sigma_E^2 + \sigma_F^2 = 1^2 + 1^2 + 0.4^2 = 2.16$$
* **Desviación estándar ($\sigma_p$):** $\sqrt{2.16} \approx 1.4697$ días.

##### ii. Intervalo de Confianza al 95%
Para el 95%, el valor crítico de dos colas es $Z = 1.96$:
$$IC = 30 \pm 1.96 \cdot \sqrt{2.16} = 30 \pm 1.96 \cdot 1.4697 = [27.1194, 32.8806] \text{ días}$$

##### iii. Evaluación del Contrato y Fecha de Indiferencia
* **Bono:** $\$150$ si $T \le 28$.
  $$Z_1 = \frac{28 - 30}{\sqrt{2.16}} = -1.36$$
  $$P(T \le 28) = 1 - \Phi(1.36) = 1 - 0.9131 = 0.0869$$
  $$VE_{\text{bono}} = 150 \cdot 0.0869 = \$13.035$$
* **Penalización:** $\$50$ si $T \ge 31$.
  $$Z_2 = \frac{31 - 30}{\sqrt{2.16}} = 0.68$$
  $$P(T \ge 31) = 1 - \Phi(0.68) = 1 - 0.7517 = 0.2483$$
  $$VE_{\text{pen}} = 50 \cdot 0.2483 = \$12.415$$
* **Valor Esperado:**
  $$VE_{\text{neto}} = 13.035 - 12.415 = +\$0.62$$
  Dado que el valor esperado es positivo ($+\$0.62$), **se acepta el contrato**.

Para encontrar la fecha de penalización que deja indiferente ($VE_{\text{neto}} = 0$):
$$VE_{\text{bono}} = P(T \ge D) \cdot 50 \implies 13.035 = P(T \ge D) \cdot 50 \implies P(T \ge D) = 0.2607$$
$$P(T \le D) = 1 - 0.2607 = 0.7393 \implies Z \approx 0.64$$
$$D = 30 + 0.64 \cdot \sqrt{2.16} = 30.9406 \text{ días}$$
La fecha que deja indiferente es de **30.94 días**.

##### iv. Rutas Alternativas e Independencia
Caminos posibles y sus duraciones esperadas:
1. **Ruta B-E-F (Crítica):** Duración = 30, Varianza = 2.16
2. **Ruta C-E-F:** Duración = 27, Varianza = 2.16
3. **Ruta A-D:** Duración = 27, Varianza = $0.5^2 + 2^2 = 4.25$
4. **Ruta B-D:** Duración = 26, Varianza = $1^2 + 2^2 = 5.00$

Calculamos la probabilidad de que cada ruta supere la duración de 30 días:
* **C-E-F:** $Z = \frac{30-27}{\sqrt{2.16}} = 2.04 \implies P(T > 30) = 1 - 0.9794 = 2.06\%$
* **A-D:** $Z = \frac{30-27}{\sqrt{4.25}} = 1.46 \implies P(T > 30) = 1 - 0.9272 = 7.28\%$
* **B-D:** $Z = \frac{30-26}{\sqrt{5}} = 1.79 \implies P(T > 30) = 1 - 0.9632 = 3.68\%$

---

### Pregunta 3: MRP y Silver-Meal para el Componente A1 (20 Puntos)

#### Enunciado
Un producto final se ensambla a partir de: 1 unidad de A, 2 unidades de B y 1 unidad de C. A su vez, A requiere 1 unidad de A1 y 2 de A2, mientras que B requiere 1 unidad de A1 y 1 unidad de B2. El tiempo de entrega de todos los componentes es de 2 semanas, excepto el producto final que se demora 1 semana.
* Inventario inicial del producto final = 50.
* Orden en tránsito del producto final = 20 en la semana 2.
* Demanda del producto final para las semanas 1 a 8:
  $$D = [0, 0, 0, 10, 50, 40, 60, 50]$$

Determine:
* **i.** Dibuje el árbol BOM.
* **ii.** Determine la matriz de MRP para el producto final usando Lote a Lote (L4L).
* **iii.** Si la demanda consolidada del componente A1 es:
  $$D_{A1} = [0, 30, 120, 180, 150, 0, 0, 0]$$
  Con costo de setup $S = \$120$ y costo de almacenamiento $H = \$0.9$ por semana por unidad, determine los lotes de lanzamiento para A1 usando Silver-Meal y su costo total.

#### Solución

##### i. Árbol BOM
```
                 [Producto Final]
               /        |         \
             A(1)      B(2)       C(1)
            /   \     /    \
         A1(1) A2(2) A1(1) B2(1)
```

##### ii. Matriz MRP para el Producto Final (L4L, LT = 1)
| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto ($GR$)** | | 0 | 0 | 0 | 10 | 50 | 40 | 60 | 50 |
| **Órdenes en Tránsito ($SR$)**| | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Stock Disponible ($I$)** | 50 | 50 | 70 | 70 | 60 | 10 | 0 | 0 | 0 |
| **Requerimiento Neto ($NR$)** | | 0 | 0 | 0 | 0 | 0 | 30 | 60 | 50 |
| **Recepción Planificada ($POR$)**| | 0 | 0 | 0 | 0 | 0 | 30 | 60 | 50 |
| **Lanzamiento Planificado ($PORelease$)**| | 0 | 0 | 0 | 0 | 30 | 60 | 50 | 0 |

##### iii. Heurística de Silver-Meal para Componente A1
Demanda de A1:
* $D_{A1} = [0, 30, 120, 180, 150, 0, 0, 0]$ para las semanas 1 a 8.
* $S = \$120$, $H = \$0.9$.
* Iniciamos los cálculos en la primera semana con demanda positiva, que es la **Semana 2** ($D_2 = 30$):

###### Paso 1: Lote en Semana 2
* $k=1$ (semana 2):
  $$C(1) = 120$$
* $k=2$ (semanas 2 y 3): $D_3 = 120$.
  $$C(2) = \frac{120 + 1 \cdot 0.9 \cdot 120}{2} = \frac{228}{2} = 114$$
  *Como $C(2) < C(1)$ ($114 < 120$), seguimos.*
* $k=3$ (semanas 2, 3 y 4): $D_4 = 180$.
  $$C(3) = \frac{228 + 2 \cdot 0.9 \cdot 180}{3} = \frac{552}{3} = 184$$
  *Como $C(3) > C(2)$ ($184 > 114$), paramos.*
* **Primer Lote (Semana 2):** Cubre semanas 2 y 3.
  $$\text{Tamaño de Lote} = D_2 + D_3 = 30 + 120 = 150 \text{ unidades}$$

###### Paso 2: Lote en Semana 4
* $k=1$ (semana 4):
  $$C(1) = 120$$
* $k=2$ (semanas 4 y 5): $D_5 = 150$.
  $$C(2) = \frac{120 + 1 \cdot 0.9 \cdot 150}{2} = \frac{255}{2} = 127.5$$
  *Como $C(2) > C(1)$ ($127.5 > 120$), paramos.*
* **Segundo Lote (Semana 4):** Cubre solo la semana 4.
  $$\text{Tamaño de Lote} = D_4 = 180 \text{ unidades}$$

###### Paso 3: Lote en Semana 5
* $k=1$ (semana 5):
  $$C(1) = 120$$
* $k=2$ (semanas 5 y 6): $D_6 = 0$.
  $$C(2) = \frac{120 + 0}{2} = 60$$
  *Seguimos.*
* $k=3$ (semanas 5..7): $D_7 = 0$.
  $$C(3) = \frac{120 + 0}{3} = 40$$
  *Seguimos.*
* $k=4$ (semanas 5..8): $D_8 = 0$.
  $$C(4) = \frac{120 + 0}{4} = 30$$
  *Alcanzamos el final del horizonte.*
* **Tercer Lote (Semana 5):** Cubre semanas 5 a 8.
  $$\text{Tamaño de Lote} = D_5 + D_6 + D_7 + D_8 = 150 + 0 + 0 + 0 = 150 \text{ unidades}$$

###### Resumen de Costos de la Política Silver-Meal
* Costos de Setup: 3 setups (semanas 2, 4 y 5) $\implies 3 \cdot 120 = \$360$.
* Costos de Almacenamiento:
  * Almacenamos 120 unidades de la semana 3 durante 1 semana (de la semana 2 a la 3):
    $$\text{Costo de Almacenamiento} = 120 \cdot 1 \cdot 0.9 = \$108$$
* **Costo Total = $\$360 + \$108 = \$468$**.
