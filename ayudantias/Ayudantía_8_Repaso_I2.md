# Ayudantía 8 - Repaso I2

**Pontificia Universidad Católica de Chile**  
**Escuela de Ingeniería**  
**Departamento de Ingeniería Industrial y de Sistemas**  
**ICS3213: Gestión de Operaciones**  
*Profesores: Alejandro Mac Cawley - Rodrigo Carrasco*  
*Semestre: Primer Semestre 2026*  
*Ayudante: Juan Pablo García (jgarca@uc.cl)*  

---

## Módulos de Repaso Teórico

### 1. Planificación Agregada

La planificación agregada es el proceso de traducir la estrategia de una empresa en acciones concretas, actuando como un puente entre la estrategia competitiva y las operaciones diarias.

*   **Nivel de Decisión:** Nivel táctico con impacto operativo (mediano plazo).
*   **Concepto de "Agregación":** Al consolidar la demanda de múltiples SKU en "unidades equivalentes", los errores de pronóstico tienden a compensarse (ley de los grandes números).
*   **Estrategias puras:**
    *   *Persecución (Chase):* Ajusta la capacidad (mano de obra, horas extra, subcontratación) para seguir la demanda período a período. Inventario mínimo, altos costos de contratación/despido.
    *   *Nivelación (Level):* Tasa de producción constante. El desajuste se absorbe con inventario o faltantes. Fuerza laboral estable, costos de inventario/quiebres de stock.
    *   *Mixta:* Combinación óptima de ambas.

### 2. MRP (Planificación de Requerimientos de Materiales)

*   **MPS (Plan Maestro de Producción):** Traduce el plan agregado en productos específicos y cantidades en el tiempo.
*   **MRP:** Explota el MPS hacia atrás usando la Lista de Materiales (BOM) y los Lead Times.
*   **Métodos de Loteo:**
    *   *Lote a Lote ($L \times L$):* Ordenar exactamente lo requerido.
    *   *EOQ:* Cantidad fija basada en promedio.
    *   *Silver-Meal:* Minimiza el costo promedio por período de manera heurística.
    *   *Wagner-Whitin:* Algoritmo exacto de programación dinámica.

### 3. PERT (Programación de Proyectos)

Duración estimada de actividad con distribución Beta $(a, m, b)$:
$$t_e = \frac{a + 4m + b}{6}$$
$$\sigma = \frac{b - a}{6}$$

*   **Ruta Crítica:** Ruta de actividades con holgura cero ($H = LF - EF = 0$).
*   **Duración del Proyecto:** Variable normal $T \sim N(T_e, \sigma_T^2)$ donde $\sigma_T^2 = \sum_{i \in \text{ruta crítica}} \sigma_i^2$.

### 4. Variabilidad

*   **Ley de Little:** $L = \lambda \cdot W \implies WIP = TH \cdot CT$.
*   **Coeficiente de Variación:** $c_x = \sigma_x / \mu_x$.
*   **Fallas y Disponibilidad:** $A = \frac{MTBF}{MTBF + MTTR}$.
*   **Ecuación de Kingman ($G/G/1$):**
    $$CT_q = \left( \frac{c_a^2 + c_e^2}{2} \right) \left( \frac{\rho}{1 - \rho} \right) t_e$$
*   **Propagación:** $c_s^2 \approx \rho^2 c_e^2 + (1 - \rho^2) c_a^2$.

---

## Enunciados de los Problemas

### Problema 1 (Planificación agregada)

La panadería "La Miga Dorada" elabora panes artesanales. Cada pan requiere 1 hora-hombre (HH) de producción. Se proyecta la siguiente demanda mensual para el primer trimestre:

| Mes | Enero | Febrero | Marzo |
| :--- | :---: | :---: | :---: |
| **Demanda (unidades)** | 1,200 | 2,000 | 1,000 |

*   **Dotación inicial:** 10 panaderos.
*   **Capacidad mensual:** Cada mes tiene 20 días hábiles de 8 horas normales (160 HH/mes por trabajador).
*   **Costo HH normal:** $\$50$/hora.
*   **Costo HH extra:** $\$80$/hora.
*   **Costo mantener inventario:** $\$10$/pan al mes.
*   **Costo de faltante:** $\$15$/pan al mes.
*   **Costos de personal:** Contratar cuesta $\$1,500$ por panadero; despedir cuesta $\$2,500$ por panadero.

Se pide comparar tres planes agregados:
1.  **Plan Chase:** Ajustar la cantidad de panaderos cada mes para producir exactamente la demanda (sin inventario ni faltantes).
2.  **Plan Nivel con Inventario y Faltante:** Mantener los 10 panaderos todo el trimestre; producir al máximo en horas normales, permitiendo inventario o faltantes.
3.  **Plan Nivel con Horas Extra:** Mantener 10 panaderos; producir a tarifa normal hasta capacidad y cubrir cualquier exceso de demanda con horas extra (no se permiten faltantes ni inventario).

Indique qué plan conviene según el costo total.

---

### Problema 2 (Planificación CP y MRP)

Una empresa fabrica un producto que ensambla a partir de: 1 unidad del producto A, 2 unidades del producto B y 1 unidad del producto C. A su vez, el producto A requiere 1 unidad de A1 y 2 de A2. El producto B requiere 1 unidad de A1 y 1 de B2.

*   **Lead Times:** Ensamblaje final = 1 semana. Todos los demás componentes = 2 semanas.
*   **Demanda final (semanas 1-8):**

| Período | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Demanda** | 0 | 0 | 0 | 10 | 50 | 40 | 60 | 50 |

Se pide:
1.  Dibuje un árbol que represente la Lista de Materiales (BOM).
2.  Considere que el inventario disponible de producto final es de 50 unidades y ya se ha iniciado la producción de un lote de 20 unidades del producto final que estará disponible en la semana 2. Determine la matriz de MRP para el producto final usando loteo Lote a Lote ($L4L$).
3.  Considere que la demanda por la parte A1 es la siguiente:

| Período | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Demanda** | 0 | 30 | 120 | 180 | 150 | 0 | 0 | 0 |

Asumiendo que el costo de setup es $\$120$ y el costo de mantener inventario es $\$0.9$ por unidad/semana, use la heurística de **Silver-Meal** para calcular los lotes óptimos e indique el costo total.

---

### Problema 3 (PERT)

Se dispone de la siguiente relación de dependencia y tiempos de etapas de un proyecto (en semanas):

| Etapa | Predecesor | Tiempo optimista ($a$) | Tiempo más probable ($m$) | Tiempo pesimista ($b$) |
| :---: | :---: | :---: | :---: | :---: |
| **A** | - | 2 | 3 | 4 |
| **B** | A | 2 | 4 | 6 |
| **C** | A | 5 | 6 | 13 |
| **D** | B, C | 3 | 6 | 9 |
| **E** | B | 2 | 5 | 8 |
| **F** | D, E | 2 | 4 | 6 |

Se pide:
1.  Encuentre los tiempos esperados y varianzas para cada actividad.
2.  Dibuje el diagrama PERT asociado al proyecto.
3.  Obtenga ES, EF, LS, LF y holgura para cada etapa. ¿Cuál es la ruta crítica y duración mínima?
4.  ¿Cuál es la probabilidad de que el proyecto sea completado en menos de 22 semanas? Realice un intervalo de confianza de $95\%$ para la duración.
5.  Su cliente ofrece un bono de $\$8,000$ si el proyecto se termina en menos de 18 semanas. Dados los siguientes costos de aceleración por semana, ¿qué actividades acortaría?

| Actividad | Reducción máx (semanas) | Costo Normal (\$) | Costo Acelerado (\$) |
| :---: | :---: | :---: | :---: |
| **A** | 1 | 10,000 | 13,000 |
| **B** | 1 | 6,000 | 9,000 |
| **C** | 2 | 4,000 | 7,000 |
| **D** | 2 | 13,000 | 18,000 |
| **E** | 2 | 9,000 | 13,000 |
| **F** | 1 | 7,000 | 8,000 |

---

### Problema 4 (Variabilidad)

Los clientes llegan a una imprenta a una tasa $\lambda$ [clientes/hr] (distribución general) y la capacidad de atención es $\mu$ [clientes/hr]. El tiempo efectivo es $t_e$, el coeficiente de variabilidad de llegadas es $c_a$ y el de servicio es $c_e$. 

Para evitar colapsos y setups costosos, evalúa realizar descuentos ($\Delta$) en el precio de venta para alterar la tasa de llegada, la cual responde a: $\lambda = \lambda_0 e^{-\Delta}$. El costo de espera del cliente es $CE(W) = 100 + W$ donde $W$ es el tiempo total en el sistema.

1.  Plantee el modelo de programación matemática que permita optimizar el proceso productivo. Deje expresadas las condiciones de primer orden (no las resuelva).
2.  Si se abre la posibilidad de adquirir nueva capacidad productiva a un costo de $\$K$ por cada unidad de aumento en la tasa de servicio, ¿cómo cambia el modelo?

---

## Solución Propuesta (Resolución Completa)

### Solución Problema 1: Planificación Agregada

#### 1. Plan Chase (Ajustar trabajadores mes a mes)
*   Capacidad de 1 trabajador = $20 \text{ días} \times 8 \text{ horas} = 160$ HH/mes.
*   Dado que $1\text{ pan} = 1\text{ HH}$, la cantidad de panaderos necesarios en el mes $t$ es $d_t / 160$:
    *   **Enero (1,200 unidades):** Requerimiento = $1200 / 160 = 7.5$ panaderos.
        *   Como iniciamos con 10, despedimos a $2.5$ panaderos.
        *   Costo de despido = $2.5 \times 2,500 = \$6,250$.
    *   **Febrero (2,000 unidades):** Requerimiento = $2000 / 160 = 12.5$ panaderos.
        *   Contratamos a $12.5 - 7.5 = 5$ panaderos.
        *   Costo de contratación = $5 \times 1,500 = \$7,500$.
    *   **Marzo (1,000 unidades):** Requerimiento = $1000 / 160 = 6.25$ panaderos.
        *   Despedimos a $12.5 - 6.25 = 6.25$ panaderos.
        *   Costo de despido = $6.25 \times 2,500 = \$15,625$.

*   **Costos Totales Plan Chase:**
    *   *Contratación y Despido:* $7,500 \text{ (contratar)} + (6,250 + 15,625) \text{ (despedir)} = \$29,375$.
    *   *Mano de Obra Normal:* $4,200\text{ HH (demanda total)} \times \$50 = \$210,000$.
    *   *Inventario / Faltante:* $\$0$ (se produce exactamente la demanda).
    *   **Costo Total Chase = \$239,375.**

#### 2. Plan Nivel con Inventario y Faltantes (10 panaderos constantes)
*   Producción mensual fija = $10 \times 160 = 1,600$ unidades.
    *   **Enero:** Demanda = 1,200. Producción = 1,600. Inventario final = $400$. Costo de almacenamiento = $400 \times \$10 = \$4,000$.
    *   **Febrero:** Demanda = 2,000. Producción = 1,600. Usamos las 400 unidades de inventario. Inventario final = $0$. Faltantes = $0$. Costo = $\$0$.
    *   **Marzo:** Demanda = 1,000. Producción = 1,600. Inventario final = $600$. Costo de almacenamiento = $600 \times \$10 = \$6,000$.

*   **Costos Totales Plan Nivel con Inventario:**
    *   *Contratación y Despido:* $\$0$.
    *   *Mano de Obra Normal:* $10 \text{ panaderos} \times 3 \text{ meses} \times 160 \text{ horas} \times \$50 = \$240,000$.
    *   *Inventario:* $\$4,000 + \$6,000 = \$10,000$.
    *   *Faltantes:* $\$0$.
    *   **Costo Total Nivel con Inventario = \$250,000.**

#### 3. Plan Nivel con Horas Extra (10 panaderos constantes, sin inventario ni faltante)
*   Mantenemos 10 panaderos. Capacidad normal = 1,600 unidades. Producimos la demanda de cada mes sin guardar stock para el siguiente:
    *   **Enero (1,200 demandados):** Producimos 1,200 en horas normales. Pagamos los salarios base de 10 trabajadores (\$80,000). Costo Horas Extra = $\$0$.
    *   **Febrero (2,000 demandados):** Producimos 1,600 en horas normales y 400 en horas extra. Costo Horas Extra = $400 \text{ HH} \times \$80 = \$32,000$.
    *   **Marzo (1,000 demandados):** Producimos 1,000 en horas normales. Costo Horas Extra = $\$0$.

*   **Costos Totales Plan Nivel con Horas Extra:**
    *   *Contratación y Despido:* $\$0$.
    *   *Mano de Obra Normal:* $10 \text{ panaderos} \times 3 \text{ meses} \times 160 \text{ horas} \times \$50 = \$240,000$.
    *   *Horas Extra:* $\$32,000$ (en Febrero).
    *   **Costo Total Nivel con Horas Extra = \$272,000.**

**Conclusión:** El plan más económico es el **Plan Chase** con un costo total de **$\$239,375$**.

---

### Solución Problema 2: Planificación CP y MRP

#### 1. Árbol Bill of Materials (BOM)
```
Producto Final
├── A (1)
│   ├── A1 (1)
│   └── A2 (2)
├── B (2)
│   ├── A1 (1)
│   └── B2 (1)
└── C (1)
```

#### 2. Matriz MRP del Producto Final (L4L, LT = 1 semana)
*   Inventario Inicial = 50. Recepción programada = 20 en la semana 2.

| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Requerimiento Bruto** | | 0 | 0 | 0 | 10 | 50 | 40 | 60 | 50 |
| **Recepciones Programadas**| | | 20 | | | | | | |
| **Inventario Disponible** | 50 | 50 | 70 | 70 | 60 | 10 | 0 | 0 | 0 |
| **Requerimiento Neto** | | 0 | 0 | 0 | 0 | 0 | 30 | 60 | 50 |
| **Recepción Planeada** | | 0 | 0 | 0 | 0 | 0 | 30 | 60 | 50 |
| **Lanzamiento Planeado** | | 0 | 0 | 0 | 0 | 30 | 60 | 50 | 0 |

#### 3. Heurística Silver-Meal para A1 (S = \$120, H = \$0.9)
Demanda neta de A1:
*   Semana 2: 30
*   Semana 3: 120
*   Semana 4: 180
*   Semana 5: 150

**Cálculo:**
*   **Lote 1 (comienza en Semana 2):**
    *   *Período 2 (1 semana):* Lote = 30. Costo = 120. Costo/período = $120 / 1 = 120$.
    *   *Períodos 2-3 (2 semanas):* Lote = 30 + 120 = 150. Costo = $120 + (120 \times 0.9 \times 1) = 228$. Costo/período = $228 / 2 = 114$.
    *   *Períodos 2-4 (3 semanas):* Lote = 330. Costo = $228 + (180 \times 0.9 \times 2) = 552$. Costo/período = $552 / 3 = 184$.
    *   *Decisión:* Detenerse. Primer lote en semana 2 para cubrir semanas 2 y 3. **Lote = 150**.
*   **Lote 2 (comienza en Semana 4):**
    *   *Período 4 (1 semana):* Lote = 180. Costo = 120. Costo/período = 120.
    *   *Períodos 4-5 (2 semanas):* Lote = 180 + 150 = 330. Costo = $120 + (150 \times 0.9 \times 1) = 255$. Costo/período = $255 / 2 = 127.5$.
    *   *Decisión:* Detenerse ya que $127.5 > 120$. Segundo lote en semana 4 para semana 4. **Lote = 180**.
*   **Lote 3 (comienza en Semana 5):**
    *   Tercer lote en semana 5 para semana 5. **Lote = 150**.

*   **Costo Total Silver-Meal:**
    *   *Setups:* $3 \text{ setups} \times \$120 = \$360$.
    *   *Inventario:* $120 \text{ unid} \times 1 \text{ sem} \times \$0.9 = \$108$.
    *   **Costo Total = \$468.**

---

### Solución Problema 3: PERT

#### 1. Tiempos Esperados y Varianzas

*   $t_e = \frac{a + 4m + b}{6}$
*   $\sigma^2 = \left(\frac{b-a}{6}\right)^2$

| Actividad | $a$ | $m$ | $b$ | $t_e$ | $\sigma^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 2 | 3 | 4 | **3** | **0.111** (1/9) |
| **B** | 2 | 4 | 6 | **4** | **0.444** (4/9) |
| **C** | 5 | 6 | 13 | **7** | **1.778** (16/9) |
| **D** | 3 | 6 | 9 | **6** | **1.000** (9/9) |
| **E** | 2 | 5 | 8 | **5** | **1.000** (9/9) |
| **F** | 2 | 4 | 6 | **4** | **0.444** (4/9) |

#### 2. Tiempos de Calendario y Ruta Crítica

*   **Forward Pass:**
    *   $ES_A = 0 \implies EF_A = 3$
    *   $ES_B = EF_A = 3 \implies EF_B = 7$
    *   $ES_C = EF_A = 3 \implies EF_C = 10$
    *   $ES_D = \max(EF_B, EF_C) = \max(7, 10) = 10 \implies EF_D = 16$
    *   $ES_E = EF_B = 7 \implies EF_E = 12$
    *   $ES_F = \max(EF_D, EF_E) = \max(16, 12) = 16 \implies EF_F = 20$
    *   *Duración mínima:* **20 semanas**.
*   **Backward Pass ($LF_F = 20$):**
    *   $LF_F = 20 \implies LS_F = 16$
    *   $LF_E = 16 \implies LS_E = 11$
    *   $LF_D = 16 \implies LS_D = 10$
    *   $LF_C = LS_D = 10 \implies LS_C = 3$
    *   $LF_B = \min(LS_D, LS_E) = \min(10, 11) = 10 \implies LS_B = 6$
    *   $LF_A = \min(LS_B, LS_C) = \min(6, 3) = 3 \implies LS_A = 0$

*   **Holguras ($H = LF - EF$):**
    *   $H_A = 3 - 3 = 0$
    *   $H_B = 10 - 7 = 3$
    *   $H_C = 10 - 10 = 0$
    *   $H_D = 16 - 16 = 0$
    *   $H_E = 16 - 12 = 4$
    *   $H_F = 20 - 20 = 0$
*   **Ruta Crítica:** $A \rightarrow C \rightarrow D \rightarrow F$.

#### 3. Análisis Probabilístico
*   **Desviación Estándar de la Ruta Crítica ($\sigma_T$):**
    $$\sigma_T = \sqrt{\sigma_A^2 + \sigma_C^2 + \sigma_D^2 + \sigma_F^2} = \sqrt{\frac{1}{9} + \frac{16}{9} + 1 + \frac{4}{9}} = \sqrt{\frac{30}{9}} \approx 1.83 \text{ semanas}$$
*   **Probabilidad de completar en menos de 22 semanas:**
    $$Z = \frac{22 - 20}{1.83} \approx 1.09 \implies P(Z \le 1.09) = 0.8621 \approx 86.2\%$$
*   **Intervalo de confianza del 95%:**
    $$[20 - 1.96 \cdot 1.83, \; 20 + 1.96 \cdot 1.83] \implies [16.41, \; 23.59] \text{ semanas}$$

#### 4. Aceleración (Crashing) para Bono de 18 semanas
*   Debemos reducir 2 semanas en la ruta crítica ($A \rightarrow C \rightarrow D \rightarrow F$):
    *   **A:** Reducción = 1 sem, costo = $\$3,000$.
    *   **C:** Reducción = 2 sem, costo = $\$1,500$/semana.
    *   **D:** Reducción = 2 sem, costo = $\$2,500$/semana.
    *   **F:** Reducción = 1 sem, costo = $\$1,000$/semana.

*   *Paso 1:* Acelerar **F** en 1 semana (costo $\$1,000$). Duración = 19 semanas.
*   *Paso 2:* Acelerar **C** en 1 semana (costo $\$1,500$). Duración = 18 semanas.
*   **Costo de aceleración total = \$2,500.**
*   *Beneficio Neto:* $\$8,000 \text{ (bono)} - \$2,500 \text{ (costo)} = \$5,500$.
*   *Decisión:* Se acortan **F** (1 semana) y **C** (1 semana).

---

### Solución Problema 4: Variabilidad

#### a) Modelo de Optimización
*   **Variable de decisión:** Descuento $\Delta$.
*   **Tasa de llegada:** $\lambda(\Delta) = \lambda_0 e^{-\Delta}$.
*   **Tiempo total en el sistema (espera + servicio) ($W$):**
    $$W = W_q + \frac{1}{\mu} = \left( \frac{c_a^2 + c_e^2}{2} \right) \left( \frac{\lambda(\Delta)}{\mu(\mu - \lambda(\Delta))} \right) + \frac{1}{\mu}$$
*   **Objetivo:** Minimizar el costo total (descuento otorgado + costo de espera del cliente):
    $$\min_{\Delta} \quad f(\Delta) = \Delta \cdot \lambda(\Delta) + [100 + W(\Delta)] \cdot \lambda(\Delta)$$
    $$\min_{\Delta} \quad \lambda_0 e^{-\Delta} \left[ \Delta + 100 + \left( \frac{c_a^2 + c_e^2}{2} \right) \frac{\lambda_0 e^{-\Delta}}{\mu(\mu - \lambda_0 e^{-\Delta})} + \frac{1}{\mu} \right]$$

*   **Restricciones de estabilidad:**
    $$\lambda_0 e^{-\Delta} < \mu \implies \Delta > \ln\left( \frac{\lambda_0}{\mu} \right)$$
    $$\Delta \ge 0$$

*   **Condiciones de Primer Orden (CPO):**
    Derivar la función objetivo $f(\Delta)$ con respecto a $\Delta$ e igualar a cero:
    $$\frac{df}{d\Delta} = 0 \implies -\lambda(\Delta) \cdot [\Delta + 100 + W] + \lambda(\Delta) \cdot \left[ 1 + \frac{dW}{d\Delta} \right] = 0$$
    $$W + 100 + \Delta - 1 - \frac{dW}{d\Delta} = 0$$
    Donde:
    $$\frac{dW}{d\Delta} = \left( \frac{c_a^2 + c_e^2}{2} \right) \left( \frac{-\lambda_0 e^{-\Delta}}{\mu - \lambda_0 e^{-\Delta}} - \frac{\lambda_0^2 e^{-2\Delta}}{(\mu - \lambda_0 e^{-\Delta})^2} \right) \frac{1}{\mu}$$

#### b) Modelo con Ampliación de Capacidad
Se agrega la variable de decisión $u$ (incremento en la tasa de servicio) de modo que la capacidad de atención pasa a ser $\mu = \mu_0 + u$.

$$\min_{\Delta, u} \quad \lambda_0 e^{-\Delta} \left[ \Delta + 100 + W(\Delta, u) \right] + K \cdot u$$

Sujeto a:
$$\Delta \ge 0, \quad u \ge 0$$
$$\lambda_0 e^{-\Delta} < \mu_0 + u$$
y la correspondiente actualización de $W(\Delta, u)$ usando la nueva capacidad $\mu_0 + u$.
