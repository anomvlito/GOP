Nombre: ______________________________________ email UC: ______________________ 

**Pontificia Universidad Católica de Chile**  
**Escuela de Ingeniería**  
**Departamento de Ingeniería Industrial y de Sistemas**  

# Examen
# Enunciados

**ICS 3213 Gestión de Operaciones**  
**1$^{er}$ semestre 2024**

**Instrucciones:**

* Responder en letra legible, en lápiz pasta o bolígrafo y poner nombre a todas las hojas.
* No debe des corchetear la prueba y responda en el espacio asignado.
* Esta sección de la prueba tiene 60 puntos, dura 60 minutos.
* Se leerá la prueba al comienzo de clases y después se permitirán preguntas en voz alta. Posteriormente en la mitad de la prueba se volverá a permitir preguntas en voz alta. No se permitirán preguntas fuera de estos intervalos. Si su duda persiste indique el supuesto y continúe.
* Al final de la prueba los alumnos deberán subir su prueba a CANVAS. Dispondrán de 15 minutos para escanear pruebas hoja por hoja y subirlas. Al final de subir la prueba deberán dejarla en el mismo puesto. Si por alguna razón hay un problema al subir la prueba, avisen al profesor/ayudante y dejen su prueba.
* Este curso adscribe el Código de Honor establecido por la Escuela de Ingeniería el que es vinculante. Todo trabajo evaluado en este curso debe ser propio. En caso de que exista colaboración permitida con otros estudiantes, el trabajo deberá referenciar y atribuir correctamente dicha contribución a quien corresponda. Como estudiante es su deber conocer la versión en línea del Código de Honor (http://ing.puc.cl/codigodehonor).

¡Muy Buena Suerte!

---

**PARTE I: Responda UNA de las siguientes dos preguntas. Si responde las dos sólo se corregirá la primera.**

**a) (20 puntos)** Usted tiene el siguiente proceso que consta de 4 etapas, que produce el producto A y durante el proceso se genera desecho.

*(Diagrama de proceso:)*
- **Proceso 1:** $20 \text{ Kg/min}$
  - $75\%$ va a **Proceso 2:** $6 \text{ Kg/min}$
  - $25\%$ va a **Proceso 3:** $8 \text{ Kg/min}$
- Desde Proceso 2 y Proceso 3, el flujo va a **Proceso 4:** $12 \text{ Kg/min}$ (P2 aporta $80\%$, P3 aporta $20\%$ al desecho/producto)
- De Proceso 4 sale el **Producto** y **Desecho**.

a) (6 ptos) Si el proceso trabaja continuamente, no permite tener inventarios y no está limitada por la demanda o la llegada de insumos. Determine el cuello de botella y la capacidad de producción del producto A.
b) (6 ptos) Si usted puede alterar los porcentajes con los que se distribuye los productos de P1, que llegan a P2 y P3. ¿Qué distribución permitiría maximizar la producción y minimizar las pérdidas? ¿Cuál sería el nivel de producción? ¿Cuál procesos sería el cuello de botella?
c) (8 ptos) Para el proceso con los porcentajes iniciales (de la parte a), el proceso funciona 8 hrs al día y la demanda del producto A es de 2.000 kgs por día y tiene una utilidad de 9 \$/Kg. Si la empresa puede producir también los productos B o C y usted sabe que: la demanda del producto B es de 2500 kgs por día, tiene tasa de producción en el cuello de botella de 15 Kg/min y tiene una utilidad de 5 \$/Kg y la demanda del producto C es de 2.000 kgs por día, tiene tasa de producción en el cuello de botella de 10 Kg/min y tiene una utilidad de 9 \$/Kg. ¿Qué productos debe producir, en qué cantidad y cuál sería la utilidad?

**b) (20 puntos)** Usted se encuentra seleccionando la localización para su planta de producción. Actualmente tiene dos lugares como posibles candidatos L1 y L2. Los valores de compra del terreno y costos variables de operación para cada localización son:

| Localización | Costo Compra (U$) | Costo Operación (U$/unidad) |
| :--- | :--- | :--- |
| L1 | 10.000.- | 25 |
| L2 | 40.000.- | 10 |

a) (4 ptos) ¿Qué nivel de producción lo deja indiferente entre L1 o L2?
b) (8 ptos) Usted sabe que hoy (Tiempo 0) tiene una demanda de 1.000 unidades, estima que en el tiempo 9 va a tener una demanda de 3.100 unidades y la demanda crece linealmente en el tiempo. Si usted puede colocarse en L1 y después cambiarse a L2, pero a un costo fijo de cambio (Dado por el costo de venta y adquisición del nuevo terreno). ¿Qué máximo costo fijo que usted estaría dispuesto a aceptar para realizar el cambio?
c) (8 ptos) Si ahora usted puede sólo decidir por una ubicación y la demanda sigue la siguiente función (qué depende del tiempo t): $Q(t) = 1000 + 250t$. Si no hay cambio de valor del dinero en el tiempo y hoy se encuentra en $t=0$ y evalúa su proyecto a $t=10$. ¿Qué ubicación es la más adecuada? Muestre todos sus cálculos.

---
**Pregunta 1**

a) Se debe analizar el proceso por medio de saturar los flujos y se determina que el cuello de botella es el proceso 2.
Esto conlleva a que el ingreso se debe ajustar al CB y por ende deben entrar 8 kg/min.
Por ende, la capacidad del proceso es $7,6 \text{ Kg/min}$

b) El siguiente CB sería el proceso 4 por ende debemos ajustar el flujo a él y por ende sacar 12 unidades. Dado que debemos minimizar el desperdicio se debe fijar al máximo el proceso P2 y por ende fijar la entrada al remanente. $12-6 = 6 \text{ kgs por min}$ desde 3 y por ende deben entrar $6/0.8 = 7.5$. Por ende, el ingreso debe ser de $13.5 \text{ kgs/min}$ y el porcentaje a P3 es de $7.5/13.5 = 55.55\%$ y por ende a P2 debe ser $45.55\%$.

c) El cuello de botella es el proceso P2 con una capacidad de 7.6 Kg/min al final por ende hay que determinar el beneficio en el CB de cada producto.

* Producto A: $9 * 7.6 = 68.4 \text{ \$/min}$
* Producto B: $15 * 5 = 75 \text{ \$/min}$
* Producto C: $10 * 9 = 90 \text{ \$/min}$

Disponemos de $60 * 8 = 480$ minutos al día. Por ende, primero pasamos el producto C y pasamos los 2000 kgs que consume 200 minutos de producción, quedando 280 minutos. Después vamos al producto B, se procesa los 2500 y consume 166,7 minutos y quedan 33.3 minutos que se ocupan en A, produciendo 253 kgs de A

**Pregunta 2:**

a) Se debe determinar el punto de equilibrio entre ambos.
$$10.000 + 25X = 40.000 + 10X \rightarrow X = 2.000$$

b) Si analizamos el beneficio asociado al cambio, debemos ver el ahorro que se produce después del punto de equilibrio.
Lugar 1 $= (3100-2000) * (87500-60000) / 2 = \$15.125.000.-$
Lugar 2 $= (3100-2000) * (71000-60000) / 2 = \$6.050.000.-$

El diferencial es de \$9.075.000.- Es lo máximo que estoy dispuesto a pagar.

c) Para analizar el impacto, se debe incorporar la función y hacer un cambio de variable.
Lugar 1 $= 35.000 + 6250t$
Lugar 2 $= 50.000 + 2500t$

Se analiza las integrales, lo cual entrega para L1 662.500 y L2 625.000 por ende L2 es más conveniente.

---
**PARTE II: Responda todas las siguientes preguntas de ejercicio.**

**PII.a (20 puntos)** Usted está realizando su trabajo de título en una empresa metalmecánica encargada de fabricar perfiles de aluminio para la construcción de edificios. Para la construcción de los perfiles, que son de 1.5 metros de largo, la empresa compra rollos de aluminio de 150 metros de largo, que por diseño tienen el ancho justo para los perfiles. Los rollos de aluminio son cortados en trozos de 1.5 metros que se dejan como inventario en proceso para entrar a la máquina que fabrica los perfiles. La perfiladora (la máquina que se encarga de armar los perfiles), similar a la de la figura abajo, recibe uno de los trozos de 1.5mt de la estación anterior y procede a fabricar el perfil.

El proceso para fabricar el perfil implica introducir la hoja de aluminio y calentar el metal a 200 °C, doblándolo para crear el perfil y pasarlo a la estación de trabajo siguiente. El tiempo que demora en llevar el metal a esa temperatura depende de las condiciones ambientales, lo que implica variabilidad en el tiempo que demora en fabricar cada perfil. Se toman mediciones del proceso y en promedio demora 12 minutos, con una desviación estándar de 2 minutos.

a) (3 Ptos.) Calcule el coeficiente de variabilidad del tiempo de flujo de cada perfil en esta máquina.

Se ha decidido invertir en una nueva máquina perfiladora, que sea más moderna para poder fabricar en forma más eficiente y rápido. La nueva máquina identificada demora en promedio 10 minutos en fabricar cada perfil, con una desviación estándar de 100 segundos.

b) (3 Ptos.) Calcule el coeficiente de variabilidad del tiempo de producción de cada perfil en la nueva máquina.

La máquina original, dada su edad, tiene un tiempo medio entre fallas de 57 horas, con un tiempo de reparación promedio de 19 horas dada su simplicidad. Por otro lado, la nueva máquina posee un tiempo medio entre fallas de 372 horas, muy superior a la máquina antigua. Dada su complejidad, cuando falla es necesario traer un técnico para repararla, lo cual implica un tiempo medio de reparación de 124 horas. Considere que todos los tiempos tienen distribución exponencial y en ambos casos las reparaciones tienen un coeficiente de variabilidad de 1.

c) (6 Ptos.) Determine la disponibilidad de cada máquina.
d) (8 Ptos.) Calcule ahora el coeficiente de variabilidad efectivo de cada máquina. Considerando su nueva métrica, ¿Cuál máquina considera que es mejor y por qué?

---
**Respuestas:**

1. El coeficiente de variabilidad es $C_t = s/t = 2/12 = 0.167$

2. En este caso el tiempo promedio de producción es de 10 minutos, con una desviación de 1.67 minutos. Esto da un coeficiente de variabilidad de 0.167 igual que antes.

3. 
Para la máquina 1:
$A = 57 / (57 + 19) = 0.75$

Para la máquina 2:
$A = 372 / (372 + 124) = 0.75$

Dado que en ambos casos la disponibilidad es la misma no hay ninguna razón para elegir una máquina sobre la otra.

4.
Para la máquina 1:
$C_e^2 = 0.1667^2 + (1 + 1^2) \times 0.75(1 - 0.75) \times 19 / 12 = 0.62$

Para la máquina 2:
$C_e^2 = 0.1667^2 + (1 + 1^2) \times 0.75(1 - 0.75) \times 124 / 10 = 4.68$

¡El coeficiente de variabilidad es mucho más grande en la máquina 2!

---

**PII.b (20 puntos)** Usted decide controlar un proceso de producción de botellas de vidrio y decide hacer un esquema de muestras de 20 botellas cada una a las cuales les mide el grosor en milímetros. Los resultados de 25 grupos de muestra se detallan a continuación, con su respectivo promedio, valor mínimo y máximo de cada muestra.

| Muestra | Promedio | Mínimo | Máximo | &nbsp;&nbsp;&nbsp;&nbsp; | Muestra | Promedio | Mínimo | Máximo |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 25.1 | 24.0 | 26.2 | | 14 | 26.1 | 24.9 | 27.3 |
| 2 | 25.8 | 24.5 | 27.1 | | 15 | 24.6 | 23.4 | 25.8 |
| 3 | 24.7 | 23.9 | 25.5 | | 16 | 27.5 | 26.2 | 28.8 |
| 4 | 26.4 | 25.2 | 27.8 | | 17 | 25.7 | 24.5 | 26.9 |
| 5 | 25.3 | 24.3 | 26.3 | | 18 | 24.8 | 23.6 | 26.0 |
| 6 | 24.5 | 23.5 | 25.5 | | 19 | 26.3 | 25.0 | 27.6 |
| 7 | 25.9 | 24.6 | 27.2 | | 20 | 25.0 | 23.9 | 26.1 |
| 8 | 25.2 | 24.2 | 26.2 | | 21 | 24.5 | 23.3 | 25.7 |
| 9 | 24.9 | 23.7 | 26.1 | | 22 | 27.6 | 26.3 | 28.9 |
| 10 | 26.0 | 24.8 | 27.2 | | 23 | 25.6 | 24.4 | 26.8 |
| 11 | 26.4 | 25.1 | 27.7 | | 24 | 25.1 | 23.8 | 26.4 |
| 12 | 25.4 | 24.4 | 26.4 | | 25 | 24.4 | 23.1 | 25.7 |
| 13 | 24.2 | 23.0 | 25.4 | | | | | |

Donde tenemos los siguientes datos de la tabla:
$$ \sum \text{Promedio} = 637.1 \quad \sum \text{Mínimo} = 607.6 \quad \sum \text{Máximo} = 666.6 $$
$$ \sum (\text{Promedio})^2 = 16,255.53 \quad \sum (\text{Mínimo})^2 = 14,784.56 \quad \sum (\text{Máximo})^2 = 17,796.96 $$

a) (3 puntos) Con esta información determine los límites de control del grosor de botella.
b) (2 puntos) Suponga ahora que calcula una nueva muestra, con media 25.3 mm y recorrido 0.8 mm. ¿Qué puede decir del proceso? ¿Se encuentra bajo control? ¿Por qué?
c) (8 puntos) Si ahora le informan que las muestras tomadas son de 30 botellas cada una (con la misma información de la tabla inicial). En base a esta nueva información, desarrolle los gráficos de control del proceso para un control 90%. ¿Cómo cambia lo obtenido en a)?
d) (5 puntos) Para el tamaño de muestra de 30 botellas ¿Cuál es el porcentaje de confianza mínimo necesario para que no se deban eliminar muestras en el desarrollo de gráficos del inciso anterior?
e) (2 puntos) ¿Este porcentaje es alto o bajo? ¿Qué indica esto sobre el proceso de producción? ¿Qué efecto tiene eliminar muestras con respecto al porcentaje de confianza en este proceso?

---
1) Como son 20 muestras, desde la tabla extraemos $A_2 = 0.18$, $D_2 = 3.735$, $D_3 = 0.415$, $D_4 = 1.585$

Luego, calculamos el promedio y recorrido medio del muestreo:
Promedio $= 25.484 \quad \text{Recorrido} = 2.36$

Finalmente, los límites de control son:
Para el promedio: $[25.06, 25.9]$, para el recorrido: $[0.979, 3.7406]$

2) El proceso no se encuentra bajo control, ya que el recorrido de la nueva muestra está fuera de los límites y además hay varias muestras previas que no se encuentran en los límites del promedio.

3) Calculamos la desviación estándar como:
$\text{Raíz} \left(\sum (\text{Promedio})^2 / 25 - (25.484)^2\right) = 0.887$

Luego, el límite inferior es: $25.484 - 0.887 * 1.64 = 24.046$
Mientras que el límite superior es: $25.484 + 0.887 * 1.64 = 26.922$

Esto indica que las muestras 16 y 22 deben ser eliminadas pues están fuera de los límites de control.

Volvemos a calcular la media y la desviación estándar sin las 2 muestras:

Promedio $= 25.304$
Desviación estándar $= 0.685$

Por lo tanto, los nuevos límites corresponden a:

Inferior: $25.304 - 0.685 * 1.64 = 24.181$
Superior: $25.304 + 0.685 * 1.64 = 26.427$

Como todos están dentro de los límites terminamos el proceso y la muestra ya se encuentra bajo control.

4) Para calcular los porcentajes de confianza, debemos igualar a los promedios de muestras extremos.

Inferior: $25.484 - 0.887 * Z = 24.2$
Superior: $25.484 + 0.887 * Z = 27.6$

Tenemos que $Z_{inf} = 1.44$ y $Z_{sup} = 2.39$. Luego, la confianza mínima donde no se borran muestras es de $98.32\%$

5) Este porcentaje de confianza es muy alto, por lo que indica un proceso que tiende a aceptar muestras que posiblemente puedan tener fallos, es decir, aumenta la probabilidad de cometer un error del consumidor (Beta). Por otro lado, eliminar muestras aumenta la probabilidad del error del productor (Alpha), se debe buscar el trade off correcto según el tipo de proceso, en este caso es mejor un error de productor, ya que el grosor de una botella puede traer consecuencias mucho más graves que el costo de oportunidad de las mermas respectivas.

---

# Formulario

**Tabla de distribución normal estándar**
$$ P(Z \le z) = \int_{-\infty}^{z} f(t) dt $$

| z | 0.00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.0** | .5000 | .5040 | .5080 | .5120 | .5160 | .5199 | .5239 | .5279 | .5319 | .5359 |
| **0.1** | .5398 | .5438 | .5478 | .5517 | .5557 | .5596 | .5636 | .5675 | .5714 | .5753 |
| **0.2** | .5793 | .5832 | .5871 | .5910 | .5948 | .5987 | .6026 | .6064 | .6103 | .6141 |
| **0.3** | .6179 | .6217 | .6255 | .6293 | .6331 | .6368 | .6406 | .6443 | .6480 | .6517 |
| **0.4** | .6554 | .6591 | .6628 | .6664 | .6700 | .6736 | .6772 | .6808 | .6844 | .6879 |
| **0.5** | .6915 | .6950 | .6985 | .7019 | .7054 | .7088 | .7123 | .7157 | .7190 | .7224 |
| **0.6** | .7257 | .7291 | .7324 | .7357 | .7389 | .7422 | .7454 | .7486 | .7517 | .7549 |
| **0.7** | .7580 | .7611 | .7642 | .7673 | .7704 | .7734 | .7764 | .7794 | .7823 | .7852 |
| **0.8** | .7881 | .7910 | .7939 | .7967 | .7995 | .8023 | .8051 | .8078 | .8106 | .8133 |
| **0.9** | .8159 | .8186 | .8212 | .8238 | .8264 | .8289 | .8315 | .8340 | .8365 | .8389 |
| **1.0** | .8413 | .8438 | .8461 | .8485 | .8508 | .8531 | .8554 | .8577 | .8599 | .8621 |
| **1.1** | .8643 | .8665 | .8686 | .8708 | .8729 | .8749 | .8770 | .8790 | .8810 | .8830 |
| **1.2** | .8849 | .8869 | .8888 | .8907 | .8925 | .8944 | .8962 | .8980 | .8997 | .9015 |
| **1.3** | .9032 | .9049 | .9066 | .9082 | .9099 | .9115 | .9131 | .9147 | .9162 | .9177 |
| **1.4** | .9192 | .9207 | .9222 | .9236 | .9251 | .9265 | .9279 | .9292 | .9306 | .9319 |
| **1.5** | .9332 | .9345 | .9357 | .9370 | .9382 | .9394 | .9406 | .9418 | .9429 | .9441 |
| **1.6** | .9452 | .9463 | .9474 | .9484 | .9495 | .9505 | .9515 | .9525 | .9535 | .9545 |
| **1.7** | .9554 | .9564 | .9573 | .9582 | .9591 | .9599 | .9608 | .9616 | .9625 | .9633 |
| **1.8** | .9641 | .9649 | .9656 | .9664 | .9671 | .9678 | .9686 | .9693 | .9699 | .9706 |
| **1.9** | .9713 | .9719 | .9726 | .9732 | .9738 | .9744 | .9750 | .9756 | .9761 | .9767 |
| **2.0** | .9772 | .9778 | .9783 | .9788 | .9793 | .9798 | .9803 | .9808 | .9812 | .9817 |
| **2.1** | .9821 | .9826 | .9830 | .9834 | .9838 | .9842 | .9846 | .9850 | .9854 | .9857 |
| **2.2** | .9861 | .9864 | .9868 | .9871 | .9875 | .4878 | .9881 | .9884 | .9887 | .9890 |
| **2.3** | .9893 | .9896 | .9898 | .9901 | .9904 | .9906 | .9909 | .9911 | .9913 | .9916 |
| **2.4** | .9918 | .9920 | .9922 | .9925 | .9927 | .9929 | .9931 | .9932 | .9934 | .9936 |
| **2.5** | .9938 | .9940 | .9941 | .9943 | .9945 | .9946 | .9948 | .9949 | .9951 | .9952 |
| **2.6** | .9953 | .9955 | .9956 | .9957 | .9959 | .9960 | .9961 | .9962 | .9963 | .9964 |
| **2.7** | .9965 | .9966 | .9967 | .9968 | .9969 | .9970 | .9971 | .9972 | .9973 | .9974 |
| **2.8** | .9974 | .9975 | .9976 | .9977 | .9977 | .9978 | .9979 | .9979 | .9980 | .9981 |
| **2.9** | .9981 | .9982 | .9982 | .9983 | .9984 | .9984 | .9985 | .9985 | .9986 | .9986 |
| **3.0** | .9987 | .9987 | .9987 | .9988 | .9988 | .9989 | .9989 | .9989 | .9990 | .9990 |
| **3.1** | .9990 | .9991 | .9991 | .9991 | .9992 | .9992 | .9992 | .9992 | .9993 | .9993 |
| **3.2** | .9993 | .9993 | .9994 | .9994 | .9994 | .9994 | .9994 | .9995 | .9995 | .9995 |
| **3.3** | .9995 | .9995 | .9995 | .9996 | .9996 | .9996 | .9996 | .9996 | .9996 | .9997 |
| **3.4** | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9998 |

---

# Formulario (Ecuaciones)

$$ CT = DC + \frac{D}{Q}S + \frac{Q}{2}H $$
$$ Q^* = F^{-1} \left( \frac{C_u}{c_o + C_u} \right) $$
$$ EF = ES + t $$
$$ LS = LF - t $$
$$ Q_{eoq} = \sqrt{\frac{2 \times D \times S}{H}} $$
$$ R = d \times L $$
$$ \mu = \frac{a + 4m + b}{6} $$
$$ \sigma = \frac{b - a}{6} $$
$$ Z = \frac{D - T_E}{\sqrt{\sum \sigma_i^2}} $$
$$ R = d \times L + z_\alpha \sigma \sqrt{L} $$

$$ Q^* = d \times (T + L) + z_\alpha \sigma \sqrt{(T + L)} - I_{\text{existente}} $$
$$ Q = T_P \times p $$
$$ T_P = \frac{Q}{p} $$
$$ ef = \frac{k}{k+1} $$
$$ I = T_P \times (p - d) $$
$$ P = \sqrt{\left(\frac{a}{2}\right) \left(\frac{q}{z}\right)} \quad P = \sqrt{\left(\frac{a}{2}\right) \left(\frac{1}{n}\right) \left( \sum_{i=1}^n \frac{q_i}{z_i} \right)} $$
$$ Ben = s p_i - c_r d_i $$
$$ Ben = s (p_i + D_i) $$
$$ Beneficio_{\min\_A} = \frac{s * p_i - c_r * d_i}{l_i} $$
$$ Restocks = \frac{f_i}{V_i} \text{ Restocks/tiempo} $$
$$ Beneficio_{\text{adic\_A}} = \frac{s * D_i + c_r * d_i}{u_i - l_i} $$
$$ \text{Costo Total} = \text{Costo Fijo} + \text{Costo Variable} \times \text{Volumen} $$
$$ v_i^* = \left( \frac{\sqrt{f_i}}{\sum_{j=1}^n \sqrt{f_j}} \right) V \frac{p_i}{\sqrt{fi}} $$
$$ C_x = \frac{\sum d_{ix} V_i}{\sum V_i} $$
$$ C_y = \frac{\sum d_{iy} V_i}{\sum V_i} $$
$$ \rho = \frac{\lambda}{\mu} $$
$$ \rho = \frac{\lambda}{c\mu} $$
$$ L = \lambda \times W $$
$$ c_T = \frac{\sigma}{t} = \frac{\sqrt{\text{Var}(T)}}{E(T)} $$
$$ L = \frac{\rho}{1 - \rho}, \quad W = \frac{1}{\mu(1 - \rho)} $$
$$ L_q = \frac{\rho^2}{1 - \rho}, \quad W_q = \frac{\rho}{\mu(1 - \rho)} $$
$$ WIP = TH \times TC $$
$$ L = \lambda * W $$
$$ A = \frac{m_f}{m_r + m_f} $$
$$ t_e = \frac{t_o}{A} $$
$$ \sigma^2_e = \left(\frac{\sigma^2_o}{A}\right) + \frac{(m_r + \sigma^2_r)(1 - A)t_o}{Am_r} $$
$$ c^2_e = \frac{\sigma^2_e}{t_e^2} = c^2_o + (1 + c^2_r)A(1 - A) \frac{m_r}{t_o} $$
$$ t_e = t_o + \frac{t_s}{N_s} $$
$$ \sigma^2_e = \sigma^2_o + \frac{\sigma^2_s}{N_s} + \frac{N_s - 1}{N_s^2} t^2_s $$
$$ c^2_e = \frac{\sigma^2_e}{t_e^2} $$
$$ (c_S)^2 \approx \rho^2 (c_e)^2 + (1 - \rho^2) (c_a)^2 $$
$$ CT_q = \left( \frac{C_a^2 + C_e^2}{2} \right) \left( \frac{\rho}{1 - \rho} \right) t_e $$

$$ L = \frac{\rho}{1 - \rho} - \frac{(b + 1)\rho^{b+1}}{1 - \rho^{b+1}} $$
$$ \lambda' = \lambda \left( \frac{1 - \rho^b}{1 - \rho^{b+1}} \right) $$
$$ L_q = \frac{\rho}{1 - \rho} \times Prob(N > c) $$
$$ W_q = \frac{\rho}{\lambda(1 - \rho)} \times Prob(N > c) $$
$$ F_t = w_1 A_{t-1} + w_2 A_{t-2} + w_3 A_{t-3} + \dots + w_n A_{t-n} $$
$$ \hat{y} = a + bx $$
$$ \sum_{i=1}^n w_i = 1 $$
$$ F_{t+1} = \alpha A_t + (1 - \alpha) F_t $$
$$ TS_k = \frac{\sum_{t=1}^k e_t}{MAD_k} $$
$$ F_t = \frac{A_{t-1} + A_{t-2} + A_{t-3} + \dots + A_{t-n}}{n} $$
$$ T_{(t, t-1)} = A_t - A_{t-1} $$
$$ \bar{T} = \frac{\sum_{i=1}^n T_{(t-i, t-i-1)}}{n} $$
$$ e_t = F_t - A_t $$
$$ \sigma = 1.25 * MAD $$
$$ FIT_t = F_t + T_t $$
$$ F_t = FIT_{t-1} + \alpha(A_{t-1} - FIT_{t-1}) $$
$$ T_t = T_{t-1} + \alpha\delta(A_{t-1} - FIT_{t-1}) $$
$$ MAD_k = \frac{1}{k} \sum_{t=1}^k |e_t| $$
$$ L = t_k + t_p + t_v $$
$$ b = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2} $$
$$ a = \frac{\sum y}{n} - b \frac{\sum x}{n} = \bar{y} - b\bar{x} $$
$$ LCS = \bar{\bar{x}} + Z * \sigma $$
$$ LCI = \bar{\bar{x}} - Z * \sigma $$
$$ N = \frac{D \times L}{C} (1 + \varepsilon) $$
$$ N = \frac{D \times L}{C} $$

| c | LTPD/AQL | n*AQL |
| :---: | :---: | :---: |
| 0 | 44,890 | 0,052 |
| 1 | 10,946 | 0,355 |
| 2 | 6,509 | 0,818 |
| 3 | 4,890 | 1,366 |
| 4 | 4,057 | 1,97 |
| 5 | 3,549 | 2,613 |
| 6 | 3,206 | 3,286 |
| 7 | 2,957 | 3,981 |
| 8 | 2,768 | 4,695 |
| 9 | 2,618 | 5,426 |

$$ p_0 \pm 3 \sqrt{\frac{p_0(1-p_0)}{n}} $$

| Tamaño Muestra | $A_2$ | $d_2$ | $D_3$ | $D_4$ |
| :--- | :--- | :--- | :--- | :--- |
| 2 | 1.880 | 1.128 | 0 | 3.267 |
| 3 | 1.023 | 1.693 | 0 | 2.574 |
| 4 | 0.729 | 2.059 | 0 | 2.282 |
| 5 | 0.577 | 2.326 | 0 | 2.114 |
| 6 | 0.483 | 2.534 | 0 | 2.004 |
| 7 | 0.419 | 2.704 | 0.076 | 1.924 |
| 8 | 0.373 | 2.847 | 0.136 | 1.864 |
| 9 | 0.337 | 2.970 | 0.184 | 1.816 |
| 10 | 0.308 | 3.078 | 0.223 | 1.777 |
| 11 | 0.285 | 3.173 | 0.256 | 1.744 |
| 12 | 0.266 | 3.258 | 0.283 | 1.717 |
| 13 | 0.249 | 3.336 | 0.307 | 1.693 |
| 14 | 0.235 | 3.407 | 0.328 | 1.672 |
| 15 | 0.223 | 3.472 | 0.347 | 1.653 |
| 16 | 0.212 | 3.532 | 0.363 | 1.637 |
| 17 | 0.203 | 3.588 | 0.378 | 1.622 |
| 18 | 0.194 | 3.640 | 0.391 | 1.608 |
| 19 | 0.187 | 3.689 | 0.403 | 1.597 |
| 20 | 0.180 | 3.735 | 0.415 | 1.585 |
| 21 | 0.173 | 3.778 | 0.425 | 1.575 |
| 22 | 0.167 | 3.819 | 0.434 | 1.566 |
| 23 | 0.162 | 3.858 | 0.443 | 1.557 |
| 24 | 0.157 | 3.895 | 0.451 | 1.548 |
| 25 | 0.153 | 3.931 | 0.459 | 1.541 |

$$ LCS \ \bar{X} = \bar{\bar{X}} + A_2 * \bar{R} $$
$$ LCI \ \bar{X} = \bar{\bar{X}} - A_2 * \bar{R} $$
$$ LCS \ R = D_4 * \bar{R} $$
$$ LCI \ R = D_3 * \bar{R} $$

$$ C_p = \frac{USL - LSL}{6\sigma} $$
$$ C_{pk} = \frac{USL - Media}{3\sigma} $$
$$ C_{pk} = \frac{Media - LSL}{3\sigma} $$
