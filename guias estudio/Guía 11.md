             Pontificia Universidad Católica de Chile
             Escuela de Ingeniería
             Departamento de Ingeniería Industrial y de Sistemas
             ICS3212 – Gestión de operaciones




                                         Guía de calidad

    María Elena Concha (meconcha1@uc.cl), Max Garafulic (mgarafulic1@uc.cl)

Pregunta 1 (Ayudantía 2014-2):
Considere una empresa que recibe grandes lotes de componentes diariamente, por lo que
decide implementar un plan estadístico de aceptación. Existen 3 planes posibles, que
requieren cada uno un muestreo de 30 componentes. Estos se presentan en la figura 1. Los
planes consisten en:
     Plan A: Aceptar el lote si no contiene ningún componente defectuoso.
     Plan B: Aceptar el lote si contiene a lo más un componente defectuoso.
     Plan C: Aceptar el lote si contiene a lo más dos componentes defectuosos.




                                          Figura 1: Planes de control

Según esta información, ¿Qué plan escogería para las siguientes situaciones?
a. Debe haber una alta probabilidad de aceptar un lote con un 2% de componentes
   defectuosos.
b. Debe haber una alta probabilidad de rechazar un lote con un 8% de componentes
   defectuosos.
c. Un balance entre el riesgo de aceptar lotes con un 8% de componentes defectuosos y
   rechazar lotes con un 2 % de componentes defectuosos.

Solución:
   a. En forma general, para una distribución binomial se tiene:
                                                𝑛
                                   𝑃(𝑥 = 𝑖) = ( ) 𝑝𝑖 (1 − 𝑝)𝑛−𝑖
                                                𝑖
       En un lote con un 2 % de componentes defectuosos, cada componente tiene una
       probabilidad de 0,02 de ser defectuoso. Luego, la probabilidad de que un componente
       no sea defectuoso es 1 − 0,02 = 0,98. Analizando los 30 componentes, la
               Pontificia Universidad Católica de Chile
               Escuela de Ingeniería
               Departamento de Ingeniería Industrial y de Sistemas
               ICS3212 – Gestión de operaciones


       probabilidad de que no hayan componentes defectuosos es 0,9830 = 0,545, que
       corresponde a la probabilidad de aceptación del Plan A.
       Así, las probabilidades de aceptación son:
            Plan A: 0,9830 = 0,545
            Plan B: 0,9830 + 30 · 0,02 · 0,9829 = 0,879.
                                                    30·29
            Plan C: 0,9830 + 30 · 0,02 · 0,9829 + 2 · 0,022 · 0,9828 = 0,978.
       El Plan C es el más adecuado porque tiene la mayor probabilidad de aceptar un lote
       con un 2 % de componentes defectuosos.

   b. Realizando los cálculos de la misma forma que en caso anterior, se tiene que la
      probabilidad de aceptación de un lote que contiene un 8 % de componentes
      defectuosos es 0,082 para el Plan A, para el Plan B 0,296 y para el Plan C 0,565.
      Luego, el Plan A es el más adecuado porque tiene la mayor probabilidad de rechazar
      un lote que contiene un 8 % de componentes defectuosos.
   c. En la figura 1, se puede apreciar que el plan B es el más adecuado.

Pregunta 2 (Guía I3):
Los pesos de las cajas de hojuelas de avena incluidas dentro de un lote de producción grande
se muestrean cada hora. Los administradores quieren establecer límites de control que
incluyan el 99,73% de las medias muestrales. Se sabe que la desviación estándar es igual a
1. Establezca los límites superior e inferior, juego analice si el proceso se encuentra o no bajo
control. ¿Qué condiciones deberían darse para que ocurra lo opuesto?

                                       Hora               Promedio 9 muestras
                                         1                       16,1
                                         2                       16,8
                                         3                       15,5
                                         4                       16,5
                                         5                       16,5
                                         6                       16,4
                                         7                       15,2
                                         8                       16,4
                                         9                       16,3
                                        10                       14,8
                                        11                       14,2
                                        12                       17,3

Solución:
Se sabe que:
     68,3%: N=1 desviaciones estándar.
     95,4%: N=2 desviaciones estándar.
     99,73%: N=3 desviaciones estándar.
               Pontificia Universidad Católica de Chile
               Escuela de Ingeniería
               Departamento de Ingeniería Industrial y de Sistemas
               ICS3212 – Gestión de operaciones


       99,9999998%: N=6 desviaciones estándar.

Calculando el promedio y la desviación de las 9 cajas:
                           𝑥1 + ⋯ + 𝑥9                   𝜎    1    1
                      𝑥̅ =              = 16,      𝜎̅ =     =    =
                                 9                      √𝑛 √9 3
Reemplazando los valores en las fórmulas de UCL y LCL:
                                                         1
                           𝑈𝐶𝐿 = 𝑥̅ + 𝑧 · 𝜎̅ = 16 + 3 · ( ) = 17
                                                         3
                                                         1
                           𝐿𝐶𝐿 = 𝑥̅ − 𝑧 · 𝜎̅ = 16 − 3 · ( ) = 15
                                                         3

Se puede notar que los últimos 3 valores de la tabla están fuera de los valores establecidos, por
lo que no se puede considerar que es un proceso bajo control.
Por otro lado, si la desviación estándar fuera 2, el resultado para UCL y LCL sería distinto, así
quedarían dentro de los límites (los cuales serían 18 y 14).

Pregunta 3 (Ex 2014-1):
Una compañía de música que fabrica teclados realiza diariamente un análisis de calidad a una
muestra de 25 teclas para poder determinar el número total de teclas defectuosas. La probabilidad
de que una tecla resulte defectuosa sigue una distribución Uniforme (0, 1).
a. Si el número de teclas defectuosas en una muestra sigue una distribución Uniforme (0, 25),
    ¿Cuál es la distribución de probabilidad del número de teclas defectuosas si se sabe qué piezas
    son defectuosas? En la siguiente tabla se muestran la cantidad de teclas defectuosas en 30
    jornadas:
b. Si la producción se considera satisfactoria cuando el número de teclas defectuosas es menor
    a 4. ¿Cuál es la probabilidad de que la producción sea considerada satisfactoria?
c. En base a la probabilidad estimada en a), elabore el gráfico de control del proceso y determine
    si el proceso está bajo control.
d. Si el plan de muestreo está definido con un AQL de 10%, un LPTD de 40%, un 𝛼 = 0,05 y
    un 𝛽 = 0,1 ¿Es correcto el tamaño muestral que está usando la compañía?
e. ¿En qué se diferencia este proceso con un proceso de control de calidad de medidas
    continuas?

Hint:
La función de probabilidad de una distribución uniforme es:
                                                       1
                                         𝑓𝑥 (𝑥) =
                                                    𝑏−𝑎
La media y la varianza son:
                                     𝑎+𝑏                  (𝑏 − 𝑎)2
                               𝜇𝑥 =          ,      𝜎𝑥2 =
                                        2                    12
La función de probabilidad de una distribución binomial es:
                                               𝑛
                                 𝑝𝑥 (𝑥) = ( ) 𝑝 𝑥 (1 − 𝑝)𝑛−𝑥
                                               𝑥
La media y la varianza son:
                                𝜇𝑥 = 𝑛𝑝,         𝜎𝑥2 = 𝑛𝑝(1 − 𝑝)
               Pontificia Universidad Católica de Chile
               Escuela de Ingeniería
               Departamento de Ingeniería Industrial y de Sistemas
               ICS3212 – Gestión de operaciones




Solución:
   a. Sea 𝑋𝑛 el número de piezas defectuosas y sea 𝜇 la probabilidad de que una pieza resulte
       defectuosa. Como 𝑋𝑛 ~𝑈𝑛𝑖𝑓𝑜𝑟𝑚𝑒(0,25) y 𝜇~𝑈𝑛𝑖𝑓𝑜𝑟𝑚𝑒(0,1), entonces:
                                  𝑋𝑛 |𝑈 = 𝜇~𝐵𝑖𝑛𝑜𝑚𝑖𝑎𝑙(25, 𝜇)

   b. A partir de la tabla, se puede obtener una estimación de la probabilidad de que una tecla
      sea defectuosa. Sea 𝑥𝑖 la cantidad de teclas defectuosas en la jornada 𝑖. Luego:
                                                          30
                                                 1     𝑥𝑖
                                              𝑝=    ·∑    = 0,17
                                                 30    25
                                                          𝑖=1
       La probabilidad de que la producción sea satisfactoria es:
                     𝑝(𝑥 < 4) = 𝑝(𝑥 = 0) + 𝑝(𝑥 = 1) + 𝑝(𝑥 = 2) + 𝑝(𝑥 = 3)
                                             25 · 24                    25 · 24 · 23
 𝑝(𝑥 < 4) = 0,8325 + 25 · 0,17 · 0,8324 +            · 0,172 · 0,8323 +              · 0,173 · 0,8322 = 0,368
                                               2!                            3!

   c. Los límites de control definen el intervalo (𝜇 − 3𝜎, 𝜇 + 3𝜎). Como la distribución es
      binomial, se tiene:
            𝐿𝐶𝐿 = 𝐿𝐶𝐼 = 𝑛𝑝 − √𝑛𝑝 · (1 − 𝑝) = 25 · 0,17 − √25 · 0,17 · 0,83 = 2,36
            𝑈𝐶𝐿 = 𝐿𝐶𝑆 = 𝑛𝑝 + √𝑛𝑝 · (1 − 𝑝) = 25 · 0,17 + √25 · 0,17 · 0,83 = 6,11

       El gráfico de control es:




       Claramente el proceso está fuera de control.

   d. A partir del plan de muestreo de la tabla se tiene:
              Pontificia Universidad Católica de Chile
              Escuela de Ingeniería
              Departamento de Ingeniería Industrial y de Sistemas
              ICS3212 – Gestión de operaciones


                                   𝐿𝑃𝑇𝐷 0,4
                                         =     =4→𝑐=4
                                    𝐴𝑄𝐿    0,1
                              𝐴𝑄𝐿 · 𝑛 = 1,970 → 𝑛 = 19,7 ≈ 20
       El tamaño de muestra no es adecuado, ya que deberían estar tomando muestras de 20
       teclados.

   e. En estos procesos basta con conocer solo la media del proceso (la varianza queda
      determinada por la media). En un caso de medidas continuas con distribuciones como la
      normal, la media y la varianza no están relacionadas, por lo que es necesario monitorear
      la media del proceso y también la variabilidad.

Pregunta 4:
Una compañía de seguros está implementado un plan de pólizas que la empresa realiza. Se
toma cada semana una muestra (en total 2.500 pólizas semanales) y se anota la cantidad de
pólizas mal confeccionadas. El criterio de control es bajo 3-sigma. La información se
presenta a continuación:
                                            Muestra      Errores
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


a) Dibuje los gráficos de control para 3-sigma.
b) Muestre que este proceso está fuera de control. ¿Cuáles podrían ser algunas razones?
c) Si se usara 2 o 1 sigma como medida de control, ¿Estaría bajo proceso?
Solución:
                      Defectos      147
a) Calculamos p                            0, 0049 , con desviación
                    Observaciones 12  2500
                  Pontificia Universidad Católica de Chile
                  Escuela de Ingeniería
                  Departamento de Ingeniería Industrial y de Sistemas
                  ICS3212 – Gestión de operaciones



                          p (1  p ) / N  0, 0049  (1  0, 0049) / 2500  0, 0014 .

Los límites inferiores y superiores son:
                                             LS3  p  3d  0, 0091
                                             LI 3  p  3d  0, 0007

Por otro lado, las proporciones de error para cada muestra son:
                                    Muestra       Errores        Proporción error
                                       1            15               0.0060
                                       2            12               0.0048
                                       3            19               0.0076
                                       4             2               0.0008
                                       5            19               0.0076
                                       6             4               0.0016
                                       7            24               0.0096
                                       8             7               0.0028
                                       9            10               0.0040
                                      10            17               0.0068
                                      11            15               0.0060
                                      12             3               0.0012
                                     Total         147               0.0049


El gráfico queda como:

                                                 Gráfico control
          0.012

           0.01

          0.008

          0.006

          0.004

          0.002

             0
                      1       2      3       4     5         6     7      8    9      10    11   12

                                    LimInf         Promedio             Obs        LimSup
              Pontificia Universidad Católica de Chile
              Escuela de Ingeniería
              Departamento de Ingeniería Industrial y de Sistemas
              ICS3212 – Gestión de operaciones




b) La proporción de la muestra 7 supera el límite superior, por lo que el proceso está fuera
de control.
c) Los límites para 2-sigma son:
                                        LS 2  p  2d  0, 0077
                                        LI 2  p  2d  0, 0021

Como la proporción de falla de la muestra 7 está en este intervalo, bajo este criterio, el
proceso sí estaría bajo control. Obviamente, bajo 1-sigma también, pues es el criterio es
menos exigente que 2-sigma.

Problema 5 (Ayudantía 2015-2):

Usted quiere implementar un nuevo sistema de muestro para controlar los lotes de manzanas.
Para ello define una política con un AQL de 0,19 y un LPTD de 0,6. Usando   0, 05 y
  0,1 indique y explique el plan de muestreo que usará.

Solución: Del enunciado se puede obtener LPTD / AQL  3,1579 . Con este valor, revisando
las tablas para  y  se obtienen valores para c y nAQL :
                                        c6
                                        nAQL  3, 286
Así, se obtiene n  17,3 . Esto quiere decir que, usando esta política, se toma una muestra de
18 unidades, de las que si 6 salen defectuosas se rechaza el lote.

Pregunta 6 (Ayudantía 2015-2):

Usted está a cargo de evaluar la política de calidad que su empresa exige a productores de
manzanas. A continuación se muestra el peso de una muestra de los 4 bins recibidos durante
los últimos 5 días:

                                      Día            Peso (kg)
                                       1     380     395 403        387
                                       2     400     393 401        392
                                       3     397     392 384        390
                                       4     402     407 403        405
                                       5     391     389 393        385

a) Con la información dada elabore los gráficos de control.
              Pontificia Universidad Católica de Chile
              Escuela de Ingeniería
              Departamento de Ingeniería Industrial y de Sistemas
              ICS3212 – Gestión de operaciones


b) Si el día 6 usted toma una muestra con los resultados: 407, 381, 392 y 396. ¿Qué puede
decir de la muestra? ¿Acepta o rechaza el lote?

Solución:
a) Se tienen los siguientes promedios y rangos:

                 Día                 Peso (kg)                  Promedio   Recorrido
                  1      380     395       403           387     391.25       23
                  2      400     393       401           392      396.5        9
                  3      397     392       384           390     390.75       13
                  4      402     407       403           405     404.25        5
                  5      391     389       393           385      389.5        8

El promedio de las muestras es 394,95 kg, el promedio de los recorridos 11,6 kg y la
desviación estándar 6,1 kg. De las tablas de control:
A2 = 0,73.
D4 = 2,28.
D3 = 0.

Los límites son, entonces:
                       LCSX  X  A2 R  394, 45  0, 73 11, 6  402,92
                       LCIX  X  A2 R  394, 45  0, 73 11, 6  385,98
                       LCSR  D4 R  2,11 11, 6  26, 45
                    LCIR  D3 R  0 11, 6  0
Eliminando las muestras fuera de los límites:

                    Día            Peso (kg)               Promedio Recorrido
                       1           395               387         391         8
                       2       400 393 401           392       396.5         9
                       3       397 392               390         393         7
                       4       402                               402         0
                       5       391 389 393                       391         4

El promedio de las muestras es 394,7 kg, el de los recorridos 5,6 kg y la desviación estándar
4,7 kg. Se definen los límites para  , 2 ,3 :
              Pontificia Universidad Católica de Chile
              Escuela de Ingeniería
              Departamento de Ingeniería Industrial y de Sistemas
              ICS3212 – Gestión de operaciones


                                               3 S  408, 7
                                               2 S  404
                                               S  399, 4
                                              3 I  380, 73
                                              2 I  385, 4
                                               I  390
Así:




b) El promedio de los datos del día 6 es 392,25 kg y su rango 26 kg. Para verificar el rango
se debe calcular los límites inferior y superior de este (considerando pesos iniciales):
                               LCSR  D4 R  2,11 11, 6  26, 45
                                LCIR  D3 R  0 11, 6  0
Tanto el promedio como el rango de los datos medidos están dentro de los rangos aceptables,
por lo que sí se acepta el lote.

Pregunta 7: Usted está encargado del control de calidad de piezas de maquinaria que
requieren medidas específicas de su diámetro. Se le proporciona la siguiente información de
los diámetros medidos en 5 muestras:
              Pontificia Universidad Católica de Chile
              Escuela de Ingeniería
              Departamento de Ingeniería Industrial y de Sistemas
              ICS3212 – Gestión de operaciones


               Muestra                                 Observación
                   1                  5.014         5.022       5.009          5.027
                   2                  5.021         5.041       5.024           5.02
                   3                  5.018         5.026       5.035          5.023
                   4                  5.008         5.034       5.024          5.015
                   5                  5.041         5.056       5.034          5.047

a) Construya los gráficos de control (construya el gráfico en escala de centésimas).
b) ¿Está el proceso bajo control?

Solución: Los promedios y rangos son los siguientes:

             Muestra                   Observación                  Promedio   Recorrido
                1           5.014      5.022 5.009        5.027        5.018     0.018
                2           5.021      5.041 5.024         5.02       5.0265     0.021
                3           5.018      5.026 5.035        5.023       5.0255     0.017
                4           5.008      5.034 5.024        5.015      5.02025     0.026
                5           5.041      5.056 5.034        5.047       5.0445     0.022

De este modo, se tiene X  5, 027 y R  0, 021 . De los valores de tabla, se obtienen:
A2 = 0,729
D3 = 0
D4 = 2,282

Ahora construimos los límites superiores e inferiores de los gráficos:
                       LCSX  X  A2 R  5, 027  0, 729  0, 021  5, 042
                       LCIX  X  A2 R  5, 027  0, 729  0, 021  5, 012
                       LCSR  D4 R  2, 282  0, 021  0, 0479
                       LCIR  D3 R  0 11, 6  0

Los gráficos, para promedios y rangos, son los siguientes respectivamente:
                Pontificia Universidad Católica de Chile
                Escuela de Ingeniería
                Departamento de Ingeniería Industrial y de Sistemas
                ICS3212 – Gestión de operaciones



                                               Promedio datos
         5.05

         5.04

         5.03

         5.02

         5.01

           5

         4.99
                         1                 2                3               4            5

                                  LimInf         Promedio             Obs       LimSup




                                                    Rango
         0.06

         0.05

         0.04

         0.03

         0.02

         0.01

           0
                         1                 2                3               4            5

                                  LimInf         Promedio             Obs       LimSup



b) La media de la muestra 5 supera el límite superior, por lo que el proceso está fuera de
control.
