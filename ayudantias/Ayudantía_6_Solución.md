# Ayudantía 6 Solución - Planificación agregada y MRP

**Pontificia Universidad Católica de Chile**  
**Escuela de Ingeniería**  
**Departamento de Ingeniería Industrial y de Sistemas**  
**ICS3213: Gestión de Operaciones**  

---

## Problema 1 (Tarea II 2024) - Solución

### a) Modelo de Programación Lineal Entera

#### Conjuntos
*   $T = \{1, 2, \dots, 12\}$: Conjunto de períodos (meses de la planificación anual).

#### Parámetros
*   $d_t$: Demanda de cajas de suministro en el período $t \in T$.
*   $l_{so}$: Límite de demanda insatisfecha (faltantes) permitido por período.
*   $c_{so}$: Costo de penalización por cada caja de suministros no entregada a tiempo.
*   $c_p$: Costo base de producir una caja de suministros de manera propia.
*   $c_{su}$: Costo de subcontratar la producción de una caja de suministros.
*   $l_{su}$: Límite de unidades que se pueden subcontratar por período.
*   $i_0$: Inventario inicial de cajas de suministro.
*   $c_i$: Costo de mantener una caja de suministro en el inventario por período.
*   $w_0$: Dotación inicial (y final requerida) de trabajadores.
*   $c_c$: Costo de contratar un trabajador.
*   $c_d$: Costo de despedir un trabajador.
*   $h$: Duración de la jornada diaria de trabajo (horas/turno).
*   $n_t$: Número de días de trabajo en el mes $t$.
*   $c_{sn}$: Salario por hora normal de trabajo.
*   $l_{he}$: Límite de horas extra permitidas por trabajador por período.
*   $c_{se}$: Salario por hora extra de trabajo.
*   $\alpha$: Factor de productividad de un trabajador novato ($0 \le \alpha \le 1$).
*   $p_{hn}$: Productividad de un trabajador experimentado en hora normal (cajas/HH).
*   $p_{he}$: Productividad de un trabajador experimentado en hora extra (cajas/HH).

#### Variables de Decisión
*   $W_t$: Dotación total de trabajadores en el período $t \in T$ ($W_t \in \mathbb{Z}^+$).
*   $C_t$: Cantidad de trabajadores contratados al inicio del período $t \in T$ ($C_t \in \mathbb{Z}^+$).
*   $D_t$: Cantidad de trabajadores despedidos al inicio del período $t \in T$ ($D_t \in \mathbb{Z}^+$).
*   $P_t$: Cantidad de cajas de suministros producidas de forma interna en el período $t \in T$ ($P_t \ge 0$).
*   $SU_t$: Cantidad de cajas de suministros producidas por subcontratación en el período $t \in T$ ($SU_t \ge 0$).
*   $PD_t$: Cantidad de cajas de suministros despachadas (entregadas) en el período $t \in T$ ($PD_t \ge 0$).
*   $SO_t$: Cantidad de cajas de suministros de demanda insatisfecha (faltantes) al final del período $t \in T$ ($SO_t \ge 0$).
*   $HE_t$: Horas extras totales trabajadas en la planta en el período $t \in T$ ($HE_t \ge 0$).
*   $I_t$: Cantidad de cajas de suministros en el inventario al final del período $t \in T$ ($I_t \ge 0$).

#### Función Objetivo
Minimizar los costos totales, los cuales incluyen: subcontratación, penalización por faltantes, contratación, despidos, salarios normales, horas extra, almacenamiento e inventario, y costo de producción propia (con descuento del $30\%$ durante los primeros 3 meses):

$$\begin{aligned}
\min \sum_{t=1}^{12} \Big( &c_{su} SU_t + c_{so} SO_t + c_c C_t + c_d D_t + c_{sn} \cdot h \cdot n_t \cdot W_t + c_{se} HE_t + c_i I_t + \text{costo\_prod}_t \Big)
\end{aligned}$$

Donde el costo de producción propia es:
$$\text{costo\_prod}_t = \begin{cases} 
0.7 c_p P_t & \text{si } t \in \{1, 2, 3\} \\
c_p P_t & \text{si } t \in \{4, \dots, 12\}
\end{cases}$$

#### Restricciones

1.  **Flujo de trabajadores:**
    $$W_1 = w_0 + C_1 - D_1$$
    $$W_t = W_{t-1} + C_t - D_t \quad \forall t \in \{2, \dots, 12\}$$
    $$W_{12} = w_0$$

2.  **Flujo de inventarios:**
    $$I_1 = i_0 + P_1 + SU_1 - PD_1$$
    $$I_t = I_{t-1} + P_t + SU_t - PD_t \quad \forall t \in \{2, \dots, 12\}$$

3.  **Capacidad de producción propia:**
    Considerando que los trabajadores contratados en el período $t$ son novatos con productividad $\alpha \cdot p_{hn}$ en horario normal, y que los experimentados ($W_t - C_t$) rinden a $p_{hn}$:
    $$P_t \le \Big[ (W_t - C_t) + \alpha C_t \Big] \cdot h \cdot n_t \cdot p_{hn} + HE_t \cdot p_{he} \quad \forall t \in T$$

4.  **Despacho y demanda insatisfecha:**
    La cantidad despachada es la demanda menos la demanda insatisfecha acumulada del período actual, considerando que lo no entregado se arrastra:
    $$PD_t = d_t - SO_t \quad \forall t \in T$$

5.  **Límite de horas extras:**
    $$HE_t \le l_{he} \cdot W_t \quad \forall t \in T$$

6.  **Límite de producción subcontratada:**
    $$SU_t \le l_{su} \quad \forall t \in T$$

7.  **Límite de demanda insatisfecha:**
    $$SO_t \le l_{so} \quad \forall t \in T$$

8.  **Naturaleza de variables:**
    $$W_t, C_t, D_t \in \mathbb{Z}^+ \quad \forall t \in T$$
    $$P_t, SU_t, PD_t, SO_t, HE_t, I_t \ge 0 \quad \forall t \in T$$

---

### b) Restricción de Capacidad de Almacenamiento Limitada

Se agrega el parámetro $I_{max} = 50$ (inventario máximo permitido por período) y las siguientes restricciones:
$$I_t \le 50 \quad \forall t \in T$$

---

### c) Sin Subcontratación

Se elimina la posibilidad de subcontratar. Esto implica:
1.  Eliminar la variable $SU_t$ del modelo (o fijar $SU_t = 0 \quad \forall t \in T$).
2.  Eliminar el término $c_{su} SU_t$ de la función objetivo.
3.  Eliminar la restricción de límite de producción subcontratada: $SU_t \le l_{su}$.

---

## Problema 2 (I2 2024) - Solución

### a) Lista de Materiales (BOM)

```
Producto Final (1 envase)
├── Envase (1 unidad)
├── Compuesto A (300 ml = 0.3 L)
└── Compuesto B (200 ml = 0.2 L)
    ├── Compuesto C (100 ml = 0.1 L)
    └── Compuesto D (100 ml = 0.1 L)
```

*Nota:* Dado que la receta está en ml y los inventarios se miden en litros para los compuestos químicos, utilizaremos la conversión $1\text{ Litro} = 1000\text{ ml}$.

*   1 unidad de Producto Final requiere: 
    *   1 pomo de Envase
    *   $0.3\text{ L}$ de Compuesto A
    *   $0.2\text{ L}$ de Compuesto B (que a su vez requiere $0.1\text{ L}$ de C y $0.1\text{ L}$ de D).

---

### b) Tablas de MRP

#### 1. Producto Final (Lead Time = 1 semana, Lote a Lote)

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto** | | 300 | 200 | 300 | 400 | 300 | 200 |
| **Inventario Disponible** | 500 | 200 | 0 | 0 | 0 | 0 | 0 |
| **Requerimiento Neto** | | 0 | 0 | 100 | 400 | 300 | 200 |
| **Recepción Planeada** | | 0 | 0 | 100 | 400 | 300 | 200 |
| **Lanzamiento Planeado** | | 0 | 100 | 400 | 300 | 200 | 0 |

#### 2. Envase (Lead Time = 3 semanas, Lote a Lote)
*Requerimiento bruto = Lanzamiento planeado de Producto Final (1 unidad por unidad).*

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto** | | 0 | 100 | 400 | 300 | 200 | 0 |
| **Recepciones Programadas** | | 0 | 400 | 0 | 0 | 0 | 0 |
| **Inventario Disponible** | 300 | 300 | 600 | 200 | 0 | 0 | 0 |
| **Requerimiento Neto** | | 0 | 0 | 0 | 100 | 200 | 0 |
| **Recepción Planeada** | | 0 | 0 | 0 | 100 | 200 | 0 |
| **Lanzamiento Planeado** | 100 | 200 | 0 | 0 | 0 | 0 | 0 |

*Nota:* El lanzamiento de 100 en la semana 0 y 200 en la semana 1 debe programarse en el pasado.

#### 3. Compuesto A (Lead Time = 1 semana, Lote a Lote)
*Requerimiento bruto = Lanzamiento planeado de Producto Final $\times 0.3\text{ L}$.*

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto** | | 0 | 30 | 120 | 90 | 60 | 0 |
| **Inventario Disponible** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Requerimiento Neto** | | 0 | 30 | 120 | 90 | 60 | 0 |
| **Recepción Planeada** | | 0 | 30 | 120 | 90 | 60 | 0 |
| **Lanzamiento Planeado** | 0 | 30 | 120 | 90 | 60 | 0 | 0 |

#### 4. Compuesto B (Lead Time = 1 semana, Lote a Lote)
*Requerimiento bruto = Lanzamiento planeado de Producto Final $\times 0.2\text{ L}$.*

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto** | | 0 | 20 | 80 | 60 | 40 | 0 |
| **Inventario Disponible** | 50 | 50 | 30 | 0 | 0 | 0 | 0 |
| **Requerimiento Neto** | | 0 | 0 | 50 | 60 | 40 | 0 |
| **Recepción Planeada** | | 0 | 0 | 50 | 60 | 40 | 0 |
| **Lanzamiento Planeado** | 0 | 0 | 50 | 60 | 40 | 0 | 0 |

#### 5. Compuesto C (Lead Time = 2 semanas, Lote a Lote)
*Requerimiento bruto = Lanzamiento planeado de Compuesto B $\times (100\text{ ml} / 200\text{ ml}) = 0.5\text{ L}$ por litro de B.*
*Es decir, $50\%$ del compuesto B es compuesto C.*
*   Semana 2: Req. Bruto = $50 \times 0.5 = 25\text{ L}$.
*   Semana 3: Req. Bruto = $60 \times 0.5 = 30\text{ L}$.
*   Semana 4: Req. Bruto = $40 \times 0.5 = 20\text{ L}$.

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto** | | 0 | 25 | 30 | 20 | 0 | 0 |
| **Inventario Disponible** | 50 | 50 | 25 | 0 | 0 | 0 | 0 |
| **Requerimiento Neto** | | 0 | 0 | 5 | 20 | 0 | 0 |
| **Recepción Planeada** | | 0 | 0 | 5 | 20 | 0 | 0 |
| **Lanzamiento Planeado** | 0 | 5 | 20 | 0 | 0 | 0 | 0 |

#### 6. Compuesto D (Lead Time = 1 semana, Lote a Lote)
*Requerimiento bruto = Lanzamiento planeado de Compuesto B $\times 0.5\text{ L}$ por litro de B.*

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto** | | 0 | 25 | 30 | 20 | 0 | 0 |
| **Inventario Disponible** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Requerimiento Neto** | | 0 | 25 | 30 | 20 | 0 | 0 |
| **Recepción Planeada** | | 0 | 25 | 30 | 20 | 0 | 0 |
| **Lanzamiento Planeado** | 0 | 25 | 30 | 20 | 0 | 0 | 0 |

---

### c) Algoritmo de Loteo para Compuesto C

Tenemos los siguientes requerimientos netos para el Compuesto C:
*   Semana 3: $5\text{ Litros}$
*   Semana 4: $20\text{ Litros}$

**Parámetros:**
*   Costo de ordenar (Setup) = $S = 10$
*   Costo de mantener inventario = $H = 1$ por litro por semana.

Evaluamos las dos políticas posibles:

#### Opción 1: Lote a Lote ($L \times L$) - No agrupar
*   **Semana 3:** Ordenamos $5\text{ L}$. Costo de ordenar = $10$. Costo de inventario = $0$.
*   **Semana 4:** Ordenamos $20\text{ L}$. Costo de ordenar = $10$. Costo de inventario = $0$.
*   **Costo Total = 20.**

#### Opción 2: Agrupar en la Semana 3 la demanda de la semana 3 y 4 (Ordenar $25\text{ L}$ en Semana 3)
*   **Semana 3:** Recibimos $25\text{ L}$. Costo de ordenar = $10$.
*   Mantenemos $20\text{ L}$ en inventario de la semana 3 a la 4 (1 semana).
*   Costo de mantener inventario = $20\text{ L} \times 1\text{ semana} \times \$1 = 20$.
*   **Costo Total = 10 (orden) + 20 (inventario) = 30.**

#### Conclusión:
La mejor opción es la **Opción 1: Lote a Lote** con un costo de **$20$**, comparado con los $30$ de agrupar. No conviene agrupar lotes debido a que el costo de mantener inventario ($20$) supera el ahorro de evitar un setup ($10$).

---

## Problema 3 (PERT) - Solución

### 1. Tiempos tempranos, tardíos y Ruta Crítica

Para cada actividad se calculan el tiempo esperado y la varianza:
*   $t_e = \frac{a + 4m + b}{6}$
*   $\sigma^2 = \left(\frac{b - a}{6}\right)^2$

| Actividad | Predecesores | $a$ | $m$ | $b$ | $t_e$ | $\sigma^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | — | 4 | 5 | 6 | 5 | 0.09 |
| **B** | — | 2 | 3 | 4 | 3 | 0.04 |
| **C** | A, B | 3 | 4 | 5 | 4 | 0.09 |
| **D** | C | 2 | 3 | 4 | 3 | 0.09 |
| **E** | C | 3 | 5 | 7 | 5 | 0.44 |
| **F** | D, E | 2 | 4 | 6 | 4 | 0.44 |

#### Cálculo de Calendario:

| Actividad | $t_e$ | ES | EF | LS | LF | Holgura ($LF - EF$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 5 | 0 | 5 | 0 | 5 | 0 (Crítica) |
| **B** | 3 | 0 | 3 | 2 | 5 | 2 |
| **C** | 4 | 5 | 9 | 5 | 9 | 0 (Crítica) |
| **D** | 3 | 9 | 12 | 11 | 14 | 2 |
| **E** | 5 | 9 | 14 | 9 | 14 | 0 (Crítica) |
| **F** | 4 | 14 | 18 | 14 | 18 | 0 (Crítica) |

*   **Ruta Crítica:** $A \rightarrow C \rightarrow E \rightarrow F$
*   **Duración Esperada ($T_e$):** $5 + 4 + 5 + 4 = 18$ semanas.
*   **Desviación Estándar de la Ruta Crítica ($\sigma_T$):**
    $$\sigma_T = \sqrt{\sigma_A^2 + \sigma_C^2 + \sigma_E^2 + \sigma_F^2} = \sqrt{0.09 + 0.09 + 0.44 + 0.44} = \sqrt{1.06} \approx 1.03 \text{ semanas}$$
    *(Nota: Si usamos la desviación estándar directa del cuadro original $\sigma_i$: $\sigma_T = \sqrt{0.9^2 + 1.0^2 + 1.1^2 + 0.8^2} = \sqrt{0.81 + 1.0 + 1.21 + 0.64} = \sqrt{3.66} \approx 1.91$ semanas).*

---

### 2. Duración doble de probabilidad de excederse que de cumplir

Sea $T_0$ el plazo buscado. Queremos que:
$$P(T > T_0) = 2 P(T \le T_0)$$
Como $P(T > T_0) + P(T \le T_0) = 1$, sustituyendo obtenemos:
$$3 P(T \le T_0) = 1 \implies P(T \le T_0) = 0.3333$$

Buscando en la tabla de la normal estándar para una probabilidad acumulada de $0.3333$, obtenemos un valor de $Z \approx -0.43$.
$$\frac{T_0 - 18}{1.91} = -0.43 \implies T_0 = 18 - 0.43 \times 1.91 \approx 17.18 \text{ semanas}$$

---

### 3. Contrato con Bono y Penalización

*   **Bono:** $\$200$ si se termina en $\le 15$ semanas.
*   **Penalización:** $-\$80$ si se termina en $\ge 20$ semanas.

#### Probabilidad de ganar el Bono ($T \le 15$):
$$Z_{bono} = \frac{15 - 18}{1.91} = -1.57 \implies P(T \le 15) = P(Z \le -1.57) \approx 0.0582 \text{ (5.8\%)}$$

#### Probabilidad de pagar Penalización ($T \ge 20$):
$$Z_{pen} = \frac{20 - 18}{1.91} = 1.05 \implies P(T \ge 20) = P(Z \ge 1.05) = 1 - 0.8531 = 0.1469 \text{ (14.7\%)}$$

#### Valor Esperado (EV):
$$EV = 200 \times P(T \le 15) - 80 \times P(T \ge 20) = 200 \times 0.0582 - 80 \times 0.1469 = 11.64 - 11.75 = -0.11$$

Como el **Valor Esperado es negativo (-\$0.11)**, se debería **rechazar** el contrato bajo estas condiciones.

#### Plazo máximo del bono para aceptar:
Para que $EV > 0$:
$$200 \times P(T \le X) - 80 \times 0.1469 = 0 \implies P(T \le X) = \frac{11.75}{200} = 0.0588$$
Esto da un $Z \approx -1.56$.
$$\frac{X - 18}{1.91} = -1.56 \implies X \approx 15.02 \text{ semanas}$$
El plazo máximo para ofrecer el bono debe ser de al menos $15.02$ semanas para que el valor esperado sea positivo.

---

### 4. Reducción de 3 semanas con costo mínimo

Queremos reducir el proyecto en 3 semanas. Las actividades en la ruta crítica que podemos acelerar a su tiempo optimista son:

*   **Actividad A:** De $5 \rightarrow 4$ semanas. Ahorro = $1$ semana. Costo adicional = $\$10$ (el doble del costo normal). Costo por semana de aceleración = $\$10$.
*   **Actividad C:** De $4 \rightarrow 3$ semanas. Ahorro = $1$ semana. Costo adicional = $\$7$. Costo por semana de aceleración = $\$7$.
*   **Actividad E:** De $5 \rightarrow 3$ semanas. Ahorro = $2$ semanas. Costo adicional = $\$12$. Costo por semana de aceleración = $\$6$.
*   **Actividad F:** De $4 \rightarrow 2$ semanas. Ahorro = $2$ semanas. Costo adicional = $\$10$. Costo por semana de aceleración = $\$5$.

#### Estrategia de Aceleración al Costo Mínimo:
1.  Aceleramos **F** por 2 semanas.
    *   Costo de aceleración = $\$10$.
    *   Duración acumulada reducida = 2 semanas.
2.  Para la tercera semana de reducción, la opción más barata disponible en la ruta crítica es acelerar **E** (costo de $\$6$ por semana) o **C** (costo de $\$7$ por semana).
    *   Dado que el enunciado indica que no se permite aceleración parcial, debemos acelerar **C** por 1 semana (costo $\$7$).
    *   *Nota:* Si aceleráramos E, tendríamos que reducir las 2 semanas completas con un costo de $\$12$, lo cual es más caro que acelerar C por $\$7$.
3.  **Costo Mínimo Adicional:** $\$10 \text{ (por F)} + \$7 \text{ (por C)} = \$17$.
4.  **Costo Total del Proyecto:** Costo normal total $(\$26) + \$17 = \$43$.
