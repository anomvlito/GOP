# Examen ICS 3213 Gestión de Operaciones
**Sección 1 y Sección 2 – 2º semestre 2015**
**Prof. Alejandro Mac Cawley**
**Prof. Fernando Tagle**

Nombre: ___________________________________ 
Sección: ① Secc. F. Tagle ② Secc. A. Mac Cawley
Número Lista: ________

Pontificia Universidad Católica de Chile  
Escuela de Ingeniería  
Departamento de Ingeniería Industrial y de Sistemas  

## Instrucciones:
* Poner nombre y número a todas y cada una de las hojas del cuadernillo.
* No descorchetear el cuadernillo en ningún momento durante la prueba.
* La prueba consta de 4 secciones. Debe contestar cada una de las preguntas en el espacio asignado.
* No se permiten resúmenes de clases, ni de casos, ni formularios.
* Se descontará 10 puntos por no cumplir alguna de estas instrucciones.
* La prueba tiene **120 y dura 120 minutos**.
* No se pueden utilizar laptops ni celulares.
* Se leerá la prueba al comienzo de clases y después se permitirán preguntas en voz alta. Posteriormente en la mitad de la prueba se volverá a permitir preguntas en voz alta. No se permitirán preguntas fuera de estos intervalos. Si su duda persiste indique el supuesto y continúe.
* Este curso adscribe el Código de Honor establecido por la Escuela de Ingeniería el que es vinculante. Todo trabajo evaluado en este curso debe ser propio. En caso de que exista colaboración permitida con otros estudiantes, el trabajo deberá referenciar y atribuir correctamente dicha contribución a quien corresponda. Como estudiante es su deber conocer la versión en línea del Código de Honor (http://ing.puc.cl/codigodehonor).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Firma Alumno

¡Muy Buena Suerte!

---

## PARTE I. (20 puntos) Sección verdadero o falso.
Indique si las siguientes afirmaciones son verdaderas (V) o falsas (F). En caso de ser falsas, indique la razón.

1. El modelo Six Sigma se enfoca principalmente en la mejora de la calidad de los procesos y en el control de los insumos.
2. En calidad de servicios, el sistema de brechas intenta comparar las expectativas que tiene la empresa de su servicio versus el que en realidad es capaz de entregar.
3. El control estadístico de procesos (SPC) se basa en controlar el valor de la variable del proceso en torno al promedio.
4. Para una empresa que produce un gran número de bienes es mejor una estrategia orientada al proceso.
5. El suavizamiento exponencial es un modelo de pronóstico que incluye solo la información del periodo anterior.
6. El modelo de inventario de EOQ tiene la ventaja de que el cometer grandes equivocaciones en los parámetros no tiene gran efecto en los costos totales.
7. En planificación de la producción se dan situaciones en donde es conveniente utilizar sub-óptimas con el objetivo de entregar robustez a la planificación.
8. En la administración de proyectos siempre será conveniente el disminuir el tiempo de las actividades.
9. En el caso Zara se aprendió que para disminuir el efecto látigo dentro de una cadena de suministro basta con integrar la información y centralizar la decisión de cuanto producir.
10. Un Cross Dock es un buen sistema de bodega, ya que minimiza el inventario.

---

## PARTE II (15 puntos)
**Responda cada una de las siguientes preguntas relacionadas con el libro "La Meta".**

El gerente de una fábrica le pide su ayuda con respecto a la gestión de sus procesos productivos. El proceso en cuestión, corresponde a 3 etapas que funcionan como una línea de producción serie donde se le realizan operaciones de trasformación al producto. El gerente se leyó un resumen del libro "La Meta" en donde se habla del cuello de botella y detecto que la tercera etapa del proceso es el cuello de botella. Como se debe asociar la entrada de material al cuello de botella, siempre se mantiene inventario disponible mediante un buffer antes de la primera etapa. Además, se trabaja 24 horas al día mediante 3 turnos de 8 horas, sin embargo, en los cambios de turno se detiene la producción durante. Finalmente, para evitar problemas de calidad, existe un control al final del proceso. Usted que se leyó el libro completo y no el resumen, explique:

a) Cómo y por qué se podría aumentar el throughput del proceso.
b) Si pudiera mover el control de calidad dentro del proceso, ¿Dónde lo pondría?

La segunda etapa del proceso depende principalmente del trabajo de obreros, mientras que la tercera se encuentra casi totalmente automatizada, la variabilidad de la segunda etapa es del doble que la de la tercera.

c) ¿Qué problemas puede causar este factor en la productividad de la planta? Refiérase a ejemplos del libro para explicar más claramente.

**(Diagrama visualizado: Inventario -> Etapa 1 -> Etapa 2 -> Etapa 3)**

**Pauta de Corrección:**
* **a)** Posibles alternativas pueden ser reducir los tiempos muertos provocados por el cambio de turno, asegurarse que el CB este siempre ocupado, aumentar la capacidad del CB, externalizar parte del trabajo que realiza el CB, etc. *(2 ptos por idea, 4 ptos máximo)*.
* **b)** Pondría el control de calidad antes del CB, porque los productos que no pasaron el control de calidad si pasaron por el CB, generaron perdidas en todo el sistema *(5 ptos)*.
* **c)** Esto podría provocar que el cuello de botella no reciba la materia prima necesaria a tiempo y ya que trabaja a toda su capacidad no logra recuperar el tiempo perdido cuando recibe los insumos más adelante *(4 pts)*. Un ejemplo podría ser el juego de Alex con los scouts y los fósforos o como el aumento de la productividad de los trabajadores no permitió que se completara el lote, debido a su irregularidad. *(2 ptos por poner un ejemplo)*.

---

## PARTE IV (85 Puntos): Ejercicios.
**Responda las siguientes 2 Preguntas**

### I. (35 Puntos)
Usted se encuentra a cargo del proceso de producción de una gran empresa productora de galletas. Su producto estrella son la galletas de arándanos y para la producción de estas galletas se requiere de la masa base y los arándanos. A continuación se detalla el proceso:

*(Diagrama de flujo)*
* Arándanos Frescos -> Secado -> Molido -> Mezclado -> Cocido -> Control Calidad
* Secado -> Azucarado -> Control Calidad -> Mezclado
* Masa Base -> Amasado -> Mezclado

Los arándanos frescos llegan de los proveedores y son sometidos a un proceso de secado, con una capacidad de 300 kg/hr. Posteriormente el 80% de los arándanos va a un proceso de molido, con una capacidad de 280 kg/hr, en donde se transforma en polvo de arándano. El restante 20% de los arándanos secos sigue a un proceso de azucarado, con una capacidad de 65 kg/hr, en donde se les coloca una capa de azúcar y posteriormente se controla la calidad y un 10% de los arándanos azucarados debe ser desechado por no cumplir con el standard de calidad. Por otro lado, la masa base pasa a la máquina de amasado, con una capacidad de 600 kg/hr. Posteriormente la masa base pasa junto a los arándanos azucarados y el polvo de arándano a la mezcladora, que tiene una capacidad de 800 kg/hr, posteriormente la mezcla pasa al cocido que tiene una capacidad de 850 kg/hr para finalmente someterse a un control de calidad, en donde el 3% no cumple el estándar y debe ser desechado.

a) (10 ptos) Cuál es la máxima capacidad productiva del proceso en términos de kilogramos de galletas por hora.
b) (2 ptos) Si el proceso funciona a 1 turno de 8 hrs. al día por 240 días al año. ¿Qué cantidad anual de arándanos frescos y masa base debe comprar?
c) (5 ptos) Si usted puede duplicar la capacidad productiva de solo 2 máquinas en el proceso. ¿Qué dos máquinas duplicaría? ¿Cuál sería la capacidad productiva nueva?

La empresa tiene dificultades para estimar la cantidad de envases que debe solicitar a su proveedor para almacenar sus galletas. De acuerdo a la información registrada en los últimos 6 meses, se estima que la demanda promedio es de 50.000 unidades. Además, suponga que el costo de inventario es de \$1,5 unidad/mes, el costo por unidad es de 60 pesos, el costo de la orden es de \$90.000 y el proveedor se demora 1 semana en entregar el pedido. Considerando una varianza de 2.500 con un nivel de servicio de 95% para no tener problemas con los minoristas. Calcule el pedido óptimo de envases para el próximo mes. Considere que tiene una política de periodo fijo de 1 mes y los pedidos llegan siempre antes de que comience el mes para el cual se requieren.

d) (4 ptos) ¿Cuál es la cantidad óptima de pedido y las fechas en que debe ordenar?
e) (4 ptos) Si ahora se considera una política de revisión continua. ¿Cuál sería la nueva cantidad óptima de pedido y el punto de re orden?
f) (5 ptos) El proveedor le ofrece firmar un contrato para asegurar la provisión de envases para los próximos 3 meses. Usted estima que las cantidades de envases para los próximos 3 meses serían 49.000, 53.000 y 47.000 respectivamente. ¿Cuál es la cantidad óptima de pedido mensuales y en qué meses ordenaría? (Hint: Utilice método Wagner-Whitin)
g) (5 ptos) Calcule el costo de inventario de los 3 sistemas. Si el proveedor le cobra un costo fijo por el contrato ¿Cuánto seria lo máximo que estaría dispuesto a pagar?

**Pauta de Corrección (Respuestas a la Pregunta 1):** 

**a)** Se utiliza el método de demanda variable en el tiempo con revisión periódica, ya que existe variabilidad y se tienen los tiempos $T$ (1 mes) y $L$ (1 semana). Para calcular la cantidad óptima:
$$Q^* = \bar{D} \cdot (T+L) + z \cdot \sigma_D \cdot \sqrt{T+L} - I \approx 67.100$$
Considerando $z = 1,645$; $T+L = 1,25$ y el inventario existente igual a cero.
Es de plazo fijo así que debe ordenarse una vez al mes, una semana previa a que termine el mes, así llegan justo a comienzos de mes y no se incurre en gastos de inventario adicionales.

**b)** Para una política de revisión continua, se considera el modelo EOQ:
$$Q^* = \sqrt{\frac{2 \cdot \bar{D} \cdot S}{H}} \approx 77.460$$
El punto de re orden:
$$R = \bar{D} \cdot L + z \cdot \sigma_D \cdot \sqrt{L} \approx 14.560$$

**c)** Dado que se conoce la demanda exacta, se sabe cuándo pedir para cada mes. Ahora se tiene que buscar la política más económica para hacerlo. Utilizando Wagner-Within, se tiene:

* **Opción 1:** Comprar mensualmente.
  * Costo por orden: $3 \times 90.000 = 270.000$
  * Costo por inventario: $1,5 \times (49.000+53.000+47.000)/2 = 111.750$
  * Costo por productos: $60 \times (49.000+53.000+47.000) = 8.940.000$
  * CT = \$ 9.321.750

* **Opción 2:** Comprar todo el primer mes.
  * Costo por orden: $1 \times 90.000 = 90.000$
  * Costo por inventario: $1,5 \times (49.000+53.000+47.000)/2 + 1,5 \times (53.000+2 \times 47.000) = 332.250$
  * Costo por productos: $60 \times (49.000+53.000+47.000) = 8.940.000$
  * CT = \$ 9.272.250

* **Opción 3:** Comprar el primer mes también los del segundo y aparte el tercero.
  * Costo por orden: $2 \times 90.000 = 180.000$
  * Costo por inventario: $1,5 \times (49.000+53.000+47.000)/2 + 1,5 \times 53.000 = 191.250$
  * Costo por productos: $60 \times (49.000+53.000+47.000) = 8.940.000$
  * CT = \$ 9.311.250

* **Opción 4:** Comprar para el primer mes y después todo junto para los siguientes.
  * Costo por orden: $2 \times 90.000 = 180.000$
  * Costo por inventario: $1,5 \times (49.000+53.000+47.000)/2 + 1,5 \times 47.000 = 182.250$
  * Costo por productos: $60 \times (49.000+53.000+47.000) = 8.940.000$
  * CT = \$ 9.302.250

La mejor opción es comprar todo el primer mes ya que el costo de orden es muy elevado.

---

### Pregunta 2.- (25 Puntos)
Usted es dueño de una local que vende diarios que tiene 1 sola caja para atender a sus clientes. Considere que los clientes llegan con una distribución Poisson con tasa de llegada de $\lambda$ [clientes/min]. Los clientes son atendidos a una tasa $\mu$ [clientes/min] que sigue una distribución exponencial.

Usted se encuentra muy preocupado por el servicio al cliente y determina que existe un costo por el tiempo que espera de los clientes en la cola de $C_q$ [\$/min] peso por minuto en la cola. Por otro lado, es posible aumentar la tasa de atención de clientes de la caja a un costo $C_k$ [\$/clientes/min] lo que claramente aumentaría el nivel de servicio de la heladería.

a) (10 Ptos) Desarrolle el modelo de programación matemática que debiera resolver el gerente de la heladería para resolver su problema. (Hint: Determine la variable de decisión y plantee la función objetivo)
b) (10 ptos) Resuelva el problema anterior y plantee la forma funcional que me permita obtener el óptimo.
c) (5 ptos) Suponga que desea establecer un tiempo promedio máximo de espera de sus clientes de $T_m$ minutos en la fila. Plantee el problema de programación matemática que le permite resolver este problema y cómo resolvería este problema.

**Pauta de Corrección (Respuestas a la Pregunta 2):**
Reordenando, tenemos: 
*(Sección en blanco en la pauta oficial).*

---

### Pregunta 3.- (25 Puntos)
La empresa Tarjetas ABC desea establecer un plan de producción JIT. La demanda diaria registrada es de 200 tarjetas telefónicas por hora. El proceso de producción de estas tarjetas pasa por 3 grandes operaciones antes del control de calidad ubicado al final de la línea: impresión de las leyendas (P1), la inclusión del chip (P2) y cortado de la tarjeta (P3).

Para una mejor compresión del problema se tiene el siguiente diagrama:
*(P1 -> P2 -> P3 -> Control de calidad)*

La empresa cuenta con un registro de los tiempos promedios de procesamiento ($t_{pi}$) por operación, además de los tiempos de envío de los Kanbans ($t_{ki}$) y tiempos de envío de los lotes ($t_{vi}$).

| Operación | Lote (C) | $t_{pi}$ (seg) | $t_{ki}$ (seg) | $t_{vi}$ (seg) |
| --- | --- | --- | --- | --- |
| P1 | 200 | 85 | 45 | 200 |
| P2 | 250 | 78 | 67 | 300 |
| P3 | 300 | 50 | 92 | 150 |

Por su parte, los registros históricos del control de calidad indican que en promedio un 15% de las unidades son descartadas.

a) (10 ptos) A partir de los datos anteriores, calcule el número de Kanbans necesarios en el proceso productivo.

Las investigaciones de la empresa han determinado que el proceso P3 es el que está actualmente generando el 15% del descarte de las tarjetas, las cuales no están saliendo con los tamaños adecuados. Se realizó un muestreo del largo de las tarjetas de 5 lotes recibidos durante los últimos 5 días. Los resultados se muestran a continuación:

| Día | \multicolumn{5}{c|}{Largo (milímetros)} |
| --- | --- | --- | --- | --- | --- |
| 1 | 70 | 56 | 49 | 67 | 61 |
| 2 | 65 | 47 | 70 | 70 | 68 |
| 3 | 70 | 49 | 42 | 68 | 54 |
| 4 | 50 | 47 | 52 | 67 | 50 |
| 5 | 48 | 65 | 51 | 50 | 65 |

A partir de lo anterior:
b) (8 ptos) Calcule los límites de control, eliminando los outliers. Realice los gráficos correspondientes.
c) (2 puntos) Si el día 6 usted toma una muestra con los siguientes resultados: 63, 54, 43, 69 y 65. ¿Qué puede decir de la muestra? ¿Está el proceso bajo control?
d) (5 ptos.) El implementar el control, reduce las fallas del sistema a solo un 5%. Con esta información ¿cambia el número Kanbans? Argumente.

**Pauta de Corrección (Respuestas a la Pregunta 3):**

**a)** Calculamos $L$ para cada proceso, como la suma de los tiempos:
$L_1 = 330$
$L_2 = 445$
$L_3 = 292$

Luego calculamos el Kanban para cada proceso como $N = \frac{D}{1 - 0,15} \cdot \frac{L}{C}$:
$N_1 = 389$
$N_2 = 419$
$N_3 = 230$

**b)** Calculamos los promedios y los rangos.
Luego, de la tabla obtenemos:
$A_2 = 0,58$
$D_3 = 0$
$D_4 = 2,11$

$LCS_R = D_4 \cdot \bar{R} = 68,3$
$LCS_{\bar{X}} = \bar{\bar{X}} + A_2 \cdot \bar{R} = 77,6$
$LCI_R = D_3 \cdot \bar{R} = 0$
$LCI_{\bar{X}} = \bar{\bar{X}} - A_2 \cdot \bar{R} = 40$

Vemos que hay números fuera de los rangos y los borramos:
El nuevo promedio de estos datos es 58,8 y el rango es 24,6.
Por ende ahora:
$LCS_R = D_4 \cdot \bar{R} = 51,9$
$LCI_R = D_3 \cdot \bar{R} = 0$

**d)** El rango de la muestra 6, tiene un rango de 54, por lo que no se acepta el lote porque está fuera del límite.

**e)** Si cambia, porque ahora cambia la demanda sería solo $2000 / 0,95$.
Luego calculamos el Kanban para cada proceso como $N = \frac{D}{0,95} \cdot \frac{L}{C}$:
$N_1 = 348$
$N_2 = 375$
$N_3 = 205$

---

## Formulario Adjunto y Tablas

### Tabla de distribución normal estándar
| z | 0.00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0 | .5000 | .5040 | .5080 | .5120 | .5160 | .5199 | .5239 | .5279 | .5319 | .5359 |
| 0.1 | .5398 | .5438 | .5478 | .5517 | .5557 | .5596 | .5636 | .5675 | .5714 | .5753 |
| 0.2 | .5793 | .5832 | .5871 | .5910 | .5948 | .5987 | .6026 | .6064 | .6103 | .6141 |
| 0.3 | .6179 | .6217 | .6255 | .6293 | .6331 | .6368 | .6406 | .6443 | .6480 | .6517 |
| 0.4 | .6554 | .6591 | .6628 | .6664 | .6700 | .6736 | .6772 | .6808 | .6844 | .6879 |
| 0.5 | .6915 | .6950 | .6985 | .7019 | .7054 | .7088 | .7123 | .7157 | .7190 | .7224 |
| 0.6 | .7257 | .7291 | .7324 | .7357 | .7389 | .7422 | .7454 | .7486 | .7517 | .7549 |
| 0.7 | .7580 | .7611 | .7642 | .7673 | .7704 | .7734 | .7764 | .7794 | .7823 | .7852 |
| 0.8 | .7881 | .7910 | .7939 | .7967 | .7995 | .8023 | .8051 | .8078 | .8106 | .8133 |
| 0.9 | .8159 | .8186 | .8212 | .8238 | .8264 | .8289 | .8315 | .8340 | .8365 | .8389 |
| 1.0 | .8413 | .8438 | .8461 | .8485 | .8508 | .8531 | .8554 | .8577 | .8599 | .8621 |
| 1.1 | .8643 | .8665 | .8686 | .8708 | .8729 | .8749 | .8770 | .8790 | .8810 | .8830 |
| 1.2 | .8849 | .8869 | .8888 | .8907 | .8925 | .8944 | .8962 | .8980 | .8997 | .9015 |
| 1.3 | .9032 | .9049 | .9066 | .9082 | .9099 | .9115 | .9131 | .9147 | .9162 | .9177 |
| 1.4 | .9192 | .9207 | .9222 | .9236 | .9251 | .9265 | .9279 | .9292 | .9306 | .9319 |
| 1.5 | .9332 | .9345 | .9357 | .9370 | .9382 | .9394 | .9406 | .9418 | .9429 | .9441 |
| 1.6 | .9452 | .9463 | .9474 | .9484 | .9495 | .9505 | .9515 | .9525 | .9535 | .9545 |
| 1.7 | .9554 | .9564 | .9573 | .9582 | .9591 | .9599 | .9608 | .9616 | .9625 | .9633 |
| 1.8 | .9641 | .9649 | .9656 | .9664 | .9671 | .9678 | .9686 | .9693 | .9699 | .9706 |
| 1.9 | .9713 | .9719 | .9726 | .9732 | .9738 | .9744 | .9750 | .9756 | .9761 | .9767 |
| 2.0 | .9772 | .9778 | .9783 | .9788 | .9793 | .9798 | .9803 | .9808 | .9812 | .9817 |
| 2.1 | .9821 | .9826 | .9830 | .9834 | .9838 | .9842 | .9846 | .9850 | .9854 | .9857 |
| 2.2 | .9861 | .9864 | .9868 | .9871 | .9875 | .9878 | .9881 | .9884 | .9887 | .9890 |
| 2.3 | .9893 | .9896 | .9898 | .9901 | .9904 | .9906 | .9909 | .9911 | .9913 | .9916 |
| 2.4 | .9918 | .9920 | .9922 | .9925 | .9927 | .9929 | .9931 | .9932 | .9934 | .9936 |
| 2.5 | .9938 | .9940 | .9941 | .9943 | .9945 | .9946 | .9948 | .9949 | .9951 | .9952 |
| 2.6 | .9953 | .9955 | .9956 | .9957 | .9959 | .9960 | .9961 | .9962 | .9963 | .9964 |
| 2.7 | .9965 | .9966 | .9967 | .9968 | .9969 | .9970 | .9971 | .9972 | .9973 | .9974 |
| 2.8 | .9974 | .9975 | .9976 | .9977 | .9977 | .9978 | .9979 | .9979 | .9980 | .9981 |
| 2.9 | .9981 | .9982 | .9982 | .9983 | .9984 | .9984 | .9985 | .9985 | .9986 | .9986 |
| 3.0 | .9987 | .9987 | .9987 | .9988 | .9988 | .9989 | .9989 | .9989 | .9990 | .9990 |
| 3.1 | .9990 | .9991 | .9991 | .9991 | .9992 | .9992 | .9992 | .9992 | .9993 | .9993 |
| 3.2 | .9993 | .9993 | .9994 | .9994 | .9994 | .9994 | .9994 | .9995 | .9995 | .9995 |
| 3.3 | .9995 | .9995 | .9995 | .9996 | .9996 | .9996 | .9996 | .9996 | .9996 | .9997 |
| 3.4 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9998 |

### Formulario

$$CT = DC + \frac{D}{Q}S + \frac{Q}{2}H$$
$$Q_{eoq} = \sqrt{\frac{2 \times D \times S}{H}}$$
$$R = d \times L$$
$$R = d \times L + z_{\alpha} \sigma \sqrt{L}$$
$$Q^* = d \times (T+L) + z_{\alpha}\sigma \sqrt{(T+L)} - I_{existente}$$
$$I = T_p \times (p - d)$$
$$Q^* = F^{-1} \left( \frac{C_u}{C_o + C_u} \right)$$
$$EF = ES + t$$
$$LS = LF - t$$
$$\mu = \frac{a + 4m + b}{6}$$
$$\sigma = \frac{b - a}{6}$$
$$Z = \frac{D - T_E}{\sqrt{\sum \sigma_i^2}}$$
$$Q = T_p \times p$$
$$T_p = \frac{Q}{p}$$

$$P = \sqrt{\left(\frac{a}{2}\right) \left(\frac{q}{z}\right)}$$
$$P = \sqrt{\left(\frac{a}{2}\right) \left(\frac{1}{n}\right) \left( \sum_{i=1}^n \frac{q_i}{z_i} \right)}$$
$$ef = \frac{k}{k+1}$$
$$Ben = s \cdot p_i - c_r \cdot d_i$$
$$Ben = s(p_i + D_i)$$
$$Beneficio_{min\_A} = \frac{s \cdot p_i - c_r \cdot d_i}{l_i}$$
$$Restocks = \frac{f_i}{V_i}$$
$$Restocks/tiempo$$
$$Beneficio_{adic\_A} = \frac{s \cdot D_i + c_r \cdot d_i}{u_i - l_i}$$
$$\text{Costo Total} = \text{Costo Fijo} + \text{Costo Variable} \times \text{Volumen}$$
$$v_i^* = \left( \frac{\sqrt{f_i}}{\sum_{j=1}^n \sqrt{f_j}} \right) V \frac{p_i}{\sqrt{f_i}}$$
$$C_x = \frac{\sum d_{ix} V_i}{\sum V_i}$$
$$C_y = \frac{\sum d_{iy} V_i}{\sum V_i}$$
$$\rho = \frac{\lambda}{\mu}$$
$$\rho = \frac{\lambda}{c\mu}$$
$$L = \lambda \times W$$
$$c_T = \frac{\sigma}{t} = \frac{\sqrt{Var(T)}}{E(T)}$$
$$L = \frac{\rho}{1 - \rho}$$
$$W = \frac{1}{\mu(1 - \rho)}$$
$$L_q = \frac{\rho^2}{1 - \rho}$$
$$W_q = \frac{\rho}{\mu(1 - \rho)}$$
$$WIP = TH \times TC$$
$$L = \lambda * W$$
$$A = \frac{m_f}{m_r + m_f}$$
$$t_e = \frac{t_o}{A}$$
$$\sigma_e^2 = \left( \frac{\sigma_o^2}{A} \right) + \frac{(m_r + \sigma^2_r)(1 - A)t_o}{A m_r}$$
$$c_e^2 = \frac{\sigma_e^2}{t_e^2} = c_o^2 + (1 + c_r^2)A(1 - A)\frac{m_r}{t_o}$$
$$t_e = t_o + \frac{t_s}{N_s}$$
$$\sigma_e^2 = \sigma_o^2 + \frac{\sigma_s^2}{N_s} + \frac{N_s - 1}{N_s^2} t_s^2$$
$$c_e^2 = \frac{\sigma_e^2}{t_e^2}$$
$$(c_S)^2 \approx \rho^2(c_e)^2 + (1 - \rho^2)(c_a)^2$$
$$CT_q = \left( \frac{C_a^2 + C_e^2}{2} \right) \left( \frac{\rho}{1 - \rho} \right) t_e$$
$$L = \frac{\rho}{1-\rho} - \frac{(b+1)\rho^{b+1}}{1-\rho^{b+1}}$$
$$\lambda' = \lambda \left( \frac{1 - \rho^b}{1 - \rho^{b+1}} \right)$$
$$L_q = \frac{\rho}{1-\rho} \times \text{Prob}(N > c)$$
$$W_q = \frac{\rho}{\lambda(1-\rho)} \times \text{Prob}(N > c)$$

$$F_t = w_1 A_{t-1} + w_2 A_{t-2} + w_3 A_{t-3} + \dots + w_n A_{t-n}$$
$$F_{t+1} = \alpha A_t + (1 - \alpha) F_t$$
$$\hat{y} = a + bx$$
$$\sum_{1}^n w_n = 1$$
$$TS_k = \frac{\sum_{t=1}^k e_t}{MAD_k}$$
$$F_t = \frac{A_{t-1} + A_{t-2} + A_{t-3} + \dots + A_{t-n}}{n}$$
$$MAD_k = \frac{1}{k} \sum_{t=1}^k |e_t|$$
$$e_t = F_t - A_t$$
$$FIT_t = F_t + T_t$$
$$F_t = FIT_{t-1} + \alpha(A_{t-1} - FIT_{t-1})$$
$$T_t = T_{t-1} + \alpha \delta (A_{t-1} - FIT_{t-1})$$
$$b = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2}$$
$$a = \frac{\sum y}{n} - b \frac{\sum x}{n} = \bar{y} - b\bar{x}$$

$$T_{(t, t-1)} = A_t - A_{t-1}$$
$$\bar{T} = \frac{\sum_{i=1}^n T_{(t-i, t-i-1)}}{n}$$

$$L = t_k + t_p + t_v$$
$$LCS = \bar{\bar{x}} + Z * \sigma$$
$$LCI = \bar{\bar{x}} - Z * \sigma$$
$$LCS_{\bar{X}} = \bar{\bar{X}} + A_2 * \bar{R}$$
$$LCI_{\bar{X}} = \bar{\bar{X}} - A_2 * \bar{R}$$
$$LCS_R = D_4 * \bar{R}$$
$$LCI_R = D_3 * \bar{R}$$
$$N = \frac{D \times L}{C}$$
$$N = \frac{D \times L}{C}(1 + \varepsilon)$$

$$C_{pk} = \frac{USL - Media}{3\sigma}$$
$$C_{pk} = \frac{Media - LSL}{3\sigma}$$
$$C_p = \frac{USL - LSL}{6\sigma}$$

### Factores para Cartas de Control

| Numero de observaciones en el subgrupo n | Factor para un diagrama X (A2) | Limite inferior de control (D3) | Limite superior de control (D4) |
| :---: | :---: | :---: | :---: |
| 2 | 1,88 | 0 | 3,27 |
| 3 | 1,02 | 0 | 2,57 |
| 4 | 0,73 | 0 | 2,28 |
| 5 | 0,58 | 0 | 2,11 |
| 6 | 0,48 | 0 | 2,00 |
| 7 | 0,42 | 0,08 | 1,92 |
| 8 | 0,37 | 0,14 | 1,86 |
| 9 | 0,34 | 0,18 | 1,82 |
| 10 | 0,31 | 0,22 | 1,78 |
| 11 | 0,29 | 0,26 | 1,74 |
| 12 | 0,27 | 0,28 | 1,72 |
| 13 | 0,25 | 0,31 | 1,69 |
| 14 | 0,24 | 0,33 | 1,67 |
| 15 | 0,22 | 0,35 | 1,65 |
| 16 | 0,21 | 0,36 | 1,64 |
| 17 | 0,20 | 0,38 | 1,62 |
| 18 | 0,19 | 0,39 | 1,60 |
| 19 | 0,19 | 0,40 | 1,61 |
| 20 | 0,18 | 0,41 | 1,59 |

| c | LTPD/AQL | n*AQL |
| :---: | :---: | :---: |
| 0 | 44,890 | 0,052 |
| 1 | 10,946 | 0,355 |
| 2 | 6,509 | 0,818 |
| 3 | 4,890 | 1,366 |
| 4 | 4,057 | 1,970 |
| 5 | 3,549 | 2,613 |
| 6 | 3,206 | 3,286 |
| 7 | 2,957 | 3,981 |
| 8 | 2,768 | 4,695 |
| 9 | 2,618 | 5,426 |
