# Interrogación 2 --- Gestión de Operaciones (ICS 3213)
## Semestre: 1er Semestre 2023
**Profesores:** Martin Garcia, Alejandro Mac Cawley
**Autores de Referencia:** César Meneses, Fabián Ortega

---

## PARTE DESARROLLO

### Pregunta A: Gestión de Inventarios y Distribución de Demanda (20 Puntos)

#### Enunciado
La nueva tienda de zapatos cerca del campus debe determinar la cantidad de zapatillas que desea comprar para la temporada navideña. Los zapatos tienen un precio alto y se importan de EE.UU. El costo unitario de cada par de zapatillas es de $U\$60$ y los venderán a $U\$300$. Cualquier par que no venda al final de la temporada lo compra un outlet por $U\$47$ el par.

* **i.** (8 puntos) Si la venta sigue una distribución normal con media 300 y desviación estándar de 40 pares. ¿Cuál sería la cantidad óptima de pares de zapatillas que debe comprar la tienda para la temporada?
* **ii.** (8 puntos) Un análisis detallado de los datos históricos de ventas muestra que la cantidad de zapatillas es igualmente probable para todos los valores entre 100 y 500 pares (inclusive) durante la estación. Con esa información, ¿cuántos pares de zapatillas debe comprar la tienda? (*HINT: La distribución de la demanda es uniforme discreta*).
* **iii.** (4 puntos) Si bien la demanda esperada en las preguntas (i) y (ii) es la misma ($300$ pares), las cantidades óptimas son distintas. ¿A qué se debe esta diferencia conceptualmente?

#### Solución

##### i. Cantidad Óptima con Demanda Normal
Utilizamos el modelo del vendedor de periódicos (*Newsvendor Problem*).
* Costo de subestimar la demanda (*Understock* --- $C_u$):
  $$C_u = \text{Precio} - \text{Costo} = 300 - 60 = U\$240$$
* Costo de sobreestimar la demanda (*Overstock* --- $C_o$):
  $$C_o = \text{Costo} - \text{Valor de Recuperación} = 60 - 47 = U\$13$$
* Razón Crítica ($CR$):
  $$CR = \frac{C_u}{C_u + C_o} = \frac{240}{240 + 13} = \frac{240}{253} \approx 0.9486 \quad (94.86\%)$$

Buscamos en la tabla de distribución normal estándar el valor $Z$ tal que $\Phi(Z) = 0.9486$.
* El valor más cercano en la tabla es $\Phi(1.64) = 0.9495$ y $\Phi(1.65) = 0.9505$. Usamos $Z \approx 1.645$.
* Calculamos la cantidad óptima $Q^*$:
  $$Q^* = \mu + Z \cdot \sigma = 300 + 1.645 \cdot 40 = 365.8 \text{ pares}$$
  La tienda debe adquirir **366 pares** de zapatillas.

##### ii. Cantidad Óptima con Demanda Uniforme Discreta
La demanda es igualmente probable en el rango discreto $[100, 500]$. El número total de posibles valores es:
$$N = 500 - 100 + 1 = 401 \text{ valores}$$
Cada valor posee una probabilidad de $P(X = x) = \frac{1}{401} \approx 0.002494$ ($0.2494\%$).

Buscamos la cantidad discreta $Q^*$ que satisfaga la condición acumulada:
$$F(Q^*) \ge 0.9486$$
En una distribución uniforme continua sobre $[100, 500]$, la función de distribución acumulada es:
$$F(Q) = \frac{Q - 100}{500 - 100} = \frac{Q - 100}{400}$$
Igualamos a la razón crítica:
$$\frac{Q^* - 100}{400} = 0.9486 \implies Q^* = 100 + 0.9486 \cdot 400 = 100 + 379.44 = 479.44 \text{ pares}$$

*Nota de la Pauta:* La pauta realiza una búsqueda discreta del extremo superior:
$$P(X > Q^*) < 1 - 0.9486 = 0.0514$$
$$\text{Cantidad de valores sobre } Q^*: \quad \text{valores} \cdot \frac{1}{401} < 0.0514 \implies \text{valores} < 20.6$$
Tomando $20$ valores, la cantidad óptima es $500 - 20 = 480$.
Se aceptan tanto **479** como **480 pares** de zapatillas.

##### iii. Explicación Conceptual de la Diferencia
Aunque el valor esperado (promedio) de la demanda es idéntico en ambos casos ($300$ unidades), la **variabilidad** es marcadamente diferente:
* La distribución normal concentra la probabilidad alrededor de la media (desviación de 40).
* La distribución uniforme reparte la probabilidad equitativamente en todo el rango $[100, 500]$, lo que representa una desviación estándar teórica mucho mayor ($\sigma = \frac{500 - 100}{\sqrt{12}} \approx 115.47$).
* Dado que el costo de quedarse corto ($C_u = \$240$) es muchísimo mayor que el costo de inventario sobrante ($C_o = \$13$), el modelo incentiva a cubrirse frente a demandas altas. Bajo mayor variabilidad (Uniforme), el riesgo de perder ventas lucrativas es mayor en los extremos altos, obligando a comprar más stock ($480$ frente a $366$).

---

### Pregunta B: Planificación de Proyectos y Crashing (20 Puntos)

#### Enunciado
Usted se encuentra a cargo de un proyecto de infraestructura y ha determinado que la fecha esperada de la ruta crítica es de 180 días con una desviación estándar de 12 días. Su mandante le ofrece un bono de $U\$2$ millones si termina en o antes de 165 días y una penalización de $U\$1$ millón si termina después de los 165 días.
* **i.** (3 ptos) ¿Aceptaría usted el contrato? Si la penalización no es transable, ¿qué monto de bono lo deja indiferente?
* **ii.** (4 ptos) Si se mantienen los montos de bono y penalización originales, ¿qué fecha lo deja indiferente?
* **iii.** (6 ptos) Usted tiene la posibilidad de implementar tecnología en una de las actividades de la ruta crítica. La actividad en cuestión tiene un tiempo esperado de 20 días, con desviación estándar de 3. La tecnología disminuye el tiempo esperado de finalización en 10 días, sin cambiar la ruta crítica, y reduce la desviación estándar de la actividad en 1.5 días. Si la tecnología cuesta $U\$10,000$, ¿la contrataría?
* **iv.** (7 ptos) Si ahora usted puede implementar otra tecnología que le permite reducir el tiempo esperado de cada actividad $(i,j)$ del proyecto en un máximo de $M_{ij}$ días con un costo lineal $C_{ij}$ por día. Para la situación inicial presente el modelo de optimización matemática que minimice el costo de reducción y maximice el valor esperado del contrato.

#### Solución

##### i. Evaluación de Aceptación del Contrato
* $\mu = 180$ días, $\sigma = 12$ días.
* Umbral de tiempo $T = 165$.
* Calculamos el valor $Z$:
  $$Z = \frac{165 - 180}{12} = -1.25$$
* La probabilidad de terminar antes es:
  $$P(T \le 165) = 1 - \Phi(1.25) = 1 - 0.8944 = 0.1056 \quad (10.56\%)$$
  $$P(T > 165) = 0.8944 \quad (89.44\%)$$
* Calculamos el valor esperado del contrato ($VE$):
  $$VE = 2 \cdot P(T \le 165) - 1 \cdot P(T > 165) = 2 \cdot 0.1056 - 1 \cdot 0.8944 = 0.2112 - 0.8944 = -U\$0.6832 \text{ millones}$$
  Dado que el valor esperado es negativo ($-\$683,200$), **no se acepta** el contrato.

* Para ser indiferente ($VE = 0$), con una penalidad de $1$ millón, calculamos el bono $B$:
  $$B \cdot (0.1056) - 1 \cdot (0.8944) = 0 \implies B = \frac{0.8944}{0.1056} \approx 8.47 \text{ millones}$$
  Se requeriría un bono de **U\$8.47 millones** para estar indiferente.

##### ii. Fecha de Indiferencia (Bono y Penalización Originales)
Buscamos la probabilidad $p = P(T \le X)$ que haga $VE = 0$:
$$2 p - 1(1 - p) = 0 \implies 3 p = 1 \implies p = 0.3333$$
El valor $Z$ asociado a una probabilidad acumulada de $0.3333$ es:
$$Z \approx -0.43$$
Despejamos el umbral de fecha $X$:
$$X = \mu + Z \cdot \sigma = 180 - 0.43 \cdot 12 = 174.84 \text{ días}$$
La fecha que deja indiferente al contratista es de **174.84 días**.

##### iii. Evaluación de la Incorporación de Tecnología
La actividad de la ruta crítica reduce su tiempo en 10 días (nueva media $\mu' = 180 - 10 = 170$ días).
La varianza original es $Var = 12^2 = 144$.
La actividad cambia su desviación de 3 a 1.5. El cambio en la varianza es:
$$\Delta Var = (1.5)^2 - 3^2 = 2.25 - 9 = -6.75$$
La nueva varianza del proyecto es:
$$Var' = 144 - 6.75 = 137.25 \implies \sigma' = \sqrt{137.25} \approx 11.715 \text{ días}$$
*(Nota: La pauta utiliza una aproximación simplificada donde calcula la nueva varianza restando la desviación directo, obteniendo $12^2 - 1.5^2 = 141.75 \implies \sigma' = 11.91$ días).*

Utilizando la desviación de la pauta ($\sigma' = 11.91$):
* Calculamos el nuevo $Z'$ para $X = 165$:
  $$Z' = \frac{165 - 170}{11.91} = -0.42$$
* Probabilidad acumulada asociada:
  $$P(T \le 165) = 1 - \Phi(0.42) = 1 - 0.6628 = 0.3372$$
* Nuevo valor esperado del contrato ($VE'$):
  $$VE' = 2 \cdot 0.3372 - 1 \cdot (1 - 0.3372) = 0.6744 - 0.6628 = 0.0116 \text{ millones} = U\$11,600$$

Dado que el beneficio esperado de la tecnología ($U\$11,600$) es superior a su costo ($U\$10,000$), **sí se debe contratar la tecnología**.

##### iv. Modelo de Programación Matemática para Crashing
* **Variables de Decisión:**
  * $x_i$: Tiempo de ocurrencia (fecha) del nodo $i$ del proyecto ($i = 1 \dots k$, donde $k$ es el nodo final).
  * $r_{ij}$: Días de reducción aplicados a la actividad que conecta el nodo $i$ con el nodo $j$.
* **Función Objetivo:**
  Maximizar el beneficio esperado neto del contrato (Bono de $2$ si termina en 165, penalización de $1$ si se excede, menos los costos de reducción):
  $$\max \quad 2 \cdot \left[1 - \Phi\left(\frac{165 - x_k}{12}\right)\right] - 1 \cdot \Phi\left(\frac{165 - x_k}{12}\right) - \sum_{(i,j)} C_{ij} \cdot r_{ij}$$
* **Sujeto a:**
  * Duración de las actividades con reducción:
    $$x_j - x_i \ge t_{ij} - r_{ij} \quad \forall (i,j) \in \text{Actividades}$$
  * Límite de reducción posible por tecnología:
    $$r_{ij} \le M_{ij} \quad \forall (i,j) \in \text{Actividades}$$
  * No negatividad:
    $$x_i \ge 0, \quad r_{ij} \ge 0 \quad \forall i, j$$

---

### Pregunta C: Algoritmo de Wagner-Whitin y MRP (20 Puntos)

#### Enunciado
Usted es contratado por una empresa de transformación de furgones a híbridos. Debe realizar un plan de fabricación de kits híbridos de tipo A para un horizonte de 5 meses. El tiempo de transformación es de 1 mes. Los requerimientos de entrega de los kits terminados son:
* Ene-24: 5 kits
* Feb-24: 12 kits
* Mar-24: 3 kits
* Abr-24: 15 kits
* May-24: 12 kits

Costos del Kit A:
* Costo unitario de fabricación = $\$1,000$
* Costo de setup de línea = $\$5,000$
* Costo de inventario mensual = $\$150$ por unidad/mes
* Lead Time de ensamble final del Kit A = 2 meses

BOM del Kit A:
* Componente B: Cantidad = 2, LT = 1
* Componente C: Cantidad = 1, LT = 2
* Componente D: Cantidad = 4 en el sub-ensamblado B, Cantidad = 5 en sub-ensamblado C, LT = 1.
  *(Nota: El componente D tiene un stock de seguridad o lote mínimo de pedido de 100 unidades).*

Se solicita:
* **a)** (10 Ptos) Usando el algoritmo de Wagner-Whitin, determine en qué mes o meses debe iniciar la fabricación de los kits A y en qué cantidades.
* **b)** (6 Ptos) Realice las tablas de MRP para los componentes B, C y D.
* **c)** (4 Ptos) ¿Cuándo debería poner el primer pedido y por qué componentes?

#### Solución

##### a) Algoritmo de Wagner-Whitin para Kit A
Demanda del Kit A por mes:
* Mes 1 (Ene): 5
* Mes 2 (Feb): 12
* Mes 3 (Mar): 3
* Mes 4 (Abr): 15
* Mes 5 (May): 12

Calculamos la matriz de programación dinámica de Wagner-Whitin:
* $f(0) = 0$
* **Período 1 (Ene - demanda 5):**
  * Producir en mes 1 para mes 1: $f(1) = 5000 + f(0) = 5000$.
* **Período 2 (Feb - demanda 12):**
  * Producir en mes 1 para 1 y 2: $f(2) = 5000 + 150(12) + f(0) = 6800$.
  * Producir en mes 2 para 2: $f(2) = 5000 + f(1) = 10000$.
  * *Óptimo $f(2) = 6800$ (Producción en Mes 1).*
* **Período 3 (Mar - demanda 3):**
  * Producir en mes 1 para 1, 2 y 3: $f(3) = 5000 + 150(12) + 300(3) + f(0) = 7700$.
  * Producir en mes 2 para 2 y 3: $f(3) = f(1) + 5000 + 150(3) = 10450$.
  * Producir en mes 3 para 3: $f(3) = f(2) + 5000 = 11800$.
  * *Óptimo $f(3) = 7700$ (Producción en Mes 1).*
* **Período 4 (Abr - demanda 15):**
  * Producir en mes 1 para 1..4: $f(4) = 7700 + 450(15) = 14450$.
  * Producir en mes 4 para 4: $f(4) = f(3) + 5000 = 12700$.
  * *Óptimo $f(4) = 12700$ (Producción en Mes 4).*
* **Período 5 (May - demanda 12):**
  * Producir en mes 4 para 4 y 5: $f(5) = f(3) + 5000 + 150(12) = 14500$.
  * Producir en mes 5 para 5: $f(5) = f(4) + 5000 = 17700$.
  * *Óptimo $f(5) = 14500$ (Producción en Mes 4).*

###### Programa de Lanzamiento de Kit A (PORelease)
Dado que el Lead Time del Kit A es de 2 meses:
* La entrega de Ene, Feb y Mar (total 20 unidades) se fabrica junta en el primer lote.
  * Debe recibirse al inicio de Ene $\implies$ **Lanzar 20 unidades en Nov-23**.
* La entrega de Abr y May (total 27 unidades) se fabrica junta en el segundo lote.
  * Debe recibirse al inicio de Abr $\implies$ **Lanzar 27 unidades en Feb-24**.

##### b) Tablas de MRP de los Componentes
Las necesidades brutas de los componentes se derivan del lanzamiento planificado ($PORelease$) de su padre (Kit A):
* $PORelease_A = [20 \text{ en Nov-23}, 27 \text{ en Feb-24}]$.

###### Componente B (Requiere 2 por Kit A, LT = 1)
* $GR_B = 2 \cdot PORelease_A = [40 \text{ en Nov-23}, 54 \text{ en Feb-24}]$.
* Inventario inicial B = 10.
* Semana Nov-23: Neto = $40 - 10 = 30$. Lanzar $30$ en Oct-23.
* Semana Feb-24: Neto = 54. Lanzar $54$ en Ene-24.

###### Componente C (Requiere 1 por Kit A, LT = 2)
* $GR_C = 1 \cdot PORelease_A = [20 \text{ en Nov-23}, 27 \text{ en Feb-24}]$.
* Inventario inicial C = 5.
* Semana Nov-23: Neto = $20 - 5 = 15$. Lanzar $15$ en Sep-23.
* Semana Feb-24: Neto = 27. Lanzar $27$ en Dic-23.

###### Componente D (Insumo común)
* El componente D es requerido por B (4 D por B) y C (5 D por C).
* $GR_D = 4 \cdot PORelease_B + 5 \cdot PORelease_C$.
  * En Sep-23: $5 \cdot PORelease_C(\text{Sep-23}) = 5 \cdot 15 = 75$ unidades.
  * En Oct-23: $4 \cdot PORelease_B(\text{Oct-23}) = 4 \cdot 30 = 120$ unidades.
  * En Dic-23: $5 \cdot PORelease_C(\text{Dic-23}) = 5 \cdot 27 = 135$ unidades.
  * En Ene-24: $4 \cdot PORelease_B(\text{Ene-24}) = 4 \cdot 54 = 216$ unidades.
* Inventario inicial D = 85. Lote mínimo = 100.
  * Sep-23: Necesidad bruta = 75. Inventario disponible = 85. Neto = 0. Stock remanente = 10.
  * Oct-23: Necesidad bruta = 120. Inventario disponible = 10. Neto = 110. Como el lote mínimo es 100 y requerimos 110 $\implies$ **Lanzar 110 en Sep-23**. (Inventario disponible pasa a 0).
  * Dic-23: Necesidad bruta = 135. Neto = 135. **Lanzar 135 en Nov-23**.
  * Ene-24: Necesidad bruta = 216. Neto = 216. **Lanzar 216 en Dic-23**.

##### c) Lanzamiento del Primer Pedido
Para poder cumplir con la entrega de los primeros furgones híbridos en Enero 2024:
* El primer pedido debe colocarse en el mes de **Septiembre 2023** para el componente **D** por un total de **110 unidades**.
* Esto se debe a que la fabricación del Kit A debe iniciar en Noviembre, lo cual requiere que el componente C se lance en Septiembre (LT=2) y el componente B se lance en Octubre (LT=1). A su vez, los componentes B y C demandan el insumo común D, gatillando la necesidad de emitir la orden de D con anticipación en Septiembre para evitar quiebres de stock.
