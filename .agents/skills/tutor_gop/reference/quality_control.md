# Control de Calidad y Cartas de Control

El control de calidad es esencial para mantener los procesos productivos estables y reducir el desperdicio. Se divide principalmente en dos análisis estadísticos:

## 1. Gráficos de Control de Variables ($\bar{X}$ y R)

Utilizados para monitorear si un proceso es estable en el tiempo. Se toman muestras sucesivas ($m$ muestras de tamaño $n$).

**Fórmulas Clave:**
*   Promedio global: $\bar{\bar{X}} = \frac{\sum \bar{X}_i}{m}$
*   Rango/Recorrido global: $\bar{R} = \frac{\sum R_i}{m}$
*   Límites Carta de Promedios: $LCS_{\bar{X}} = \bar{\bar{X}} + A_2\bar{R}$ ; $LCI_{\bar{X}} = \bar{\bar{X}} - A_2\bar{R}$
*   Límites Carta de Recorridos: $LCS_R = D_4\bar{R}$ ; $LCI_R = D_3\bar{R}$

**Protocolo de Examen:**
1.  Calcula primero los límites iniciales con todas las muestras.
2.  Revisa si alguna muestra (tanto en su $\bar{X}$ como en su $R$) cae fuera de los límites respectivos.
3.  **Si hay muestras fuera de control:** Elimínalas.
4.  **Recalcula:** Obtén un nuevo $\bar{\bar{X}}'$ y $\bar{R}'$ promediando solo las muestras restantes.
5.  Calcula los **nuevos límites de control** y verifica que ahora sí todas las muestras restantes estén dentro. Si es así, el proceso ya está bajo control.

## 2. Capacidad del Proceso ($C_p$ y $C_{pk}$)

Una vez que el proceso está bajo control, necesitamos saber si es "capaz" de cumplir las exigencias del cliente. 
El cliente impone los Límites de Especificación ($USL$ y $LSL$).

*   Estimación de desviación estándar: $\hat{\sigma} = \frac{\bar{R}}{d_2}$
*   **$C_p$ (Capacidad Potencial):** Asume que el proceso está perfectamente centrado.
    $C_p = \frac{USL - LSL}{6\hat{\sigma}}$
*   **$C_{pk}$ (Capacidad Real):** Penaliza si el proceso está descentrado (su media $\bar{\bar{X}}$ está más cerca de un límite que del otro).
    $C_{pk} = \min \left( \frac{USL - \bar{\bar{X}}}{3\hat{\sigma}}, \frac{\bar{\bar{X}} - LSL}{3\hat{\sigma}} \right)$

Si $C_{pk} < 1$, el proceso producirá demasiados defectos (fuera de especificación). Un valor aceptable estándar es $> 1.33$.

## 3. Error Tipo I y Tipo II
*   **Error Tipo I (Riesgo del productor, $\alpha$):** Probabilidad de que un punto caiga fuera de los límites de control aún cuando el proceso está operando correctamente. Depende del ancho de los límites (usualmente $3\sigma$). Si la prueba indica usar $Z$ en lugar de $A_2$, $LCS = \bar{\bar{X}} + Z \frac{\sigma}{\sqrt{n}}$.
*   **Error Tipo II (Riesgo del consumidor, $\beta$):** Probabilidad de que el proceso se descontrole (la media cambie a $\mu'$) pero los puntos sigan cayendo dentro de los límites de control antiguos.
