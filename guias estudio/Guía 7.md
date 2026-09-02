                   Pontificia Universidad Católica de Chile
                   Escuela de Ingenierı́a
                   Departamento de Ingenierı́a Industrial y de Sistemas
                   ICS3212 - Gestión de Operaciones
                   Ayudantes: Joaquı́n Gûell (jaguell@uc.cl) y José Rebolledo (jtrebolledo@ing.puc.cl)
                   Primer Semestre 2019




                                     Guı́a de Ejercicios:
                                                   Variabilidad



Problema 1
   Considerando el siguiente proceso:




   Si el proceso 1 tiene un tiempo de proceso de 21 minutos por trabajo y el proceso 2 procesa 3 productos
por hora. Ambos tienen in coeficiente de variación cuadrático de 1, para cada unidad producida, con distribución
exponencial. La capacidad máxima del buffer es ilimitada. No hay restricciones de insumos ni de bodegaje de
productos terminados.
(a) Con esta información determine: ¿Cuál es el throughput en la cola? ¿Cuál es el throughput del proceso completo?
    ¿Cuántas unidades se encuentran en proceso WIP? ¿Cuál es el tiempo de ciclo total (no incluyendo el tiempo
    en insumos)? ¿Cuál es el Work in Process (WIPP)?
(b) La empresa está muy preocupada por los inventarios, ya que corresponden a una parte importante de los costos
    del producto. Para ello está pensando limitar el producto en proceso o en cola a solo 4 unidades. Si el costo
    de mantener una unidad en proceso (WIP) es de $7.000 dólares al año y el margen de cada unidad es de $100
    dólares. Si el proceso trabaja 8 hrs. al dı́a, 5 dı́as a la semana por 50 semanas. ¿Es conveniente realizar el
    cambio? Justifique su respuesta.
(c) Para la situación inicial (no hay lı́mite en la espera) usted se percata que el proceso no sigue una distribución de
    procesos exponencial, sino que más bien una distribución general. ¿Cómo cambian los indicadores del proceso?
    ¿Es mejor o peor que el proceso tenga distribución general?


Solución Problema 1
Parte a
   El proceso corresponde a un M/M/1. La utilización del proceso corresponde a la razón entre la entrada de
productos al sistema y la tasa de salida (entrada es el proceso 1 y la salida el proceso 2)

                                                       1/21
                                                  ρ=        = 0, 9524
                                                       1/20



                                                            1
   Luego, tenemos que el trabajo en proceso en el Buffer 2 es igual al largo del proceso, para ello utilzamos la
ecuaciones de un sistema M/M/1 y determinamos que:

                                                                   ρ
                                            W IP == L                 = 20 Trabajos
                                                                  1−ρ

   Y el throughput (TH) del proceso es igual al throughput del cuello de botella:

                                                         1                trabajos
                                          TH =                  = 0, 0476
                                                     21 minutos           minutos

   Por lo tanto, el tiempo de ciclo (CT o FT) es igual a:

                                                 W IP      20
                                        FT =          =         = 420, 16 minutos
                                                 TH     0, 0476

   Por otro lado, tenemos que el largo de la cola es igual a:

                                             ρ2   (20/21)2
                        W IP P = Lq =           =           = 19, 05 ≈ 19 trabajos en cola
                                            1−ρ   1 − 20/21

   Finalmente, como el proceso es en serie, se tiene que el THcola es igual al throughput del sistema:

                                                                           trabajos
                                                 T Hcola = 0, 0476
                                                                           minutos

Parte b
   Ahora el proceso es M/M/1/b con:

                                      b = 4 elementos en la cola + 2 máquinas = 6

   Tenemos que el número de clientes en el sistema es igual a (recordando que ρ = 0, 9524):

                                             ρ    (b + 1)ρb+1
                                       L=       −             = 2, 805 trabajos
                                            1−ρ     1 − ρb+1
Y el TH del proceso se calcula utilizando la formula de tasa efectiva de clientes para un sistema M/M/1/b:

                                       1 − ρb                      1 − 0, 9524b
                                                                                
                                                         1                                          trabajos
                         λ0 = λ                      =                                 = 0, 04177
                                      1 − ρb+1           21       1 − 0, 9524b+1                    minutos

   Al restringir o bloquear la cola se reduce el throughput a 2,51 trabajos por hora (0, 04177 trabajos/min × 60
min/hora). Esto tiene un impacto de reducir los ingresos anuales:
                                                               
                                                  1
                              Ingresos =            · 60 − 2, 51 · 100 · 8 · 5 · 50 = $69.400
                                                 21

   Se reducen la cola promedio de 19,05 trabajos a 2,805 trabajos por lo que el beneficio anual en:


                                      W IP P = (19, 05 − 2, 805) · $7.000 = $113.715

   Dado que la disminución en el costo de inventario es mayor a la disminución del TH, aplico la medida.


                                                                      2
Parte c
   Para este caso utilizamos la ecuación de Kingman:

                                                            2
                                                              + Ce2
                                                                              
                                                           CA               ρ
                                       CT = V U T =                                  te
                                                              2            1−ρ
   Como este caso, los coeficientes de variabilidad del sistema en ambos casos es igual a 1, tenemos que el término
de variabilidad es igual a 1. Y por consiguiente no hay diferencias en el tiempo de ciclo calculado anteriormente.


Problema 2
   Se tiene una fábrica de pintado pelotas de pool, el cual está compuesto por dos procesos. El primero corresponde
pintar la pelota completa y la segunda a pintar el número en ella (el secado de la pintura se realiza en las máquinas).
Para el primer proceso se tienen dos máquinas en paralelo, mientras que para el segundo sólo se tiene una máquina.
Por otra parte, se tiene un buffer finito antes entre los procesos que tiene una capacidad de 12, (10 en el buffer y 1
en cada máquina). La primera parte toma un tiempo de 4 minutos por unidad, mientras que la segunda máquina
tarda un tiempo de trabajo de 1 minutos en todo lo que debe hacer. Además, se tiene que el proceso es exponencial
(Ce1 = Ce1 = 1). Se le pide calcular en este ejercicio el throughput, el tiempo de proceso y el tiempo de ciclo de
toda la lı́nea.


Solución Problema 2
   Primero se debe calcular la utilización de la segunda máquina, ya que las primeras máquinas se encuentran en
trabajo constante y la llegada de la segunda depende de las primeras máquinas:

                       2 máquinas disponibles en el primer proceso · 1/4 unidad por minuto
                  ρ=                                                                        = 0, 5
                                             1/1 trabajos por minuto

   Se puede calcular los indicadores de la máquina de segundo proceso usando las fórmulas de M/M/1:

                                                  ρ       0, 5
                                        W IP =        =          = 1 trabajos
                                                1−ρ     1 − 0, 5
                                         T H = ra = 1/1 = 1 trabajos/minuto
                                                     W IP      1
                                         CT = F T =        = = 1 minutos
                                                      TH       1
   Ahora, como se tiene un buffer finito, se puede calcular el TH y el WIPP usando M/M1/b, con b = 10 unidades
en cola + 2 procesos:

                                   1 − ρb          1 − 0, 51 2 1
                            TH =       b+1
                                           · ra =             · = 0, 999 trabajos/minutos
                                  1−ρ              1 − 0, 51 3 1
                                                 ρ      (b + 1)ρb+1
                                L = W IP P =          −             = 0, 9984 trabajos
                                               1−ρ        1 − ρb+1
   Por lo tanto, el tiempo de ciclo en todo el proceso corresponde a:

                       W IP P        0, 9984         4 minutos por unidad
              CT =            + te =         +                                       = 2, 9986 minutos
                        TH            0, 998   2máquinas en paralelo en la lı́nea 1
   Por lo tanto, el tiempo de proceso en toda la lı́nea corresponde a:


                                W IP = CT · T H = 2, 9986 · ·0, 999 = 2, 9956 trabajos


                                                             3
Problema 3
    Suponga que los trabajos llegan a una estación a una tasa de 20 por hora y el tiempo promedio de procesamiento
es 2,5 minutos.
(a) ¿Cuál es el nivel de utilización de la estación?
(b) Suponga que el tiempo de arribo y de proceso es exponencial. ¿Cuál es el tiempo medio que un trabajo espera
    en la estación? ¿Cuál es el número promedio de trabajos en la estación? ¿Cuál es la probabilidad de observar
    más de tres trabajos en la estación?
(c) Suponga ahora que el tiempo de proceso no se comporta exponencialmente, presentando una media de 2,5
    minutos y una desviación de 5 minutos. ¿Cuál es el tiempo medio que un trabajo espera en la estación? ¿Cuál
    es el número promedio de trabajos en la estación? ¿Cuál es el número promedio de trabajos en la cola?


Solución Problema 3
Parte a
   El nivel de utilización se calcula como:

                                                          λ     20      5
                                                     ρ=     =         =
                                                          µ   60/2, 5   6

Parte b
   El tiempo medio de espera es:

                                                  1            1
                                         W =            =             = 0, 25 horas
                                               µ(1 − ρ)   24(1 − 5/6)

   El número promedio de trabajos es:

                                                    ρ      5/6
                                             L=        =         = 5 trabajos
                                                   1−ρ   1 − 5/6

   Y la probabilidad de este caso corresponde a:


                                                   P (L ≥= 4) = ρ4 = 0, 482

Parte c
   Se calcula el coeficiente de variación como:

                                                         σ     5 minutos
                                                  Ce =      =              =2
                                                         te   2, 5 minutos

  El tiempo medio de espera en la cola ahora depende de la variabilidad del sistema, por lo cual se calcula por
medio de VUT. Si asumimos que la variabilidad de la entrada (Ca ) es igual a 1, tenemos que:

                             2
                               + Ce2
                                                     2
                                                        1 + 22
                                                                      
                            CA               ρ      1               5/6     1
                CTq =                                 =                        = 31, 25 minutos
                               2            1−ρ     µ      2      1 − 5/6   24
                                       CT = CTq + te = 32, 25 + 2, 5 = 33, 75 minutos



                                                               4
   El número promedio de trabajos en la estación y en la cola es:

                                                                       1 hora
                  L = T H · CT = 20 trabajos/hora · 33, 75 minutos ·             = 11, 25 trabajos
                                                                     60 minutos
                                                                        1 hora
                 Lq = T H · CTq = 20 trabajos/hora · 31, 25 minutos ·            = 10, 42 trabajos
                                                                      60 minutos

Problema 4
    Una máquina que produce circuitos tiene un tiempo medio de proceso por unidad de 2 minutos con una desviación
estándar de 1,5 minutos por unidad.
(a) ¿Cuál es el coeficiente de variación del proceso?
(b) Si los tiempos de proceso de las unidades son independientes, ¿cuál serı́a la varianza de un trabajo compuesto
    por 60 circuitos? ¿Cuál serı́a su coeficiente de variación?
(c) Si la máquina puede fallar y el tiempo entre fallas se distribuye exponencialmente con media de 60 hrs. y un
    tiempo de reparación que también se distribuye exponencialmente con media de 2 hrs. Además, se tiene un
    coeficiente de variación (CV) para la reparación de 1 ¿Cuál es el tiempo medio y el CV de un trabajo compuesto
    de 60 circuitos?
(d) Suponga que se ha estimado que el batch óptimo de ”trabajo”que la máquina realiza es de 60 circuitos. Para
    cambiar de un tipo de circuito a otro se debe realizar un setup que dura aproximadamente 2 hrs y una desviación
    estándar de 0,5 hrs. Para simplificar el proceso productivo, se ha dispuesto que se realicen setups cada 60 hrs.
    de proceso. Con esta información, determine el tiempo medio efectivo de proceso de cada ”trabajo su CV.
                                                                                                        2




Solución Problema 4
Parte a
   El coeficiente de variación en este caso se calcula como:

                                                       σe   1, 5
                                                Ce =      =      = 0, 75
                                                       te    2

Parte b
   La varianza para los 60 circuitos corresponde a:


                                           V ar(T ) = nσ 2 = 60 · 1, 52 = 135

   El coeficiente de variación es:

                                                     σ   1, 5
                                            Ce =     √ = √ = 0, 0968
                                                   te n 2 60

Parte c
   Primero, se debe ordenar toda la información disponible:
                                           tm     60 h    tr = mr       2h
                                           to    2 min    σo          1,5 min
                                           co     0,75




                                                           5
   Es importante conocer la disponibilidad, que se calcula de la siguiente forma:

                                                     tm        60
                                              A=           =        = 0, 968
                                                   tm + tr   60 + 2

   Entonces, el tiempo medio corresponde a:

                                              tm + tr   60 + 2
                                       te =           =        = 64, 07 minutos
                                                A       0, 968

   Y el coeficiente de variación del trabajo para los 60 trabajos, es:

                                                                               mr
                                              Ce2 = c20 + (1 + c2r )A(1 − A)
                                                                               t0
                                                                                    2
                             Ce2 = 0, 09682 + (1 + 12 ) · 0, 0968 · (1 − 0, 0968)     = 0, 0713
                                                                                    2
                                                         Ce = 0, 2671

Parte d
   Primero, se debe calcular el tiempo medio efectivo de proceso de cada trabajo. Esto implica que el número de
setups que se realizaran corresponde a 1 solamente. Por lo tanto, se tiene:

                                                    ts     120
                                       te = t0 +       =2+     = 122 minutos
                                                    Ns      1

   Luego, se debe calcular la desviación estándar que posee el realizar un setup. Esto serı́a:

                                                             σs2   Ns − 1 2
                                               σe2 = σo2 +       +       · ts
                                                             Ns     Ns2
                                                       302  1−1
                                      σe2 = 1, 52 +        + 2 · 1202 = 902, 25
                                                        1    1
   Por lo tanto, para obtener el coeficiente de variación:

                                                       σe2   902, 25
                                               Ce2 =       =         = 0, 0606
                                                       t2e    1222
                                                         Ce = 0, 2462




                                                               6
Problema 5
   Considere el sistema productivo que se muestra en la figura:




    En este sistema se procesan órdenes para dos productos: P1 y P2. Ambos siguen rutas diferentes en la red.
P1 usa la estación E1 y después continúa a E2, y P2 usa la estación E1 y después continúa a E3. Cada estación
tiene un buffer con capacidad Ci ; i = 1, 2, 3 (el triángulo invertido antes de cada estación). Cada estación tiene una
capacidad de producción expresada en una tasa máxima posible de µi , i = 1, 2, 3 órdenes por hora. Al sistema llegan
para proceso órdenes del producto P1 a una tasa de λ1 órdenes por hora y para el producto 2 a una tasa λ2 órdenes
por hora. Cada uno de los tiempos entre llegada de cada tipo de orden tiene una variabilidad expresada por un
coeficiente de variación si , i = 1, 2 y el tiempo de procesamiento en cada estación también posee una variabilidad
expresada por un coeficiente de variación ei , i = 1, 2, 3.
    Un problema muy relevante en un sistema productivo es poder estimar cuanto será el leadtime para la entrega
de una orden; es decir, el tiempo desde que una orden llega al sistema hasta que es terminada. Este es, básicamente,
el tiempo de cumplimiento que se promete al cliente.
(a) Asumiendo que las capacidades de los buffers son suficientemente grandes como para nunca llenarse y producir
    bloqueos (es decir, el supuesto de çapacidad infinita”), calcule un estimador del leadtime promedio para cada
    uno de los tipos de productos. (Puede dejar términos intermedios expresados, pero sea claro en lo que escribe
    y explique los supuestos que haga).
(b) En la pregunta anterior, usted calculó solo un estimador del tiempo medio de flujo, pero en la realidad uno
    estará interesado en un estimado para el momento en que llega una orden y según las condiciones del sistema
    productivo en ese momento particular. Su ponga que llega una orden para el 5 producto P2 y en este momento
    hay f (1) órdenes de P (1) y f (2) órdenes de P (2) en espera en la estación E1, g órdenes de P1 en espera en
    la estación E2 y h órdenes de P2 en espera en la estación E3. Explique cómo calcular un estimador para el
    tiempo de entrega de la orden recién llegada. (Use, si quiere, lo que ya ha calculado y otras cosas adicionales y
    supuestos que considere adecuados, pero explique todo con claridad).


Solución Problema 5
Parte a
   Haremos uso de la fórmula de Kingman para estimar el tiempo medio de espera en cola en cada una de las
estaciones. Esto requiere calcular el coeficiente de variabilidad a la salida de E1 y para eso usaremos la fórmula de
propagación de variabilidad. Primero notemos que los coeficientes de congestión en cada estación son:
                                     ρ = λ1µ+λ
                                             1
                                               2
                                                          ρ2 = µλ12        ρ3 = µλ23
    Lo anterior supone que las tasas son tales que ρ1 < 1, i = 1, 2, 3. Denotemos por Li el tiempo medio de espera en
el sistema de la estación i. Primero debemos ver cuál es la variabilidad de la llegada a E1. Los dos tipos de órdenes
tiene tiempos de llegada con variabilidad s1 y s2 , la variabilidad combinada es igual a:


                                                            7
                                                     λ1           λ2
                                             s=           s1 +         s2
                                                  λ1 + λ2      λ1 + λ2

   Tenemos, entonces:

                                         2
                                         s + e21
                                                              
                                                       ρ1      1    1
                                   L1 =           ·          ·    +
                                            2        1 − ρ1    µ1   µ1

   El coeficiente de variación de la salida podemos estimarlo como:


                                             (s)2 = ρ21 (e22 ) + (1 − ρ21 )(s)2

   Y este se preserva igual tanto hacia la estación E2 como hacia E3. Con esto tenemos que:

                                         2
                                         s + e22
                                                              
                                                       ρ2      1    1
                                   L2 =           ·          ·    +
                                            2        1 − ρ2    µ2   µ2
                                         2    2
                                                              
                                         s + e3        ρ3      1    1
                                   L3 =           ·          ·    +
                                            2        1 − ρ3    µ3   µ3

   Luego, el leadtime medio para las órdenes tipo 1 es L1 + L2 y el de las órdenes tipo 2 es el L1 + L3 .

Parte b
  En las condiciones dadas, podrá estimarse el tiempo medio exactamente como el indicado en la parte (a). Sin
embargo hay en parte un error en esto y es que esas son cantidades promedios.
   Si se sabe que hay ciertas cantidades en cola, esa
                                                    información
                                                                 es útil. En particular, si hay f1 órdenes de P1 y
                                                      1
f2 de P2, esas tardaran, en promedio (f1 + f2 ) × µ1 en ser procesadas y en total la nueva orden requerirá en
                          
promedio (f1 + f2 + 1) × µ11 en ser liberada a la siguiente etapa (suponemos que hay una orden en proceso en la
estación). De este modo, dependiente del tipo de orden, tenemos que los Lead-times promedios serán:
     Si la orden es de P1:
                                                                                             
                                                                1                          1
                                          (f1 + f2 + 1) ×                + (g + 1) ×
                                                                µ1                         µ2

     Si la orden es de P2:
                                                                                             
                                                                1                          1
                                          (f1 + f2 + 1) ×                + (h + 1) ×
                                                                µ1                         µ3

Problema 6
   Se tiene la siguiente lı́nea de producción con dos estaciones de trabajo y dos buffers:




                                                             8
   Las órdenes llegan a una tasa de 12 órdenes por hora con una distribución G/G/1 y tienen un coeficiente de
variación entre tiempos de llegada de 1,1.
   E1 tiene un tiempo medio de procesamiento de 4 minutos con coeficiente de variación de 0,7. E2 tiene 4,2 minutos
con coeficiente de variación de 1. La capacidad de los buffers es infinita
   Calcule el tiempo total del ciclo y largo medio de las colas.


Solución Problema 6
   Del enunciado podemos obtener las siguientes tasas de llegada de ordenes:

                                                                   órdenes
                                                         λ1 = 12
                                                                      hora
                                                                    órdenes
                                                         λ1 = 0, 2
                                                                    minutos
   Adicionalmente, tenemos que la máquina E1 tiene los siguientes parámetros:

                                                           1         ordenes
                                                   µ1 =      = 0, 25
                                                           4         minuto
                                                           CVE1 = 0, 7

   Y en la máquina E2 tenemos los siguientes parámetros:

                                                           1           ordenes
                                                  µ2 =         = 0, 24
                                                          4, 2         minuto
                                                             CVE2 = 1

   Con estos datos, tenemos que el tiempo de cico se obtiene de la siguiente fórmula:

                                                                   Ca2 + Ce2
                                                                                      
                                                                                    ρ     1
                      Ciclo de tiempo = CTq = F Tq =                            ·       ·    = V UT
                                                                       2           1−ρ    µ

   Máquina E1
   Para esta máquina tenemos que la utilización (ρ) es igual a:

                                                            λ    0, 2
                                                     ρ=       =       = 0, 8
                                                            µ   0, 25

   Adicionalmente, sabemos que la variación de la llega de órdenes es igual a 1,1. Entonces, el tiempo de ciclo es
igual a:

                                         1, 12 + 0, 72
                                                                           
                                                               0, 8         1
                          F Tq,1 =                        ·            ·          = 13, 6 minutos
                                               2             1 − 0, 8     0, 25

   Para el largo de la cola:


                                                             L=λ·W

   Por lo tanto,



                                                                   9
                                              L1 = 0, 20 · 13, 6 = 2, 72 minutos

   Máquina E2
   Primero se debe determinar la variación de entrada de la estación 2 que corresponde a la de salida de la estación
1 y puede estimarse con la siguiente fórmula:


                                                 Cs2 ≈ ρ2 (Ce )2 + (1 − ρ2 )Ca2

   Obtenemos entonces,


                                    Cs2 ≈ 0, 82 (0, 7)2 + (1 − 0, 82 )1, 12 = 0, 749 = Ca2

   Este Ca obtenido es del proceso 2. Adempas del proceso tenemos que:

                                                                 λ2    0, 2
                                            Utilización = ρ =      =       = 0, 83
                                                                 µ2   0, 24

   Entonces, el tiempo de ciclo del proceso 2 es:

                                        0, 7492 + 12
                                                                          
                                                             0, 83         1
                         F Tq,2 =                       ·             ·          = 15, 88 minutos
                                              2            1 − 0, 83     0, 24

   Para la cola,


                                                L2 = 0, 2 · 15, 88 = 3, 18 min

   Por lo tanto, el tiempo de ciclo total es:


                   Tiempo de ciclo total = Tiempo MedioE1 + Tiempo MedioE2 + F Tq,1 + F Tq,2
                         Tiempo de ciclo total = 4 + 4, 2 + 13, 6 + 15, 88 = 37, 68 minutos


Problema 7
    Un sistema productivo consiste en dos estaciones de trabajo conectadas en serie, E1 y E2, como muestra. La
figura. Frente a cada estación existen áreas de almacenamiento (buffers), B1 y B2.




    Las órdenes para procesar llegan a E1 (esperan en el buffer, si es necesario) son procesadas y pasan a E2. Si B2
se llena, entonces E1 debe parar y no puede seguir procesando e, igualmente, si B1 se llena, el sistema no puede
recibir nuevas órdenes. Tanto E1 como E2 pueden procesar 55 órdenes por hora, pero son procesos variables. El
coeficiente de variación de cada uno es de un 50 %. Las órdenes llegan a este sistema a una tasa promedio de 50
órdenes por hora, con una variación de un 50 %.



                                                               10
(a) Suponiendo primero que los buffers tienen “capacidad infinita”, determine aproximadamente cuánto serı́a el
    inventario en espera en estos y el tiempo medio de flujo estimado para una orden desde que entra hasta que
    sale del sistema.
(b) Suponga ahora que el buffer en E2 (es decir, B2) tiene una capacidad igual al valor del inventario en B2 estimado
    por usted en a), mientras que B1 sigue con capacidad infinita. ¿Qué pasarı́a con el tiempo de flujo en el sistema?
    ¿Por qué? (No se requieren cálculos numéricos)
(c) Luego de analizar exhaustivamente el inventario se aprecia que si el segundo buffer tuviera capacidad igual al
    inventario promedio, entonces se llenará un 5 % de las veces. Estime cuanto aumentará el tiempo de fujo de las
    órdenes en el sistema, si la capacidad del B1 sigue siendo infinita.
(d) Usted también ha decidido definirle una capacidad al primer buffer igual a la cantidad calculada en el punto
    anterior, y que denotaremos por C, de modos que ambos buffers tienen la misma capacidad. ¿Qué pasará
    ahora con el tiempo de fujo total? ¿Qué pasará con el throughtput neto del sistema? (No se requieren cálculos
    numéricos)


Solución Problema 7
Parte a
   Aquı́ hay que usar las relaciones de las “Fı́sica de la Fábrica”:

                                                                            Ca2 + Ce2
                                                                                               
                                                                                             ρ     1
                          Ciclo de tiempo = CTq = F Tq =                                 ·       ·
                                                                                2           1−ρ    µ

   Y la propagación de variabilidad es:


                                                    Cs2 ≈ ρ2 (Ce )2 + (1 − ρ2 )(Ca2 )

   Para E1 los coeficientes de variación son 0,5. Tenemos además que ρ = 50
                                                                              
                                                                           55 = 0, 91. Luego el tiempo de espera
en B1 se puede estimar como:

                                    0, 52 + 0, 52
                                                                 
                                                          0, 91      1
                       F Tq =                        ·             ·    = 0, 0459 ≈ 2, 75 minutos
                                          2             1 − 0, 91    55

   Por la fórmula de Little, el inventario promedio en B1 se puede estimar en 50 × 0, 0459 = 2, 3 unidades.
    Ahora notemos que como la variación del servidor E1 y la de la entrada es la misma e igual a 0,5. Esta relación
también se repite en los coeficientes de variación de los procesos. Además, tenemos que la tasa de llegada λ sigue
siendo el mismo, el cálculo para E2 es también el mismo. El tiempo de servicio promedio en E1 o E2 es de µ1 , es
decir, 0,018 horas que equivale a 1,09 minutos. Sumando tanto el tiempo de servicio como de espera que tenemos
que el tiempo de flujo total se puede estimar en 7,68 minutos (2,75+1,09+2,75+1,09).

Parte b
    Ahora vamos a poner un buffer con capacidad de aproximadamente 3 unidades. Esto va a producir que cuando
el buffer se llene, E1 tenga que parar. Cuando eso pasa, la cola de E1 aumenta, y este aumento si es significativo,
el tiempo de flujo puede aumentar.

Parte c
   Podemos estimar que el buffer se llena un 5 % del tiempo, entonces E1 se parará un 10 % del tiempo, es decir
su productividad disminuirá en un 5 %. Esto es válido, desde luego, suponiendo que E1 esté ocupado siempre que,
dado que ρ es alto, esto es un supuesto razonable. De este modo, la tasa de servicio de E1 deberı́a disminuir a un


                                                                   11
                                                                                                 50
95 % de su valor original, es decir, a 52,25 unidades por hora. Con esto, el nuevo ρ es igual a 50,25 = 0.957. El nuevo
tiempo de espera en B1 es:

                                   0, 52 + 0, 52
                                                                        
                                                         0, 957         1
                     F Tq∗ =                        ·              ·           = 0, 106 ≈ 6, 39 minutos
                                         2             1 − 0, 957     52, 25

   El tiempo original en B1 era de 2,75 minutos ahora existe un aumento de 3.61 minutos.

Parte d
    Si ahora se restringe además B1 el resultado será que se producirá un fuerte rechazo de órdenes a la entrada del
sistema. Esto se traduce en que el through-put neto de sistema podrı́a disminuir de forma significativa.


Problema 8
    Actualmente el banco posee dos cajeros y está considerando contratar a una tercera persona. Las personas llegan
al banco con un promedio de 1 cada 10 minutos, y cada persona requiere en promedio 5 minutos para ser atendido.
Supongamos que las personas arriban de acuerdo a una distribución Poisson y que el tiempo necesario para prestar
el servicio distribuye exponencial.
(a) Determine la razón de utilización del sistema.
(b) ¿Cuál serı́a el efecto sobre la lı́nea de espera si se contrata a una tercera persona como cajero?


Solución Problema 8
Parte a
   De los datos entregados por el enunciado, obtenemos que λ = 1 clientes por minuto. Y que cada cajero puede
atender a un cliente en 5 minutos. Entonces la utilización es igual a:

                                                                                     clientes
                                                             λ                 0.1 minuto
                         Utilización = ρ =                                =                   = 0, 25
                                                    Número de cajeros · µ   2 · 0, 2 clientes
                                                                                       minuto


Parte b
   Para calcular el efecto sobre la cola de agregar un tercer cajero, calculamos Lq para conocer el número de cliente
en cola:

                                                 λ2            0, 12
                                       Lq =            =                   = 0, 5 clientes
                                              µ(µ − ρ)   0, 2(0, 2 − 0, 1)

   Claramente no se justifica contratar a otro cajero dado que el sistema está subutilizado, lo podemos ver en el
tiempo de espera y el número de clientes en un momento dado. En promedio un cliente espera 5 minutos y nunca
hay más de un cliente en la cola.




                                                                  12
