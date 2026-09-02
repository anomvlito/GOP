# Pauta Examen
## PAUTA
### ICS 3213 Gestión de Operaciones
**1er semestre 2023**

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

**Pregunta 1 (20 puntos)** Un almacén ha decidido sofisticar la forma que hace los pedidos. Para ello la dueña del almacén ha tomado varias decisiones que espera surtan efecto en reducir sus costos y mejorar la atención a sus clientes. 
Ahora, usted, como ingeniero(a) industrial experto(a) en gestión de operaciones, debe apoyarla y darle buenas recomendaciones en qué hacer. La primera acción que hace es mejorar la forma de gestión de los productos que compran a Carozzi. En particular, quiere gestionar los tallarines grado 1 en paquetes de 400 gramos. A continuación, está una tabla con las ventas semanales de las últimas 5 semanas de este producto.

| Semana | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ventas (unidades)** | 36 | 18 | 0 | 20 | 27 |

a) (7 ptos) Lo primero que ha hecho la dueña, es comenzar a usar métodos de estimación de demanda. En particular, para la semana 6 ha decidido usar medias móviles, pero no sabe si el tamaño de la ventana debería ser 2 o 3 semanas. ¿Cuál de las dos le recomendaría usted?
b) (6 ptos) Como vimos en clase, un pronóstico siempre debe venir asociado a un “para qué hacerlo”, es decir, a una finalidad. Conteste las siguientes preguntas con este objetivo en mente:
    i. ¿Está de acuerdo con los datos usados por el dueño del almacén para hacer el pronóstico de demanda? Preocúpese de justificar si el pronóstico obtenido logra o no el objetivo de la dueña del almacén.
    ii. La almacenera no sabe si su pronóstico es “bueno”. ¿Cuál(es) métrica(s) usted le recomendaría utilizar y por qué? Justifique su respuesta.
c) (7 ptos) Suponga que la estimación de demanda para la semana 6 resulta en 25 unidades y la dueña del almacén considera que se mantendrá constante semanalmente por las próximas 20 semanas. Comprar a Carozzi cada paquete cuesta \$580.
Considerando los costos de almacenar en la tienda, el costo financiero y las pérdidas por mermas, la dueña estima que el costo de mantener el inventario es un 7% del costo del producto por semana. Adicionalmente, cada vez que compra, entre el tiempo que gasta haciendo la compra y el costo de transporte, ella estima que gasta \$1,316 por compra y demora 2 semanas en llagar. ¿Cuántas unidades le recomienda a la dueña comprar cada vez de forma de asegurar de tener producto siempre y minimizar los costos de gestión del inventario?

**Pregunta 2 (20 puntos)** Usted trabaja en una empresa vitivinícola, en donde se han ganado un importante contrato que requiere ampliar su capacidad de producción de vinos embotellados para el próximo año.
Para poder asegurar la fecha del primer envío a este nuevo cliente (una vez que la planta ampliada esté operativa), usted decide contratar a una empresa de ingeniería, con tal de que le pueda presentar alternativas constructivas de ampliaciones de planta. La empresa de ingeniería le entrega un estudio que resume la secuencia más lógica de construcción, el escenario de sus duraciones (optimista, más probable, pesimista).

| Actividad | Antecesora | Tiempos (Semana)<br>Optimista | Más Probable | Pesimista |
| :---: | :---: | :---: | :---: | :---: |
| A | - | 1 | 2 | 3 |
| B | A | 4 | 5 | 12 |
| C | B | 5 | 6 | 7 |
| D | B | 1 | 1 | 1 |
| E | B,D | 1,5 | 3 | 4,5 |
| F | C,E | 2 | 2 | 2 |

a) (8 ptos) Elabore el diagrama de PERT y determine la ruta crítica del proyecto.
b) (8 ptos) Considerando que la construcción parte en un mes más, y en base a los antecedentes entregados por la empresa de ingeniería, en cuantos meses más, podría asegurarle el primer envío al nuevo cliente (Utilice un nivel de confianza del 95%)?
c) (4 ptos) Usted va a implementar el sistema del Ultimo Planificador en el proyecto y su cliente quiere estar despachando en la semana 15 con un 98% de confianza. ¿Cuál debería ser la máxima variabilidad permitida en el proyecto para poder cumplir con el cliente?

---

### Parte 1
**Pregunta 1**

**a.**
Para poder comparar ambos, se debe usar alguna medida de desempeño, como MSE o MAPE. En ambos casos, el mejor pronóstico histórico se obtiene con $n = 3$, que resulta en un MSE de 104.7; mientras el caso con $n = 2$ tiene un MSE de 379.7.

**b.1.**
El punto principal en esta argumentación debería ser que ventas no es lo mismo que demanda. En particular, en la semana 3 no hubo ventas, pero no sabemos si eso fue porque no hubo demanda o porque no había inventario disponible esa semana. Para poder hacer una estimación adecuada de demanda se deben corregir estos datos, y en particular revisar los niveles de inventario para los días con 0 venta. Si había inventario disponible podría ser una excelente forma de pronosticar demanda, pero si no había inventario estaremos subestimando el nivel de demanda futura.
Dado que el objetivo es no tener venta perdida, no corregir este factor sería un problema serio pensando en el objetivo del pronóstico.

**b.2.**
MSE es una excelente medida para ver qué tan bueno es un pronóstico, pero no nos identifica si estamos subestimado o sobreestimando en nuestro pronóstico. Dado que el objetivo en particular es no tener ventas perdidas, estamos más interesados en no subestimar que sobreestimar, o al menos nos interesa en forma importante si nuestro pronóstico está estimando sistemáticamente por encima o por debajo de la demanda real.
Una métrica de desempeño que nos permite ver esto es justamente el MFE, pues identifica si estamos constantemente por arriba o por abajo del valor de la variable. Por ello, esta métrica sería más deseable para el almacenero y el objetivo que tiene con su pronóstico.

**c.**
Dado que la demanda es constante y conocida, podemos usar el modelo de EOQ para calcular el tamaño del lote.
La demanda completa para el período de análisis es de $D = 500$. Por otro lado, el costo de mantener el inventario por una semana es $H = \$40.6$, mientras que el de hacer el pedido es $S = \$1,316$. Dado ello, el tamaño óptimo de la orden es $Q = 180$ unidades.

---

**Pregunta 2**

**Diagrama**
*(Diagrama PERT referencial: nodos del 1 al 6 unidos por las actividades A, B, C, D, E, F)*
`1 --(A)--> 2 --(B)--> 3 --(C)--> 5 --(F)--> 6`
`(B) también va hacia 4 vía (D), y de 4 a 5 vía (E)`

**Tiempos**

| Actividad | Antecesora | a | m | b | Mu | Sigma | Var |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | - | 1 | 2 | 3 | 2 | 0.33 | 0.111 |
| B | A | 4 | 5 | 12 | 6 | 1.33 | 1.778 |
| C | B | 5 | 6 | 7 | 6 | 0.33 | 0.111 |
| D | B | 1 | 1 | 1 | 1 | 0.00 | 0.000 |
| E | B,D | 1.5 | 3 | 4.5 | 3 | 0.50 | 0.250 |
| F | C,E | 2 | 2 | 2 | 2 | 0.00 | 0.000 |

La ruta critica es A-B-C-F el tiempo es 16 semanas.
La varianza es $= 0.111 + 1.778 + 0.111 = 2$

**Pregunta b**
Para un 95% de confianza es con una cola por lo que es $= 4 + 16 + 1.65 \times \sqrt{2} = 22.33$

**Pregunta c**
Dado que el tiempo de 15 es menor que el promedio, a ningún nivel de confianza es posible cumplir con el cliente.

---

**PARTE II: Responda todas las siguientes preguntas de ejercicio.**

**(20 puntos)** Usted es el Gerente de Logística y debe determinar el tamaño del nuevo centro de distribución de la empresa. Un problema que enfrenta es que la demanda es variable y debe tomar en cuenta esto para definir el tamaño. En una primera etapa usted captura la información de la llegada de las órdenes al centro, determinando que distribuye de forma general y en promedio las ordenes llegan en promedio cada 3 minutos con un coeficiente de variación de 0,4. 
a) (8 Ptos) Si la tasa de atención o capacidad de procesamiento promedio del centro tiene un coeficiente de variación de 0.2 y distribuye general. ¿Cuánto es lo máximo que se debe demorar en promedio pickear la orden, si los pedidos de los clientes no pueden estar en espera más de 1 hr en promedio en cola para pickeo? (HINT: suponga que el sistema se comparta como G/G/1)
b) (5 ptos) Suponga que decide dejar en 2,6 minutos el tiempo promedio en pickear una orden. Si usted quiere contratar a sólo 5 personas en el CD y el tamaño promedio de cada orden es de 1 caja, cada pallet tiene 40 cajas y la demanda promedio es de 5.000 pallets a la semana. ¿Cuál debería ser el tamaño óptimo (En términos de pallets) de la bodega para manejar el flujo? Suponga que cada trabajador dispone de 40 hrs. semanales.
c) (7 ptos) Si usted determina que puede reducir el tiempo ($\Delta$ en minutos) desde que el cliente coloca la orden hasta que recibe el producto y esto genera un beneficio monetario (B) para la organización con rendimientos decrecientes, el cual esta descrito por la ecuación $B(\Delta) = K e^{-\Delta}$ dónde K es una constante. Si el costo por almacenar un pallet adicional tiene un costo \$MT por pallet. ¿Plantee el problema de programación matemática u optimización que le permitiría obtener el tamaño óptimo de la bodega? Indique las variables de decisión, función objetivo y restricción(es).

**Respuesta a)**
Se debe utilizar la ecuación de Kingmann para solucionar.
$$CT_q = \left( \frac{C_a^2 + C_e^2}{2} \right) \left( \frac{\rho}{1 - \rho} \right) t_e$$
$$ \left( \frac{0.4^2 + 0.2^2}{2} \right) \left( \frac{\frac{t_e}{3}}{1 - \frac{t_e}{3}} \right) t_e = 60$$
$$ \frac{t_e^2}{3 - t_e} = 600$$
$$ t_e^2 + 600 t_e - 1800 = 0 $$
Se resuelve el polinomio para $t_e$ y se obtiene que la tasa de procesamiento debe ser mayor de 2,985 minutos en pickear cada orden.

**Respuesta b)**
Debemos determinar la capacidad de movimiento de la bodega. Dado que hay 5 trabajadores que trabajan 40 hrs a la semana, se dispone de 12.000 minutos de trabajador. Como cada orden debe demorar como máximo 2.6 minutos. Podemos mover 4.615 órdenes a la semana, como cada orden es de 1 caja y el pallet tiene 40 cajas, se dispone de una capacidad de mover 115.4 pallets a la semana.
Se utiliza la fórmula de flujo $q = A \times v$. Mi caudal que mover son 5.000 pallets y mi velocidad es de 115.4 pallets, por ende, el volumen es de 43.32 pallets o 44 pallets.

**Pregunta c)**
Las variables de decisión:
$t_n$: Tiempo nuevo de espera del cliente.
$BA$: Pallets adicionales en bodega

Función objetivo:
$$ \text{Max } K e^{-(60 - t_n)} - MT \times BA $$
S/A:
$$ \left( \frac{0.4^2 + 0.2^2}{2} \right) \left( \frac{\frac{t}{3}}{1 - \frac{t}{3}} \right) t = t_n $$
$$ t_n \le 60 $$
$$ 5.000 = (50 + BA) \times \left( \frac{5 \times 40 \times 60}{t} \times \frac{1}{40} \right) $$
$$ BA, t_n \ge 0 $$

---

**PII.b (20 puntos)** Usted está considerando convertirse en una franquicia de una cadena de cafeterías especializadas en café de alta calidad. La demanda mensual de café (Q) se relaciona con el precio al mercado del café (P) mediante la siguiente función de demanda: $P = 8 - 0.2Q$. Los costos variables relevantes incluyen el costo de los granos de café por taza y el costo del personal, considerando \$1.75 en costos de esto último. Actualmente, tiene dos opciones de franquicias que está evaluando:
**Opción 1: "Caffe Zanetti ":** La franquicia ofrece un contrato con una tarifa fija mensual de \$15 y suministra los granos de café a \$1.50 por taza. Además, te ofrece libertad para establecer tus precios de venta.
**Opción 2: "StarWorlds":** Esta franquicia no cobra una tarifa fija anual, pero vende los granos de café a \$1.75 por taza. Sin embargo, le obliga a vender cada taza de café a un precio máximo de \$4.

a) (8 ptos) ¿Cuál es el precio y cantidad que debe vender con la opción 1? ¿Cuál es la utilidad para la cafetería, la franquicia y la cadena completa?
b) (8 ptos) ¿Cuál es el precio y cantidad que debe vender con la opción 2? ¿Cuál es la utilidad para la cafetería, la franquicia y la cadena completa?
c) (4 ptos) ¿Qué opción de franquicia elegiría y por qué? (considere: maximizar sus ganancias)

**Pregunta a)**
Ingresos: $P \times Q = (8 - 0.2Q) \times Q$
Costos: $\$1.50$ (granos de café) $\times Q + \$1.75$ (costos de personal) $\times Q + 15$

Igualando los ingresos y los costos:
$$ (8 - 0.2Q) \times Q = 1.50Q + 1.75Q + 15 $$
$$ 8Q - 0.2Q^2 = 3.25Q + 15 $$
$$ 0.2Q^2 - 8Q + 3.25Q + 15 = 0 $$
$$ 0.2Q^2 - 4.75Q + 15 = 0 $$

Resolviendo la ecuación:
$$ Q = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
Esto nos da dos posibles soluciones:
$Q = 3.75$
$Q = 20$
La máxima cantidad de tazas de café que se venderían mensualmente es de 20 para que sea rentable. Sustituyendo este valor en la función de demanda:
$$ P = 8 - 0.22 \times 20 $$
$$ P = \$3.60 $$
Con la opción "Caffe Zanetti", el precio mínimo de venta de cada taza de café sería de \$3.60.

**Pregunta b)**
Ingresos: $P \times Q = (8 - 0.2Q) \times Q$
Costos: $\$1.75$ (granos de café) $\times Q + \$1.75$ (costos de personal) $\times Q$

Igualando los ingresos y los costos:
$$ (8 - 0.2Q) \times Q = 1.75Q + 1.75Q $$
$$ 8Q - 0.2Q^2 = 3.5Q $$
$$ 0.2Q^2 - 8Q + 3.5Q = 0 $$
$$ 0.2Q^2 - 4.5Q = 0 $$

Resolviendo la ecuación:
$$ Q = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
Esto nos da dos posibles soluciones:
$Q = 0$
$Q = 22.5$
La mínima cantidad de tazas de café que se venderían mensualmente es de 20 para que sea rentable. Sustituyendo este valor en la función de demanda:
$$ P = 8 - 0.22 \times 22.5 $$
$$ P = \$3.05 $$
Con la opción "StarWorlds", el precio mínimo de venta de cada taza de café sería de \$3.05.

**Pregunta c)**
**Zanetti:**
$$ P = 8 - 0.2Q $$
$$ Q = 40 - 5P $$
$$ \Pi = Q(P - C) $$
$$ \Pi_1 = (40 - 5P) (P - (C_c + C_p)) - C_f $$
$$ \Pi_1 = (40 - 5P)(P - (1.5 + 1.75)) - 15 $$
$$ \Pi_1 = 40P - 5P^2 - 130 + 16.25P - 15 $$
$$ \Pi_1 = 56.25P - 5P^2 - 145 $$
$$ \frac{d\Pi_1}{dP} = 56.25 - 10P = 0 $$
$$ P^* = 5.625 $$
$$ Q^* = 40 - 5(5.625) = 11.875 $$
$$ \Pi_1 = 11.875(5.625 - 3.25) - 15 = 13.2 $$

**StarWorlds:**
$$ P = 8 - 0.2Q $$
$$ Q = 40 - 5P $$
$$ \Pi = Q(P - C) $$
$$ \Pi_2 = (40 - 5P) (P - (C_c + C_p)) $$
$$ \Pi_2 = (40 - 5P)(P - (1.75 + 1.75)) $$
$$ \Pi_2 = (40 - 5P)(P - 3.5) = 40P - 140 - 5P^2 + 17.5P $$
$$ \Pi_2 = 57.5P - 5P^2 - 140 $$
$$ \frac{d\Pi_2}{dP} = 57.5 - 10P = 0 $$
$$ P^* = 5.75 $$
Pero no se puede vender a ese precio, es máximo \$4.
$$ P = 4 $$
$$ Q = 40 - 5(4) = 20 $$
$$ \Pi_2 = 20(4 - 3.5) = 10 $$
Es mejor la opción 1.

---

### Formulario

**Tabla de distribución normal estándar**
$$P(Z \le z) = \int_{-\infty}^{z} f(t) dt$$

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
| **3.0** | .9987 | .9987 | .9987 | .9988 | .9988 | .9989 | .9989 | .9990 | .9990 |
| **3.1** | .9990 | .9991 | .9991 | .9991 | .9992 | .9992 | .9992 | .9993 | .9993 |
| **3.2** | .9993 | .9993 | .9994 | .9994 | .9994 | .9994 | .9994 | .9995 | .9995 | .9995 |
| **3.3** | .9995 | .9995 | .9995 | .9996 | .9996 | .9996 | .9996 | .9996 | .9996 | .9997 |
| **3.4** | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9998 |

**Fórmulas Varias (Gestión de Operaciones)**

$$ CT = DC + \frac{D}{Q} S + \frac{Q}{2} H $$
$$ Q_{eoq} = \sqrt{\frac{2 \times D \times S}{H}} $$
$$ R = d \times L $$
$$ R = d \times L + z_{\alpha} \sigma \sqrt{L} $$
$$ Q^* = F^{-1} \left( \frac{C_u}{C_o + C_u} \right) $$
$$ EF = ES + t $$
$$ LS = LF - t $$
$$ \mu = \frac{a + 4m + b}{6} $$
$$ \sigma = \frac{b - a}{6} $$
$$ Z = \frac{D - T_E}{\sqrt{\sum \sigma_i^2}} $$
$$ Q^* = d \times (T + L) + z_{\alpha} \sigma \sqrt{(T + L)} - I_{\text{existente}} $$
$$ I = T_p \times (p - d) $$
$$ Q = T_p \times p \implies T_p = \frac{Q}{p} $$
$$ ef = \frac{k}{k + 1} $$
$$ P = \sqrt{\left(\frac{a}{2}\right) \left(\frac{q}{z}\right)} \quad P = \sqrt{\left(\frac{a}{2}\right) \left(\frac{1}{n}\right) \left(\sum_{i=1}^{n} \frac{q_i}{z_i}\right)} $$
$$ Ben = s p_i - c_r d_i \quad Ben = s(p_i + D_i) $$
$$ Beneficio_{\min\_A} = \frac{s * p_i - c_r * d_i}{l_i} $$
$$ Restocks = \frac{f_i}{V_i} \quad \text{Restocks/tiempo} $$
$$ Beneficio_{\text{adic\_A}} = \frac{s * D_i + c_r * d_i}{u_i - l_i} $$
$$ \text{Costo Total} = \text{Costo Fijo} + \text{Costo Variable} \times \text{Volumen} $$
$$ v_i^* = \left( \frac{\sqrt{f_i}}{\sum_{j=1}^{n} \sqrt{f_j}} \right) V \sqrt{\frac{p_i}{f_i}} $$
$$ C_x = \frac{\sum d_{ix} V_i}{\sum V_i} \quad C_y = \frac{\sum d_{iy} V_i}{\sum V_i} $$
$$ \rho = \frac{\lambda}{\mu} \quad \rho = \frac{\lambda}{c \mu} $$
$$ L = \lambda \times W $$
$$ c_T = \frac{\sigma}{t} = \frac{\sqrt{Var(T)}}{E(T)} $$
$$ L = \frac{\rho}{1 - \rho} \quad W = \frac{1}{\mu(1 - \rho)} $$
$$ L_q = \frac{\rho^2}{1 - \rho} \quad W_q = \frac{\rho}{\mu(1 - \rho)} $$
$$ WIP = TH \times TC \quad L = \lambda * W $$
$$ A = \frac{m_f}{m_r + m_f} \quad t_e = \frac{t_o}{A} $$
$$ \sigma^2_e = \left(\frac{\sigma^2_o}{A}\right) + \frac{(m_r + \sigma^2_r)(1 - A)t_o}{A m_r} $$
$$ c^2_e = \frac{\sigma^2_e}{t_e^2} = c^2_o + (1 + c^2_r) A(1 - A) \frac{m_r}{t_o} $$
$$ t_e = t_o + \frac{t_s}{N_s} \quad \sigma^2_e = \sigma^2_o + \frac{\sigma^2_s}{N_s} + \frac{N_s - 1}{N_s^2} t^2_s \quad c^2_e = \frac{\sigma^2_e}{t_e^2} $$
$$ (c_S)^2 \approx \rho^2 (c_e)^2 + (1 - \rho^2)(c_a)^2 $$
$$ CT_q = \left( \frac{C_a^2 + C_e^2}{2} \right) \left( \frac{\rho}{1 - \rho} \right) t_e $$
$$ L = \frac{\rho}{1 - \rho} - \frac{(b+1)\rho^{b+1}}{1 - \rho^{b+1}} $$
$$ \lambda' = \lambda \left( \frac{1 - \rho^b}{1 - \rho^{b+1}} \right) $$
$$ L_q = \frac{\rho}{1 - \rho} \times Prob(N > c) $$
$$ W_q = \frac{\rho}{\lambda(1 - \rho)} \times Prob(N > c) $$
$$ F_t = w_1 A_{t-1} + w_2 A_{t-2} + w_3 A_{t-3} + \dots + w_n A_{t-n} $$
$$ F_{t+1} = \alpha A_t + (1 - \alpha) F_t $$
$$ \hat{y} = a + bx $$
$$ \sum_{1}^{n} w_n = 1 $$
$$ T(t, t-1) = A_t - A_{t-1} $$
$$ T = \frac{\sum_{i=1}^{n} T(t-i, t-i-1)}{n} $$
$$ TS_k = \frac{\sum_{t=1}^{k} e_t}{MAD_k} $$
$$ F_t = \frac{A_{t-1} + A_{t-2} + A_{t-3} + \dots + A_{t-n}}{n} $$
$$ e_t = F_t - A_t $$
$$ \sigma = 1.25 * MAD $$
$$ MAD_k = \frac{1}{k} \sum_{t=1}^{k} |e_t| $$
$$ FIT_t = F_t + T_t \quad (\text{Pronóstico} + \text{Tendencia}) $$
$$ F_t = FIT_{t-1} + \alpha(A_{t-1} - FIT_{t-1}) $$
$$ T_t = T_{t-1} + \alpha \delta (A_{t-1} - FIT_{t-1}) $$
$$ L = t_k + t_p + t_v $$
$$ b = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2} $$
$$ a = \frac{\sum y}{n} - b \frac{\sum x}{n} = \bar{y} - b \bar{x} $$
$$ LCS = \bar{x} + Z * \sigma $$
$$ LCI = \bar{x} - Z * \sigma $$
$$ N = \frac{D \times L}{C} (1 + \varepsilon) \quad N = \frac{D \times L}{C} $$
$$ p_0 \pm 3 \sqrt{\frac{p_0(1 - p_0)}{n}} $$
$$ C_p = \frac{USL - LSL}{6\sigma} $$
$$ LCS \; \bar{X} = \bar{\bar{X}} + A_2 * \bar{R} $$
$$ LCI \; \bar{X} = \bar{\bar{X}} - A_2 * \bar{R} $$
$$ LCS \; R = D_4 * \bar{R} $$
$$ LCI \; R = D_3 * \bar{R} $$
$$ C_{pk} = \frac{USL - Media}{3\sigma} \quad C_{pk} = \frac{Media - LSL}{3\sigma} $$

**Tablas de Control de Calidad**

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

| Tamaño Muestra | $A_2$ | $d_2$ | $D_3$ | $D_4$ |
| :---: | :---: | :---: | :---: | :---: |
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
