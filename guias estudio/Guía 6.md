                   Pontificia Universidad Católica de Chile
                   Escuela de Ingenierı́a
                   Departamento de Ingenierı́a Industrial y de Sistemas
                   ICS3212 - Gestión de Operaciones
                   Ayudantes: Sergio Dı́az (sidiaz2@uc.cl) y José Rebolledo (jtrebolledo@ing.puc.cl)
                   Primer Semestre 2019




                                     Guı́a de Ejercicios:
                                                  Localización



Problema 1
   Maravillalandia, una cadena chilena con 10 parques de diversión decidió ampliarse al extranjero mediante la
apertura de un parque fuera de Chile. Debido al crecimiento de los mercados de los paı́ses cercanos a Chile se
decidió considerar entre las opciones a Perú y Colombia. Para la decisión final, se contrató a una consultora para
que califique cada uno de los paı́ses según los criterios entregados por la empresa. Todos estos datos son entregados
a continuación:
                                                                         Calificaciones (hasta 100)
                   Factor Crı́tico de éxito                     Peso
                                                                         Perú       Colombia
                   Disponibilidad de mano de obra y actitud      0,25     70             75
                   Razón de personas sobre automóviles         0,05     50             80
                   Ingreso per cápita                           0,10     85             90
                   Estructura Fiscal                             0,39     75             70
                   Educación y Salud                            0,21     60             70
   Con esta información determine el mejor paı́s para localizar su próximo parque de atracciones.


Solución Problema 1
   Para resolver este problema tenemos que utilizar la tabla entregada. Para ello, lo que tenemos que hacer es
ponderar cada factor con su respectivo peso y comparar los resultados finales. Este cálculo se presenta en la
siguiente tabla:
                                                        Calificaciones (hasta 100)     Calificaciones Ponderadas
  Factor Crı́tico de éxito                      Peso
                                                        Perú       Colombia                 Perú       Colombia
  Disponibilidad de mano de obra y actitud       0,25    70             75            0, 25 · 70 = 17, 5  18,75
  Razón de personas sobre automóviles          0,05    50             80                     2,5           4
  Ingreso per cápita                            0,10    85             90                     8,5           9
  Estructura Fiscal                              0,39    75             70                    29,3         27,3
  Educación y Salud                             0,21    60             70                    12,6         14,7
                                                                            Total             70,4        73,75
    Con estos resultados es evidente que la mejor localización es Colombia. Sin embargo, hay que tener presente que
si existe un cambio en las ponderaciones entregadas por la empresa, por ejemplo, aumenta la ponderación entregada
a la Estructura Fiscal podrı́a ocurrir que Perú se vuelva la mejor solución.




                                                          1
Problema 2
    VamosYa, una cadena de cuatro tiendas de autoservicio grandes tiene establecimientos ubicados en Santiago,
La Serena, Córdoba (Argentina) y Valparaı́so; en la actualidad reciben sus provisiones de un almacén viejo e
inadecuado que está en Valparaı́so, donde se abrió la primera tienda de la cadena. La compañı́a quiere encontrar
alguna localización “central” en la cual construir un nuevo almacén. Para ello, el gerente de planificación construye
la siguiente tabla con las coordenadas de las diversas ubicaciones de los actuales localaes y el número de containers
enviados por mes a las diferentes sucursales
             Sucursal      Coordenada X      Coordenada Y       Número de Containers enviados por mes
             Valparaı́so        -33               -71                           4.000
             Santiago           -33               -70                          10.000
             Córdoba           -31               -64                           2.700
             La Serena          -29               -71                           7.000
   Con esta información determine la posición del nuevo centro de distribución que mejor se adecúa a la situación
presentada por la empresa.


Solución Problema 2
   Como en la tabla se hace entrega de las coordenadas y la cantidad de containers enviados a los diferentes puntos
es posible realizar el cálculo del centro de gravedad de esta situación:
   Coordenada x del centro de gravedad: Para realizar este cálculo se utiliza la siguiente formula:
                                                                            P
                                                                             i dix Qi
                                 Coordenada x del centro de gravedad =       P
                                                                               i Qi
donde:
                                       dix = coordenada x de la localización i
                        Qi = cantidad de bienes que se llevan desde o hacia la localización i

   Con ello hacemos el cálculo y obtenemos lo siguiente:

                                          P
                                           i dix Qi   (−33 · 4.000) + (−33 · 25.000) + (−31 · 2.700) + (−29 · 20.000)
Coordenada x del centro de gravedad =      P        =
                                             i Qi                    4.000 + 25.000 + 2.700 + 20.000
                                 Coordenada x del centro de gravedad = −31, 3482

   Coordenada y del centro de gravedad: En el caso de la coordenada y tenemos que el procedimiento es
similar, pero utilizando la siguiente formula:
                                                                       P
                                                                         i diy Qi
                                  Coordenada y del centro de gravedad = P
                                                                           i Qi
donde:
                                       diy = coordenada y de la localización i

   Con ello hacemos el cálculo y obtenemos lo siguiente:

                                     P
                                      i diy Qi   (−71 · 4.000) + (−70 · 25.000) + (−64 · 2.700) + (−71 · 20.000)
Coordenada y del centro de gravedad = P        =
                                         Q
                                        i i                     4.000 + 25.000 + 2.700 + 20.000
                                 Coordenada y del centro de gravedad = −70, 1509

   Por lo tanto las coordenadas del nuevo centro de distribución se encuentra en: (-31,5907; -70.1509).


                                                            2
Problema 3
   Una empresa presenta desea instalar una nueva sucursal y para ellos dispone de 3 posiciones diferentes (A, B,
C). Cada una de estas ubicaciones posee ventajas y desventajas. Debido a esto, el gerente de operaciones decidió
dividir los factores diferenciadores de cada posición en factores objetivos y factores subjetivos.
   Los factores objetivos están compuestos de todos los costos asociados a la construcción y puesta en marcha de
una sucursal en las diferentes posiciones. Estos factores son los siguientes:
                                                     Costos en Miles de Pesos
       Posición
                   Materia Prima    Transporte       Energı́a Transporte Impuestos         Costo de Transporte
       A                100             50            100         80          100                  430
       B                 90             80             80         90          80                   420
       C                 80            100             70         100         60                   410
   Y los factores subjetivos son aquellos parámetros que la gerencia considera importante, pero que no es posible
cuantificar en un monto monetario. Estos factores son los siguientes:
                   Factor Subjetivo                     Código del factor     A     B     C    Total
                   Clima                                       K1             0,7   0,7   0,6    2,0
                   Instituciones recreativas                   K2             0,8   0,6   0,5    1,9
                   Servicios complementarios                   K3             0,3   0,4   0,3    1,0
                   Costo de vida                               K4             0,2   0,3   0,5    1,0
                   Disponibilidad de Mano de obra              K5             0,4   0,5   0,7    1,6
   Considerando estos datos y suponiendo que la gerencia considera que los factores objetivos tiene un 70 % del
peso relativo, determine cuál es la mejor posición para la nueva sucursal.


Solución Problema 3
   Para este ejemplo debemos seguir los siguientes pasos:
    Cálculo de la Medida de Localización del Factor Objetivo (FOi ): Normalmente los factores objetivos
son posibles de cuantificar en términos de costos, lo que permite calculo el costo total anual de cada punto de
localización i. Luego, el FOi se determina al multiplicar el costo total de la posición i (CTFi ) por la suma de los
recı́procos de los costos totales de cada posición y luego tomar el reciproco del dicho resultado. Es decir:

                                                 "
                                                           X              #−1
                                                                    1
                                         F Oi = COFi ·
                                                               i
                                                                   CT Fi

   En el caso de nuestro problema, obtenemos los siguientes resultados:
                                                         
                                                1   1   1
                                F OA = 430 ·      +   +       = 0, 325458325
                                               430 420 410
                                                         
                                                1   1   1
                                F OB = 420 ·      +   +       = 0, 333207334
                                               430 420 410
                                                         
                                                1   1   1
                                F OC = 410 ·      +   +       = 0, 341334341
                                               430 420 410

   Cálculo de la Medida de Localización del Factor Subjetivo (FSi ): El carácter subjetivo de los factores
de orden cualitativo hace necesario asignar una medida de comparación como el valor de los distintos factores en
orden relativo, mediante tres etapas:



                                                           3
     Determinar una calificación Wj para cada localización i en base a las calificaciones del factor en la localidad
     respecto del total de ese mismo factor para todas las localizaciones.
     Dar una calificiación Rji para cada factor en base a las calificaciones del factor en la localidad respecto del
     total de los factores de la misma localidad.
     Para cada localización, combinar la calificación del factor Wi con su ordenación jerárquica Rji , para determinar
     la Medida del Factor Subjetivo (F Si ), de acuerdo a la siguiente forma:

                                                               X
                                                      F Si =           (Rji · Wi )
                                                                   j

   Con esta métrica se obtiene la siguiente tabla:
   Factor Subjetivo                      Código del factor         A      B      C        Total        WA          WB      WC
                                                                                                    0,7
   Clima                                        K1                 0,7    0,7    0,6        2,0     2,0 = 0, 350   0,350   0,300
   Instituciones recreativas                    K2                 0,8    0,6    0,5        1,9        0,421       0,316   0,263
   Servicios complementarios                    K3                 0,3    0,4    0,3        1,0        0,300       0,400   0,300
   Costo de vida                                K4                 0,2    0,3    0,5        1,0        0,200       0,300   0,500
   Disponibilidad de Mano de obra               K5                 0,4    0,5    0,7        1,6        0,250       0,313   0,438
                           Suma                                    2,4    2,5    2,6
                   Factor Subjetivo                       Calificación                A             B       C
                                                                                0,7
                   Clima                                     RK1                2,4 = 0, 292       0,280   0,231
                   Instituciones recreativas                 RK2                     0,333         0,240   0,192
                   Servicios complementarios                 RK3                     0,125         0,160   0,115
                   Costo de vida                             RK4                     0,083         0,120   0,192
                   Disponibilidad de Mano de obra            RK5                     0,167         0,200   0,269
   Con estos valores, reemplazamos en la ecuación de FSi y obtenemos lo siguiente:


         F SA = 0, 350 · 0, 292 + 0, 421 · 0, 333 + 0, 300 · 0, 125 + 0, 200 · 0, 083 + 0, 250 · 0, 167 = 0, 338243
          F SB = 0, 350 · 0, 280 + 0, 316 · 0, 240 + 0, 400 · 0, 160 + 0, 300 · 0, 120 + 0, 313 · 0, 200 = 0, 33644
         F SC = 0, 300 · 0, 231 + 0, 263 · 0, 192 + 0, 300 · 0, 115 + 0, 500 · 0, 192 + 0, 438 · 0, 269 = 0, 368118

    Cálculo de la Medida de Preferencia de Localización (MPLi ): Una vez valorados en términso relativos
los factores objetivos y subjetivos de localización, se procede a calcular la medida de preferencia de localización
mediante la aplicación de las siguiente fórmula:


                                            M P Li = k(F Oi ) + (1 − k)(F Si )

    donde k es el peso relativo asignada a cada uno de los factores (objetivo y subjetivo). En este caso el valor de k
es igual a 70 % tal como se menciona en el enunciado. Con ello hacemos el siguiente cálculo:


                            M P LA = (0, 325458325 · 0, 7) + (0, 338243 + 0, 3) = 0, 336311
                            M P LB = (0, 333207334 · 0, 7) + (0, 33644 + 0, 3) = 0, 334177
                            M P LC = (0, 341334341 · 0, 7) + (0, 368118 + 0, 3) = 0, 349369

   Selección del lugar: De acuerdo con el Método de Brown y Gibson (el método desarrollado en los puntos
anteriores), la alternativa elegida es la localización C puesto que recibe el mayor valor de medida de preferencia
de localización. También esta alternativa habrı́a sido la más atrayente si se hubiese comparado exclusivamente los
valores objetivos o si se compararan exclusivamente los factores subjetivos. De cualquier manera, es fácil apreciar,
por último, que un cambio en la ponderación entre factores objetivos y subjetivos podrı́a llevar a un cambio en la
decisión.


                                                               4
Problema 4
   En una empresa se cuentra con dos plantas productivas que permiten suplir completamente los requerimientos
de las demanda de los 3 almacenes que tienen. La empresa en estos momentos desea determinar la localización final
de cada uno de los productos generados por cada una de sus plantas. Para ello se provee de la siguiente tabla:
                             Costo en UF de embargar una unidad de producto al almacén
          Planta                                                                               Capacidad
                              1     2                         3
          Planta 1           5,0 6,0                         5,4                                   400
          Planta 2           7,0 4,6                         6,6                                   500
          Requerimientos     200 400                         300
   Con estos datos, determine la localización final de cada uno de los productos generados por cada una de las
plantas


Solución Problema 4
   Con los datos entregados, es posible apreciar que es importante para una empresa minimizar los costos de
transporte lo más posible. Por ello, cada planta siempre dará prioridad a las sucursales que presentan un mejor
coste.
   Con ello, es posible notar que la planta 1 puede suplir toda la demanda del almacén 1 y le sobra capacidad
de 200 para entregar al almacén 3. Asimismo, la planta 2 puede suplir 400 al almacén 2 y los 100 que faltaban al
almacén 3. Con ello la tabla queda de la siguiente manera:

                     Costo en UF de embargar una unidad de producto                      Cantidad entregada al almacén
 Planta                                                              Capacidad
                      1     2                    3                                         1           2           3
 Planta 1            5,0 6,0                    5,4                      400              200                     200
 Planta 2            7,0 4,6                    6,6                      500                          400         100
 Requerimientos      200 400                    300
                                                                  Costos Totales        1.000 UF    1.840 UF     1.740 UF
   Esto da un total de 4.580 UF por transporte.


Problema 5
   Una empresa de pastas llamada Barilla SPA cuenta con 3 plantas de produccion de tallarines que actualmente
despachan a 3 supermercados mayoristas. Sin embargo, el directorio se dio cuenta que lo ideal seria construir un
Centro de Distribucion de modo de poder satisfacer mejor los requerimientos de los supermercados mayoristas que
abastece. Para esto, lo contratan a usted para que decida la ubicacion y el funcionamiento del Centro de Distribucion
en cuestion. Su nueva secretaria le indica la informacion correspondiente al numero de unidades transportadas de
cada instalacion, al igual que los costos unitarios y las coordenadas de estos:
                     Instalación    Unidades    Costo/Unidad     Coordenada X      Coordenada Y
                      Planta 1          68            20              250               540
                      Planta 2          72            34              820               450
                      Planta 3         135            13              340               730
                   Supermercado 1       97            19              120               910
                   Supermercado 2       87            16              760                50
                   Supermercado 3       91            24              420               240
(a) Se le pide determinar las coordenadas de este Centro de Distribucion, mediante el metodo del centro de gravedad
    con costos.


                                                         5
(b) El directorio de la compania le informa que ya definio la ubicacion del centro de distribucion(X:537 , Y:479),
    y que tambien aparecio un nuevo supermercado mayorista interesado en recibir las deliciosas pastas de la
    compania. Este nuevo cliente se ubica en (X:620 , Y:430), y sera abastecido gracias a un aumento de capacidad
    de la planta 2, el que tendra un costo de 18 CLP/unidad. Se le pide determinar la cantidad de unidades que
    se le despacharan al nuevo supermercado considerando que no debe variar la ubicacion del nuevo centro de
    distribucion.


Solución Problema 5

Parte a

   Utilizando el metodo solicitado:
                                P
                                  Costo ∗ U nidades ∗ CoordenadaX   5.140.420
                         Cx =          P                          =           = 468
                                          Costo ∗ U nidades           10.982

                                P
                                    Costo ∗ U nidades ∗ CoordenadaY   5.388.040
                         Cy =            P                          =           = 491
                                            Costo ∗ U nidades           10.982


Parte b

   Se puede usar cualquiera de las dos ecuaciones para llegar a que Z = 68 unidades

                                       5.140.420 + 18 ∗ z ∗ 620 + 34 ∗ z ∗ 820
                                Cx =                                           = 537
                                              10.982 + 18 ∗ z + 34 ∗ z

                                       5.388.040 + 18 ∗ z ∗ 430 + 34 ∗ z ∗ 450
                                Cy =                                           = 479
                                              10.982 + 18 ∗ z + 34 ∗ z




                                                         6
