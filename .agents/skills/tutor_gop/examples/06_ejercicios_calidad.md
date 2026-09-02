# Ejercicios Tipo Examen: Calidad, Localización y Colas (2024-2025)

## 1. Ejercicio de Control de Calidad y Recálculo (Examen 2024)

**Problema:** Se toman 25 muestras de 20 botellas cada una (n=20) midiendo grosor.
Datos dados: $\sum \text{Promedio} = 637.1$, $\sum \text{Mínimo} = 607.6$, $\sum \text{Máximo} = 666.6$.

**Solución Paso a Paso:**
1.  **Cálculos Iniciales:** 
    $\bar{\bar{X}} = 637.1 / 25 = 25.484$
    El Recorrido Medio $\bar{R}$ se saca usando los máximos y mínimos: 
    $\sum \bar{R} = (666.6 - 607.6)/25 = 59.0 / 25 = 2.36$.
2.  **Límites Iniciales (n=20, A2=0.18):**
    $LCS = 25.484 + 0.18 \times 2.36 = 25.9$
    $LCI = 25.484 - 0.18 \times 2.36 = 25.06$
3.  **Fuera de control:** Si el problema te da una lista de muestras individuales y alguna (ej. muestra con media 27.5 y 27.6) se pasa de 25.9, el proceso está fuera de control. Se deben borrar esas muestras.
4.  **Recálculo:** Borrar las muestras atípicas (por ej. la 16 y 22), restar sus promedios de la suma original (637.1 - 27.5 - 27.6 = 582.0) y dividir por las nuevas muestras (23 en vez de 25).
    $\bar{\bar{X}}_{nuevo} = 582.0 / 23 = 25.304$.
    Se recalcula la desviación y los nuevos límites. Si todo entra ahora, el proceso final está bajo control.

## 2. Ejercicio de Break-Even Lineal Dinámico (Examen 2024)

**Problema:** Elegir entre Planta L1 (Compra 10.000, costo op 25) y L2 (Compra 40.000, costo op 10).
Demanda crece lineal: $Q(t) = 1000 + 250t$. Proyecto a 10 años.

**Solución Paso a Paso:**
1.  **Costo Total como Función del Tiempo:**
    $CT_{L1}(t) = 10.000 + 25(1000 + 250t) = 35.000 + 6250t$
    $CT_{L2}(t) = 40.000 + 10(1000 + 250t) = 50.000 + 2500t$
2.  **Integrar en el horizonte [0, 10]:**
    Costo Acumulado L1 = $\int_{0}^{10} (35.000 + 6250t) dt = [35.000t + 3125t^2]_0^{10} = 350.000 + 312.500 = 662.500$
    Costo Acumulado L2 = $\int_{0}^{10} (50.000 + 2500t) dt = [50.000t + 1250t^2]_0^{10} = 500.000 + 125.000 = 625.000$
3.  **Decisión:** L2 tiene menor costo acumulado (625.000 vs 662.500), por ende conviene más colocar la planta en L2 a largo plazo gracias al menor costo variable, aunque cueste más caro al inicio.

## 3. Ejercicio de Colas Comparativo (Kingman)

**Problema:** Máquina antigua procesa en promedio 12 min (stdev 2 min). MTTF=57h, MTTR=19h (stdev MTTR = 1).
Máquina nueva procesa en 10 min (stdev 100s = 1.67 min). MTTF=372h, MTTR=124h (stdev MTTR = 1). ¿Cuál es mejor bajo métricas de variabilidad?

**Solución Paso a Paso:**
1.  **Disponibilidad (A):**
    Antigua: $A = 57 / (57 + 19) = 0.75$
    Nueva: $A = 372 / (372 + 124) = 0.75$
    (Tienen la misma disponibilidad).
2.  **Coeficiente de Variabilidad Operativo ($C_0^2$):**
    Antigua: $(2 / 12)^2 = 0.1667^2 = 0.027$
    Nueva: $(1.67 / 10)^2 = 0.167^2 = 0.027$
3.  **Variabilidad Efectiva por Fallas ($C_e^2 = C_0^2 + (1+C_r^2)A(1-A)MTTR/t_0$):**
    Antigua: $0.027 + (1+1^2) \times 0.75 \times 0.25 \times (19 \times 60 \text{ min} / 12 \text{ min}) \rightarrow$ (Cálculo depende si MTTR se deja en horas o minutos, pero al dejar la razón $\frac{MTTR}{t_0}$ deben estar en la misma unidad).
    $19 \text{ horas} = 1140 \text{ min}$. Razón = $1140 / 12 = 95$.
    $C_e^2 (\text{Antigua}) = 0.027 + 2 \times 0.1875 \times 95 = 0.027 + 35.625 = 35.65$
    Nueva: $124 \text{ horas} = 7440 \text{ min}$. Razón = $7440 / 10 = 744$.
    $C_e^2 (\text{Nueva}) = 0.027 + 2 \times 0.1875 \times 744 = 0.027 + 279 = 279.02$
4.  **Conclusión:** Aunque la máquina 2 es ligeramente más rápida en procesamiento, sus fallas son tan catastróficas (larguísimo MTTR aunque infrecuente) que destruye el flujo. La máquina antigua es mucho mejor (menos variabilidad efectiva).
