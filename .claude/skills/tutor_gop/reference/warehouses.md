# Localización y Decisiones de Bodegas

El modelado de la ubicación óptima de una bodega o centro de distribución (CD) permite reducir los costos de transporte de la cadena de suministro al minimizar las distancias ponderadas por el volumen de carga.

## 1. Método del Centro de Gravedad (CG)
El Centro de Gravedad es una aproximación continua para la ubicación de una sola instalación que interactúa con múltiples proveedores y clientes.
* **Coordenadas Óptimas ($C_x, C_y$):**
  $$C_x = \frac{\sum_{i} V_i \cdot x_i}{\sum_{i} V_i}, \quad C_y = \frac{\sum_{i} V_i \cdot y_i}{\sum_{i} V_i}$$
  Donde:
  * $(x_i, y_i)$: Coordenadas de la instalación $i$ (fábrica, mercado o proveedor).
  * $V_i$: Volumen anual o diario transportado hacia o desde la instalación $i$ [toneladas, viajes, unidades].

## 2. Distancia Rectangular (Manhattan)
En tramas urbanas o pasillos de bodegas, la distancia euclidiana no es realista. Se utiliza la distancia Manhattan (métrica $L_1$):
$$d(x_1, y_1; x_2, y_2) = |x_1 - x_2| + |y_1 - y_2|$$

### Linealización de Valores Absolutos en MILP
Para modelar distancias en programación lineal, el término $|x_i - CX_b|$ se linealiza introduciendo variables auxiliares de desviación $DX_{i,b} \ge 0$ y restricciones lineales:
$$DX_{i,b} \ge x_i - CX_b - M \cdot (1 - B_{i,b})$$
$$DX_{i,b} \ge CX_b - x_i - M \cdot (1 - B_{i,b})$$
*Donde $B_{i,b}$ es una binaria de asignación de la instalación $i$ a la bodega $b$, y $M$ es un número grande.*

## 3. Análisis de Punto de Equilibrio Lineal y Dinámico (Break-even)
Cuando se comparan opciones de localización discretas con diferentes costos fijos y variables de transporte, la función de costo es:
$$CT(V) = CF + CV \cdot V$$
El punto de equilibrio entre dos bodegas es el volumen $V^*$ donde sus costos se igualan:
$$V^* = \frac{CF_2 - CF_1}{CV_1 - CV_2}$$

### Decisiones a Largo Plazo con Demanda Creciente
Si la demanda o volumen $V(t)$ cambia a lo largo de un horizonte $[T_0, T_f]$:
* No basta con evaluar el costo hoy y el costo final.
* Se debe integrar el costo a lo largo de todo el horizonte temporal:
  $$\text{Costo Acumulado} = \sum_{t=T_0}^{T_f} CT\big(V(t)\big) = \sum_{t=T_0}^{T_f} \left( CF + CV \cdot V(t) \right)$$
* Geométricamente, si el crecimiento es lineal, la diferencia de costo acumulado entre dos opciones se calcula como las áreas de los trapecios o triángulos delimitados por el punto de equilibrio en el gráfico de costo versus volumen.
* Se selecciona la bodega que minimiza el costo total acumulado (o maximiza el beneficio neto acumulado).
