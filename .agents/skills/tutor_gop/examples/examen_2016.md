# Examen

**ICS 3213 Gestión de Operaciones**
**Sección 1 y Sección 2 – 1er semestre 2016**
**Prof. Alejandro Mac Cawley**
**Prof. Isabel Alarcón**

## Instrucciones:

*   **Poner nombre y número a todas y cada una de las hojas del cuadernillo.**
*   No descorchetear el cuadernillo en ningún momento durante la prueba.
*   La prueba consta de 2 secciones. Debe contestar cada una de las preguntas en el espacio asignado.
*   No se permiten resúmenes de clases, ni de casos, ni formularios.
*   **Se descontará 10 puntos por no cumplir alguna de estas instrucciones.**
*   La prueba tiene 110 puntos y dura 110 minutos.
*   No se pueden utilizar laptops ni celulares.
*   Se leerá la prueba al comienzo de clases y después se permitirán preguntas en voz alta. Posteriormente en la mitad de la prueba se volverá a permitir preguntas en voz alta. No se permitirán preguntas fuera de estos intervalos. Si su duda persiste indique el supuesto y continúe.
*   Este curso adscribe el Código de Honor establecido por la Escuela de Ingeniería el que es vinculante. Todo trabajo evaluado en este curso debe ser propio. En caso de que exista colaboración permitida con otros estudiantes, el trabajo deberá referenciar y atribuir correctamente dicha contribución a quien corresponda. Como estudiante es su deber conocer la versión en línea del Código de Honor (http://ing.puc.cl/codigodehonor).

---

## PARTE I. (20 puntos) Sección verdadero o falso. 
**Indique si las siguientes afirmaciones son verdaderas (V) o falsas (F). En caso de ser falsas, indique la razón.**

1.  Los errores sistemáticos asociados a pronósticos son aquellos que no pueden ser explicados con ningún modelo.
    **Falso.** Esos son los errores aleatorios.
2.  Entre los supuestos del modelo EOQ está que el costo de emitir una orden disminuye al aumentar la cantidad ordenada.
    **Falso.** Es constante.
3.  Las empresas usan el sistema L4L, ya que produce solo lo necesario minimizando los costos de inventario.
    **Falso.** Porque este sistema asume capacidad ilimitada, supuesto que no siempre es verdadero, y que los costos de set-up son 0.
4.  Las pseudo actividades son aquellas que requieren más de un recurso a la vez para llevarse a cabo.
    **Falso.** No tienen duración ni consumen recursos.
5.  Tanto el método de análisis de punto de equilibrio como el de centro de gravedad tienen en común que poseen una cantidad acotada de soluciones factibles.
    **Falso.** En el método de centro de gravedad tiene infinitas soluciones factibles.
6.  El tiempo de flujo promedio es directamente proporcional al porcentaje de utilización de un recurso.
    **Falso.** Crece de manera exponencial.
7.  Las actividades que realiza un centro de distribución son: recepcionar, guardar, buscar y despachar.
    **Verdadero.**
8.  La ecuación de Kingman o VUT permite determinar analíticamente el tiempo de espera de la cola.
    **Falso**, ya que es una aproximación.
9.  Siempre se debe intentar aumentar las posiciones asignadas en el almacenamiento compartido.
    **Falso**, la subdivisión está limitada por los costos.
10. La calidad percibida por el cliente es objetiva.
    **Falso**, ya que su percepción depende de las características del producto, las características del servicio y las creencias personales del cliente, entre otros.

---

## PARTE II (90 Puntos): Ejercicios. Responda las siguientes 3 Preguntas

**1.- (35 Puntos)** La empresa Jot Wilz fabrica autos de juguete de distintos tamaños y colores. Para ello utiliza dos insumos: aluminio (para la carrocería) y ruedas. Actualmente trabajan 8 horas al día, 5 días a la semana y cada parte del proceso lo realiza una maquina diferente:

En primer lugar se vierte una unidad de aluminio en el molde de plantilla creado por los diseñadores, para darle forma a los autos y luego se llevan a una cámara de enfriado. A continuación se ensamblan las 4 ruedas en los ejes y se pinta el auto. Finalmente se empacan en cajas para ser distribuidos. Un 10% de los autos son testeados antes de ser empaquetados.

Todo el proceso funciona como una línea de producción continua, donde cada una de las máquinas tiene una capacidad promedio de trabajo, indicado en la siguiente tabla:

| Proceso | Capacidad máquina (autos /hr) | Máquinas |
| :--- | :---: | :---: |
| Molde | 55 | 6 |
| Enfriado | 79 | 5 |
| Ensamblaje | 65 | 4 |
| Pintura | 100 | 2 |
| Testeo | 48 | 1 |
| Empaque | 110 | 4 |

El precio de una unidad de aluminio es de $\$500$ y cada rueda tiene un precio de $\$100$. La empresa tiene un mismo proveedor para ambos insumos, que demora 2 días hábiles en entregar los pedidos requeridos. Cada orden tiene un costo de $\$50.000$ y el costo de mantener inventario a la semana es un $10\%$ del precio de cada insumo. Cada auto de juguete vendido genera una utilidad de $\$350$.

Responda las siguientes preguntas:
a. (8 puntos) Determine la capacidad máxima que la fábrica puede procesar al día. ¿Cuál es el cuello de botella? ¿Cuál es la utilidad semanal de la empresa?
b. (6 puntos) Los gerentes han decidido realizar una mejora en la cadena de producción y le han pedido ayuda para determinar qué procesos deberían aumentar su capacidad y en cuánto (cantidad de máquinas extra) para poder satisfacer una demanda diaria de 2.400 autos. ¿Cuánto estarían dispuestos a pagar los gerentes por este cambio en el sistema?
c. (6 puntos) Asumiendo que los pedidos llegan de manera instantánea, la demanda diaria de 2.400 autos permanece constante al igual que el costo por emisión de la orden y el tiempo de entrega de un pedido, calcule las cantidades óptimas a pedir de aluminio y ruedas. ¿Cuál es el punto de reorden de cada insumo?
d. (5 puntos) Calcule el costo anual total de la fábrica Jot Wilz.
e. (10 puntos) Si ahora el gerente le informa que el proveedor está teniendo problemas y ya no puede entregar los pedidos completos, sino a una tasa de 4.000 unidades/día para el aluminio y 12.000 ruedas/día, calcule cuánto debería pedir ahora de cada insumo y cuánto le cuesta este cambio en comparación a la situación anterior. Explique a qué se debe este cambio en el costo total.

### Respuesta de la Parte II Pregunta 1:
**a)**

| Proceso | Capacidad máquina (autos /hr) | Máquinas | Capacidad total (autos/hr) |
| :--- | :---: | :---: | :---: |
| Molde | 55 | 6 | 330 |
| Enfriado | 79 | 5 | 395 |
| Ensamblaje | 65 | 4 | 260 |
| Pintura | 100 | 2 | 200 |
| Testeo | 48 | 1 | =48$\cdot$1/0,1=480 |
| Empaque | 110 | 4 | 440 |

El cuello de botella es Pintura, porque solo puede producir 200 autos por hora.
$$Capacidad\ m\acute{a}xima\ diaria = Cap.\ cuello\ de\ botella = 200 \cdot 8 = 1.600\ \frac{autos}{d\acute{i}a}$$
$$Utilidad\ semanal = 1.600 \cdot 350 \cdot 5 = \$2.800.000$$

**b)** Se evalúa el aumento de 1 máquina en el cuello de botella (Pintura). Esto aumenta la capacidad del proceso a 260 autos /hr, porque el Ensamblaje se transforma en el nuevo cuello de botella. Con este cambio la nueva capacidad de la fábrica es de 2.080 autos/día, lo que no es suficiente para suplir la demanda.

Si además se agrega 1 máquina en el Ensamblaje, Pintura vuelve a ser el cuello de botella, con una capacidad de 300 autos/hr, con lo que la capacidad diaria es de 2.400 autos, lo que suple la demanda.

Los gerentes estarán dispuestos a pagar como máximo el equivalente a la utilidad generada por este cambio:
$$350 \cdot (2.400 - 1.600) = \$280.000$$

**c)** Utilizando el modelo EOQ se tiene que $S = \$50.000$ y $H$ se obtiene multiplicando el precio de cada insumo por $10\%$ y por 52 semanas al año. Además, hay que calcular la demanda anual, que corresponde a $2.400 \cdot 5 \cdot 52 = 624.000$ autos.

Para el aluminio:
$$Q_{EOQ} = \sqrt{\frac{2\cdot D\cdot S}{H}} = \sqrt{\frac{2\cdot 624.000\cdot 50.000}{500\cdot 0,1\cdot 52}} = 4.898,98 \approx 4.899\ unidades$$

Para las ruedas hay que considerar además que se requieren 4 ruedas por cada auto demandado:
$$Q_{EOQ} = \sqrt{\frac{2\cdot D\cdot S}{H}} = \sqrt{\frac{2\cdot 624.000\cdot 4\cdot 50.000}{100\cdot 0,1\cdot 52}} = 21.908,9 \approx 21.909\ ruedas$$

El punto de reorden para cada insumo es:
Aluminio: $R = L \cdot d = 2 \cdot 2.400 = 4.800\ unidades$
Ruedas: $R = L \cdot d = 2 \cdot 2.400 \cdot 4 = 19.200\ ruedas$

**d)**
$$CT = D \cdot C + \frac{D \cdot S}{Q} + \frac{Q \cdot H}{2}$$

Aluminio:
$$CT = 624.000 \cdot 500 + \frac{624.000 \cdot 50.000}{4.899} + \frac{4.899 \cdot 500 \cdot 0,1 \cdot 52}{2} = \$324.737.347$$

Ruedas:
$$CT = 624.000 \cdot 4 \cdot 100 + \frac{624.000 \cdot 4 \cdot 50.000}{21.909} + \frac{21.909 \cdot 100 \cdot 0,1 \cdot 52}{2} = \$260.992.629$$

Luego el costo anual total de la fábrica es de $\$585.729.976$.

**e)**
$$Q_{opt} = \sqrt{\frac{2 \cdot D \cdot S}{H}} \cdot \sqrt{\frac{p}{p - d}}$$
$$CT = D \cdot C + \frac{D \cdot S}{Q} + \frac{Q \cdot H}{2} \left(1 - \frac{d}{p}\right)$$

Para el aluminio:
$$Q_{opt} = 4.899 \cdot \sqrt{\frac{p}{p-d}} = 7.746\ unidades$$
$$CT = 624.000 \cdot 500 + \frac{624.000 \cdot 50.000}{7.746} + \frac{7.746 \cdot 500 \cdot 0,1 \cdot 52}{2} \cdot \left(1 - \frac{2.400}{4.000}\right) = \$320.055.805,4$$

Para las ruedas:
$$Q_{opt} = 21.909 \cdot \sqrt{\frac{p}{p-d}} = 48.990\ ruedas$$
$$CT = 624.000 \cdot 4 \cdot 100 + \frac{624.000 \cdot 4 \cdot 50.000}{48.990} + \frac{48.990 \cdot 100 \cdot 0,1 \cdot 52}{2} \cdot \left(1 - \frac{2.400 \cdot 4}{12.000} \right) = \$248.963.108,7$$

Luego el costo anual total de la fábrica es de $\$569.018.914$, que es $\$16.711.062$ menor al costo de la situación anterior, porque se genera un ahorro en inventario.

---

**2.- (35 Puntos)** En un centro de distribución se tienen los siguientes SKU con las características que se presentan en la tabla:

| SKU | PICKS | DDA(PALLETS) | DDA PALLETS COMPLETOS | MIN | MAX |
| :---: | :---: | :---: | :---: | :---: | :---: |
| A | 80 | 10 | 21 | 2 | 10 |
| B | 71 | 9 | 35 | 3 | 9 |
| C | 74 | 8 | 12 | 3 | 7 |
| D | 95 | 7 | 3 | 3 | 8 |

A la empresa le toma 1 minuto realizar el *picking* en el área frontal, 3 minutos en el área de reserva y la reposición del pallet le toma 3 minutos.
a) (9 puntos) Usted tiene 2 posiciones de 3 pallet de profundidad cada una. ¿Qué SKUs dispondría? ¿Cuánto de cada uno? ¿Cuál es el beneficio total de esa configuración? Calcule los beneficios mínimos, adicionales y máximos unitarios para cada SKU.
b) (5 puntos) ¿Cómo debería variar la demanda del ultimo SKU que NO eligió en a) para que reemplace al “peor” SKU en área frontal?
c) (6 puntos) Usted recientemente egreso de Ingeniería y es contratado por el dueño de un centro de distribución en el puerto de San Antonio. Para introducirlo al negocio le comenta que al CD llegan containers según un proceso de Poisson a tasa $\lambda \left[\frac{\text{container}}{\text{hora}}\right]$. En el CD cuentan con k operarios y el tiempo de atención de cada uno distribuye exponencial con un tiempo medio de $\mu$ horas. Además, el CD admite como máximo Z containers en su interior. Finalmente, se le comenta que existe un costo asociado por espacio utilizado en el CD por cada container de $C \left[\frac{\$}{\text{container-hora}}\right]$ y, por otro lado, existe un costo de mano de obra de $S \left[\frac{\$}{\text{operario-hora}}\right]$. Como egresado de ingeniería, su jefe le pide que desarrolle un modelo de programación matemática que minimice el costo total del CD. Hint: considere que el CD se encuentra en estado de régimen.

En otro centro de distribución se tiene un área de Picking rápido cuyo espacio total disponible es de $1500\ \text{m}^3$, en la cual se busca disponer tres SKU: X, Y, Z y W.

| SKU | UNIDADES/MES | UNIDADES/CAJA | M3/CAJA |
| :---: | :---: | :---: | :---: |
| X | 3000 | 20 | 3 |
| Y | 3600 | 24 | 2 |
| Z | 2040 | 36 | 1.5 |
| W | 1000 | 50 | 5 |

d) (4 puntos) Plantee el problema de optimización que minimiza el costo total del área de picking rápido. Suponga que el costo de *restock* es $c_r$.
e) (5 puntos) Con los datos de la tabla anterior calcule el espacio óptimo y la frecuencia de *restock* para cada SKU.
f) (6 puntos) Calcule el espacio asignado y el *restock* para cada SKU considerando las siguientes configuraciones: igual volumen para los SKU y con igual frecuencia de *restock*.

### Respuesta de la Parte II Pregunta 2:
**a)** Primero se calculan los $l_i$ y $u_i$ según el diseño del área frontal (2 puntos):

| SKU | $l_i$ | $u_i$ |
| :---: | :---: | :---: |
| A | 1 | 4 |
| B | 1 | 3 |
| C | 2 | 3 |
| D | 2 | 3 |

Se tiene la siguiente tabla ahora:

| SKU | PICKS | DDA(PALLETS) | DDA PALLETS COMPLETOS | MIN | MAX |
| :---: | :---: | :---: | :---: | :---: | :---: |
| A | 80 | 10 | 21 | 1 | 4 |
| B | 71 | 9 | 35 | 1 | 3 |
| C | 74 | 8 | 12 | 1 | 3 |
| D | 95 | 7 | 3 | 1 | 3 |

Utilizando las fórmulas se calculan los beneficios (4.5 puntos):

| SKU | BEN_MIN | BEN_ADIC | BEN_MAX_Unit |
| :---: | :---: | :---: | :---: |
| A | 130 | 24 | 50.5 |
| B | 115 | 48.5 | 70.67 |
| C | 124 | 24 | 57.33 |
| D | 169 | 13.5 | 65.33 |

Se utiliza el método propuesto en clases para asignar maximizando beneficio, que consiste en ordenar de mayor a menor beneficio. Las primeras 2 posiciones corresponden a (1.5 puntos):

| SKU | Posiciones | Beneficio |
| :---: | :---: | :---: |
| D-MIN | 1 | 169 |
| A-MIN | 1 | 130 |

Por lo tanto se asigna 1 posición al SKU al D y 1 al A.
El beneficio total corresponde a (1 puntos):
$$BEN = 1 * 169 + 1 * 130 = 299\ min$$

**b)** Los SKU que no se disponen en el área frontal son B y C. Para que convenga colocarlos ahí, su beneficio mínimo unitario debe ser igual o mayor que el de A: 130 minutos (2 puntos).

Se tiene que:
$$BEN_{min-i} = \frac{p_i * s - d_i c_r}{l_i}$$

Despejamos la Demanda:
$$d_i = \frac{p_i * s - BEN_{min-i} * l_i}{c_r}$$

De esta manera, se reemplaza los valores: $c_r = 3$, $s = 2$, $BEN_{min-i} = 130$ y los valores de $p_i$ y $l_i$ para cada SKU se obtiene la Demanda de Pallets necesaria para que reemplacen al SKU A (4 puntos).

| SKU | Nueva Dda | Variación |
| :---: | :---: | :---: |
| B | 4 | -5 |
| C | 6 | -2 |

**c)** Este sistema corresponde un sistema de espera M/M/C. En el que la tasa de llegada es $\lambda$ y la tasa de atención es $\frac{1}{\mu}$ por operario. Como hay k operarios el $\rho = \frac{\lambda}{\frac{k}{\mu}} = \frac{\lambda\mu}{k}$ (1 pto)
La cantidad promedio de container en el CD corresponde a L. Dado que se alcanza régimen se puede aplicar Little:
$$L = \lambda * W = \lambda * (\mu + W_q)\ \ \ \ \ \ \ \ (1\ pto)$$

El tiempo promedio en cola queda determinado por:
$W_q = \frac{\rho}{\lambda(1-\rho)} * Prob(N > k)$; reemplazando el valor de $\rho$, se tiene:
$$W_q = \lambda * \left(\mu + \frac{\mu}{k(k - \lambda\mu)}\right) * Prob(N > k)$$

Así podemos plantear el problema de programación matemática:
$$Min_k\ \left(\lambda * \left(\mu + \lambda * \left(\mu + \frac{\mu}{k(k-\lambda\mu)}\right) * Prob(N > k)\right)\right) * C + k * S\ \ \ \ \ \ \ \ (2\ ptos)$$
$$s.a.$$
$$\lambda * \left(\mu + \lambda * \left(\mu + \frac{\mu}{k(k-\lambda\mu)}\right) * Prob(N > k)\right) < Z$$
$$k \ge 0$$
(1pto)

**d)** $Min\ c_r \sum_i \frac{f_i}{v_i}$
$$s.a\ \ \ \sum_i v_i = V$$
$$v_i \ge 0\ \forall i$$

En este caso es :
$$Min\ c_r * \left(\frac{f_x}{v_x} + \frac{f_y}{v_y} + \frac{f_z}{v_z} + \frac{f_w}{v_w}\right)\ \ \ \ \ \ \ \ (2\ ptos)$$
$$s.a\ \ \ v_x + v_y + v_z + v_w = 1500\ \ \ \ \ \ \ \ (1pto)$$
$$v_x, v_y, v_z, v_w \ge 0\ \ \ \ \ \ \ \ (1pto)$$

**e)** Se calculan las frecuencias para cada SKU (2 puntos):

| SKU | FRECUENCIAS M3/MES |
| :---: | :---: |
| X | 450 |
| Y | 300 |
| Z | 85 |
| W | 100 |

Luego se asigna el espacio según la condición de optimalidad y se calculan las frecuencias (3 puntos):

| SKU | Espacio | Restock |
| :---: | :---: | :---: |
| X | 550.96 | 0.82 |
| Y | 449.86 | 0.67 |
| Z | 239.46 | 0.35 |
| W | 259.73 | 0.39 |

**f)** Igual espacio (3 puntos):

| SKU | Espacio | Restock |
| :---: | :---: | :---: |
| X | 375 | 1.2 |
| Y | 375 | 0.8 |
| Z | 375 | 0.23 |
| W | 375 | 0.27 |

Igual tiempo (3 puntos):

| SKU | Espacio | Restock |
| :---: | :---: | :---: |
| X | 721.925 | 0.623 |
| Y | 481.283 | 0.623 |
| Z | 136.364 | 0.623 |
| W | 160.428 | 0.623 |

---

**3.- (20 Puntos)** Usted es el titular de una empresa de café preparado llamada “Juana Valdez Café”. Habitualmente compra el grano, y en cada uno de sus tres locales lo muele y sirve en vasos de cartón térmico. Debido a las quejas de los clientes, han registrado que los vasos no siempre se comportan térmicamente bien. Por ello ha decidido hacer un estudio de proveedores. Usted ha determinado que los vasos deberían tolerar un mínimo de $90^\circ\text{C}$ para para que sean seguros y coincida con lo que exige a sus proveedores. Por otro lado, tiene un histórico de muestreos de recepción en donde en promedio los vasos tienen una resistencia de $95^\circ\text{C}$, con una desviación estándar de $2^\circ\text{C}$. Actualmente su proveedor “Kartoon” le entrega en lotes de 5000 vasos.

Usted ha decidido iniciar un estudio del problema y está analizando como definir bien el problema para poder llegar a una solución. Revisando sus apuntes de Gestión de Operaciones se encuentra con 4 preguntas que le pueden ayudar en su trabajo. A continuación, desarrolle las respuestas para cada pregunta:
a) (5 puntos) Determine la información que necesitaría recopilar del proceso y del proveedor para analizar el problema.
b) (5 puntos) Establezca que metodología utilizaría para mejorar la calidad del proceso y cómo evaluaría esta.
c) (5 puntos) Realice el mismo análisis, pero ahora enfocado en la recepción de los insumos del proveedor.
d) (5 puntos) ¿La aplicación de ambos cambios llevaría a mejorar la calidad del producto final?

### Respuesta de la Parte II Pregunta 3:
**a)** En proceso hay que registrar y buscar los elementos que permitan reflejar el problema, y algunos elementos que en principio puedan reflejar algunas razones. Asi se recolectan:
- Temperatura de llenado de los vasos: temperatura de las bebidas servidas en vasos, discriminadas por tipo
- Temperaturas que indican los equipos en sus visores
- Dato de lote de producto ingresado a línea (en este caso usado para lo que son despachos de bebidas calientes)
- Volumen de llenado habitual (puede que las quemaduras sean no porque el vaso no tolere sino porque hay salpicaduras)
- Registro de quejas de los clientes con detalle

Para vincular de manera correcta el idioma del proveedor y el de la cafetería es necesario cotejar y homologar la practica de muestreo que usan ellos para liberar producto y el esquema de aceptación de la cafetería. Es puntualmente revisión de los nuestros de aceptación y liberación y las practicas analíticas, en un estudio R&R

Sobre el proceso del proveedor se puede recuperar información de ensayos en el momento productivo para ver como ha sido el comportamiento histórico en la variable y si se observan curvas que estén fuera de control o lotes que sean lindantes con los limites especificados. Asi mismo se puede leer si el proceso en forma genérica es un productor de no conforme o no.

Como datos duros, para poder disparar estos planes se requieren conocer la tolerancias aceptadas en la cafetería, las especificaciones de cada producto y cuales son los mas críticos. Respecto al proveedor su tasa de defectos medios, tamaño lote, y comportamiento de proceso (SPC).

**b)** Para mejorar la calidad del proceso focalizaríamos en algunos elementos de las metodologías presentadas en el curso a grandes rasgos. Entre ellos podemos mencionar:
- Mejora sobre línea de proceso atento a disminuir la dispersión por ej. de las temperaturas de llenado. Esto puede aplicarse por ej. siguiendo la metodología de DMAIC; aunque no es precisa la aplicación de acuerdo a 6Si, igualmente el criterio que representa DMAIC es valido
- Desarrollo de proveedores atentos a lograr condiciones de diseño tales que las características que se desean mantener de resistencia termina vengan dadas desde un primer momento (por ej. elección de material de vasos)
- Estandarización de operaciones dentro de la cafetería con controles visuales que permitan de una manera mas acabada y fácil el control del proceso

La evaluación de estas medidas se basarían en
- Un plan de análisis donde habría protocolos de control que apunten a ver la funcionalidad del vaso en una situación extrema (basados en un buen diseño, lo que aporta es un control sobre la fabricación del lote, por ej. soldaduras). Para ello se aplican los conceptos de muestreo y con estos datos podemos construir un histórico con forma de SPC.
- Auditorias periódicas al proveedor en donde se revisen además de fabricaciones en línea, registros históricos de análisis.

**c)** La recepción al proveedor de insumos esta basado en un muestreo y un set de análisis en donde se determina si se acepta o no el lote contra especificación. Este proceso es mecánico:
- Se decide inicialmente el tipo de muestreo que se va a aplicar: simple, doble, o triple
- En base al tamaño de lote, el diferencial que se quiere destacar o piezas con fallas a encontrar, o con el nivel de calidad aceptable como recepción, se calcula el tamaño de la muestra y los criterios que tiene que cumplir en cantidad de defectos para ser aceptado.
- A partir de este punto se decide en función de la constitución de los pallets como se hara el pickeo de muestras
- Aplicación de análisis y resultados, con la decisión consecuente.

Es importante recordar que un control de calidad tradicional carece de utilidad si detrás de los parámetros no hay un desarrollo de proveedores y el interés común de mantener un negocio en el tiempo. Son elementos que hacen a la calidad acordada y que requieren mucho más que una especificación.

**d)** El producto final de aplicarse estos esquemas debería presentar una mejora, aunque posiblemente no sea sostenible. Sin embargo es factible que a nivel global la mejora no sea tal, e incluso en la misma cafetería el efecto sea negativo; por ej. quiebres de stock si los rechazos se incrementan por efecto de no haber mejorado la calidad en origen.
Hacer controles más fuertes, por ej. en la recepción y disminuir las variaciones en proceso de llenado, así como en las condiciones de máquina, suman y son de importancia. Sin embargo estas mejoras solo podrán ser reales si:
- Se desarrollo con el proveedor una alternativa que produzca calidad desde su proceso de fabricación, y no tan solo se circunscribe a un control más estricto del estilo pasa - no pasa
- El procedimiento de la cafetería está suficientemente controlado de manera de evitar puntos que lleven a recorrer los límites de la especificación de proceso del vaso. Esto es que los limites de proceso deben encuadrar las especificaciones de uso.

Es vital que exista un conocimiento del cliente y especialmente de la identificación del defecto que menciona. Sin esto la medida puede repercutir en algo que no genere valor realmente para el cliente, o lo que es peor aún, que no solucione el problema de fondo porque ha sido mal identificado inicialmente.

---

## Formulario

$$Q_w = \sqrt{\frac{2C_0D}{C_h}}$$
$$R = d * L$$
$$CT = DC + \frac{D}{Q}S + \frac{Q}{2}H$$
$$CT = D \cdot C + \frac{D \cdot S}{Q} + \frac{Q \cdot H}{2}\left(1 - \frac{d}{p}\right)$$
$$Q_{opt} = \sqrt{\frac{2DC_0}{C_H}}\sqrt{\frac{p}{p-d}}$$
$$\frac{k}{k+1}$$
$$Prof = \sqrt{\left(\frac{a}{2}\right)\left(\frac{q_i}{z_i}\right)}$$
$$Prof = \sqrt{\left(\frac{a}{2}\right)\left(\frac{1}{n}\right)\left(\sum_{i=1}^n \frac{q_i}{z_i}\right)}$$
$$Ben = sp_i - c_r d_i$$
$$Ben = s(p_i + D_i)$$
$$Beneficio_{min\_A} = \frac{s * p_i - c_r * d_i}{l_i}$$
$$Beneficio_{max\_A} = \frac{s(p_i + D_i)}{u_i}$$
$$Beneficio_{adic\_A} = \frac{s * D_i + c_r * d_i}{u_i - l_i}$$
$$v_i^* = \left(\frac{\sqrt{f_i}}{\sum_{j=1}^n \sqrt{f_j}}\right) V$$
$$\frac{p_i}{\sqrt{f_i}}$$

$$\rho = \frac{\lambda}{\mu}$$
$$\rho = \frac{\lambda}{c\mu}$$
$$L = \lambda \times W$$
$$L = \frac{\rho}{1-\rho}$$
$$W = \frac{1}{\mu(1-\rho)}$$
$$L_q = \frac{\rho^2}{1-\rho}$$
$$W_q = \frac{\rho}{\mu(1-\rho)}$$
