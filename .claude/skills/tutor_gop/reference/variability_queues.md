# Variabilidad en Operaciones y Teoría de Colas

La variabilidad en los procesos de fabricación y servicios deteriora severamente el rendimiento del sistema, provocando esperas y acumulaciones de inventario en cola incluso cuando la tasa de llegada es inferior a la capacidad nominal.

## 1. Coeficiente de Variación ($C_x$)
Mide la variabilidad relativa de una variable aleatoria (como los intervalos entre llegadas o los tiempos de servicio):
$$C_x = \frac{\sigma_x}{\mu_x}$$
* Si $C_x = 1$, la distribución es de tipo exponencial (sin memoria, asociada a procesos de Poisson o colas M/M/1).
* Si $C_x < 1$, el proceso es más regular que el exponencial.
* Si $C_x > 1$, el proceso es altamente variable.

## 2. Ecuación de Kingman (Cola G/G/1)
Aproxima el tiempo de espera promedio en la cola ($W_q$) para una cola con un único servidor y distribuciones generales de llegada y servicio:
$$W_q \approx \left( \frac{C_a^2 + C_s^2}{2} \right) \left( \frac{\rho}{1 - \rho} \right) \left( \frac{1}{\mu} \right)$$
Donde:
* $C_a$: Coeficiente de variación de los tiempos entre arribos (llegadas).
* $C_s$: Coeficiente de variación de los tiempos de servicio.
* $\mu$: Tasa de servicio del servidor [clientes/hora].
* $\lambda$: Tasa de llegada de clientes [clientes/hora].
* $\rho = \frac{\lambda}{\mu}$: Utilización del servidor. Debe cumplirse $\rho < 1$ para la estabilidad del sistema.

### Componentes de la Fórmula VUT:
* **V (Variabilidad):** $\left( \frac{C_a^2 + C_s^2}{2} \right)$. Si no hay variabilidad ($C_a = C_s = 0$), el tiempo de espera en cola es cero.
* **U (Utilización):** $\left( \frac{\rho}{1 - \rho} \right)$. A medida que la utilización se acerca al 100%, el tiempo de espera tiende al infinito debido al denominador.
* **T (Tiempo de Servicio):** $\left( \frac{1}{\mu} \right)$. El tiempo físico de atención.

## 3. Propagación de Variabilidad en Sistemas en Tándem
En una red de colas en serie, la salida de una estación $i$ alimenta las llegadas de la estación $i+1$. El coeficiente de variación de las salidas ($C_d^2$) se aproxima por:
$$C_{d,i}^2 \approx \rho_i^2 \cdot C_{s,i}^2 + (1 - \rho_i)^2 \cdot C_{a,i}^2$$
El coeficiente de variación de llegadas de la siguiente estación es:
$$C_{a,i+1}^2 = C_{d,i}^2$$
Esta relación demuestra que un servidor altamente inestable aguas arriba (alto $C_s$) perjudica de forma directa el tiempo de espera de las estaciones aguas abajo al inyectar variabilidad en el flujo de llegadas.

## 4. Ley de Little
Relaciona de forma general el inventario o número de clientes en el sistema ($L$) con el tiempo de permanencia ($W$):
* **Para el sistema completo:**
  $$L = \lambda \cdot W$$
  *Donde $W = W_q + \frac{1}{\mu}$ es el tiempo total en el sistema.*
* **Para la cola:**
  $$L_q = \lambda \cdot W_q$$
