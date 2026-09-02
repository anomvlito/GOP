                   Pontificia Universidad Católica de Chile
                   Escuela de Ingenierı́a
                   Departamento de Ingenierı́a Industrial y de Sistemas
                   ICS3212 - Gestión de Operaciones
                   Ayudantes: Sergio Dı́az (sidiaz2@uc.cl) y José Rebolledo (jtrebolledo@ing.puc.cl)
                   Primer Semestre 2019




                                    Guı́a de Ejercicios:
                                            PERT y Ruta Crı́tica



Problema 1
   La construcción de una casa es una actividad bastante simple. Lo primero que se debe instalar es el piso. Una
vez completado el piso se puede empezar a poner cada una de las murallas de manera independiente y solo una vez
que todas las murallas están en pie se puede armar el techo. Además las ventanas y puertas se pueden instalar en
cada muralla una vez que esta está lista, de manera paralela al techo.
   Usted debe planificar el proyecto de construir una casa de 40 m2 y 4 murallas. Dos paredes tienen sólo una ventana
y otra tiene una ventana y una puerta. La siguiente tabla define el tiempo y número de personas disponibles para
hacer cada parte de la casa.
                                        Actividad     Tiempo [HH]    Personas
                                        Piso             1 x m2         5
                                        Muralla             6           2
                                        Techo            1 x m2         4
                                        Ventana             4           2
                                        Puerta              8           2
   Hint: Considere que cada ventana o muralla podrı́a ser realizada por un equipo separado (en paralelo). Y los
tiempos entregados en la tabla corresponden a los tiempos necesarios para realizar la actividad por una sóla persona
 (a) Haga un diagrama PERT de este proyecto.
 (b) Indique en una tabla el ES, EF, LS, LF y la holgura de cada actividad.
 (c) Señale la ruta crı́tica y la duración mı́nima del proyecto.
    Ahora existe la posibilidad de aumentar el número de personas en cada etapa. Considere que cada persona extra
asignada a una etapa tiene un costo de $10.000 y el tiempo total de HH requeridas por cada etapa se mantiene. El
beneficio por reducir el tiempo de duración del proyecto en 1 hora es de $20.000. Si el número de personas en una
actividad supera al cuádruple de lo inicial, ya no entrega beneficios asignar más personas a esa actividad.
 (d) ¿Cuál es el tiempo mı́nimo al que se puede realizar la casa? ¿Cuánto cuesta llegar a ese nivel?
 (e) ¿Cuál es el óptimo de personal a contratar?


Solución Problema 1
Parte a
   El diagrama PERT de esta situación es el siguiente:




                                                           1
Parte b
   La tabla de actividades es la siguiente:
                           Actividad    Personas Disponibles               Horas
                                                                       40m2
                           Piso                  5                1×m2 ×5 personas = 8horas
                                                                       6 HH
                           Muralla 1             2                  2 personas = 3 horas
                           Muralla 2             2                         3 horas
                           Muralla 3             2                         3 horas
                           Muralla 4             2                         3 horas
                           Ventana 1             2                         2 horas
                           Ventana 2             2                         2 horas
                           Ventana 3             2                         2 horas
                           Puerta                2                         4 horas
                           Techo                 4                        10 horas
   Con estos datos es posible realizar el análisis de holgura calculando ES, EF, LS y LF:
                  Actividad    Personas Disponibles     Horas       ES    EF    LS   LF       Holgura
                  Piso                  5              8 horas       0     8     0    8          0
                  Muralla 1             2              3 horas       8    11     8   11          0
                  Muralla 2             2              3 horas       8    11     8   11          0
                  Muralla 3             2              3 horas       8    11     8   11          0
                  Muralla 4             2              3 horas       8    11     8   11          0
                  Ventana 1             2              2 horas      11    13    19   21          8
                  Ventana 2             2              2 horas      11    13    19   21          8
                  Ventana 3             2              2 horas      11    13    19   21          8
                  Puerta                2              4 horas      11    15    17   21          6
                  Techo                 4              10 horas     11    21    11   21          0

Parte c
  Al revisar las holguras de las actividades tenemos que la ruta crı́tica está compuesta por: Piso - Todas las
murallas - Techo.
   Y el tiempo de construcción de la casa es de 21 horas.

Parte d
   Como se apreciar en el análisis anterior de holguras, las etapas que podrı́amos acelerar directamente son las
pertenencientes a la ruta crı́tica y en primera instancia hasta un máximo de 6 semanas reducción de tiempo ya que
en ese momento la instalación de la puerta pertenece a la ruta crı́tica.



                                                         2
     A continuación tenemos que determinar si es rentable que añadir personas extra a las actividades de la ruta
crı́tica. En primer lugar tenemos la construcción e instalación del piso:
             Número de           Tiempo de demora                              ¿Es rentable con respecto al
         trabajadores extra    del trabajo con el nuevo       Horas reducidas       beneficio de reducir
                               número de trabajadores                            el tiempo del proyecto?
                   1                     6.67                      1.33                      Si
                   2                     5.71                      2.28                      Si
                   3                       5                        3                        Si
                   4                     4.44                      3.56                      Si
                   5                       4                        4                        Si
                   6                     3.64                      4.36                      Si
                   7                     3.33                      4.67                      Si
                   8                     3.08                      4.92                      Si
                   9                     2.86                      5.14                      Si
                  10                     2.67                      5.33                      Si
                  11                     2.50                      5.50                      No
                  12                     2.35                      5.65                      No
                  13                     2.22                      5.78                      No
                  14                     2.11                      5.89                      No
                  15                     2.00                      6.00                      No
                   6                     3.64                      4.36                      No
   Hacemos el mismo análisis para el caso de las murallas:
             Número de           Tiempo de demora                              ¿Es rentable con respecto al
         trabajadores extra    del trabajo con el nuevo       Horas reducidas       beneficio de reducir
                               número de trabajadores                            el tiempo del proyecto?
                  1                      2.00                      1.00                      Si
                  2                      1.50                      1.50                      Si
                  3                      1.20                      1.80                      No
                  4                      1.00                      2.00                      Si
                  5                      0.86                      2.14                      No
                  6                      0.75                      2.25                      No
   Y el caso del Techo:
             Número de           Tiempo de demora                              ¿Es rentable con respecto al
         trabajadores extra    del trabajo con el nuevo       Horas reducidas       beneficio de reducir
                               número de trabajadores                            el tiempo del proyecto?
                   1                     8.00                      2.00                      Si
                   2                     6.67                      3.33                      Si
                   3                     5.71                      4.29                      Si
                   4                     5.00                      5.00                      Si
                   5                     4.44                      5.56                      Si
                   6                     4.00                      6.00                      Si
                   7                     3.64                      6.34                      Si
                   8                     3.33                      6.67                      Si
                   9                     3.08                      6.92                      Si
                  10                     2.86                      7.14                      Si
                  11                     2.67                      7.33                      Si
                  12                     2.50                      7.50                      Si
   Con este análisis y como estamos buscando reducir al máximo el tiempo del proyecto no nos importa la
rentabilidad por lo tanto es posible reducir los tiempos lo máximo que se pueda. Para el caso de los trabajadores del
piso y las murallas no hay problema, pero los trabajadores del techo si agregamos más de 6 el tiempo de proceso se


                                                          3
reduce a un tiempo menor al de holgura de las puertas. Para ello primero desarollamos el análisis de holgura para
el caso donde se agregen 15 trabajadores en el piso, 6 en cada muralla y 6 en el techo:
              Actividad     Personas Disponibles       Horas         ES    EF       LS     LF    Holgura
              Piso                   20               2 horas         0     2        0      8       0
              Muralla 1              8               0.75 horas       2    2.75      2    2.75      0
              Muralla 2              8               0.75 horas       2    2.75      2    2.75      0
              Muralla 3              8               0.75 horas       2    2.75      2    2.75      0
              Muralla 4              8               0.75 horas       2    2.75      2    2.75      0
              Ventana 1              2                2 horas       2.75   4.75    4.75   6.75      2
              Ventana 2              2                2 horas       2.75   4.75    4.75   6.75      2
              Ventana 3              2                2 horas       2.75   4.75    4.75   6.75      2
              Puerta                 2                4 horas       2.75   6.75    2.75   6.75      0
              Techo                  10               4 horas       2.75   6.75    2.75   6.75      0
   En esta nueva situación tenemos que hacer el análisis de añadir trabajadores a la instalación de la puerta:
             Número de           Tiempo de demora                                ¿Es rentable con respecto al
         trabajadores extra    del trabajo con el nuevo       Horas reducidas         beneficio de reducir
                               número de trabajadores                              el tiempo del proyecto?
                  1                      2.66                      1.33                        Si
                  2                      2.00                      2.00                        Si
                  3                      1.60                      2.40                        Si
                  4                      1.33                      2.67                        Si
                  5                      1.14                      2.86                        No
                  6                      1.00                      3.00                        Si
   Y si se hace un análisis rápido tenemos que si añadimos 2 trabajadores y 6 trabajadores más al techo se obtiene
el máximo tiempo de reducción posible. Y por lo tanto, el análisis de holgura es el siguiente:
              Actividad     Personas Disponibles       Horas         ES    EF       LS     LF    Holgura
              Piso                   20               2 horas         0     2        0      8       0
              Muralla 1              8               0.75 horas       2    2.75      2    2.75      0
              Muralla 2              8               0.75 horas       2    2.75      2    2.75      0
              Muralla 3              8               0.75 horas       2    2.75      2    2.75      0
              Muralla 4              8               0.75 horas       2    2.75      2    2.75      0
              Ventana 1              2                2 horas       2.75   4.75    3.25   5.25     0.5
              Ventana 2              2                2 horas       2.75   4.75    3.25   5.25     0.5
              Ventana 3              2                2 horas       2.75   4.75    3.25   5.25     0.5
              Puerta                 4                2 horas       2.75   4.75    3.25   5.25     0.5
              Techo                  16              2.5 horas      2.75   5.25    2.75   5.25      0
   El tiempo total de este proyecto es de 5.25 horas y como se añadieron 53 trabajadores más (15 en el piso, 6 por
casa muralla, 2 en la puerta y 12 en el techo) se obtiene un costo de $530 mil.

Parte e
   Haciendo uso del análisis de factibilidad económica hecho en el punto anterior, es posible obtener que el óptimo
económico se encuentra en añadir 4 trabajadores más al piso y 5 al techo:




                                                          4
                Actividad    Personas Disponibles       Horas     ES    EF     LS     LF    Holgura
                Piso                  9               4.4 horas    0     4.4    0     4.4      0
                Muralla 1             2                3 horas    4.4    7.4   4.4    7.4      0
                Muralla 2             2                3 horas    4.4    7.4   4.4    7.4      0
                Muralla 3             2                3 horas    4.4    7.4   4.4    7.4      0
                Muralla 4             2                3 horas    4.4    7.4   4.4    7.4      0
                Ventana 1             2                2 horas    7.4    9.4   9.8   11.8     2.4
                Ventana 2             2                2 horas    7.4    9.4   9.8   11.8     2.4
                Ventana 3             2                2 horas    7.4    9.4   9.8   11.8     2.4
                Puerta                2                4 horas    7.4   11.4   7.8   11.8     0.4
                Techo                 9               4.4 horas   7.4   11.8   7.4   11.8      0


Problema 2
   Considere el siguiente proyecto, cuyos tiempos por tarea están en semanas:
                                                      Tiempos por tarea
                                 Tarea
                                          Optimista     Más probable Pesimista
                                   A          3               4           5
                                   B          5               7           9
                                   C          4               12         14
                                   D          1               3          11
                                   E          3               6           9
                                   F          1               4           7
                                   G          3               6           9
                                   H          2               5           8
                                   I          5               10         21
                                   J          1               3          11
                                   K          1               2           3
                                   L          3               8          19
                                   M          1               5          15
   A continuación, se muestra el diagrama PERT asociado a este proyecto:




(a) Calcule la ruta crı́tica del proyecto, indicando los valores de ES, EF, LS y LF para cada actividad.
(b) ¿Cuál es la probabilidad de que el proyecto termine en 26 semanas o menos? ¿Y en 32 semanas o menos?



                                                         5
(c) ¿Cómo cambia su respuesta anterior si para la tarea B los tiempos optimista, más probable y pesimista cambian
    a 1, 2 y 9 semanas, respectivamente?


Solución Problema 2
Parte a
   La ruta crı́tica se compone por las actividades que no tienen holgura. Recordar que para llenar esta tabla, se
debe partir con los ES y EF para cada actividad de arriba hacia abajo, y una vez terminado, se puede comenzar
con los LS y LF para cada actividad de abajo hacia arriba.
                                            Tarea      µ     σ       Varianza
                                             A         4    0.3        0.1
                                             B         7    0.7        0.4
                                             C         11   1.7        2.8
                                             D         4    1.7        2.8
                                              E        6    1.0        1.0
                                              F        4    1.0        1.0
                                             G         6    1.0        1.0
                                             H         5    1.0        1.0
                                              I        11   2.7        7.1
                                              J        4    1.7        2.8
                                             K         2    0.3        0.1
                                              L        9    2.7        7.1
                                             M         6    2.3        5.4
                                    Actividad     ES    EF      LS     LF   Holgura
                                        A          0     4       5      9      5
                                        B          0     7       4     11      4
                                        C          0    11       0     11      0
                                        D          4     8      13     17      9
                                        E          4    10       9     15      5
                                        F          7    11      11     15      4
                                        G         11    17      11     17      0
                                        H         11    16      17     22      6
                                        I          8    19      17     28      9
                                        J         11    15      15     19      4
                                        K         17    19      17     19      0
                                        L         19    28      19     28      0
                                       M          16    22      22     28      6
   La ruta crı́tica está determinada por las actividades cuya holgura es igual a 0. Finalmente, ésta es C - G - K - L.

Parte b
     La media de la duración del proyecto es de 28 semanas, que se calcula sumando las duraciones de las actividades
que componen la ruta crı́tica. La desviación estándar es de 3.3 (sumar la varianza de las actividades de la ruta
crı́tica y obtener la raı́z cuadrada). Con estos valores, se estandariza y luego se busca en la Tabla Normal (ver
Pregunta 1 de la Ayudantı́a 6 por si quedan dudas).
   Luego, la probabilidad de terminar en menos de 26 semanas es 27.4 % y la probabilidad de terminar en menos
de 32 semanas es de 88.69 %.




                                                            6
Parte c
   La respuesta no cambia, ya que la actividad B no es parte de la ruta crı́tica. Por ende, una disminución en su
duración sólo afecta a la holgura de la actividad, pero no a la duración del proyecto.


Problema 3
   Para la realización de un proyecto X en una empresa de cemento consiste de los siguientes procesos:
      Actividad     Predecesor     Tiempo optimista (a)      Tiempo más probable (m)          Tiempo Pesimista (b)
          A             -                  5                            6                               7
          B             -                  1                            3                               5
          C             -                  1                            4                               7
          D             A                  1                            2                               3
          E             B                  1                            2                               9
          F             C                  1                            5                               9
          G             C                  2                            2                               8
          H            E, F                4                            4                              10
          I             D                  2                            5                               8
          J           H, G                 2                            2                               8
   Utilizando estos datos responda las siguientes preguntas:
(a) ¿Cuál es la duración esperada y la varianza de cada actividad?
(b) ¿Qué actividades pertenecen a la ruta crı́tica y el tiempo del proyecto completo?
(c) ¿Cuál es la posibilidad de que el proyecto se complete en un tiempo menor o igual a 22 semanas?


Solución Problema 3
Parte a
                                            Tiempo         Tiempo          Tiempo      Tiempo      Varianza
              Actividad     Predecesor     optimista    más probable     Pesimista      (µ)         (σ)
                                              (a)            (m)             (b)
                   A             -             5              6               7            6          0.11
                   B             -             1              3               5            3          0.44
                   C             -             1              4               7            4          1.00
                   D            A              1              2               3            2          0.11
                   E            B              1              2               9            3          1.78
                   F            C              1              5               9            5          1.00
                   G            C              2              2               8            3          1.00
                   H           E, F            4              4              10            5          1.00
                   I            D              2              5               8            5          1.00
                   J           H, G            2              2               8            3          1.00

Parte b
   Para realizar el análisis de ruta crı́tica es necesario realizar el grafo de flujo de actividades:




                                                             7
   Con este grafo y utilizando los tiempos medios (µ) se obtiene el siguiente análisis de holgura:
                                   Actividad      µ   ES     EF       LS   LF    Holgura
                                       A          6    0      6        4   10       4
                                       B          3    0      3        3    6       3
                                       C          4    0      4        0    4       0
                                       D          2    6      8       10   12       4
                                       E          3    3      6        6    9       3
                                       F          5    4      9        4    9       0
                                       G          3    4      7       11   14       7
                                       H          5    9     14        9   14       0
                                       I          5    8     13       12   17       4
                                       J          3   14     17       14   17       0
   De este análisis de obtiene que la ruta crı́tica es: C-F-H-J. Y
   Y el tiempo promedio del proyecto es igual a 17 semanas.

Parte c
   Para hacer este análisis es necesario determinar la desviación estandar de la ruta crı́tica:

                         p                                        √
                    σ=       V arC + V arF + V arH + V arJ =          1.00 + 1.78 + 1.00 + 1.00 = 2.19

   Con este dato es posible determinar la probabilidad de que el proyecto se complete en un tiempo igual o menor
a 22 semanas:
                                                                                  
                                                  X −µ                     22 − 17
                       P (X ≤ 22) = P        Z≤              =P       Z≤                 = P (Z ≤ 2.28)
                                                    σ                       2.19

   Este valor de Z entrega probabilidad de 98.87 %. Por lo tanto, la probabilidad de el proyecto demore 22 semanas
o menos es igual a 98.87 %


Problema 4
   Se tiene un proyecto que consta de 9 actividades, con los tiempos y relaciones de precedencia mostrados en la
tabla.


                                                             8
                        Actividad     Predecesor    Tiempo promedio (semanas)     (semanas)
                            A              -                    2                    0,5
                            B              -                    2                     1
                            C              -                    2                    0,2
                            D             A                     9                     2
                            E             A                     5                    1,5
                            F            B, D                  10                    2,1
                            G          B, D, E                  6                    1,7
                            H            C, E                   5                     2
                            I          F, G, H                  1                     0
(a) Desarrollar el diagrama CPM del proyecto.
(b) Identificar la ruta crı́tica y duración mı́nima del proyecto, indicando los valores ES, EF, LS y LF, además de
    las holguras para cada actividad.
(c) ¿Cuál es la probabilidad de que el proyecto términe en menos de 21 semanas?


Solución Problema 4
Parte a
   El grafo de este problema es el siguiente:




Parte b
   El análisis de holgura es el siguiente:
                                      Actividad    ES   EF    LS   LF   Holgura
                                          A         0    2     0    2      0
                                          B         0    3     8   11      8
                                          C         0    2    14   16     14
                                          D         2   11     2   11      0
                                          E         2    7    10   15      8
                                          F        11   21    11   21      0
                                          G        11   17    15   21      4
                                          H         7   12    16   21      9
                                          I        21   22    21   22      0
    Ruta crı́tica: A - D - F - I. La duración media del proyecto es de 22 semanas con varianza de 8.66 semanas
(0.52 + 22 + 2.12 + 02 ).


                                                          9
Parte c

                                           X − Tproyecto   21 − 22
                                      z=                 = √       = −0.3398
                                                σ             8.66
                                              P (z < −0.3398) = 0.3669
Por lo tanto, hay una probabilidad de un 36.7 % de que el proyecto termine en menos de 21 semanas.


Problema 5
   Considerando el mismo proyecto de la pregunta anterior, pero teniendo seguridad respecto a la duración de las
actividades, existe la posibilidad de terminar el proyecto antes de lo previsto.
                           Tiempo promedio                           Tiempo más corto      Costo tiempo
              Actividad                         Costo normal ($)
                              (semanas)                                 (semanas)           más corto ($)
                  A               2                    $50                  1                     $90
                  B               3                    $200                 2                    $300
                  C               2                    $30                  1                     $50
                  D               9                   $1.000                4                   $1.700
                  E               5                    $500                 2                    $800
                  F               10                  $1.300                5                   $2.000
                  G               6                    $700                 3                   $1.100
                  H               5                    $600                 2                   $1.000
                  I               1                    $20                  1                     $20
(a) ¿Cuál es el costo normal de terminar el proyecto?
(b) ¿Cuál es la ruta crı́tica y el tiempo de terminar el proyecto lo antes posible?
(c) Si se tiene un presupuesto de $6.600, ¿se podrı́a terminar el proyecto en 11 semanas?


Solución Problema 5
Parte a
   Considerando las duraciones normales del proyecto, se tiene un costo normal de $4.400.

Parte b
                          Actividad    Tiempo más corto (semanas)      ES    EF       LS   LF
                              A                     1                    0     1        0    1
                              B                     2                    0     2        3    5
                              C                     1                    0     1        7    8
                              D                     4                    1     5        1    5
                              E                     2                    1     3        5    7
                              F                     5                    5    10        5   10
                              G                     3                    5     8        7   10
                              H                     2                    3     5        8   10
                              I                     1                   10    11       10   11

Parte c
    A partir de las holguras anteriores, se aprecia que no habrı́a necesidad de acortar todas las actividades, de tal
forma de optimizar el costo. Es el caso de las actividades C (podrı́a mantenerse en 3 semanas), C (2 semanas) y H
(5 semanas).


                                                          10
                      Actividad     Tiempo (semanas)    Costo ($)   ES    EF    LS   LF     H
                          A                1               $90       0     1     0    1     0
                          B                3              $200       0     3     2    5     2
                          C                2               $30       0     2     3    5     3
                          D                4             $1.700      1     5     1    5     0
                          E                2              $800       1     3     3    5     2
                          F                5             $2.000      5    10     5   10     0
                          G                3             $1.100      5     8     7   10     2
                          H                5              $600       5    10     5   10     0
                          I                1               $20      10    11    10   11     0
   El mı́nimo costo de terminar el proyecto lo antes posible es de $6.540. Por lo tanto, se tiene que es factible
terminar el proyecto en 11 semanas con el presupuesto de $6.600.


Problema 6
   Un proyecto consta de 9 actividades cuyos tiempos de duración se encuentran en semanas. En la tabla siguiente
se muestran las relaciones de precedencia de las actividades:
                        Actividad     Predecesor   Tiempo Normal     Desviación Estandar
                            A              -             4                     1
                            B             A              3                    0.5
                            C             A              2                   0.75
                            D             B              5                    0.8
                            E            B, C            1                    0.1
                            F             C              3                    0.6
                            G            E, F            4                     1
                            H            D, E            4                    1.1
                            I           H, G             6                     2
(a) Dibuje el diagrama PERT del proyecto
(b) Calcular ES, LS, EF, LF, las holguras de las actividades y el tiempo estimado de duración del proyecto. ¿Cuál
    es la ruta crı́tica?
(c) ¿Cuál es la probabilidad de terminar el proyecto en un tiempo menor a 20 semanas?
    Suponga que las actividades ahora pueden acortarse con un costo asociado. En la tabla siguiente se muestran
los costos normales y los costos de acortar las actividades:
       Actividad    Predecesor    Tiempo Normal     Tiempo más corto     Costo Normal      Costo más corto
           A             -              4                  3                    6                  9
           B            A               3                  2                    8                 15
           C            A               2                  1                    4                  6
           D            B               5                  3                    5                  8
           E           B, C             1                  1                   12                 12
           F            C               3                  3                    5                  5
           G           E, F             4                  3                    4                  6
           H           D, E             4                  1                    3                  7
           I          H, G              6                  5                    5                  6
 (d) ¿En cuántas semanas se acortarı́a la duración del proyecto si todas las actividades se demorasen su tiempo
     más corto? ¿Se mantiene la ruta crı́tica? ¿En cuánto aumentarı́an los costos?
 (e) Suponga que ninguna actividad se ha acortado. ¿Cuánto costarı́a adelantar el término del proyecto en 3
     semanas?



                                                        11
Solución Problema 6
Parte a
   La red PERT de este proyecto es:




   en esta figura las lı́neas azules representan actividades ficticias o dummy.

Parte b
   El análisis requerido para este problema es el siguiente
                           Actividad     Tiempo Normal       EF    EF    LS    LF    Holgura
                               A               4              0     4     0     4       0
                               B               3              4     7     4     7       0
                               C               2              4     6     7     9       3
                               D               5              7    12     7    12       0
                               E               1              7     8    11    12       4
                               F               3              6     9     9    12       3
                               G               4              9    13    12    16       3
                               H               4             12    16    12    16       0
                               I               6             16    22    16    22       0
   La duración del proyecto es de 22 semanas. La ruta crı́tica corresponde a las actividades que no tienen holgura,
es decir, la ruta crı́tica es A-B-D-H-I.

Parte c
   Para esto se necesita saber la desviación estándar de la ruta crı́tica:

                                            p
                                       σ=       1 + 0.52 + 0.82 + 1.12 + 22 = 2.66

   Y la probabilidad pedida es:
                                                
                                         20 − 22
                      P (X < 20) = P z <           = P (z < −0.75) = 1 − 0.7734 = 0.2266
                                          2.66

   Luego, el proyecto puede terminarse en menos de 20 semanas con una probabilidad de un 22.6 %.

Parte d
   En esta pregunta hay que hacer el mismo análisis de holgura pero con los tiempos más cortos:




                                                            12
                        Actividad     Tiempo más cortos      EF     EF     LS   LF   Holgura
                            A                3                 0      3      0    3      0
                            B                2                 3      5      4    6      1
                            C                1                 3      4      3    4      0
                            D                3                 5      8      6    9      1
                            E                1                 5      6      6    7      1
                            F                3                 4      7      4    7      0
                            G                3                 7     10      7   10      0
                            H                1                 8      9      9   10      1
                            I                5                10     15     10   15      0
  Con esta medida la duración del proyecto cambia a 15 semanas, es decir, 7 semanas menos que el caso anterior.
Cabe destacar que la ruta crı́tica es ahora A-C-F-G-I.
   El costo de realizar el proyecto sin acortar ninguna actividad corresponde a la suma de los costos normales de
todas las actividades:


                              Costo Normal = 6 + 8 + 4 + 5 + 12 + 5 + 4 + 3 + 5 = $52

   Por otro lado, el costo de acortar todas las actividades es de:


                           Costo más rápido = 9 + 15 + 6 + 8 + 12 + 5 + 6 + 7 + 6 = $74

   Luego, los costos aumentan en $22.

Parte e
   Se debe analizar el costo por unidad de tiempo de todas las actividades de la ruta crı́tica:
    Actividad    Predecesor        Tiempo          Tiempo          Costo      Costo         Costo por adelantar
                                Tiempo Normal     más corto       Normal    más corto   actividad en una semana
        A             -               4               3               6           9                   3
        B            A                3               2               8          15                   7
        C            A                2               1               4           6                   2
        D            B                5               3               5           8                  1.5
        E           B, C              1               1              12          12                   -
        F            C                3               3               5           5                   -
        G           E, F              4               3               4           6                   2
        H           D, E              4               1               3           7                 1.33
        I           H, G              6               5               5           6                   -
   Como se estableció en (a), la ruta crı́tica corresponde a A-B-D-H-I.
   Se puede observar que conviene adelantar la actividad A en una semana. De esta forma el proyecto podrı́a
terminar en 21 semanas. La siguiente actividad a adelantar debe ser H, ya que tiene el menor costo por semana.
Esta actividad podrı́a adelantarse 3 semanas desde un tiempo normal de 4 hasta un tiempo más corto de 1, pero en
este caso solo se necesita adelantar dicha actividad en 2 semanas, ya que se pide adelantar el proyecto en un total
de 3 semanas y ya se adelantó la actividad I en una semana.
   Entonces, el costo normal aumenta en 1 por adelantar I en una semana y en 1.33 por cada semana que se
adelanta H (1.33 × 2 = 2.66). Es decir, adelantar el término del proyecto en 3 semanas cuesta $52 (costo normal)
+ 1 + 2.66 = $55.66.




                                                         13
Problema 7
   Suponga que la empresa en la que usted trabaja está evaluando un próximo contrato consistente en la realización
de un proyecto por etapas. Se le ha pedido a usted que haga el análisis preliminar del proyecto para definir ciertos
aspectos del contrato.
   La relación de dependencia entre las etapas del proyecto y los tiempos esperados (en semanas) de duración de
cada una se muestran a continuación:
          Etapa    Predecesor    Tiempo optimista (a)     Tiempo más probable      Tiempo pesismista (b)
            A           -                2                        3                          4
            B          A                 2                        4                          6
            C          A                 5                        6                         13
            D         B, C               3                        6                          9
            E          B                 2                        5                          8
            F         D, E               2                        4                          6
    En base a ésta información y usando el método PERT que usted aprendió en el curso Gestión de Operaciones
se le pide:
(a) Encuentre los tiempos esperados y varianza para cada actividad
(b) Dibuje el diagrama PERT asociado al proyecto
(c) Obteniendo ES, EF, LS, LF y h para cada etapa ¿Cuál es la ruta crı́tica? ¿Cuál es la duración mı́nima del
    proyecto?
(d) ¿Cuál es la probabilidad de que el proyecto sea completado en menos de 22 semanas? Además, realice un
    intervalo de confianza de 95 % para la duración del proyecto.
   Suponga que usted puede reducir los tiempos de cada etapa manteniendo la varianza de las actividades inalterada.
Y una vez tomada la decisión el costo se asume antes de comenzar con el proyecto. La posible disminución en los
tiempos de cada etapa, el costo normal de cada etapa y costo acelerado son los siguientes:
             Actividad    Reducción de tiempo (Semanas)      Costo Normal ($)      Costo Acelerado ($)
                 A                        1                        10000                  13000
                 B                        1                         6000                   9000
                 C                        2                         4000                   7000
                 D                        2                        13000                  18000
                 E                        2                         9000                  13000
                 F                        1                         7000                   8000
 (e) Si su cliente le ofrece un bono de $8000 al finalizar el proyecto si el éste es terminado en menos de 18 semanas.
     Si debe determinar hoy que actividades acortar ¿Qué actividades acortarı́a?


Solución Problema 7
Parte a
   Utilizando las formulas de µ y σ de una distribución beta, obtenemos lo siguiente:
                                Actividad   Tiempo esperado (semanas)        Varianza
                                    A                   3                      0.1
                                    B                   4                      0.4
                                    C                   7                      1.8
                                    D                   6                      1.0
                                    E                   5                      1.0
                                    F                   4                      0.4



                                                         14
Parte b
   Viendo la tabla con los predecedores construimos el siguiente diagrama:




Parte c
              Actividad     Tiempo esperado (semanas)         Varianza    ES     EF   LS   LF   Holgura
                  A                     3                       0.1        0      3    0    3      0
                  B                     4                       0.4        3      7    6   10      3
                  C                     7                       1.8        3     10    3   10      0
                  D                     6                       1.0       10     16   10   16      0
                  E                     5                       1.0        7     12   11   16      4
                  F                     4                       0.4       16     20   16   20      0
   Por lo tanto la ruta crı́tica es: A-C-D-F y el tiempo de duración del proyecto es de 20 semanas.

Parte d
   Primero calculamos que la desviación estandar de la ruta crı́tica es:

                                                √
                                           σ=       0.1 + 1.8 + 1 + 0.4 = 1.82

   Con ello, el calculo que hay que realizar es el siguiente:

                                                         22 − 20
                                                    z=           = 1.1
                                                          1.82
   Buscando z = 1.1 en la tabla normal se obtiene que la probabilidad de que el proyecto sea completado en menos
de 22 semanas es de 86.4 %.
   Para un intervalo de confianza de 95 %, se tiene que buscar el z correspondiente a 0.975, ya que el intervalo de
confianza requiere de la distribución de dos colas (z = 1.96). El intervalo de confianza está dado por:


                          Intervalo de confianza 95 % = 20 ± 1.96 × 1.8 = 20 ± 3.6 semanas

Parte e
   Para obtener esto es necesario ver el ahorro generado en cada actividad y el costo asociado:




                                                            15
  Actividad    Reducción de tiempo (Semanas)      Costo Normal ($)     Costo Acelerado ($)     Aumento Costo ($)
      A                        1                        10000                 13000                  3000
      B                        1                         6000                  9000                  3000
      C                        2                         4000                  7000                  3000
      D                        2                        13000                 18000                  5000
      E                        2                         9000                 13000                  4000
      F                        1                         7000                  8000                  1000
   Para determinar si conviene o no acortar el proyecto y en cuánto se deberı́a acortar hay que obtener el beneficio
esperado de terminar el proyecto en menos de 18 semanas:
   Si no se hace ningún cambio en el proyecto:

                                                      18 − 20
                                                 z=           = −1.1
                                                       1.82
   Usando la tabla normal se obtiene que la probabilidad de que el proyecto sea completado en menos de 18 semanas
es de 13.6 %.
   Por lo tanto la utilidad esperada en este caso es:

                                    Beneficio Esperado = 0.136 × $8000 = $1086

                                                      Costos = 0
                           Utilidad esperada sin acortar proyecto = $1085 − $0 = $1086

    Si se acorta en una semana el proyecto Considerando las actividades de la ruta crı́tica, hay que decidir
cuál conviene acortar para evaluar el impacto en beneficio obtenido y costos asociados:
                              Alternativas   Tiempo Ahorrado (Semanas)         Costo ($)
                                   A                     1                       3000
                                   F                     1                       1000
   Considerando los costos, para acortar el proyecto en una semana conviene invertir en acelerar la etapa F.

                                                      18 − 19
                                                z=            = −0.55
                                                       1.82
   Buscando en la tabla normal se obtiene que la probabilidad de que el proyecto sea completado en menos de 18
semanas, dado que se acortó una semana, es de 29.12 %.
   Por lo tanto la utilidad esperada en este caso es:

                                  Beneficio Esperado = 0.2912 × $8000 = $2329.6

                                                    Costos = 1000
                        Utilidad esperada sin acortar proyecto = $2329.6 − $1000 = $1329.6

   Si se acorta en dos semanas el proyecto
   Considerando las actividades de la ruta crı́tica, hay que decidir cuál(es) conviene acortar para evaluar el impacto
en beneficio obtenido y costos asociados:
                              Alternativas   Tiempo Ahorrado (Semanas)         Costo ($)
                                 AyF                     2                       4000
                                   C                     2                       3000
                                   D                     2                       5000



                                                          16
   Considerando los costos, para acortar el proyecto en dos semanas conviene invertir en acelerar la etapa C

                                                        18 − 18
                                                   z=           =0
                                                         1.82
   Buscando en la tabla normal se obtiene que la probabilidad de que el proyecto sea completado en menos de 18
semanas, dado que se acortó dos semanas, es de 50 %.
   Por lo tanto la utilidad esperada en este caso es:

                                     Beneficio Esperado = 0.5 × $8000 = $4000

                                                    Costos = 3000
                          Utilidad esperada sin acortar proyecto = $4000 − $3000 = $1000

   Por lo tanto, finalmente al evaluar las distintas alternativas. Conviene acortar el proyecto en 1 semana invirtiendo
en acelerar la etapa F. De esta manera se logra maximizar el beneficio esperado.


Problema 8
   Elabore la función objetivo y las restricciones del modelo de optimización que permita minimizar el tiempo total
de un proyecto con determinadas actividades, de las que se conoce su duración y precedentes.


Solución Problema 8
   La variable considerada en este problema es Ti , que corresponde al tiempo de finalización de la actividad i.
   La función objetivo de este problema es
                                                        M in    Tn
, donde n es el ı́ndice que corresponde a la última actividad.
   Las restricciones de este problema son de la forma

                                                    Ti − Tj ≥ Dj

donde Dj es la duración de la actividad j, y esta restricción se plantea para todas las actividades j, y para todas
las actividades i precedentes de j.


Problema 9
   Se ha establecido que un proyecto tiene la siguiente lista de actividades y los correspondientes tiempos para
terminarlas:
                                      Actividad    Tiempo (dı́as)    Predecesor
                                          A             1                -
                                          B             4                A
                                          C             3                A
                                          D             7                A
                                          E             6                B
                                          F             2               C,D
                                          G             7               E,F
                                          H             9                D
                                          I             4               G,H
(a) Dibuje el diagrama de la ruta crı́tica.


                                                           17
(b) Marque los tiempos de inicio y fi nal más próximos.
(c) Marque la ruta crı́tica.
(d) ¿Qué pasarı́a si se modifi cara la actividad F de modo que tomara cuatro dı́as en lugar de dos?


Solución Problema 9
Parte a, b y c
   El siguiente diagrama muestra las respuestas a los incisos a, b y c.




   En una tabla el análisis de holgura es el siguiente.
                               Actividad    Tiempo (dı́as)       ES   EF   LS   LF   H
                                   A             1                0    1    0    1   0
                                   B             4                1    5    1    5   0
                                   C             3                1    4    6    9   5
                                   D             7                1    8    8    9   1
                                   E             6                5   11    5   11   0
                                   F             2                8   10    9   11   1
                                   G             7               11   18   11   18   0
                                   H             9                8   17    9   18   1
                                   I             4               18   22   18   22   0
   La ruta crı́tica es A-D-F-G-I. El tiempo del proyecto 22 dı́as.

Parte d
   Nueva ruta crı́tica: A-D-F-G-I. El tiempo para terminar es 23 dı́as.


Problema 10
   Considere un proyecto con 7 actividades, con los tiempos, costos y relaciones de precedencia mostrados en la
tabla.




                                                            18
                       Actividad    Predecesor     Tiempo normal (semanas)       Costo normal
                           A            -                    2                      50.000
                           B            -                    3                     200.000
                           C            -                    2                      30.000
                           D            A                    9                    1.000.000
                           E           A, B                  5                     500.000
                           G         D, E, F                 6                     700.000
(a) Desarrollar el diagrama CPM del proyecto.
(b) Identificar la ruta crı́tica, duración y costo del proyecto, indicando los valores de ES, EF, LS, LF y holguras
    para cada actividad.
    Usted desea tener en funcionamiento la cafeteria para las vacaciones, periodo en el cual se espera una mayor
afluencia de clientes. Afortunadamente existe la posibilidad de acortar los tiempos del proyecto, no obstante esto
significa un aumento en los costos de las actividades de acuerdo a dos posibles contratos.
1 Contrato 1: Cada semana en que se reduce una actividad involucra un costo incremental de 25.000. Las actividades
  pueden llegar solo un minimo de duracion de 1 semana.
2 Contrato 2: Un contratista le ofrece hacerse cargo del proyecto, con un costo fijo adicional de 310.000 (independiente
  de las actividades) y le ofrece terminar en 9 semanas.
   Bajo cualquiera de ambos contratos los costos considerados se suman al Costo normal del proyecto.
(c) Si se desea terminar el proyecto en 9 semanas, ¿que contrato resulta mas conveniente, y que costo involucra?


Solución problema 10
Parte a




                                                          19
Parte b
                                        Actividad   ES    LF    LS    LF    H
                                            A        0     2     1     3    1
                                            B        0     3     0     3    0
                                            C        0     2     1     3    1
                                            D        2    11     4    13    2
                                            E        3     8     8    13    5
                                            F        3    13     3    13    0
                                            G       13    18    13    18    0
Ruta crı́tica: B - F - G.
Duración proyecto: 18 semanas.
Costo Proyecto: 3.780.000

Parte c
   Se desea una duracion del proyecto de 9 semanas. Para ello se evaluan ambas alternativas de contratos.

Contrato 1
- Se intenta acortar principalmente a las actividades de la ruta critica que determinan la duracion del proyecto.
- Para que el proyecto termine en 9 semanas, G debe terminar en 9, por lo que podemos acortar la actividad G en
4 semanas, con un costo de 100.000.
- Luego, se acorta la actividad B en una semana, con un costo de 25.000. Con ello el proyecto tendria una duracion
de 11 semanas.
- Finalmente, D y F deben acortarse tal que se terminen antes de las 8 semanas (comienzo de G). Implica acortar
en 3 y 4 semanas a D y F respectivamente. Esto significa un costo de 175.000
- Costo total contrato 1 = 300.000

                            Actividad    Tiempo (semanas)      ES    EF    LS   LF    H
                                A                2              0     2     1    3     1
                                B                3              0     3     0    3     0
                                C                2              0     2     1    3     1
                                D                9              2    11     4   13     2
                                E                5              3     8     8   13    15
                                F               10              3    13     3   13     0
                                G                5             13    18    13   18     0
Se aprecia que ahora todas las actividades a excepcion de E son criticas (no poseen holgura).

Contrato 2
Contrato 2: tiene un costo fijo de 310.000. Por lo tanto, resulta mas conveniente utilizar el contrato 1.




                                                         20
