                    Pontificia Universidad Católica de Chile
                    Escuela de Ingenierı́a
                    Departamento de Ingenierı́a Industrial y de Sistemas
                    Profesores: Alejandro Mac Cawley y Jorge Morales
                    Ayudantes: Alberto Busch (atbusch@uc.cl) y Francisco Lira (fvlira@uc.cl)



1    Inventario
Problema 1
Como gerente de una fábrica de chocolates debe elegir una polı́tica óptima de abastecimiento de cacao. La
empresa vende chocolate a distintos supermercados de la ciudad. El consumo de los supermercados es de
400kg de chocolate diario y el precio de este es de $4.000 el kilo. Para comprar el cacao existen dos opciones,
una es comprar el saco de 40kg con un costo de $80.000 y la otra es comprar en lotes pequeños de 10kg con un
costo de $25.000. La diferencia entre los pedidos es que los tiempos de entrega son distintos, por una parte
los sacos se demoran 5 dı́as en llegar y los lotes pequeños sólo 2 dı́as. Los costos de envı́o también varı́an,
ya que para los sacos el costo de envı́o es de $30.000 y para los lotes pequeños es de $10.000. Finalmente el
costo de inventario es de $100 el kilo al dı́a.


a) ¿Cuál es la cantidad óptima a pedir de cacao para cada tipo de pedido? ¿Cada cuánto tiempo hay que
hacer el pedido?
b) ¿Cuánto es el costo de dos semanas con cada una de las polı́ticas de inventario? ¿Qué polı́tica es más
conveniente?


Solución

Primera opción:
Costo: $ 80.000
Demanda: 400kg/40kg = 10 sacos diarios
Costo Orden: $ 30.000
Costo Inventario: 100*40 = 4.000 el saco

Segunda opción:
Costo: $ 25.000
Demanda: 400kg/10kg = 40 lotes pequeños
Costo Orden: $ 10.000
Costo Inventario: 100*10 = 1.000 el saco


a) Se utiliza
       r el modelo EOQ para calcular la cantidad óptima de cada pedido. La fórmula es
           2DS
Qopt =          , donde D es el costo de una orden, S es la demanda diaria y H es el costo de inventario.
            H
Reemplazando queda:
         r          r
            2DS       2 ∗ 30.000 ∗ 10
Qopt1 =           =                   = 12,24 sacos.
              H            4.000
                                                                                                Qopt
Por su parte, para calcular cada cuánto hay que hacer el pedido, se utiliza la fórmula T =     D .


                                                        1
                                                                Qopt 12,24
Para este pedido, por lo tanto, el tiempo óptimo es T1 =        D = 10 = 1, 22 dı́as.

Para el segundo
         r       pedido,
                    r     los cálculos son los siguientes:
           2DS        2 ∗ 10.000 ∗ 40
Qopt1 =          =                      = 28,28 sacos.
            H               1.000
      Qopt   128,28
T2 = D = 40 = 2, 828 dı́as.
                                                                      D         Q
b) La fórmula de costo total de inventario es T C = D ∗ C + S ∗         + H ∗ , donde D es la demanda diaria,
                                                                      Q         2
C es el costo unitario (del saco en este caso), S es el costo fijo de la orden, Q es la cantidad óptima calculada
anteriormente y H es el costo de inventario. Por lo tanto, los costos para ambas opciones son:
                             D      Q
        T C1 = D ∗ C + S ∗     +H ∗                             10
                                      = 10 ∗ 80.000 + 30.000 ∗ 12,24 + 4.000 ∗ 12,24
                                                                                 2   = $848.989,804
                             Q      2
                                                      40              28, 28
                     T C2 = 40 ∗ 25.000 + 10.000 ∗          + 1.000 ∗        = $1.028.290,39
                                                     28, 28             2
De esta manera sabemos que diariamente el costo es mayor para la segunda opción. En dos semanas los
costos van a mantener la misma proporción de diferencia, por lo que la mejor polı́tica para la empresa es
comprar de lotes más grandes, independiente de que se demoren más dı́as en llegar. (El tiempo de entrega
se considera para el punto de reorden).


Problema 2
Un supermercado de manejar polı́ticas de inventario de muchos productos, uno de ellos es el pan. La de-
manda por pan es de 1.000kg diarios en promedio. Sin embargo tiene variabilidad, la que se expresa en una
desviación estándar de 66kg. El kilo de pan tiene un costo de fabricación de $500. El costo de inventario es
de $100 al dı́a. Finalmente el costo de empezar la producción de pan es de $10.000 y esta demora 2 horas.

a) Calcule el lote óptimo según EOQ.
b) ¿Cuánto es el tiempo de ciclo?
c) Usando el lote calculado en a) calcule el punto de reorden que permita tener un nivel de servicio del 95%.
d) ¿Cuál es el gasto promedio por mantener este nivel de servicio?


Solución

Se tiene la siguiente información:
Demanda: 1.000kg diarios
Desviación estándar: 66kg
Costo producción: $500 por kg Costo de inventario: $100 al dı́a
Costo Orden: $10.000

a) El lote óptimo es lo mismo que la cantidad óptima a pedir, por lo que se utiliza la fórmulo EOQ del
problema anterior:

                                            q          q
                                                2DS        2∗1.000∗10.000
                                   Qopt =        H =            100       = 447 kg

b) El tiempo se ciclo se calcula de la siguiente manera:



                                                           2
                                               Qopt  447
                                         T =    D = 1.000 = 0, 447 dı́as

c) El punto de reorden√es la cantidad de stock a partir de la cual hay que realizar el pedido. La fórmula es
R = D ∗ L + Zα ∗ σ ∗ L, donde D es la demanda, L es el lead time o periodo de reaprovisionamiento (en
dı́as), Zα está dado por el nivel de servicio requerido y σ es la desviación estándar.
Por lo tanto, el cálculo de reorden es:
                                                √             2
                                                                               q
                                                                                   2
                        R = D ∗ L + Zα ∗ σ ∗ L = 1.000 ∗ 24      + 1, 64 ∗ 66 ∗ 24   = 115

d) El gasto viene del inventario de seguridad que se debe mantener. Esto produce mayores costos de
inventario.                                                              √
Para calcular el inventario de seguridad se utiliza la fórmula Zα ∗ σ ∗ L. Reemplazando, queda
                                                   q
                                                      2
                                       1, 64 ∗ 66 ∗ 24    = 32 unidades.

El costo de mantener este inventario es de: $3.200 diarios.

Problema 3
Usted es el gerente de compras de una panaderı́a. En estos momentos debe elegir una polı́tica óptima de
abastecimiento de harina. La panaderı́a atiende colegios y casinos que consumen 100kg de pan diarios a $800
el kilo. Un saco de harina (50kg) cuesta $15.000 y rinde para aproximadamente 65kg de pan. Cada viaje
al molino involucra $20.000 pesos de gasto en bencina. Finalmente el costo de almacenamiento de harina se
estima en $100 el saco.

a) ¿Cuál es la cantidad optima a pedir de harina? ¿Cada cuánto hay que hacer el pedido?
b) ¿Cuál es el costo diario de esta polı́tica de inventario?


Solución

Costo: $15.000
Demanda: 100kg
           65kg = 1, 538 sacos diarios
Costo orden: $20.000
Costo inventario : $100

Se utilizan las fórmulas utilizadas en los problemas anteriores:

a)

                                         q          q
                                             2DS        2∗20.000∗1,538
                                Qopt =        H =             100      = 24, 8 sacos

                                                  Qopt  24,8
                                         Topt =    D = 1,538 = 16, 1 dı́as

b)
                               D      Q
            TC = D ∗ C + S ∗     +H ∗   = 1, 538 ∗ 15.000 + 20.000 ∗ 1,538       24,8
                                                                     24,8 + 100 ∗ 2 = $25.558
                               Q      2




                                                          3
Problema 4 (utilizando problema 3)
Considere que el molino tiene ahora más oferta, rebaja el precio a $14.000 por saco de harina si la compra
es mayor a 40 sacos.

a) ¿Cambia la cantidad óptima a comprar? En caso que sı́, ¿a cuánto cambia?
b) ¿Cuánto es el beneficio diario debido a la nueva polı́tica?


Solución

a) En el gráfico se puede observar que el óptimo con este nuevo precio es el mismo. Sin embargo, esa
cantidad la oferta no es válida, por lo tanto se debe evaluar en el lı́mite (40).




   El costo diario con lotes de 40 sacos es:

                               D      Q
            TC = D ∗ C + S ∗     +H ∗   = 1, 538 ∗ 14.000 + 20.000 ∗ 1,538        40
                                                                       40 + 100 ∗ 2 = $24.308
                               Q      2
   Como el costo es menor (antes era de $25.558) cambia la cantidad óptima a 40.

b) Beneficio diario = 25.558 – 24.308 = $1.250

Problema 5
Usted trabaja en una empresa que fabrica celulares y está negociando un nuevo contrato con su proveedor de
pantallas. Actualmente la demanda por pantallas es de 100.000 pantallas al mes, el costo de cada pantalla
es de $40.000, el costo de inventario de pantallas es de $100 al dı́a (considere 30 dı́as) y el costo de poner
una orden es de $500.000.

a) Identifique el costo de inventario de la situación base (Mantener los detalles del contrato).
b) ¿Cuánto estarı́a dispuesto a pagar por la opción de recibir las pantallas a una tasa de 10.000 pantallas


                                                      4
diarias por un año?
c) ¿Cuál es la tasa diaria a la que se minimizan los costos de inventario?


Solución

a) Se debe calcular primero la cantidad óptima a pedir y con eso el costo de inventario. Utilizando las
fórmulas ya mostradas en los problemas anteriores, queda de la siguiente manera:

                                            q          q
                                                2DS        2∗ 100.000 ∗500.000
                                   Qopt =        H =
                                                                30
                                                                   100         = 5774

En el caso del costo de inventario, se usa la fórmula anterior pero sin considerar el costo de compra o
producción (demanda ∗ costounitariodelproducto).
                                D      Q             100.000
                     CD = S ∗     +H ∗   = 500.000 ∗ 30∗5774 + 100 ∗ 5774
                                                                      2   = $577.350
                                Q      2
b)

                                   q          q                   q
                                       2DS          P                     10.000
                          Qopt =        H ∗       P −D = 5774 ∗       10.000− 100.000
                                                                                30
                                                                                        = 5873

                            (1 − D
                                                                                    100.000
                     D           P )Q
                                                                        30
                                                                  (1− 10.000 )∗5873
                                                  100.000
            CD = S ∗   +H ∗           = 500.000 ∗ 30∗5873 + 100 ∗         2         = $479.551
                     Q          2

El beneficio es de $97.799 al dı́a.
Por lo tanto estoy dispuesto a pagar $35.207.640 (por ser anual) por esta opción.

c) Cuando la tasa es igual a la demanda: 100.000
                                           30 .




Problema 6
En un determinado vuelo Santiago-Lima hay 200 asientos. Suponga que la utilidad que deja un pasaje es
US$475 en promedio y que el número de pasajeros que reserva un asiento pero que no llega al momento del
despegue (no-shows) distribuye normal con media 30 y desviación estándar 15. Usted decide sobrevender
(overbooking) el vuelo, y estima que la pérdida promedio por un pasajero que hay que dejar abajo del avión
en caso de que lleguen más que los asientos disponibles es de US$800. ¿Cuál es el máximo número de reservas
que debiesen aceptarse en este vuelo?

Solución


En este caso se debe usar el modelo de vendedor de diarios. Se define como x el número máximo de reservas
que debe aceptar el vuelo. La cantidad S de sobrecupo se define como: S = X - 200. Donde Co es el costo
por pasaje que sobra al final, y Cu el costo por demanda insatisfecha. Usando el modelo de vendedor de
diarios obtenemos:


                                                Q∗ = F −1 ( CoC+C
                                                                u
                                                                  u
                                                                    )
                                                  Cu         475
                                       Fn (s) = Cu +Co = 475+800 = 0, 3725



                                                           5
Lo que es la frecuencia acumulada óptima. Es decir, estadı́sticamente conviente sobrevender el 37,25% del
vuelo.
Por lo tanto usando la tabla de la normal:

                                                     Z = −0, 325

De esta forma:
                                   S = µ + σ ∗ Z = 30 − 15 ∗ 0, 325 = 25, 12
Finalmente, el número máximo de reservas X, es:

                                             X = S + 200 = 225, 12

O bien, 225 reservas.


Problema 7
Usted acaba de hacerse cargo de una bomba de bencina. En una manera de disminuir los costos decide
reevaluar la polı́tica de reabastecimiento del petróleo diesel. El diesel es el principal producto de esta bomba
y tiene una demanda de 10.000 lt diarios aproximadamente con una variabilidad de 500 lt /dı́a. Es necesario
mantener un nivel de servicio del 90 %. El diesel se entrega en camiones con capacidad de 35.000 lt y el
costo pedir un camión se estima en $300.000 (el camión demora 1 dı́a en llegar). El costo de almacenar el
diesel se estima en $20 por litro por dı́a.
a) ¿Cuál es la cantidad optima bajo revisión continua? ¿Cuál es el punto de reorden?
Existe una opción de abastecerse todas las noches con un camión compartido con otras 3 bombas. El costo
de pedir un camión baja a $100.000 lo demás se mantiene igual.
b) ¿Cuál es la cantidad óptima a pedir bajo este sistema de revisión periódica?
c) ¿Cuál de las dos opciones es preferible?


Solución


a) La cantidad óptima es igual al lote óptimo según EOQ:
                                       q         q
                                Q∗ = 2DS    H  =    2∗10.000∗300.000
                                                           20        = 17.321 lt

y su punto de re-orden, buscando el z90 en la tabla normal estandar:
                                         √                        √
                    R = d ∗ L + zα ∗ σ ∗ L = 10.000 ∗ 1 + 1, 28 ∗ 500 ∗ 1 = 10.029 lt

b) En el caso del sistema de revisión periódica:
                                                        p
                            Q∗ = d ∗ (L + T ) + Zαp∗ σ ∗ (L + T ) − Iexistente
                                           √
             Q∗ = 10.000 ∗ (1 + 1) + 1.28 ∗ 500 ∗ (1 + 1) − Iexistente = 20.040, 5 − Iexistente
                                          Q∗ = 20.041 − Iexistente

c) Para saber cual de las dos soluciones es mejor, se comparan los coston, sin incluir el costo del Diesel al
ser igual para ambos:
Primer caso:
                                   Q
                     CT = D                 10.000
                          Q ∗ Co + 2 ∗ Ch = 17.321 ∗ 300.000 +
                                                               17.321
                                                                  2   ∗ 20 = $346.410


                                                         6
Segundo caso:
El costo de órdenes en la segunda opción es 100.000 diarios. Para calcular el costo de inventario necesitamos
la cantidad almacenada promedio. Cada vez que se hace un pedido se debe esperar L hasta que llegue, por lo
tanto, el Inventario que deberı́a haber cuando se hace un pedido (Iexistente ) deberı́a cubrir L más un factor
de seguridad.
Luego el inventario promedio es:
                                                20.041−10.029
                                                      2       = 5.006
Finalmente, el CT:
                                      CT = 100.000 + 5.006 ∗ Ch = $200.120
Por lo que es preferible la segunda opción

Problema 8
Usted es gerente de operaciones de una fábrica de lácteos y esta interesado en optimizar la polı́tica de in-
ventarios. El proceso de la empresa consiste en embotellar los productos obtenidos en el reactor principal
a través de una máquina con capacidad de procesamiento de 150 unidades por hora, a costo de $100 por
producto. Esta máquina tiene un costo de set up de $60.000 para iniciar sus actividades, y tarda 4 horas.
Una vez procesados, los productos se almacenan en frio a un costo de $100 por unidad por hora, hasta que
son requeridos por los minoristas. La demanda de los minoristas es de 90 productos por hora. Dada la
informacion anterior, indique el tamaño óptimo de los pedidos a ser procesados. ¿Qué porcentaje del tiempo
la máquina está en funcionamiento? ¿Cuál es el nivel maximo al que llega el inventario? ¿Cuál es el punto
de re-orden?


Solución


Primero se calcula el lote óptimo:
                                                           q         q
                                                               2DS        p
                                                 Q∗ =           H        p−d
                                         q                 q
                                             2∗90∗60.000         150
                                 Q∗ =            100           150−90 = 520 unidades

Con el valor del lote mı́nimo es posible calcular el tiempo de producción dado por 520/150 = 3,5 horas.
También se puede calcular el tiempo de consumo dado por 520/90 = 5,8 horas. Es importante notar que el
tiempo de consumo no alcanza a cubrir el tiempo total de producción (tiempo de produccion + tiempo de
set up). Para resolver esto es necesario incrementar el lote mı́nimo para que se satisfaga la demanda en el
perı́odo de set up.
Dado que el tiempo de set up es de 4 horas se puede calcular el consumo en este perı́odo dado por 90*4 =
360 unidades. El tiempo que demora producirlas es de 360/(150-90) = 6 horas. Con eso puede calcular el
nuevo lote mı́nimo:
                                  Q∗2 = Tprod ∗ p = 6 ∗ 150 = 900 unidades
Para determinar el % de utilización se debe obtener el tiempo que demora en producirse las unidades (6
horas previamente calculado) y el tiempo que demora en ser consumidos dado por 900/90 = 10 horas. Con
esto se calcula que el porcentaje de eso es del 60%
Finalmente se determina el inventario máximo dado por:
                           Imax = Tprod ∗ (p − d) = 6 ∗ (150 − 90) = 360 unidades
Y el punto de reorden está dado por:
                                       ROP = d ∗ L = 90 ∗ 4 = 360 horas


                                                               7
Problema 9
Quieres saber cómo se comporta la demanda de latas de bebida en una de las máquinas en ingenierı́a. La
máquina es revisada cada 7 dı́as y las latas son entregadas en el mismo momento de la revisión. Al terminar
una de las revisiones, observaste que la máquina quedo con 485 latas. Ellos utilizan el metodo de periodos
fijos con inventario de seguridad y quieren asegurar que haya bebidas el 95% de las veces. Por otra parte,
supiste que el consumo de la máquina en un mes fue de 630kWh y que la potencia de operación de la máquina
es:
                                             P = 199 + 2NL [W ]
Donde NL el número de latas en la máquina. Obtener promedio y desviación estándar de la demanda diaria.

Solución


Según los datos entregados en el enunciado se sabe que:

                                              q + I = 485 latas
                                               T + L = 7 dias
                                                 Z95 = 1, 65
Junto con esto podemos definir la relación de la cantidad de latas según:
                                                           √
                                           ¯ + L) + zα σ T + L − I
                                      q = d(T                   √
                                                ¯ + L) + zα σ T + L
                                      q + I = d(T               √
                                           485 = d¯ ∗ 7 + 1, 65σ 7
Es necesario encontrar una segunda relación para encontrar los valores pedidos. Podemos calcular la potencia
promedio según el consumo:
                                                 630 kW h
                                        P̄ = 24 horas ∗30 dias
                                                               = 875 W
                                                 dia


Según la formula dada por el enunciado, se puede calcular el número de latas promedio:

                                             875 = 199 + 2 ∗ NL
                                                 NL = 338
El inventario promedio es de 338 latas. Si se calcula el inventario promedio es:
                                              Iprom = d∗T
                                                       2 + SS

Reemplazando:
                                                             √
                                         Iprom = d∗T
                                                   2 + zα σ T √  +L
                                           338 = d∗7
                                                  2  + 1, 65 ∗ σ  7
De las dos ecuaciones planteadas anteriormente se despeja que:

                                                    d¯ = 42
                                                  σ = 43, 80




                                                       8
Problema 10
Una tienda de pinturas utiliza un sistema de inventario bajo incertidumbre para controlar sus niveles de
existencias. Para una pintura de latex amarillo en particular, los datos históricos muestran que la distribución
de la demanda mensual es aproximadamente normal, con una media de 100 latas y 35 latas de desviación
estándar. El tiempo de reaprovisionamiento para esta pintura es de dos meses.
El dueño de la tienda de pintura, dice: ”Quiero estar seguro de que nunca me quedaré sin latas de pintura
de latex de color amarillo. Siempre trato de mantener el suministro de al menos tres meses del promedio
de venta en stock. Cuando mi posición de inventario cae por debajo de ese nivel, ordeno otro suministro de
tres meses. He estado usando este método durante 10 años, y funciona.”
Cada lata de pintura le cuesta a la tienda $10.000. Los costos fijos de reposición son de $50.000 por orden
y costo anual de inventario equivale al 30% del costo unitario. Finalmente el dueño estima que el costo de
una orden no satisfecha es de $8.000 (p).
a) ¿Qué valor de R y Q esta utilizando el dueño de la tienda actualmente? ¿Qué tan grande es el stock de
seguridad?
b) Bajo la polı́tica actual, ¿cuál es la probabilidad de que el inventario no se agote?
c) Encuentre R si el objetivo es que la probabilidad de que el inventario no se agote es del 95 %.
d) El dueño le indica que una vez un consultor trato de cambiar su sistema y le dio una aproximación para
calcular los Q y R optimos para el menor costo total de inventario, los cuales se muestran a continuación:
                                                             q
                                               Q∗ = EOQ = 2DS     H
                                                1 − F (R) = Qh
                                                            pD

Donde F(R) es la probabilidad de que la demanda durante el periodo de reposición sea menor o igual a R.
Calcule los valores de Q y R recomendados por el consultor y la probabilidad de que no se agote el inventario.

Solución


a) Los calculos de R y Q estan definidos por (Siempre quiere tener 3 meses de demanda en stock y cuando
baja de eso, ordena 3 meses más de demanda):
                                               R = 3 ∗ 100 = 300
                                               Q = 3 ∗ 100 = 300
Usando estos valores podemos calcular el stock de seguridad mediante:
                                    R = d ∗ L + SS = 100 ∗ 2 + SS = 300
Despejando se obtiene que:
                                                   SS = 100
b) Para calcular la probabilidad de que el inventario no se agote, resolvemos la siguiente ecuación:
                                                            √
                                             R = d¯ ∗ L + zσ L √
                                        300 = 100 ∗ 2 + z ∗ 35 ∗ 2
                                                  z = 2, 02
Con un z = 2,02 se tiene que la probabilidad es del 97.83%
c) Para una probabilidad de que no se agote el inventario del 95% se tiene un z = 1,65. Con esto resolvemos
la siguiente ecuación:
                                                            √
                                            R = d¯ ∗ L + zσ L √
                                       R = 2 ∗ 100 + 1, 65 ∗ 35 ∗ 2
                                         R = 281, 67 ⇒ R = 282


                                                        9
d) Primero se calcula Q de la forma (Lo haremos anualmente):
                                            q
                                       Q = 2∗100∗12∗50.000
                                                0,3∗10.000 = 200

Usando la formula dada podemos calcular la probabilidad:
                                  F (R) = 1 − 200∗0,3∗10.000
                                               8.000∗12∗100 = 93, 75%

Con esta probabilidad se obtiene un zα = 1, 53. Reemplazando se obtiene que:
                                              √                         √
                              R = d¯ ∗ L + zσ L = 100 ∗ 2 + 1, 53 ∗ 35 ∗ 2
                                                R = 275, 73




                                                  10
