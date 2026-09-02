# Administración de Proyectos (PERT/CPM)

La administración de proyectos mediante técnicas de camino crítico (CPM) y evaluación probabilística (PERT) permite planificar la duración de un proyecto y evaluar los riesgos asociados a la variabilidad de sus actividades.

## 1. Algoritmo del Camino Crítico (CPM)
Para cada actividad se calculan cuatro tiempos clave y la holgura:
* **Early Start ($ES$):** El tiempo más temprano en que la actividad puede iniciar.
  $$ES_j = \max_{i \in \text{Predecesores}} \left( EF_i \right)$$
* **Early Finish ($EF$):** El tiempo más temprano en que la actividad puede terminar.
  $$EF_j = ES_j + TE_j$$
* **Late Finish ($LF$):** El tiempo más tardío en que la actividad puede finalizar sin retrasar el proyecto.
  $$LF_i = \min_{j \in \text{Sucesores}} \left( LS_j \right)$$
* **Late Start ($LS$):** El tiempo más tardío en que la actividad puede iniciar sin retrasar el proyecto.
  $$LS_i = LF_i - TE_i$$
* **Holgura ($H$):** Margen de tiempo disponible para retrasar una actividad.
  $$H_i = LS_i - ES_i = LF_i - EF_i$$

Las actividades con **holgura cero** conforman la **Ruta Crítica**. Cualquier retraso en ellas posterga la fecha de término del proyecto completo.

## 2. Análisis Probabilístico (PERT)
PERT asume que la duración de cada actividad es una variable aleatoria que sigue una distribución Beta, aproximada por sus tres estimaciones de tiempo: optimista ($a$), más probable ($m$), y pesimista ($b$).

* **Tiempo Esperado ($TE$):**
  $$TE = \frac{a + 4m + b}{6}$$
* **Desviación Estándar ($\sigma$):**
  $$\sigma = \frac{b - a}{6} \implies Var = \sigma^2 = \left( \frac{b - a}{6} \right)^2$$

### Duración del Proyecto
Por el Teorema del Límite Central (TLC), la duración total del proyecto ($T$) se aproxima mediante una distribución normal:
$$T \sim N\left(\mu_p, \sigma_p^2\right)$$
* **Media del Proyecto ($\mu_p$):** La suma de los tiempos esperados de las actividades de la ruta crítica.
  $$\mu_p = \sum_{i \in \text{Ruta Crítica}} TE_i$$
* **Varianza del Proyecto ($\sigma_p^2$):** La suma de las varianzas de las actividades de la ruta crítica (asumiendo independencia).
  $$\sigma_p^2 = \sum_{i \in \text{Ruta Crítica}} \sigma_i^2 \implies \sigma_p = \sqrt{\sigma_p^2}$$

### Cálculo de Probabilidades
Para hallar la probabilidad de terminar antes de un plazo $X$:
$$P(T \le X) = \Phi\left( Z \right) \quad \text{donde } Z = \frac{X - \mu_p}{\sigma_p}$$
Para plazos inferiores a la media ($X < \mu_p$), $Z$ es negativo, por simetría:
$$P(T \le X) = 1 - \Phi\left( |Z| \right)$$

## 3. Negociación de Contratos e Indiferencia
En contratos con bonos por finalización temprana y multas por retrasos, el valor esperado ($VE$) del contrato es:
$$VE = \text{Bono} \cdot P(T \le X_{\text{bono}}) - \text{Penalidad} \cdot P(T > X_{\text{pen}})$$

El punto de indiferencia se logra cuando $VE = 0$. Se busca el valor crítico de probabilidad $p$ y se despeja el plazo $X$ o los montos usando la tabla normal estándar.

## 4. Crashing (Compresión de Tiempos)
El crashing consiste en reducir la duración esperada de las actividades críticas al menor costo posible.
* **Costo Marginal de Crashing ($CC_i$):**
  $$CC_i = \frac{\text{Costo Crashing} - \text{Costo Normal}}{TE_{\text{normal}} - TE_{\text{crashing}}}$$
* **Procedimiento:**
  1. Identifica las actividades de la ruta crítica actual.
  2. Selecciona la actividad crítica con el menor costo marginal de crashing ($CC_i$).
  3. Comprime esa actividad en 1 período o hasta que se alcance su límite técnico, o hasta que surja una nueva ruta crítica paralela.
  4. Si surgen rutas críticas paralelas, se deben comprimir simultáneamente actividades en ambos caminos para lograr un beneficio de tiempo neto.
