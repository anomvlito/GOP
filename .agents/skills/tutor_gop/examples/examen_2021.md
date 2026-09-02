**Nombre:** _______________________________ **email UC:** ______________________ **Sección:**_____

**Pontificia Universidad Católica de Chile**
**Escuela de Ingeniería**
**Departamento de Ingeniería Industrial y de Sistemas**

# Examen - Enunciados
**ICS 3213 Gestión de Operaciones**
**Sección 1 y Sección 2 – 1er semestre 2021**
**Prof. Herman Gothe**
**Prof. Alejandro Mac Cawley**

**Instrucciones:**
* Responder en letra legible, en lápiz pasta o bolígrafo y poner nombre a todas las hojas.
* Responder las preguntas en orden e indicar claramente la pregunta (i.a, i.b, ii.a y ii.b)
* Esta sección de la prueba tiene 68 puntos, dura 70 minutos y consta de 2 secciones.
* Se leerá la prueba al comienzo de clases y después se permitirán preguntas en voz alta. Posteriormente en la mitad de la prueba se volverá a permitir preguntas en voz alta. No se permitirán preguntas fuera de estos intervalos. Si su duda persiste indique el supuesto y continúe.
* Al final de la prueba los alumnos deberán mantener online y se dividirán los alumnos en distintos break rooms numeradas, cada una de las cuales tiene un ayudante o profesor a cargo. Dispondrán de 15 minutos para escanear pruebas hoja por hoja y subirlas. Para subir las pruebas, los alumnos deberán subir su prueba I1 en la web de CANVAS en la Tarea con el número de su breakup-room. Es decir, si fui asignado al breakup-room 1, debo subir mi I2 en la tarea que dice I2 Breakup-Room 1. Al final de los 15 minutos el ayudante o profesor revisara las pruebas en el sistema e indicara si están OK y se podrán desconectar. Si por alguna razón hay un problema al subir la prueba, podrán mandarla por mail al profesor.
* Este curso adscribe el Código de Honor establecido por la Escuela de Ingeniería el que es vinculante. Todo trabajo evaluado en este curso debe ser propio. En caso de que exista colaboración permitida con otros estudiantes, el trabajo deberá referenciar y atribuir correctamente dicha contribución a quien corresponda. Como estudiante es su deber conocer la versión en línea del Código de Honor (http://ing.puc.cl/codigodehonor).

¡Muy Buena Suerte!

---

**PARTE I (20 Puntos): Responda todas las siguientes preguntas cortas de ejercicio.**

**i.** Usted se encuentra a cargo de un proceso productivo que tiene 3 máquinas en serie, como se detalla en el esquema a continuación.

Máquina 1 $\rightarrow$ Máquina 2 $\rightarrow$ Máquina 3

El sistema es capaz de procesar 3 SKU distintos (A, B y C) a tasa productivas distintas para cada máquina y que no tienen tiempos de setup. A continuación se detallan los tiempos requridos para procesar cad unidad en cada máquina, el márgen obtenido y su demanda diaria.

| SKU | Capacidad en CB (min/unid) - Maq 1 | Capacidad en CB (min/unid) - Maq 2 | Capacidad en CB (min/unid) - Maq 3 | Margen ($/unid) | Demanda diaria (unidades) |
|---|---|---|---|---|---|
| SKU A | 1 | 2 | 0,3 | 18 | 120 |
| SKU B | 0,8 | 0,5 | 1 | 10 | 240 |
| SKU C | 3 | 2 | 1 | 25 | 120 |

a) Si el proceso productivo funciona 1 turno de 8 hrs al día los 7 días de la semana. ¿Cuál será el plan diario de producción?

Se debe determinar el Cuello de botella para cad SKU. A es M2, B es M3 y C es M1.
Se obtiene el margen por minuto en el CB.

| SKU | MM |
|---|---|
| SKU A | 9 |
| SKU B | 10 |
| SKU C | 8,33333333 |

Por ende, se pasa primero el SKU B y después el A y se utilizan los 480 minutos del turno.

b) Si el activar un turno adicional de 8 hrs tiene un costo fijo de $3.500. ¿Activaría usted este turno? 

El procesar el producto C genera un margen de $3000 que es inferior que el costo de activar y por ende NO conviene activar el turno.

**ii.** Usted se encuentra a cargo de un proyecto y ha determinado que la ruta crítica esperada tiene una duración de 240 días con una desviación standard de 20 días. Actualmente se encuentra cerrando el contrato del proyecto y su contraparte le ofrece un bono de $ 300 Millones por terminar antes de una fecha y una penalidad de $200 millones si termina después de dicha fecha.

a) (4 puntos) Si la contraparte le ofrece terminar el proyecto en 220 días. ¿Acepta usted el contrato? Muestre todos sus cálculos.

$$Z = \frac{D - T_E}{\sqrt{\sum \sigma_i^2}} = \frac{220 - 240}{20} = -1$$

$$Pr(z < -1) = 0,1587 = 15.87\%$$

P() Bono = $300 \cdot 0.1587 = 47.61$
P() Penalidad = $200 \cdot (1 - 0.1587) = 168.26$
No Acepto

b) (6 puntos) Una empresa consultora le asegura que puede reducir el tiempo del proyecto a 225 días y su desviación standard a 15 días a costo fijo de $10 millones. Utilizando la consultora, ¿Aceptaría el contrato de terminar en 220 días? Muestre todos sus cálculos.

$$Z = \frac{D - T_E}{\sqrt{\sum \sigma_i^2}} = \frac{220 - 225}{15} = -0.33$$

$$Pr(z < 0.33) = 0,3707 = 37.07\%$$

P() Bono = $(300 - 10) \cdot 0.3707 = 107.503$
P() Penalidad = $(200 + 10) \cdot (1 - 0.3707) = 132.153$
No acepto el contrato a pesar de la consultora.

---

**PARTE II (20 Puntos): Responda todas las siguientes preguntas cortas de ejercicio.**

**i.** (12 puntos) Usted quiere abrir una tienda de mascotas y desea dar un buen servicio a sus clientes. Usted hace un estudio de mercado y determina que en la zona la tasa de llegada de clientes a la tienda será de 18 clientes/hora y se distribuye Poisson. Por otro lado, usted tiene una caja que tiene la capacidad de atender a 20 clientes/hora y se distribuye Poisson. Si el tiempo promedio que el cliente se encuentra en la tienda (mirando productos y en la caja) es de 3 minutos. Si por la pandemia, el aforo máximo de la tienda es de 1 cliente adentro.
a) ¿Cuánto tiempo esperan los clientes en la cola afuera?

Se utiliza la ecuación M/M/1

$$L_q = \frac{\rho^2}{1-\rho}, \quad W_q = \frac{\rho}{\mu(1-\rho)}$$

$\rho$ es igual a $= 18/20 = 0.9$
$L_q$ es $= 0.9 / 20 \cdot 0.1 = 0.45$ hrs o $27$ minutos 

b) Si usted puede hacer un sistema online de reserva de horario, que permita que lleguen los clientes sigan llegando Possion pero a una tasa definida. Si desea que sus clientes no esperen más de 15 minutos. ¿Cuál debería ser la tasa de llegada de clientes que debe apuntar a tener con el sistema de citas?

$0.25 = L / 20 / (20 \cdot (1 - L/20))$
se despeja $L$ y llegamos a $16.667$

**ii.** Usted se encuentra determinando el tamaño mínimo de bodega que debe adquirir. Para ello usted determina que la demanda anual es de 60.000 pallets y los operadores de montacargas trabajan turnos de 8 hrs. por 250 días al año, con un sueldo mensual de $15 mil. El tiempo medio desde la recepción a bodega y a despacho es de 20 minutos. Si el costo anual por mt2 de terreno e infraestructura para bodega es de $1.000 el mt2 y cada pallet utiliza 4 mt2 de piso en la bodega (Ya que pueden ser apilados). Caracterice la función de costos totales anuales de la bodega. Determine la cantidad de trabajadores y el tamaño óptimo de bodega. Muestre todos sus cálculos. 

Los minutos anuales disponibles por operador $= 60 \cdot 8 \cdot 250 = 120.000$ minutos
Como se demora 20 minutos en mover un pallet, son 6.000 pallets que puede mover al año, por ende 1 opear es capaz de rotar $(60.000 / 6.000) = 10$ rotaciones/año.

Si utilizamos la formula de flujo $Q = A \cdot v$. Disponemos de la cantidad que hay que mover $(Q) = 60.000$ y la velocidad $v$ esta dada por la cantidad de personas ($T$) $v = 10 \cdot T$ por ende el área en términos de pallets que se requiere es $A = Q / v = 60.000 / 10T$.

Si transformamos el costo de espacio en términos de pallets es $= 1.000 \ \$/\text{mt}^2 \cdot 4 \ \text{mt}^2/\text{pallet} = 250 \ \$/\text{pallet}$.

Por ende la función de costo total en términos de Trabajadores es $CT (T) = 250 \cdot (60.000 / 10T) + 15.000 \cdot T$
Derivando por T e igualando a 0 se obtiene $= -1.500.000 / T^2 + 15.000 = 0$
Despejando T se obtiene 10 personas.
En tamaño utilizando la formula es 600 pallets, que corresponden a $600 \cdot 4 = 2.400 \ \text{mt}^2$

**iii.** Su empresa ha construido una zona de *picking* rápido de 20 m$^3$ y se le pide a usted ubicar los SKU que se detallan en la tabla a continuación.

| SKU | cajas/mes | m$^3$/caja |
|---|---|---|
| A | 40 | 2 |
| B | 20 | 1,5 |
| C | 45 | 1 |

Si el costo de reposición es de \$ 3 por reposición para cada SKU y usando una política de volumen óptimo y otra de igual tiempo. Determine:
a) (8 puntos) Para cada política ¿Cuánto espacio asigna a cada uno? ¿Cuál es el costo de cada política?

Se determinan los flujos:

$$f_A = \frac{\text{cajas}}{\text{mes}} \cdot \frac{\text{m}^3}{\text{caja}} = 40 \cdot 2 = 80 \ \frac{\text{m}^3}{\text{mes}}$$

$$f_B = \frac{\text{cajas}}{\text{mes}} \cdot \frac{\text{m}^3}{\text{caja}} = 20 \cdot 1,5 = 30 \ \frac{\text{m}^3}{\text{mes}}$$

$$f_C = \frac{\text{cajas}}{\text{mes}} \cdot \frac{\text{m}^3}{\text{caja}} = 45 \cdot 1 = 45 \ \frac{\text{m}^3}{\text{mes}}$$

Se calcula el volumen optimo:

$$v_A^* = \frac{\sqrt{f_A}}{\sum_{i=1}^n \sqrt{f_i}} \cdot V = \frac{\sqrt{80}}{\sqrt{80} + \sqrt{30} + \sqrt{45}} \cdot 25 = 10,58 \ \text{m}^3$$

$$v_B^* = \frac{\sqrt{f_B}}{\sum_{i=1}^n \sqrt{f_i}} \cdot V = \frac{\sqrt{30}}{\sqrt{80} + \sqrt{30} + \sqrt{45}} \cdot 25 = 6,48 \ \text{m}^3$$

$$v_C^* = \frac{\sqrt{f_C}}{\sum_{i=1}^n \sqrt{f_i}} \cdot V = \frac{\sqrt{45}}{\sqrt{80} + \sqrt{30} + \sqrt{45}} \cdot 25 = 7,94 \ \text{m}^3$$

Se tienen un total de 17,85 reposiciones lo cual da un costo de 53,575

Bajo igual tiempo

| | | 25 | | |
|---|---|---|---|---|
| | | **Porcentaje** | **Vol** | **Repos** |
| A | | 80 | 0,51612903 | 12,9032258 | 6,2 |
| B | | 30 | 0,19354839 | 4,83870968 | 6,2 |
| C | | 45 | 0,29032258 | 7,25806452 | 6,2 |
| | | 155 | | | 18,6 |
| | | | **Costo** | 55,8 |

b) (4 puntos) Si los costos de cada reposición son distintos para cada SKU, siendo: \$3 para SKU A, \$2 para SKU B y \$ 3 para SKU C. Plantee un modelo que permita determinar la asignación óptima para cada SKU

Se debe tomar el modelo de optimización y colocarle un costo de reposición distinto a cada SKU. El Cr es para cada SKU.

- Minimizar costo total:

$$Min \ \sum_i c_{r_i} f_i / v_i$$

Sujeto a

$$\sum_i v_i \le V$$
$$v_i \ge 0$$

**iv.** Usted tiene la siguiente información de un proceso en el cual se han tomado 16 muestras de 5 unidades cada una y se le ha determinado el promedio de la muestra y el recorrido.

| Muestra | Promedio | Recorrido | Muestra | Promedio | Recorrido |
|---|---|---|---|---|---|
| 1 | 31 | 3 | 9 | 33 | 1 |
| 2 | 32 | 1 | 10 | 33 | 1 |
| 3 | 34 | 1 | 11 | 34 | 3 |
| 4 | 31 | 6 | 12 | 33 | 4 |
| 5 | 34 | 3 | 13 | 34 | 7 |
| 6 | 33 | 5 | 14 | 35 | 6 |
| 7 | 31 | 4 | 15 | 31 | 2 |
| 8 | 29 | 3 | 16 | 31 | 3 |
| | | | **Promedio** | 32,4375 | 3,3125 |
| | | | **Suma** | 519 | 53 |

a) (5 Ptos) Determine el grafico de control de procesos, indicando los límites.

| Muestra | Promedio | Recorrido | Muestra | Promedio | Recorrido | | |
|---|---|---|---|---|---|---|---|
| 1 | 31 | 3 | 9 | 33 | 1 | | |
| 2 | 32 | 1 | 10 | 33 | 1 | | |
| 3 | 34 | 1 | 11 | 34 | 3 | | |
| 4 | 31 | 6 | 12 | 33 | 4 | | |
| 5 | 34 | 3 | 13 | 34 | 7 | | |
| 6 | 33 | 5 | 14 | 35 | 6 | | |
| 7 | 31 | 4 | 15 | 31 | 2 | | |
| 8 | 29 | 3 | 16 | 31 | 3 | | |
| | | | **Promedio** | 32,4375 | 3,3125 | **LCS X** | 34,3488125 |
| | | | **Suma** | 519 | 53 | **LCI X** | 30,5261875 |
| | | | | | | **LCS R** | 7,002625 |
| | | | | | | **LCI R** | 0 |

| Muestra | Promedio | Recorrido | Muestra | Promedio | Recorrido | | |
|---|---|---|---|---|---|---|---|
| 1 | 31 | 3 | 9 | 33 | 1 | | |
| 2 | 32 | 1 | 10 | 33 | 1 | | |
| 3 | 34 | 1 | 11 | 34 | 3 | | |
| 4 | 31 | 6 | 12 | 33 | 4 | | |
| 5 | 34 | 3 | 13 | 34 | 7 | | |
| 6 | 33 | 5 | 14 | | | | |
| 7 | 31 | 4 | 15 | 31 | 2 | | |
| 8 | | | 16 | 31 | 3 | | |
| | | | **Promedio** | 32,5 | 3,14285714 | **LCS X** | 34,3134286 |
| | | | **Suma** | | | **LCI X** | 30,6865714 |
| | | | | | | **LCS R** | 6,644 |
| | | | | | | **LCI R** | 0 |

| Muestra | Promedio | Recorrido | Muestra | Promedio | Recorrido | | |
|---|---|---|---|---|---|---|---|
| 1 | 31 | 3 | 9 | 33 | 1 | | |
| 2 | 32 | 1 | 10 | 33 | 1 | | |
| 3 | 34 | 1 | 11 | 34 | 3 | | |
| 4 | 31 | 6 | 12 | 33 | 4 | | |
| 5 | 34 | 3 | 13 | | | | |
| 6 | 33 | 5 | 14 | | | | |
| 7 | 31 | 4 | 15 | 31 | 2 | | |
| 8 | | | 16 | 31 | 3 | | |
| | | | **Promedio** | 32,3846154 | 2,84615385 | **LCS X** | 34,0268462 |
| | | | **Suma** | | | **LCI X** | 30,7423846 |
| | | | | | | **LCS R** | 6,01676923 |
| | | | | | | **LCI R** | 0 |

b) (2 Ptos) Se toma una muestra (de 5 unidades) que tiene un promedio de 30 y un recorrido de 7. ¿Qué puede decir del proceso?

El proceso no esta bajo control, la muestra se desvía en el recorrido. LCSR 6,02 y la muestra es 7.

c) (3 Ptos) Si el plan de control del proceso se estableció para que todo se encontrara dentro de $\pm$ 3 Sigma. ¿Cuál podría ser el mínimo LPTD que establezca el cliente de este proceso?

En la tabla 3 sigma corresponde a $(1 - 0.9987) = 0,0013$ con una cola. Es decir con dos colas $0.0026$ o $0.26\%$. Es decir el mínimo LPTD es 0.26%

**Tabla de distribución normal estándar**

| z | 0.00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
|---|---|---|---|---|---|---|---|---|---|---|
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
| **2.2** | .9861 | .9864 | .9868 | .9871 | .9875 | .9878 | .9881 | .9884 | .9887 | .9890 |
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

**Formulario**

$$Q_w = \sqrt{\frac{2 C_0 D}{C_h}}$$

$$CT = DC + \frac{D}{Q}S + \frac{Q}{2}H$$

$$R = d \cdot L$$

$$R = d \times L + z_\alpha \sigma \sqrt{L}$$

$$Q^* = d \times (T + L) + z_\alpha \sigma \sqrt{(T+L)} - I_{existente}$$

$$EF = ES + t$$

$$LS = LF - t$$

$$\mu = \frac{a + 4m + b}{6}$$

$$\sigma = \frac{b - a}{6}$$

$$C_x = \frac{\sum d_{ix} V_i}{\sum V_i}$$

$$C_y = \frac{\sum d_{iy} V_i}{\sum V_i}$$

$$Z = \frac{D - T_E}{\sqrt{\sum \sigma_i^2}}$$
