# Ayudantía 8 — Repaso I2: Pauta Completa

**Pontificia Universidad Católica de Chile**
**Departamento Ingeniería Industrial y de Sistemas**
**ICS3213 – Gestión de Operaciones**
*Profesores: Alejandro Mac Cawley — Rodrigo Carrasco (Secciones 1, 2 y 3)*
*Primer Semestre 2026*
*Ayudante: Juan Pablo García — jgarca@uc.cl*

---

## Repaso Teórico y Consejos por Módulo

### Módulo 1: Planificación Agregada

La planificación agregada traduce la estrategia de una empresa en acciones concretas, actuando como puente entre la estrategia competitiva y las operaciones diarias.

**Nivel de Decisión:** Táctico con impacto operativo (mediano plazo), entre la planeación estratégica (largo plazo) y la programación diaria (corto plazo).

**Concepto de "Agregación":**
- Los pronósticos por producto individual (SKU) tienen alto nivel de error.
- Al consolidar la demanda de múltiples productos, los errores individuales tienden a compensarse (ley de los grandes números).
- Se usan "unidades equivalentes" que agrupan productos similares.
- Objetivo: igualar demanda prevista con capacidad productiva, tomando decisiones sobre producción, subcontratación, inventario y fuerza laboral.

**Estrategias para abordar la demanda:**

| Estrategia | Descripción | Ventaja | Desventaja |
|:---|:---|:---|:---|
| **Persecución (Chase)** | Ajusta capacidad para seguir la demanda período a período (contratar/despedir/horas extra) | Inventario mínimo | Costos altos de contratación/despido, impacto en moral |
| **Nivelación (Level)** | Tasa de producción constante; el desajuste se absorbe con inventario o faltantes | Fuerza laboral estable, sin costos de rotación | Costos de inventario o pérdida de ventas |
| **Mixta** | Combinación de ambas según temporada, costo y restricciones laborales | Equilibrio costo-flexibilidad | Mayor complejidad de planificación |

---

### Módulo 2: MRP (Planificación de Requerimientos de Materiales)

**Jerarquía de planificación:**
$$\text{Planificación Agregada} \to \text{MPS} \to \text{MRP} \to \text{Programación diaria}$$

- **MPS:** Traduce el plan agregado en productos específicos, cantidades y períodos. Responde: ¿cuántas unidades del producto X en la semana Y?
- **MRP:** Explota el MPS hacia atrás en el tiempo usando el BOM y los Lead Times. Responde: ¿qué materiales, en qué cantidad y cuándo lanzar órdenes?

**Métodos de Lotificación:**

| Método | Lógica | Ventaja | Desventaja |
|:---|:---|:---|:---|
| **Lote a Lote (L×L)** | Ordena exactamente lo necesario cada período | Cero inventario | Muchos setups si la demanda es frecuente |
| **Cantidad Fija** | Siempre la misma cantidad predefinida | Simple | Puede generar inventario innecesario |
| **Período Fijo** | Ordena cada N períodos | Reduce frecuencia de órdenes | Inventario variable e impredecible |
| **EOQ** | Cantidad óptima con demanda promedio constante | Óptimo con demanda estable | Asume demanda constante (rara vez real en MRP) |
| **Silver-Meal** | Minimiza costo promedio por período heurísticamente | Se adapta a demanda variable, simple | No garantiza el óptimo global |
| **Wagner-Whitin** | Programación dinámica exacta | Óptimo matemático | Computacionalmente costoso, menos intuitivo |

**Consejo clave para Silver-Meal:** Calcular $C(1), C(2), \ldots$ hasta que $C(k+1) > C(k)$, donde:
$$C(k) = \frac{S + H \sum_{j=1}^{k-1} j \cdot D_{t+j}}{k}$$
Parar en $k$ y lanzar ese lote. Iniciar nueva iteración desde el período siguiente con demanda.

---

### Módulo 3: PERT (Programación de Proyectos)

**Distribución Beta para duración de actividad $(a, m, b)$:**
$$t_e = \frac{a + 4m + b}{6}, \qquad \sigma = \frac{b - a}{6}, \qquad \sigma^2 = \left(\frac{b-a}{6}\right)^2$$

**Tiempos de calendario:**
- **ES** (Earliest Start): máximo de los EF de todos los predecesores. Para actividades sin predecesores: ES = 0.
- **EF** (Earliest Finish): $EF = ES + t_e$.
- **LF** (Latest Finish): mínimo de los LS de los sucesores. Para la última actividad: $LF = T$.
- **LS** (Latest Start): $LS = LF - t_e$.
- **Holgura:** $H = LS - ES = LF - EF$.
- **Ruta Crítica:** actividades con holgura = 0. La duración del proyecto es $T = \max(EF)$.

**Estadísticas de la ruta crítica:**
$$\mu_p = \sum_{i \in RC} t_{e,i}, \qquad \sigma_p^2 = \sum_{i \in RC} \sigma_i^2, \qquad \sigma_p = \sqrt{\sigma_p^2}$$

**Crashing:** Reducción de duración a costo mínimo. La pendiente de crashing por actividad es:
$$\text{Pendiente}_i = \frac{CC_i - CN_i}{TN_i - TC_i} \quad [\$/\text{semana}]$$
Menor pendiente = más barato. Evaluar por valor esperado neto: $VE = \text{bono} \cdot P(\text{terminar antes}) - \text{costo aceleración}$.

---

### Módulo 4: Variabilidad (Teoría de Colas)

**Ley de Little:** $L = \lambda \cdot W \implies WIP = TH \cdot CT$

**Coeficiente de variación:** $c_x = \sigma_x / \mu_x$

**Disponibilidad ante fallas:**
$$A = \frac{MTBF}{MTBF + MTTR}$$
> Paradas largas e infrecuentes aumentan **mucho más** la variabilidad efectiva que paradas cortas y frecuentes.

**Impacto de Setups** en tiempo efectivo y varianza:
$$t_e = t_o + \frac{t_s}{N_s}, \qquad \sigma_e^2 = \sigma_o^2 + \frac{\sigma_s^2}{N_s} + \frac{N_s - 1}{N_s^2} t_s^2$$

**Modelo G/G/1 — Ecuación de Kingman (VUT):**
$$CT_q = \left(\frac{c_a^2 + c_e^2}{2}\right) \cdot \frac{\rho}{1-\rho} \cdot t_e, \qquad \rho = \frac{\lambda}{\mu}$$

**Propagación de variabilidad en serie:**
$$c_s^2 \approx \rho^2 \cdot c_e^2 + (1 - \rho^2) \cdot c_a^2$$

**Estrategias prácticas:**
- La utilización $\rho$ es el factor crítico: cuando $\rho \to 1$, el tiempo en cola explota exponencialmente.
- **Pooling (unifila):** consolida recursos y promedia la variabilidad global — siempre reduce la espera.
- **Psicología de la espera:** el cliente percibe el tiempo ocioso y las esperas injustas/inciertas como más largas. Distraer, explicar retrasos, ocultar empleados inactivos.

---

## Problema 1: Planificación Agregada — La Miga Dorada

### Enunciado

La panadería "La Miga Dorada" elabora panes artesanales. Cada pan requiere 1 hora-hombre (HH) de producción. Demanda mensual del primer trimestre:

| Mes | Enero | Febrero | Marzo |
|:---|:---:|:---:|:---:|
| **Demanda (panes)** | 1 200 | 2 000 | 1 000 |

**Datos:**
- Dotación inicial: 10 panaderos.
- Días hábiles por mes: 20 días × 8 horas = **160 HH/mes por panadero**.
- Costo HH normal: $\$50$/hora.
- Costo HH extra: $\$80$/hora.
- Costo inventario: $\$10$/pan al mes.
- Costo faltante: $\$15$/pan al mes.
- Contratar: $\$1\,500$/panadero. Despedir: $\$2\,500$/panadero.

**Se pide comparar:**
1. **Plan Chase:** ajustar panaderos mes a mes para producir exactamente la demanda.
2. **Plan Nivel con Inventario y Faltante:** mantener 10 panaderos; producir máximo normal; permitir inventario o faltantes.
3. **Plan Nivel con Horas Extra:** mantener 10 panaderos; cubrir exceso con horas extra; sin faltantes ni inventario.

### Solución Oficial

**Datos previos:**
- Capacidad normal mensual (10 panaderos): $10 \times 160 = 1\,600$ panes/mes.

---

#### Plan 1 — Chase

Panaderos requeridos cada mes = demanda / 160, **redondeando al entero más cercano**:

| Mes | Demanda | Panaderos req. | Transición | Costo cont./desp. |
|:---|:---:|:---:|:---|:---:|
| Enero | 1 200 | 8 | 10 → 8: **despido de 2** | $2 \times 2\,500 = \$5\,000$ |
| Febrero | 2 000 | 13 | 8 → 13: **contratación de 5** | $5 \times 1\,500 = \$7\,500$ |
| Marzo | 1 000 | 7 | 13 → 7: **despido de 6** | $6 \times 2\,500 = \$15\,000$ |
| **Total** | | | | **$\$27\,500$** |

- Costo MO normal: $(1\,200 + 2\,000 + 1\,000) \times \$50 = 4\,200 \times 50 = \$210\,000$.
- Inventario / Faltante: $\$0$ (produce exactamente la demanda).

$$\boxed{\text{Costo Total Plan Chase} = 210\,000 + 27\,500 = \$237\,500}$$

> **Nota de cálculo:** La pauta redondea a enteros al calcular los panaderos requeridos ($1200/160 = 7{,}5 \to 8$, etc.). Si se trabaja con fracciones el costo de cont./desp. cambia ligeramente pero la lógica es idéntica.

---

#### Plan 2 — Nivel con Inventario y Faltante

10 panaderos fijos → producción = 1 600 panes/mes:

| Mes | Producción | Demanda | Inv. final | Faltante | Costo |
|:---|:---:|:---:|:---:|:---:|:---:|
| Enero | 1 600 | 1 200 | **400** | 0 | $400 \times 10 = \$4\,000$ |
| Febrero | 1 600 | 2 000 | **0** | 0 | $\$0$ |
| Marzo | 1 600 | 1 000 | **600** | 0 | $600 \times 10 = \$6\,000$ |

- Costo MO normal: $3 \times 1\,600 \times \$50 = \$240\,000$.
- Costo inventario total: $\$10\,000$.

$$\boxed{\text{Costo Total Plan Nivel + Inv./Falt.} = 240\,000 + 10\,000 = \$250\,000}$$

---

#### Plan 3 — Nivel con Horas Extra

10 panaderos fijos → producción normal máxima = 1 600 panes/mes; el exceso se cubre con HH extra:

| Mes | Demanda | Prod. normal | Exceso | HH extra | Costo HE |
|:---|:---:|:---:|:---:|:---:|:---:|
| Enero | 1 200 | 1 200 | 0 | 0 | $\$0$ |
| Febrero | 2 000 | 1 600 | 400 | 400 | $400 \times 80 = \$32\,000$ |
| Marzo | 1 000 | 1 000 | 0 | 0 | $\$0$ |

- Costo MO normal: $\$240\,000$.
- Costo HH extra: $\$32\,000$.

$$\boxed{\text{Costo Total Plan Nivel + HE} = 240\,000 + 32\,000 = \$272\,000}$$

---

#### Conclusión

| Plan | Costo Total |
|:---|:---:|
| Chase | $\$237\,500$ |
| Nivel con Inventario y Faltante | $\$250\,000$ |
| Nivel con Horas Extra | $\$272\,000$ |

**El plan más económico es Plan Chase** ($\$237\,500$).

> **Supuesto de redondeo:** la pauta redondea los panaderos requeridos a enteros ($1200/160 = 7{,}5 \to 8$). Esto significa que en enero se producen $8 \times 160 = 1\,280$ panes, no 1,200 exactos — el plan Chase no es estrictamente puro. En la prueba, si el enunciado no especifica, declara tu supuesto (enteros o fracciones) y sé consistente. Ambos son aceptados si el cálculo es coherente.

---

## Problema 2: Planificación CP y MRP

### Enunciado

Una empresa fabrica un producto final ensamblado a partir de:
- 1 unidad de A → requiere 1 unidad de A1 y 2 de A2.
- 2 unidades de B → cada B requiere 1 unidad de A1 y 1 de B2.
- 1 unidad de C.

**Lead Times:** Ensamblaje final = 1 semana. Todos los demás componentes = 2 semanas.

Demanda del producto final (semanas 1–8):

| Período | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Demanda** | 0 | 0 | 0 | 10 | 50 | 40 | 60 | 50 |

**Se pide:**
1. Árbol BOM.
2. Matriz MRP del producto final con inventario inicial = 50 unidades, orden en tránsito = 20 unidades con llegada en semana 2. Usar **Lote a Lote (L4L)**.
3. Demanda consolidada de A1:

| Período | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Demanda A1** | 0 | 30 | 120 | 180 | 150 | 0 | 0 | 0 |

Costo de setup $S = \$120$, costo de inventario $H = \$0{,}9$ por unidad/semana. Usar **Silver-Meal**.

### Solución Oficial

#### i) Árbol BOM

```
Producto Final
├── A  (×1)
│   ├── A1 (×1)
│   └── A2 (×2)
├── B  (×2)
│   ├── A1 (×1)
│   └── B2 (×1)
└── C  (×1)
```

> **Nota:** A1 aparece en dos ramas: lo necesita A (×1) y B (×1 por cada B, pero se usan 2 B por PF → 2 unidades de A1 provenientes de B). La demanda consolidada de A1 = $1 \times \text{lanz. A} + 1 \times \text{lanz. B}$.

---

#### ii) Matriz MRP — Producto Final (L4L, LT = 1 semana)

- Inventario inicial (período 0): **50 unidades**.
- Orden en tránsito (SR): **20 unidades** en semana 2.

| Período | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Req. Bruto (GR)** | | 0 | 0 | 0 | 10 | 50 | 40 | 60 | 50 |
| **Recepciones Program. (SR)** | | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Inventario Final (OH)** | 50 | 50 | 70 | 70 | 60 | 10 | 0 | 0 | 0 |
| **Req. Neto (NR)** | | 0 | 0 | 0 | 0 | 0 | 30 | 60 | 50 |
| **Recepción Planeada (POR)** | | 0 | 0 | 0 | 0 | 0 | 30 | 60 | 50 |
| **Lanzamiento Planeado (PORelease)** | | 0 | 0 | 0 | 0 | 30 | 60 | 50 | — |

> **Cálculo inventario:** $OH_t = OH_{t-1} + SR_t + POR_t - GR_t$. Ej.: $OH_2 = 50 + 20 + 0 - 0 = 70$.

---

#### iii) Silver-Meal para A1

$S = \$120$, $H = \$0{,}9$/unidad/semana. Demanda: $[0, 30, 120, 180, 150, 0, 0, 0]$ (semanas 1–8).

> **Regla de aplicación:** Silver-Meal arranca siempre en el **primer período con demanda positiva**. El período 1 tiene demanda = 0: no hay nada que ordenar, $Q_1 = 0$ trivialmente. Empezamos el algoritmo en el período 2.

**Lote 1 — arranca en período 2 ($D_2 = 30$):**
- $k=1$ (solo sem. 2): $C(1) = 120$.
- $k=2$ (sem. 2–3, $D_3 = 120$): $C(2) = (120 + 1 \cdot 0{,}9 \cdot 120)/2 = 228/2 = 114 < 120$ → seguir.
- $k=3$ (sem. 2–4, $D_4 = 180$): $C(3) = (228 + 2 \cdot 0{,}9 \cdot 180)/3 = 552/3 = 184 > 114$ → **PARAR**.

**Lote en sem. 2:** cubre semanas 2 y 3. $Q_2 = 30 + 120 = \mathbf{150}$.

**Lote 2 — arranca en período 4 ($D_4 = 180$):**
- $k=1$: $C(1) = 120$.
- $k=2$ (sem. 4–5, $D_5 = 150$): $C(2) = (120 + 1 \cdot 0{,}9 \cdot 150)/2 = 127{,}5 > 120$ → **PARAR**.

**Lote en sem. 4:** cubre solo semana 4. $Q_4 = \mathbf{180}$.

**Lote 3 — arranca en período 5 ($D_5 = 150$):**
- Único período restante con demanda. **Lote en sem. 5:** $Q_5 = \mathbf{150}$.

**Política resultante:**

| Período | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Demanda** | 0 | 30 | 120 | 180 | 150 | 0 | 0 | 0 |
| **Lote $Q$** | 0 | **150** | 0 | **180** | **150** | 0 | 0 | 0 |
| **Inventario** | 0 | 120 | 0 | 0 | 0 | 0 | 0 | 0 |

**Costos totales:**
- Setups: $3 \times \$120 = \$360$.
- Almacenamiento: 120 unidades almacenadas 1 semana en semana 3 → $120 \times 1 \times 0{,}9 = \$108$.

$$\boxed{\text{Costo Total Silver-Meal} = 360 + 108 = \$468}$$

---

## Problema 3: PERT y Crashing

### Enunciado

| Etapa | Predecesor | $a$ (optim.) | $m$ (probable) | $b$ (pesim.) |
|:---:|:---:|:---:|:---:|:---:|
| A | — | 2 | 3 | 4 |
| B | A | 2 | 4 | 6 |
| C | A | 5 | 6 | 13 |
| D | B, C | 3 | 6 | 9 |
| E | B | 2 | 5 | 8 |
| F | D, E | 2 | 4 | 6 |

**Datos de crashing** (costo acelerado = asumir antes de comenzar, varianza inalterada):

| Actividad | Reducción máx. (sem.) | Costo Normal (\$) | Costo Acelerado (\$) | Δ Costo |
|:---:|:---:|:---:|:---:|:---:|
| A | 1 | 10 000 | 13 000 | 3 000 |
| B | 1 | 6 000 | 9 000 | 3 000 |
| C | 2 | 4 000 | 7 000 | 3 000 |
| D | 2 | 13 000 | 18 000 | 5 000 |
| E | 2 | 9 000 | 13 000 | 4 000 |
| F | 1 | 7 000 | 8 000 | 1 000 |

**Se pide:**
- (a) Tiempos esperados y varianzas.
- (b) Diagrama PERT.
- (c) ES, EF, LS, LF, holgura, ruta crítica y duración mínima.
- (d) Probabilidad de terminar en < 22 semanas. IC 95%.
- (e) Si el cliente ofrece bono de $\$8\,000$ al terminar en < 18 semanas, ¿qué actividades acortaría?

### Solución Oficial

#### (a) Tiempos Esperados y Varianzas

$$t_e = \frac{a + 4m + b}{6}, \qquad \sigma^2 = \left(\frac{b-a}{6}\right)^2$$

| Actividad | $t_e$ (sem.) | $\sigma^2$ |
|:---:|:---:|:---:|
| A | 3 | 0,111 (≈ 1/9) |
| B | 4 | 0,444 (≈ 4/9) |
| C | 7 | 1,778 (≈ 16/9) |
| D | 6 | 1,000 |
| E | 5 | 1,000 |
| F | 4 | 0,444 (≈ 4/9) |

> Verificación C: $t_e = (5 + 4 \times 6 + 13)/6 = 42/6 = 7$. $\sigma^2 = ((13-5)/6)^2 = (8/6)^2 = 64/36 = 1{,}78$.

---

#### (b) Diagrama PERT

```
         B(4)           E(5)
    2 ────────── 3 ────────── 5
   /                           \
1 ─── A(3)                       ─── F(4) ─── 6
   \                           /
    ─────────── 4 ────────── 5
         C(7)           D(6)
```

Nodos: 1 (inicio) → [A] → 2 → [B] → 3 → [E] → 5 → [F] → 6  
                      1 → [A] → 2 → [C] → 4 → [D] → 5 → [F] → 6

---

#### (c) Tiempos de Calendario y Ruta Crítica

**Pasada forward:**

| Actividad | $t_e$ | ES | EF |
|:---:|:---:|:---:|:---:|
| A | 3 | 0 | 3 |
| B | 4 | 3 | 7 |
| C | 7 | 3 | 10 |
| D | 6 | max(7, 10) = **10** | 16 |
| E | 5 | 7 | 12 |
| F | 4 | max(16, 12) = **16** | **20** |

**Duración del proyecto: T = 20 semanas.**

**Pasada backward** ($LF_F = 20$):

| Actividad | $t_e$ | LF | LS | **Holgura** |
|:---:|:---:|:---:|:---:|:---:|
| F | 4 | 20 | 16 | **0** |
| E | 5 | 16 | 11 | **4** |
| D | 6 | 16 | 10 | **0** |
| C | 7 | 10 | 3 | **0** |
| B | 4 | min(10, 11) = 10 | 6 | **3** |
| A | 3 | min(6, 3) = 3 | 0 | **0** |

**Ruta crítica: A → C → D → F.** Holgura = 0 en todas.

---

#### (d) Probabilidades e Intervalo de Confianza

$$\sigma_p = \sqrt{\sigma_A^2 + \sigma_C^2 + \sigma_D^2 + \sigma_F^2} = \sqrt{0{,}111 + 1{,}778 + 1{,}000 + 0{,}444} = \sqrt{3{,}333} \approx 1{,}82 \text{ sem.}$$

**Probabilidad de terminar en < 22 semanas:**
$$Z = \frac{22 - 20}{1{,}82} \approx 1{,}10 \implies \Phi(1{,}10) = 0{,}864 \implies \mathbf{86{,}4\%}$$

**Intervalo de confianza al 95% (bilateral, $Z = 1{,}96$):**
$$IC_{95\%} = 20 \pm 1{,}96 \times 1{,}82 = 20 \pm 3{,}57 \implies [16{,}43;\; 23{,}57] \text{ semanas}$$

---

#### (e) Crashing para Bono de $\$8\,000$ (< 18 semanas)

Necesitamos reducir **2 semanas** en la ruta crítica A–C–D–F. Se evalúa el **valor esperado neto** para cada escenario.

**Escenario 0: Sin aceleración (duración = 20 sem.)**
$$Z = \frac{18 - 20}{1{,}82} = -1{,}10 \implies P(T < 18) = 13{,}6\%$$
$$VE_{\text{neto}} = 0{,}136 \times 8\,000 - 0 = \$1\,086$$

**Escenario 1: Acortar 1 semana — opciones en ruta crítica:**

| Actividad | Reducción | Costo |
|:---:|:---:|:---:|
| A | 1 sem. | $\$3\,000$ |
| F | 1 sem. | $\$1\,000$ |

Óptimo: acelerar **F** ($\$1\,000$). Nueva duración = 19 sem.
$$Z = \frac{18 - 19}{1{,}82} = -0{,}55 \implies P(T < 18) = 29{,}1\%$$
$$VE_{\text{neto}} = 0{,}291 \times 8\,000 - 1\,000 = 2\,328 - 1\,000 = \$1\,330$$

**Escenario 2: Acortar 2 semanas — opciones en ruta crítica:**

| Combinación | Costo total |
|:---|:---:|
| A (1 sem.) + F (1 sem.) | $\$4\,000$ |
| **C (2 sem.)** | **$\$3\,000$** |
| D (2 sem.) | $\$5\,000$ |

Óptimo: acelerar **C** en 2 semanas ($\$3\,000$). Nueva duración = 18 sem.
$$Z = \frac{18 - 18}{1{,}82} = 0 \implies P(T < 18) = 50\%$$
$$VE_{\text{neto}} = 0{,}50 \times 8\,000 - 3\,000 = 4\,000 - 3\,000 = \$1\,000$$

**Resumen comparativo:**

| Escenario | Costo aceleración | $P(T < 18)$ | VE bruto | **VE neto** |
|:---|:---:|:---:|:---:|:---:|
| Sin aceleración | $\$0$ | 13,6% | $\$1\,086$ | $\$1\,086$ |
| Acelerar F 1 sem. | $\$1\,000$ | 29,1% | $\$2\,328$ | **$\$1\,330$** ← máximo |
| Acelerar C 2 sem. | $\$3\,000$ | 50,0% | $\$4\,000$ | $\$1\,000$ |

$$\boxed{\text{Decisión: Acelerar F 1 semana (costo } \$1\,000\text{). VE neto máximo = } \$1\,330}$$

> **Verificación: ¿se vuelve crítica alguna ruta no crítica tras el crashing?**
> Las rutas alternativas y sus duraciones originales son:
> - A–B–D–F: $3+4+6+4 = 17$ sem.
> - A–B–E–F: $3+4+5+4 = 16$ sem.
>
> Tras acelerar F en 1 semana, la nueva duración de F = 3 sem. Las rutas alternativas pasan a:
> - A–B–D–F: $3+4+6+3 = 16$ sem. $< 19$ ✓
> - A–B–E–F: $3+4+5+3 = 15$ sem. $< 19$ ✓
>
> Ninguna supera la nueva RC (19 sem.), por lo que el análisis es válido y no se generan rutas críticas adicionales.

---

## Problema 4: Variabilidad — Optimización de Capacidad

### Enunciado

Empresa de imprenta: clientes llegan a tasa $\lambda$ [clientes/hr], capacidad de atención $\mu$ [clientes/hr], distribuciones generales con tiempo efectivo $t_e$, coeficientes de variación $c_a$ (llegadas) y $c_e$ (servicio).

La empresa evalúa ofrecer descuentos $\Delta$ para modular la demanda:
$$\lambda(\Delta) = \lambda_0 e^{-\Delta}$$
El costo de espera del cliente es $CE(W) = 100 + W$, donde $W$ es el tiempo total en el sistema.

**a)** Plantear el modelo de programación matemática y las condiciones de primer orden.

**b)** Si se puede adquirir capacidad adicional $IC$ [clientes/hr] a un costo $\$K$ por unidad, ¿cómo cambia el modelo?

### Solución Oficial

#### a) Modelo de Optimización (variable de decisión: $\Delta$)

$$\min_{\Delta \ge 0} \quad F = 100 + W + \Delta$$

Sujeto a:
$$W = \left(\frac{c_a^2 + c_e^2}{2}\right) \cdot \frac{\rho}{1 - \rho} \cdot t_e, \qquad \rho = \frac{\lambda}{\mu} = \frac{\lambda_0 e^{-\Delta}}{\mu}, \qquad \Delta \ge 0$$

**Forma compacta** (sustituyendo $\lambda = \lambda_0 e^{-\Delta}$ directamente):

$$\min_{\Delta \ge 0} \quad F = 100 + \left(\frac{c_a^2 + c_e^2}{2}\right) \cdot \frac{\dfrac{\lambda_0 e^{-\Delta}}{\mu}}{1 - \dfrac{\lambda_0 e^{-\Delta}}{\mu}} \cdot t_e \;+\; \Delta$$

**Condición de primer orden** ($\partial F / \partial \Delta = 0$, no resolver):
$$\frac{\partial F}{\partial \Delta} = \frac{\partial W}{\partial \Delta} + 1 = 0$$

donde $\partial W / \partial \Delta$ involucra la derivada de $\rho/(1-\rho)$ respecto a $\Delta$, que resulta negativa (al aumentar $\Delta$, baja $\lambda$ y baja la espera). La CPO iguala la ganancia marginal en espera con el costo marginal del descuento.

---

#### b) Modelo con Capacidad Adicional (variables de decisión: $\Delta$ y $IC$)

Se suma $IC$ a la capacidad base, por lo que $\rho = \lambda / (\mu + IC)$:

$$\min_{\Delta \ge 0,\; IC \ge 0} \quad F = 100 + W(\Delta, IC) + \Delta + K \cdot IC$$

Sujeto a:
$$W = \left(\frac{c_a^2 + c_e^2}{2}\right) \cdot \frac{\rho}{1 - \rho} \cdot t_e, \qquad \rho = \frac{\lambda_0 e^{-\Delta}}{\mu + IC}$$
$$\lambda_0 e^{-\Delta} < \mu + IC \quad (\text{condición de estabilidad})$$
$$\Delta \ge 0, \quad IC \ge 0$$

> **Interpretación:** Ahora hay dos palancas para reducir la espera: bajar la demanda vía descuento ($\Delta$) o aumentar la capacidad ($IC$). La CPO para $IC$ iguala el costo marginal $K$ con la reducción marginal en $W$.
