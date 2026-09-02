                      Pontificia Universidad Católica de Chile
                      Escuela de Ingenierı́a
                      Departamento de Ingenierı́a Industrial y de Sistemas
                      ICS3212 – Gestión de Operaciones
                      Ayudantes: René Acuña (rtacuna@uc.cl) y Esteban Brito (eabrito@uc.c)
                      Primer Semestre 2018



                                              Guı́a de Ejercicios:
                                            Variabilidad y Calidad
   Esta guı́a concentra material pasado de guı́as y pruebas anteriores. Se recomienda, para potenciar el estudio, revisar en
Siding semestres anteriores disponibles.


Variabilidad
Problema 1
Un promedio de 10 automoviles por hora llegan a un cajero con un solo servidor que proporciona un servicio sin que uno
descienda del automovil. Suponga que el tiempo de ciclo promedio por cada cliente es de 4 minutos, y que tanto los tiempos
entre llegadas como los tiempos de servicio son exponenciales.

a) ¿Cual es la probabilidad de que el cajero este ocioso?
b) ¿Cual es el numero promedio de autos que estan en la cola del cajero? (Considerar que un automovil que esta siendo
   atendido no esta en la cola esperando)
c) ¿Cual es la cantidad promedio de tiempo que un cliente pasa en el estacionamiento del banco (incluyendo el tiempo de
   servicio)?
d) ¿Cuantos clientes atendera en promedio el cajero por hora?

Solución problema 1
a) Se denominará π0 a la probabilidad de que el cajero este atendiendo a 0 personas:

                                                            λ     10    2  1
                                         π0 = 1 − ρ = 1 −     =1−    =1− =
                                                            µ     15    3  3
Por lo tanto, el cajero esta vacı́o un tercio del tiempo.

b) El numero promedio de autos en la cola es:

                                                      ρ2   ( 2 )2 4
                                              Lq =       = 3 2 = clientes
                                                     1−ρ  1− 3    3

c) El tiempo que una persona pasa en el sistema, incluyendo el servicio, es:
                                                           2
                                                      ρ
                                               L=        = 3 2 = 2 clientes
                                                     1−ρ  1− 3

                                                       L     2   1
                                                   W =   =     = horas
                                                       λ    10   5
d) Si el cajero siempre estuviese ocupado, atenderia un promedio deµ = 15 clientes por hora. Pero de a. sabemos que solo
esta ocupado dos tercios del tiempo. Por lo tanto, durante cada hora, el cajero atendera un promedio de:
                                                      2
                                                        ∗ 15 = 10 clientes
                                                      5


                                                               1
Problema 2
Actualmente el banco posee dos cajeros y esta considerando contratar a una tercera persona. Las personas llegan al banco
con un promedio de 1 cada 10 minutos, y cada persona requiere en promedio 5 minutos para ser atendido. Supongamos
que las personas arriban de acuerdo a una distribucion Poisson y que el tiempo necesario para prestar el servicio distribuye
exponencial.

a) Determine la razon de utilizacion del sistema.
b) ¿Cual seria el efecto sobre la linea de espera si se contrata a una tercera persona como cajero?

Solución problema 2
a) La razon de utilizacion esta dada por la ecuacion:

                                                     λ       6clientes/hora
                                             ρ=         =
                                                    s∗µ   2 ∗ 12clientes/hora

El sistema estara ocioso un 75% del tiempo
b) ara calcular el efecto sobre la cola de agregar un tercer cajero, se debe calcular Lq para conocer el numero de cliente en
cola:
                                           λ              6
                                 wq =            =                = 0.0833 horas = 5 minutos
                                        µ(µ − λ)    12 ∗ (12 − 6)
Claramente no se justifica contratar a otro cajero dado que el sistema esta subutilizado, lo podemos ver en el tiempo de
espera y el numero de clientes en un momento dado. En promedio un cliente espera 5 minutos y nunca hay mas de un
cliente en la cola.

Problema 3
Una maquina que produce unidades con un tiempo medio de proceso de 2 minutos con una desviacion estandar de 1,5
minutos por unidad.

a) ¿Cual es el coeficiente de variacion del proceso?
b) Si los tiempos de proceso de las unidades son independientes, ¿cual seria la varianza de la produccion de 60 unidades?
   ¿Cual seria su coeficiente de variacion?
c) Si la maquina puede fallar y el tiempo entre fallas distribuye exponencialmente con media de 60 horas, y un tiempo de
   reparacion que tambien distribuye exponencialmente con media de 2 horas. ¿Cual es el tiempo medio y el coeficiente de
   variacion para la produccion de 60 unidades?

Solución problema 3
a) El coeficiente de variacion del proceso esta dado por:
                                                          σ   1.5
                                              CT =          =     = 0.75 minutos
                                                          t    2
b) La produccion se compone de proceso independientes, asi, la la varianza de la produccion de 60 unidades se puede
calcular como:
                                            X60
                                     V ar =     σi2 = 60σi2 = 60 ∗ 1.52 = 125
                                                    i=1
                                                          √
                                                       135
                                              CT =         = 0.0968 minutos
                                                    2 ∗ 60
c) Primero se calcula la disponibilidad de la maquina:
                                                      mf        60
                                            A=              =        = 96.77%
                                                    ma + mf   2 + 60



                                                                 2
Luego,el tiempo medio efectivo en que esta funcionando la maquina es:
                                                    t       60
                                             te =     =2∗        = 124 minutos
                                                    A     0.9677
Finalmente, se calcula el coeficiente de variacion segun la relacion:
                                                                                       ma
                                            c2e = c2o + (1 + c2a ) ∗ A ∗ (1 − A) ∗
                                                                                        t
Donde ca = 1 porque las llegadas distribuyen exponenciales, ası́:
                                                                                            2
                                c2e = 0.09682 + (1 + 12 ) ∗ 0.9677 ∗ (1 − 0.9677) ∗           = 0.07188
                                                                                            2
                                                             √
                                                ce = 60 ∗        0.07188 = 16, 0867

Problema 4
Un sistema productivo consiste en dos estaciones de trabajo conectadas en serie, E1 y E2. Se muestra la disposición en la
siguiente figura:




    Frente a cada estación existen áreas de almacenamiento (buffers), B1 y B2. Las órdenes a procesar llegan a E1 (esperan
en el buffer, si es necesario) son procesadas y pasan a E2. Si B2 se llena, entonces E1 debe parar y no puede seguir
procesando e, igualmente, si B1 se llena, el sistema no puede recibir nuevas órdenes. Tanto E1 como E2 pueden procesar
30 órdenes por hora, pero son procesos variables. El coeficiente de variación de cada uno es de un 40%. Las órdenes llegan
a este sistema a una tasa promedio de 25 órdenes por hora, con una variación de un 40%.

a) Suponiendo primero que los buffer tienen capacidad infinita, determine aproximadamente cuánto serı́a el inventario en
   espera en estos y el tiempo medio de flujo estimado para una orden desde que entra hasta que sale del sistema.
b) Suponga ahora que el buffer en E2 (es decir, B2) tiene un capacidad igual al valor del inventario en B2 estimado por
   usted en a), mientras que B1 sigue con capacidad infinita. ¿Qué pasará con el tiempo de flujo en el sistema? ¿Por qué?
c) Luego de analizar exhaustivamente el inventario se aprecia que si el segundo buffer tuviera capacidad igual al inventario
   promedio, entonces se llenará un 5% de las veces. Estime cuanto aumentará el tiempo de flujo de las órdenes en el
   sistema, si la capacidad del B1 sigue siendo infinita.
d) Usted también ha decidido definirle una capacidad al primer buffer igual a la cantidad calculada en el punto anterior, y
   que denotaremos por C, de modos que ambos buffers tienen la mismas capacidad. ¿Qué pasará ahora con el tiempo de
   flujo total?¿Qué pasará con el throught-put neto del sistema? (No se requieren cálculos numéricos)

Solución problema 4
a) Considere:
                                                           (c2a + c2e )    ρ   1
                                                 F Tq =                 ∗    ∗
                                                                2         1−ρ µ
                                                    c2s ≈ ρ2 ∗ c2e + (1 − ρ2 ) ∗ c2a
Para E1 los coeficientes de variación es 40%. El rho es igual a velocidad de llegada/capacidad, es decir:
                                                              25
                                                                 = 0, 83
                                                              30
El tiempo de espera en B1 es entonces 1,56 minutos. Aplicando Little se tiene que:

                         25 ∗ 0, 026 = 0, 65 unidades como inventario promedio esperando en B1.


                                                                   3
El coeficiente de variación en E1 y en la llegada es similar, y además la tasa de llegada se mantiene para E2. El tiempo de
estadı́a en el servidor en E1 es la inversa de la tasa de atención, es decir 1/30. Dado que E1 y E2 tienen iguales capacidades
e iguales variabilidades, sus tiempos son similares. Ası́ el tiempo estimado en sistema es:
                                         2
                                           + 2 ∗ 0, 026(espera B1+B2) = 7.12 minutos
                                        30
b) Si B2 tiene capacidad limitada, cuando alcance su lı́mite, E1 deberá parar. Si es ası́ la cola en B1 seguirá creciendo.
Esto tenderı́a a aumentar el tiempo de estadı́a del sistema.

c) Podemos estimar que el buffer se llena un 5% del tiempo, entonces E1 se parará un 10% del tiempo, es decir su
productividad disminuirá en un 5%. Esto es válido, desde luego, suponiendo que E1 esté ocupado siempre que dado que
ρ es alto, esto es un supuesto razonable. De este modo, la tasa de servicio de E1 deberı́a disminuir a un 95% de su valor
original, es decir, a 28,5 unidades por hora. COn esto se tiene que:
                                                             25
                                                       ρ=         = 0, 877
                                                            28, 5
El nuevo tiempo de espera en B1 es 0,037 horas, aproximadamente 2,25 minutos. Se puede verificar un aumento del tiempo
en sistema.

d) Si ahora se restringe además B1 el resultado será que se producirá un fuerte rechazo de órdenes a la entrada del
sistema. Esto se traduce en que el through-put neto de sistema podrı́a disminuir de forma significativa.

Problema 5
Un consultorio de salud primaria atiende pacientes que llegan a una tasa media igual a 10 pacientes por hora. La distribución
de probabilidad de tiempo entre llegadas no es conocida pero se ha estimado que su desviación estandar es igual a 5 minutos.
Los pacientes son atendidos por un equipo de médicos, despues de ser fichados por una enfermera. La enfemera tarda 2
minutos en fichar a los pacientes, siento ese tiempo muy exacto. Un médico tarda, en promedio, 15 minutos en atender un
paciente y ese tiempo de atención tiene una variacion de un 70%. A la administración del consultorio le interesa determinar
el número de médicos que debe tener de modo que el tiempo medio estimado de espera de los pacientes para ver algñun
médico (después de ser fichados) no supere 30 minutos:
a) Utilice las relaciones fı́sicas de la fábrica para escribir una expresión que permita estimar cuántos médicos se necesitan
   para cumplir con el requerimiento de la administración del consultorio. Sea claro y justifique sus argumentos. (Si bien,
   este es un sistema con ervidores paralelos, puede simplificar la situación a un sólo servidor con una tasa de atención
   equivalente adecuada según el número de médicos, y variabilidad también adecuada a esa situación)
b) ¿Cuántos pacientes, en promedio, están esperando?¿Es correcto usar este número para definir el número de silla a tener
   en la sala de espera? Explique

Solución problema 5
a) Sea λ la tasa de llegada de pacientes y µ la tasa de servicio de un médico. Notemos que sólo es relevante el tiempo después
del fichaje, por la forma en que está redactada la pregunta. Podemos considerar un sistema equivalente con n médicos y
que da una tasa de atención igual a nµ. El coeficiente de variación para un médico es 0.7, lo que √
                                                                                                     da un σ = 10.5 minutos. Si
tenemos n médicos, la desviación estandar el tiempo de atención √ del  conjunto equivalente es σ/   n. Luego el coeficiente de
variación del tiempo de atención del conjunto n médicos es 0.7/ n. Por otro lado, el sistema equivalente tiene un coeficiente
de ocupación igual a:
                                                                λ     2.5
                                                         ρe =      =
                                                               nµ      n
El coeficiente de variación de la llegada es ca = 0.83. COn esto podemos usar la fórmula para estimar el tiempo medio de
espera en cola en función del número de médios:
                                                        (c2a + c2e )     ρe    1
                                                 CT ≈                ∗       ∗
                                                             2         1 − ρe µ
donde el subı́ndice e indica los parámetros para el modelo equivalente. Esta formula se reduce a:
                                                   (0.832 + n(0.7)2 )     2.5    15
                                            CT ≈                      ∗        ∗
                                                           2            n − 2.5 n

                                                                4
Basta determinar n tal que:
                                                         CT (n) ≤ 30
b) Se calcula la ecuación de Little, con el n determinado en a:

                                                       L(n) = λ ∗ CT (n)

Usar ese número de sillas no es correcto ya que corresponde sólo al promedio y no se está tomando en cuenta la variabilidad,
que puede ser mucha especialmente si hay un alto nivel de ocupación. Esto significa que una gran cantidad de personas
podrı́an quedar de pie, no muy presentable si se trata de un consultorio de salud.

Problema 6
Considere el sistema productivo que se muestra en la figura:




     En este sistema se procesan órdenes para dos productos: P1 y P2. Ambos siguen rutas diferentes en la red. P1 usa
la estación E1 y después continúa a E2, y P2 usa la estación E1 y después continúa a E3. Cada estación tiene un buffer
con capacidad Ci ; i=1,2,3 (el triángulo invertido antes de cada estación). Cada estación tiene una capacidad de producción
expresada en una tasa máxima posible de µi , i=1,2,3 , ordenes por hora. Al sistema llegan para proceso órdenes del pro-
ducto P1 a una tasa de λ1 ordenes por hora y para el producto 2 a una tasa λ2 órdenes por hora. Cada uno de los tiempos
entre llegada de cada tipo de orden tiene una variabilidad expresada por un coeficiente de variación si , i = 1,2 y el tiempo
de procesamiento en cada estación también posee una variabilidad expresada por un coeficiente de variación ei , i = 1,2,3.
Un problema muy relevante en un sistema productivo es poder estimar cuanto será el lead -time para la entrega de una
orden; es decir, el tiempo desde que una orden llega al sistema hasta que es terminada. Este es, básicamente, el tiempo de
cumplimiento que se promete al cliente. En este problema desarrollaremos ese concepto.


a) Asumiendo que las capacidades de los buffers son suficientemente grandes como para nunca llenarse y producir bloqueos
   (es decir, el supuesto de ”capacidad infinita”), calcule un estimador del lead-time promedio para cada uno de los tipos
   de productos. (Puede dejar términos intermedios expresados, pero sea claro en lo que escribe y explique los supuestos
   que haga).
b) En la pregunta anterior, usted calculó solo un estimador del tiempo medio de flujo, pero en la realidad uno estará
   interesado en un estimado para el momento en que llega una orden y según las condiciones del sistema productivo en
   ese momento particular. Su ponga que llega una orden para el 5 producto P2 y en este momento hay f(1) órdenes de
   P(1) y f(2) órdenes de P(2) en espera en la estación E1, g órdenes de P1 en espera en la estación E2 y h órdenes de P2
   en espera en la estación E3. Explique cómo calcular un estimador para el tiempo de entrega de la orden recién llegada.
   (Use, si quiere, lo que ya ha calculado y otras cosas adicionales y supuestos que considere adecuados, pero explique todo
   con claridad).

Solución problema 6
a) Haremos uso de la fórmula de Kingman para estimar el tiempo medio de espera en cola en cada una de las estaciones.
   Esto requiere calcular el coeficiente de variabilidad a la salida de E1 y para eso usaremos la fórmula de propagación de
   variabilidad. Primero notemos que los coeficientes de congestión en cada estación son:
                                                       λ1 + λ2      λ1      λ2
                                                ρ1 =           ρ1 =    ρ1 =                                                (1)
                                                         µ1         µ2      µ3
   Lo anterior supone que las tasas son tales que ρ1 < 1, i= 1,2,3. Denotemos por L(i) el tiempo medio de espera en el
   sistema de la estación i. Primero debemos ver cuál es la variabilidad de la llegada a E1. Los dos tipos de órdenes tiene


                                                               5
   tiempos de llegada con variabilidad s1 y s2 , la variabilidad combinada es igual a:
                                                             λ1           λ2
                                                   s̄ =           s1 +         s2                                       (2)
                                                          λ1 + λ2      λ1 + λ2
   Tenemos entonces:
                                                         s̄2 + e1 2     ρ1    1   1
                                                L1 =                ∗       ∗   +                                       (3)
                                                             2        1 − ρ1 µ1   µ1
   El coeficiente de variación de la salida podemos estimarlo como:

                                                    s̄2 = ρ21 ∗ e22 + (1 − ρ21 ) ∗ s̄2                                  (4)

   Y este se preserva igual tanto hacia la estación E2 como hacia E3. Con esto tenemos que:

                                                         s̄2 + e2 2     ρ2    1   1
                                                L2 =                ∗       ∗   +                                       (5)
                                                             2        1 − ρ2 µ2   µ2

                                                         s̄2 + e3 2     ρ3    1   1
                                                L3 =                ∗       ∗   +                                       (6)
                                                             2        1 − ρ3 µ3   µ3
   Luego, el lead-time medio para las órdenes tipo 1 es L1 + L2 y el de las órdenes tipo 2 es el L1 + L3 .

b) En las condiciones dadas, podrá estimarse el tiempo medio exactamente como el indicado en la parte a). Sin embargo
   hay en parte un error en esto y es que esas son cantidades promedios. Si se sabe que hay ciertas cantidades en cola, esa
   información es útil. En particular, si hay f1 órdenes de P1 y f2 de P2, esas tardaran, en promedio:
                                                                            1
                                                             (f1 + f2 ) ∗                                               (7)
                                                                            µ1
   En ser procesadas y en total la nueva orden requerirá en promedio:
                                                                             1
                                                           (f1 + f2 + 1) ∗                                              (8)
                                                                             µ1

   En ser liberada a la siguiente etapa (suponemos que hay una orden en proceso en la estación). De este modo, dependiente
   del tipo de orden, tenemos que los Lead-times promedios serán: Si la orden es de P1:
                                                                   1              1
                                                 (f1 + f2 + 1) ∗      + (g + 1) ∗                                       (9)
                                                                   µ1             µ2
   Si la orden es de P2:
                                                                   1              1
                                                 (f1 + f2 + 1) ∗      + (h + 1) ∗                                     (10)
                                                                   µ1             µ3

Problema 7
Una fábrica de pastas de Santiago tiene un tiempo medio de proceso por caja producida de 2 minutos con una desviación
estándar de 0,2 minutos por caja. Le piden que los ayude con algunas dudas, por favor responda:
a) ¿Cuál es el coeficiente de variación del proceso?

b) Si los tiempos de proceso de las unidades son independientes, ¿Cuál serı́a la varianzade la producción de 30 cajas? ¿y
   su coeficiente de variación?
c) La maquina que produce las pastas, presenta fallas. El tiempo entre fallas distribuye exponencialmente con media de
   60 horas y un tiempo de reparación con la misma distribución, con media de 1 hora. ¿Cuál es el tiempo medio y el CV
   para la producción de 200 cajas de pasta?




                                                                  6
Solución problema 7
a)
                                                            σ    0.2
                                                        C(t) ==                                                             (11)
                                                            t     2
b) La varianza es igual a la varianza acumulada de las unidades independientes:
                                                       30 ∗ (0.2)2 = 1.2                                                    (12)
El coeficiente de variación es:
                                                           1.2( 1/2)
                                                  C(t) =             = 0.01825                                              (13)
                                                            2 ∗ 30
c) El tiempo de utilización de maquina es:
                                                   mf        60
                                                         =        = 0, 9836                                                 (14)
                                                 mr + mf   60 + 1
El tiempo efectivo de funcionamiento para fabricar las 200 cajas es el tiempo sin fallo afectado por la disponibilidad.
Entonces el tiempo efectivo, te, es t/A, 2*200/0,9836 = 407 minutos aproximadamente para producir las 200 cajas.
El coeficiente de variación responde a la formula:
                                                                                    mr
                                             c2e = c2o + (1 + c2r ) ∗ A ∗ (1 − A) ∗                                (15)
                                                                                     t
Con c(0) igual a 0,1 y con c(r)= 1, por su distribución exponencial, el coeficiente de variación es 0,0169.

Problema 8
Un banco considera si debe abrir una ventanilla para el sercicio a clientes. La administración estima que los clientes llegarán
con una tasa de 15 por hora. El cajero que atenderá la ventanilla puede atender a los clientes con una rapidez de uno cada
tres minutos.
Suponiendo llegadas Poisson y un servicio exponencial, encuentre:
a) La utilización del cajero
b) El número promedio en la fila de espera.
c) El número promedio en el sistema.
d) El tiempo promedio de espera en la fila.
e) El tiempo promedio de espera en el sistema, incluyendo el servicio.

Solución problema 8
Tenemos que:
                                                           clientes
                                                        λ = 15                                                              (16)
                                                             hora
                                                           clientes
                                                    µ = 20                                                                  (17)
                                                             hora
El sistema consiste en un sistema M/M/1, por lo tanto:




                                                                 7
Problema 9
Usted es dueño de una tienda de helados tiene 1 sola caja para atender a sus clientes. Considere que los clientes llegan con
una tasa de llegada de λ [clientes/min], que distribuye en forma general G y son atendidos a una tasa µ [clientes/min] que
también distribuyen en forma general. Usted mide el tiempo medio de espera, siendo este de Te minutos, el coeficiente de
variabilidad del tiempo promedio de llegadas de personas siendo este Ca y también mide el coeficiente de variabilidad del
tiempo efectivo de la atención siendo este Ce .
Usted se encuentra muy preocupado por el servicio al cliente de su heladerı́a y determina que existe un costo por el tiempo
que espera de los clientes en la cola de Cq [$/m] peso por minuto en la cola. Es posible aumentar la tasa de atención de
clientes de la caja a un costo Ck [$/clientes/min] lo que claramente aumentarı́a el nivel de servicio de la heladerı́a.

a) Grafique cómo varı́a el costo de espera de los clientes en la cola, el costo de operación de la caja y el costo total;
versus la tasa de atención a clientes (realice un gráfico para cada caso).

b) Escriba el modelo de programación matemática que debiera resolver el gerente de la heladerı́a. (Hint: Determine
la variable de decisión y plantee la función objetivo).

c)Resuelva el problema anterior y plantee la forma funcional que me permita obtener el óptimo. Sólo plantee la for-
mula funcional y el mecanismo para obtener el óptimo.

d) Suponga que desea establecer un tiempo promedio máximo de espera de sus clientes de T minutos en la fila. Plantee el
problema de programación matemática que le permite resolver este problema y cómo resolverı́a este problema.

Solución problema 9
a) Al aumentar la tasa de atención de clientes, el costo por espera en la cola del cliente irá disminuyendo de forma cuadrática,
debido a cómo se compone el tiempo de espera de la cola según la ecuación de Kingman. De esta forma, el gráfico queda
como sigue:




                                                                8
Por otro lado, el costo por capacidad se mueve de forma lineal a la tasa de atención, por lo que el gráfico queda como sigue:




b) Se pide escribir la función objetivo, dado que no existen restricciones al problema. El gerente debiera buscar mini-
mizar el costo total, el que se compone de la siguiente forma:

                                                  Ctotal = Cq ∗ CTq + Ck ∗ µ                                              (18)

El tiempo de espera en cola, por Kingman:
                                                                            λ
                                                           Ca2 + Ce2       µ
                                              CTq = (                )∗(        ) ∗ Te                                    (19)
                                                               2         1 − µλ

Luego, la F.O. es:
                                                      Ca2 + Ce2       λ/µ
                                      min : Cq ∗ (              )∗(         ) ∗ Te + Ck ∗ µ                               (20)
                                                          2         1 − λ/µ
   c) Para determinar la tasa de atención óptima, se debe derivar la expresión anterior e igualar a 0. Al hacer esto, se
obtiene lo siguiente:
                                    d         C 2 + Ce2       λ/µ
                                      [Cq ∗ ( a         )∗(         ) ∗ Te + Ck ∗ µ] = 0                               (21)
                                   dx             2         1 − λ/µ
                                              Ca2 + Ce2               −λ
                                         Cq ∗ (         ) ∗ Te ∗ (           ) + Ck = 0                                   (22)
                                                  2                (µ − λ)2
                                                        s
                                                                      C 2 +C 2
                                                           λ ∗ Cq ∗ ( a 2 e ) ∗ Te
                                             µ=λ+−                                                                        (23)
                                                                      Ck
   Despejando µ la expresión anterior, se obtiene la tasa de atención óptima.


   d)
                                                      Ca2 + Ce2       λ/µ
                                      min : Cq ∗ (              )∗(         ) ∗ Te + Ck ∗ µ                               (24)
                                                          2         1 − λ/µ
s/a:

                                                              Te <= T                                                     (25)
En este caso, la ecuación de Kingman quedarı́a como sigue:
                                                      Ca2 + Ce2       λ/µ
                                                  (             )∗(         ) ∗ Te                                        (26)
                                                          2         1 − λ/µ
Al igual que antes, se debe encontrar la tasa de atención óptima que cumpla con esta restricción, que se obtendrı́a como
sigue:
                                          C 2 + Ce2       λ/µ
                             min : [Cq ∗ ( a        )∗(         ) ∗ Te + Ck ∗ µ] + λ ∗ (T − Te )                        (27)
                                              2         1 − λ/µ

                                                                   9
Como la optimalidad se encuentra igualando a T derivando con respecto a µ e igualando a 0 se obtiene:

                                                 Ca2 + Ce2           −λ
                                        Cq ∗ (             )∗T ∗(          ) + Ck = 0                               (28)
                                                     2            (µ − λ)2
De donde se podrı́a obtener el valor de µ.

Problema 10
Suponga que tiene una maquina a la que le llegan 20 piezas en una hora para ser procesadas. El tiempo medio de
procesamiento es de 2,5 minutos por pieza. Tanto las llegadas como las salidas del sistema son un proceso de Poisson.
presentan en la figura 1. Los planes consisten en:
   • ¿Cual es la tasa de utilizacion del sistema?
   • ¿Cual es el tiempo medio de espera de una pieza para ser procesada por la maquina?
   • ¿Cual es numero promedio de piezas en el sistema?
   • ¿Es igual el numero promedio de piezas en el sistema que el numero promedio de piezas en cola? ¿Por que valor esta
     acotado?
Ahora suponga que la misma máquina posee varianza asociada al tiempomedio de procesamiento igual a 25 minutos.
   • ¿Cual es la tasa de utilizacion del sistema?
   • ¿Cual es el tiempo medio de espera de una pieza para ser procesada por la maquina?
   • ¿Cual es numero promedio de piezas en el sistema?

Solución problema 10
a) Por enunciado tenemos que el sistema es de tipo M/M/1, donde: λ = 20 piezas        piezas
                                                                         hora y µ = 24 hora . Asi:

                                                    λ   20
                                              ρ=      =    = 0, 833333 = 83, 3%                                     (29)
                                                    µ   24
b) Para este sistema el tiempo medio de espera es:
                                                              1
                                                   W =               = 15min                                        (30)
                                                         µ ∗ (1 − ρ)

c) El número promedio de piezas en el sistema está dado por:
                                                         ρ
                                                 L=           = 4, 9999piezas                                       (31)
                                                      (1 − ρ)

d) El número de personas en cola no es igual a la cantidad de personas en el sistema. Siempre es menor o igual ya que no
considera la persona que esta siendo atendida. Solo son iguales cuando el sistema esta vacio (es decir, cuando no existe
cola y no hay persona en el servidor).
                                                           ρ2
                                                  Lq =          = 4, 1655                                            (32)
                                                        (1 − ρ)
e) Por enunciado tenemos el mismo sistema M/M/1 en el cual la tasa de ocupación no se ve afectada, por lo tanto, es el
mismo 83,3%.
f) El tiempo de espera se ve afectado por la variabilidad:

                                                              c2a + c2e      ρ
                                             F Tq = V U T =             ∗         ∗ te                              (33)
                                                                  2       (1 − ρ)

donde ce = 5/2, 5 = 2, y donde ca = 1 porque las llegadas distribuyen exponenciales, ası́:

                                                  12 + 22      0, 8333
                                F Tq = V U T =            ∗               ∗ 2, 5 = 31, 2425min                      (34)
                                                     2      (1 − 0, 8333)

                                                               10
g) El número promedio de piezas en el sistema depende del throughput:

                             CT = F Tq + te = V U T = 31, 2425 + 2, 5 = 33, 7425min   (35)

                                                      33, 7425
                                 L = T H ∗ CT = 20 ∗            = 11, 2465piezas      (36)
                                                         60
                                                       31, 7425
                                Lq = T H ∗ F Tq = 20 ∗          = 10, 4142piezas      (37)
                                                          60




                                                       11
Calidad
Problema 1
Considere una empresa que recibe grandes lotes de componentes diariamente, por lo que decide implementar un plan
estadistico de aceptacion. Existen 3 planes posibles, que requieren cada uno un muestreo de 30 componentes. Estos se
presentan en la figura 1. Los planes consisten en:
   • Plan A: Aceptar el lote si no contiene ningun componente defectuoso.
   • Plan B: Aceptar el lote si contiene a lo mas un componente defectuoso.
   • Plan C: Aceptar el lote si contiene a lo mas dos componentes defectuosos.




Segun esta informacion, ¿Que plan escogeria para las siguientes situaciones?

a) Debe haber una alta probabilidad de aceptar un lote con un 2% de componentes defectuosos.
b) Debe haber una alta probabilidad de rechazar un lote con un 8% de componentes defectuosos.
c) Un balance entre el riesgo de aceptar lotes con un 8% de componentes defectuosos y rechazar lotes con un 2% de
   componentes defectuosos.

Solución problema 1
a) En forma general, para una distribucion binomial se tiene:
                                                           
                                                            n i
                                              P (x = i) =     p (1 − p)n−i
                                                            i
En un lote con un 2% de componentes defectuosos, cada componente tiene una probabilidad de 0,02 de ser defectuoso.
Luego, la probabilidad de que un componente no sea defectuoso es 10.02 = 0.98. Analizando los 30 componentes, la
probabilidad de que no hayan componentes defectuosos es 0.9830 = 0.545, que corresponde a la probabilidad de aceptacion
del Plan A.Asi, las probabilidades de aceptacion son:

   • Plan A: 0, 9830 = 0.545
   • Plan B: 0, 9830 + 30 ∗ 0.02 ∗ 0.9829 = 0.879
   • Plan C: 0, 9830 + 30 ∗ 0.02 ∗ 0.9829 + 30∗29
                                              2   ∗ +0.022 ∗ 0.9828 = 0.978

El Plan C es el mas adecuado porque tiene la mayor probabilidad de aceptar un lote con un 2% de componentes defectuosos.

b) Realizando los calculos de la misma forma que en caso anterior, se tiene que la probabilidad de aceptacion de un
lote que contiene un 8% de componentes defectuosos es 0.082 para el Plan A, para el Plan B 0.296 y para el Plan C
0.565. Luego, el Plan A es el mas adecuado porque tiene la mayor probabilidad de rechazar un lote que contiene un 8% de
componentes defectuosos.

c) En la figura 1, se puede apreciar que el plan B es el mas adecuado.


                                                            12
Problema 2
Los pesos de las cajas de hojuelas de avena incluidas dentro de un lote de produccion grande se muestrean cada hora.
Los administradores quieren establecer limites de control que incluyan el 99,73% de las medias muestrales. Se sabe que la
desviacion estandar es igual a 1. Establezca los limites superior e inferior, juego analice si el proceso se encuentra o no bajo
control. ¿Que condiciones deberian darse para que ocurra lo opuesto?

                                                  Hora     Promedio 9 muestras
                                                    1             16.1
                                                    2             16.8
                                                    3             15.5
                                                    4             16.5
                                                    5             16.5
                                                    6             16.4
                                                    7             15.2
                                                    8             16.4
                                                    9             16.3
                                                   10             14.8
                                                   11             14.2
                                                   12             17.3



Solución problema 2
Se sabe que:
   • 68.3%: N=1 desviaciones estandar.
   • 95.4%: N=1 desviaciones estandar.
   • 99.73%: N=1 desviaciones estanda.
   • 99.9999998%: N=6 desviaciones estandar.
Calculando el promedio y la desviacion de las 9 cajas:
                                                           x1 + ... + x9
                                                    x̄ =                 = 16
                                                                 9
                                                      σ    1  1
                                                 σ̄ = √ = √ =
                                                       n    9 3
Reemplazando los valores en las formulas de UCL y LCL:
                                                                             1
                                             U CL = x̄ + z ∗ σ̄ = 16 + 3 ∗     = 17
                                                                             3
                                                                           1
                                             LCL = x̄ − z ∗ σ̄ = 16 − 3 ∗    = 15
                                                                           3
Se puede notar que los ultimos 3 valores de la tabla estan fuera de los valores establecidos, por lo que no se puede considerar
que es un proceso bajo control. Por otro lado, si la desviacion estandar fuera 2, el resultado para UCL y LCL seria distinto,
asi quedarian dentro de los limites (los cuales serian 18 y 14).

Problema 3
Una compania de seguros esta implementado un plan de polizas que la empresa realiza. Se toma cada semana una muestra
(en total 2.500 polizas semanales) y se anota la cantidad de polizas mal confeccionadas. El criterio de control es bajo
3-sigma. La informacion se presenta a continuacion:
a) Dibuje los graficos de control para 3-sigma.
b) Muestre que este proceso esta fuera de control. ¿Cuales podrian ser algunas razones?
c) Si se usara 2 o 1 sigma como medida de control, ¿Estaria bajo proceso?


                                                                13
                                                        Muestras     Errores
                                                           1           15
                                                           2           12
                                                           3           19
                                                           4            2
                                                           5           19
                                                           6            4
                                                           7           24
                                                           8            7
                                                           9           10
                                                          10           17
                                                          11           15
                                                          12            3
                                                         Total        147


Solución problema 3
a) Calculamos:
                                                    Def ectos        147
                                           p̄ =                 =           = 0.0049
                                                  Observaciones   12 ∗ 2500
con desviación:                   p              p
                                    p̄(1 − p̄)/N = 0.0049 ∗ (1 − 0.0049)/2500 = 0.0014
Los limites inferiores y superiores son:
                                                      LS3 = p̄ + 3d = 0.00091
                                                      LI3 = p̄ − 3d = 0.0007
Por otro lado, las proporciones de error para cada muestra son:

                                            Muestras      Errores    Proporción error
                                               1            15           0.0060
                                               2            12           0.0048
                                               3            19           0.0076
                                               4             2           0.0008
                                               5            19           0.0076
                                               6             4           0.0016
                                               7            24           0.0096
                                               8             7           0.0028
                                               9            10           0.0040
                                              10            17           0.0068
                                              11            15           0.0060
                                              12             3           0.0012
                                             Total         147           0.0049




El grafico queda como:

b) La proporcion de la muestra 7 supera el limite superior, por lo que el proceso esta fuera de control.

c) Los limites para 2-sigma son:
                                                      LS2 = p̄ + 2d = 0.0077
                                                      LI2 = p̄ − 2d = 0.0021
Como la proporcion de falla de la muestra 7 esta en este intervalo, bajo este criterio, el proceso si estaria bajo control.
Obviamente, bajo 1-sigma tambien, pues es el criterio es menos exigente que 2-sigma.


                                                                14
Problema 4
Los capturistas de Dossier Data Systems intrducen miles de registros de seguros cada dı́a para una variedad de clientes
corporativos. La directora general, Donna Mosier, quieres establecer lı́mites que incluyan el 99.73% de la variación aleatoria
en el proceso de introducción de datos cuando se encuentra bajo control. Se recopilan muestras de trabajo de 20 capturistas
(datos que se encuentran en la tabla). Se pide examinar cuidadosamente los 100 regustros capturados por cada empleado
y contar el número de errores. Despues se pide calcular la fracción defectuosa en cada muestra.

                                     N de muestra     N de errores    Fracción defetuosa
                                           1               6                  0.06
                                           2               5                  0.05
                                           3               0                  0.00
                                           4               1                  0.01
                                           5               4                  0.04
                                           6               2                  0.02
                                           7               5                  0.05
                                           8               3                  0.03
                                           9               3                  0.03
                                          10               2                  0.02
                                          11               6                  0.06
                                          12               1                  0.01
                                          13               8                  0.08
                                          14               7                  0.07
                                          15               5                  0.05
                                          16               4                  0.04
                                          17              11                  0.11
                                          18               3                  0.03
                                          19               0                  0.00
                                          20               4                  0.04



Solución problema 4
Se define un control de atributos como la decisión de aceptar o rechazar lotes viendo sólo unos pocos ı́tems. Luego se define:

                                                      p = % de defectos
                                                            r
                                                              p(1 − p)
                                                       σp =
                                                                 n

                                                              15
Se calcula p sumando el total de errores y dividiéndolo por el total de ı́tems analizados (20 lotes * 100 ı́tems c/u = 2000).
Reemplazando p = 4$ y σp = 2%
                                         U CL = p + z ∗ σp = 4% + 3 ∗ 2% = 10%
                            LCL = 4% − 3 ∗ 2% = −2% = 0% (no puede haber lı́mite negativo)
Por lo tanto se rechaza el lote 17 por presentar más defectos que lo deseado.

Problema 5
Usted quiere implementar un nuevo sistema de muestro para controlar los lotes de manzanas. Para ello define una politica
con un AQL de 0,19 y un LPTD de 0,6. Usando α = 0.05 y β = 0.1 indique y explique el plan de muestreo que usara.

Solución problema 5
Del enunciado se puede obtener LPTD / AQL = 3.1579 . Con este valor, revisando las tablas para α y β se obtienen valores
para c y nAQL :
                                                      c=6
                                                       nAQL = 3.286
Asi, se obtiene n = 17, 3 . Esto quiere decir que, usando esta politica, se toma una muestra de 18 unidades, de las que si 6
salen defectuosas se rechaza el lote.

Problema 6
Una compañı́a de música que fabrica teclados realiza diariamente un ana lisis de calidad a una muestra de 25 teclas para
poder determinar el numero total de teclas defectuosas. La probabilidad de que una tecla resulte defectuosa sigue una
distribucion Uniforme (0, 1).
a) Si el numero de teclas defectuosas en una muestra sigue una distribucion Uniforme (0, 25)¿Cual es la distribucion de
   probabilidad del numero de teclas defectuosas si se sabe que piezas son defectuosas?

b) Si la produccion se considera satisfactoria cuando el numero de teclas defectuosas es menor a 4. ¿Cual es la probabilidad
   de que la produccion sea considerada satisfactoria?
c) En base a la probabilidad estimada en a), elabore el grafico de control del proceso y determine si el proceso esta bajo
   control.

d) Si el plan de muestreo está definido con un AQL de 10% un LPTD de 40%, un α = 0, 05 y β = 0, 1. ¿Es correcto el
   tamaño muestral que está usando la compañı́a?
e) ¿En que se diferencia este proceso con un proceso de control de calidad de medidas continuas?




                                                             16
Solución problema 6
a) Sea Xn el número de piezas defectuosas y sea µ la probabilidad de que una pieza resulte defectuosa. Como Xn −
   U nif orme(0, 25) y µ − U nif orme(0, 1) entonces:

                                                  Xn |U = µ − Binomial(25, µ)                                              (38)

b) A partir de la tabla, se puede obtener una estimacion de la probabilidad de que una tecla sea defectuosa. Sea xi la
   cantidad de teclas defectuosas en la jornada i. Luego:
                                                               30
                                                           1 X xi
                                                      p=     ∗       = 0, 17                                               (39)
                                                           30 i=1 25

   La probabilidad de que la producción sea satisfactoria es:

                                     p(x < 4) = p(x = 0) + p(x = 1) + p(x = 2) + p(x = 3)                                  (40)
                                                      25 ∗ 24                    25 ∗ 24 ∗ 23
             p(x < 4) = 0.8325 + 25 ∗ 17 ∗ 0.8324 +           ∗ 0.172 ∗ 0.8323 +              ∗ 0, 173 ∗ 0.8222 = 0, 368   (41)
                                                        2!                            3!
c) Los lı́mites de control definen el intervalo (µ − 3σ, µ + 3σ). Como la distribución es binomial, se tiene:
                                                 p                           p
                           LCL = LCI = np − np ∗ (1 − p) = 25 ∗ 0, 17 − 25 ∗ 0, 17 ∗ 0, 83 = 2, 36                         (42)
                                                 p                           p
                           U CL = LCI = np + np ∗ (1 − p) = 25 ∗ 0, 17 + 25 ∗ 0, 17 ∗ 0, 83 = 6, 11                        (43)
   El grafico de control es muesta que el proceso esta fuera de control:




                                                               17
d) A partir del plan de muestreo de la tabla se tiene:

                                                   LP T D   0, 4
                                                          =      =4→
                                                                   − c=4                                              (44)
                                                    AQL     0, 1

                                               AQL ∗ n = 1, 970 →
                                                                − n = 19, 7 ≈ 20                                      (45)
   El tamaño de muestra no es adecuado, ya que deberı́an estar tomando muestras de 20 teclados.
e) En estos procesos basta con conocer solo la media del proceso (la varianza queda determinada por la media). En un
   caso de medidas continuas con distribuciones como la normal, la media y la varianza no están relacionadas, por lo que
   es necesario monitorear la media del proceso y también la variabilidad.

Problema 7
Usted está encargado del control de calidad de piezas de maquinaria que requieren medidas especı́ficas de su diámetro. Se
le proporciona la siguiente información de los diámetros medidos en 5 muestras:




a) Construya los gráficos de control (construya el gráfico en escala de centésimas)

b) ¿Está el proceso bajo control?


                                                              18
Solución problema 7
Los promedios y rangos son los siguientes: De este modo se tiene que: X = 5, 027 y R = 0, 021. De los valores de tabla, se




obtiene que: A2 = 0, 729D3 = 0D4 = 2, 282.
Ahora construimos los lı́mites superiores e inferiores de los gráficos:

                                     LCSX = X + A2 R = 5, 027 + 0, 729 ∗ 0, 021 = 5, 024                             (46)

                                     LCIX = X − A2 R = 5, 027 − 0, 729 ∗ 0, 021 = 5, 012                             (47)
                                          LCSR = D4 ∗ R = 2, 282 ∗ 0, 021 = 0, 0479                                  (48)
                                                      LCIR = D3 ∗ R = 0                                              (49)
Los gráficos, para promedios y rangos, son los siguientes respectivamente:




                                                               19
   b) La media de la muestra 5 supera el lı́mite superior, por lo que el proceso está fuera de control.

Problema 8
Usted está a cargo de evaluar la polı́tica de calidad que su empresa exige a productores de manzanas. A continuación se
muestra el peso de una muestra de los 4 bins recibidos durante los últimos 5 dı́as:




a) Con la información dada elabore los gráficos de control.
b) Si el dı́a 6 usted toma una muestra con los resultados: 407, 381, 392 y 396. ¿Qué puede decir de la muestra? ¿Acepta o
   rechaza el lote?


                                                                20
Solución problema 8
a) Se tienen los siguientes promedios y rangos:




El promedio de las muestras es 394,95 kg, el promedio de los recorridos 11,6 kg y la desviación estándar 6,1 kg. De
las tablas de control: A2 = 0, 72, D4 = 2, 28, D3 = 0.
Los lı́mites son, entonces:
                                    LCSX = X + A2 R = 394, 45 + 0, 73 ∗ 11, 6 = 402, 92                           (50)

                                   LCIX = X − A2 R = 394, 45 − 0, 73 ∗ 11, 6 = 385, 98                                   (51)
                                          LCSR = D4 ∗ R = 2, 11 ∗ 11, 6 = 26, 45                                         (52)
                                                    LCIR = D3 ∗ R = 0                                                    (53)
Eliminando las muestras fuera de los lı́mites:




El promedio de las muestras es 394,7 kg, el de los recorridos 5,6 kg y la desviación estándar 4,7 kg. Se definen los
lı́mites para σ, 2σ, 3σ. 3σs = 408, 7
2σs = 404
σs = 399, 4
3σi = 380, 73
2σi = 385, 4
σi = 390
Por lo tanto: (ver grafico)


b) El promedio de los datos del dı́a 6 es 392,25 kg y su rango 26 kg. Para verificar el rango se debe calcular los lı́mites
inferior y superior de este (considerando pesos iniciales):

                                          LCSR = D4 ∗ R = 2, 11 ∗ 11, 6 = 26, 45                                         (54)

                                                    LCIR = D3 ∗ R = 0                                                    (55)
Tanto el promedio como el rango de los datos medidos están dentro de los rangos aceptables, por lo que sı́ se acepta el lote.




                                                             21
Problema 9
Un proceso genera lotes de 8000 piezas y se sabe que tiene una proporción de defectos de 0,26%. Se desea evitar con buena
probabilidad que salgan lotes al mercado con proporción mayor a 1%. Se establece un plan de muestreo con RQL=1%.
Informe los elementos del plan de muestreo simple para el lote usando Dodge-Roming

Solución problema 9
Generacion de planes para el limite de tolerancia de recibo (Plan LTPD – Basado en la tolerancia de recibo del mercado).
Los pasos para resolver son los siguientes:
   • Fijo x% LPTD razonable (si soy muy exigente, es conveniente muestrear 100%)
   • Especificar tamaño de lote (N)
   • Determinar proporción de defectos en el proceso del productor, %p defectos del proceso

   • De tabla LPTD (x%) leer n, c, AOQL
Por lo tanto, tenemos:
   • NCL = 1%
   • N = 8000

   • %p = 0,26%
   • De tabla %p (0,21-0,3%)
   • Ver tabla LTPD

Se identifica que en un intervalo (0,21%-0,3%) como se exige con un lote de tamaño 8.000. Luego, tenemos que N=8000
piezas, p=0,26%, RQL=1%
                                         → n = 910, c = 5, AQLproductor = 0, 32




                                                           22
Problema 10
Sobre los siguientes datos que se obtienen de recopilación de información de un muestreo de proceso sobre el largo de cierto
material que debe ser analizado en control de calidad. Se realizan muestreos durante 5 dı́as y se resume en los siguiente:




   A partir de lo anterior:
a) Calcule los lı́mites de control, eliminando los outliers.
b) Si el dı́a 6 usted toma una muestra con los siguientes resultados: 63, 54, 43, 69 y 65. ¿Qué puede decir de la muestra?
   ¿Está el proceso bajo control?

Solución problema 10
a) Primero se calculan los promedios y los rangos de cada uno de los dı́as para luego calcular el total:



                                                               23
De este modo se tiene que: X = 58, 04 y R = 21, 8. De esta tabla se obtiene que como son observaciones de subgru-
pos de n=5, se tiene A2 = 0, 58; D3 = 0; D4 = 2, 11.




Luego:
                                    LCSX = X + A2 R = 58, 04 + (0, 58 ∗ 21, 8) = 70, 7                                 (56)

                                    LCIX = X − A2 R = 58, 04 − (0, 58 ∗ 21, 8) = 45, 4                                 (57)
                                           LCSR = D4 ∗ R = 2, 11 ∗ 21, 8 = 46                                          (58)
                                              LCIR = D3 ∗ R = 0 ∗ 21, 8 = 0                                            (59)
Ahora teniendo los lı́mites de control se eliminan los outliers, los outliers son los valores que se encuentran fuera de los
lı́mites de control:




                                                            24
Volvemos a calcular la tabla de promedios reciente:




De este modo se tiene que: X = 58, 8 y R = 20, 4.
Luego:
                                   LCSX = X + A2 R = 58, 8 + (0, 58 ∗ 20, 4) = 70, 6                                  (60)

                                     LCIX = X − A2 R = 58, 8 − (0, 58 ∗ 20, 4) = 47                                   (61)
                                           LCSR = D4 ∗ R = 2, 11 ∗ 20, 4 = 43                                         (62)
                                             LCIR = D3 ∗ R = 0 ∗ 20, 4 = 0                                            (63)
   b) Entonces ahora se tiene la muestra de un dı́a 6, con los valores ( 63, 54, 43, 69 y 65) el cuál tiene un promedio de
muestra de 58,8 coincidente con el promedio anterior y un rango de 26, ambos se encuentran dentro de los lı́mites por lo
tanto se debe aceptar el lote y se encuentra el proceso bajo control.




                                                            25
