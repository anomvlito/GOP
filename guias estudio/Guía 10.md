                  Pontificia Universidad Católica de Chile
                  Escuela de Ingenierı́a
                  Departamento de Ingenierı́a Industrial y Sistemas
                  ICS3213 - Gestion de Operaciones
                  Ayudantes: Josefina Elsaca y Juan José Feller
                  2018-I


                                              Guı́a de Ejercicios:
                                              Lean y Bodegas y CD


1. Calidad
1.1. Problema 1
   En una fabrica de galletas, la lı́nea está trabajando en régimen. Se han tomado muestras, con 5 elementos
cada una, una vez por hora. La empresa le da a usted una tabal de datos de esos muestreos, Los dueños de la
empresa esperan que pueda decir si el proceso está o no fuera de control realmente.




    A su vez están analizando dos nuevos clientes:
· Cliente 1 plantea una especificación que es 1.4 a 1.6.
· Cliente 2 plantea una especificación que es 1.2 a 1.8

                                                            1
    Además para la empresa implican costos tanto fijos com variables aceptar a cliente, ya que ambos clientes
provocan constos fijos de $3,000,000 y para mantener su nivel de calidad el cliente 1 cobra una multa de $500.000
por el porcentaje de veces que el material se encuentre dentro de su rango de especificación, mientras que el
cliente 2 cobra una multa de $100.000 por el porcentaje de veces que el material no se encuentre en su rango
de especificación.
Usted está asesorando a la fábrica de galletas, quien le plantea que desea minimizar sus costos al contratar
clientes. ¿Con cúal d elos dos clientes le recomendarı́a hacer negocios?




   Solución:
   Primero debemos identificar que se tienen 25 muestras con un tamaño de muestras de 5 unidades. Con esto
y con los datos recopilados de la tabla del formulario se puede calcular:

                                            X = 1,5056 y R = 0,325

                                A2 = 0,577 ; D3 = 0 ; D4 = 2,1144 ; d2 = 2,326
   COn esta información proseguimos a calular los lı́mites de control de fábrica:
                                              b = X + A2 · R = 1,7
                                          LCS X
                                              b = X − A2 · R = 1,32
                                          LCI X
                                            LCSR = D4 · R = 0,69
                                              LCIR = D3 · R = 0
   Con esto podemos calcular las probabilidades de especificación de los clientes:
   Cliente 1 :


                                      P (x ≤ 1,6) = P (z ≤ 0,64) = 73,9 %
                                     P (x ≤ 1,4) = P (z ≤ −0,79) = 21,5 %
   Lo que requiere cliente uno es
                                           P (1,4 ≤ x ≤ 1,6) = 52,5 %
   La fábrica cumplirá con las especificaciones con un 52.4 %.
   Cliente 2 :


                                     P (x ≤ 1,8) = P (z ≤ 2,07) = 98,08 %
                                      P (x ≤ 1,2) = P (z ≤ −2,2) = 1,39 %
   Lo que requiere cliente uno es
                                           P (1,2 ≤ x ≤ 1,8) = 96,7 %


                                                        2
   La fábrica cumplirá con las especificaciones con un 96.7 %.
Ahora proseguimos a calcular los costos de ambos clientes.
   Costo Cliente 1= 3, 000, 000 + 500, 000 · P (nocumplir) = 3, 238, 000
Costo Cliente 2= 3, 000, 000 + 100, 000 · P (nocumplir) = 3, 003, 300

   Luego el cliente que minimiza los costos es el cliente 2, por lo tanto escojo hacer negocios con él.

1.2. Problema 2
    La empresa ABC desea establecer un plan de producción JIT. La demanda diaria registrada es de 200
tarjetas telefónicas por hora. El proceso de producción de estas tarjetas pasa por 3 grandes operaciones antes
del contro de calidad ubicado al final de la lı́nea: impresión de leyendas (P1), la inclusión de chip (P2) y cortado
de tarjetas (P3). Esto se muestra en la siguiente figura:




    La empresa cuenta con un registro de los tiempos promedios de procesamiento (tpi ) por operación, además
de los tiempos de envı́o de los Kanban (tki ) y los tiempos de envı́o de los lotes (tvi ).

                                  OPERACIÓN        Lote (C)    tpi s   tki s   tvi s
                                      P1              200        85      45     200
                                      P2              250        78      67     300
                                      P3              300        50      92     150

   Por su parte, los registros de control de calidad indican que en promedio un 15 % de kas unidades son
descartadas.

   a) A partir de los registros históricos de los datos anteriores, calcule el numero de Kanban necesarios en el
proceso productivo.

    Las investigaciones de la empresa han determinado que el proceso P3 es el que está actualmente generando
el 15 % del descarte de las tarjetas, las cuales no están saliendo con los tamaños adecuados. Se realizó un
muestreo del largo de las tarjetas de 5 lotes recibidos durante los últimos 5 dı́as. Los resultados se muestran a
continuación:

                                            Dı́a   Largo (mm)
                                            1      70 56 49       67    61
                                            2      65 47 70       70    68
                                            3      70 49 42       68    54
                                            4      50 47 52       67    50
                                              5    48 65 51       50    65

   b) Calcule los lı́mites de control, eliminando los outliners. Realice los gráficos correspondientes.




                                                          3
    c) Si al dı́a 6 usted toma una muestra con los siguientes resultados: 63, 54, 43, 69 y 65. ¿ Qué se puede decir
de la muestra? ¿El proceso está bajo control?

    d) EL implementar el control, reduce la fallas del sistema solo un 5 %. Con esta información, ¿cambia el
número Kanban? Argumente.

    Solución:
a) Se calcula L para cada proceso, como la suma de los tiempos:
· L1 = 330
· L2 = 445
· L3 = 292

                                                      D    L
   Ahora se calcula el Kanban para cada proceso, N = 0,85 ·C
· N1 = 389
· N2 = 419
· N3 = 230

   b)Se calculas los promedios y los rangos de le los largos de tarjetas

                                                     X          R
                                                   60.6         21
                                                    64          23
                                                   54.6         28
                                                   53.2         20
                                                   55.8         17
                                                   58.04       21.8

   De la tabla del ejercicio anterior obtenemos los siguientes valores:
· A2 = 0,58
· D3 = 0
· D4 = 2,11

   · LCS R = 46
·Xb = 70,7
· LCI R = 0
· LCI X
      b = 45,4

   Podemos apreciar de que tenemos numeros fuera de rango.

                                         Dı́a   Largo (mm)
                                         1      70 56 49          67   61
                                         2      65 47 70          70   68
                                         3      70 49             68   54
                                         4      50 47 52          67   50
                                           5    48 65 51          50   65

   Se vuelve a calcular el promedio de estos datos y se obtiene un promedio 58.8 y un rango de 24.6, ahora
obtenemos:


                                                           4
    · LCS R = 43
· X = 70,6
  b
· LCI R = 0
· LCI Xb = 46,9

     c) El rango de la muestra del dı́a 6 tienen un rango de 26 y un promedio de 58.8, lo que está dentro de los
lı́mites. Se puede aceptar el lote.

   d) Si cambia, porque ahora cambia la demanda. Esta serı́a solo 2,000/0.05. Si volvemos a calcular el Kanban
                                        D    L
para cada proceso, pero utilizando N = 0,95 ·C
· N1 = 348
· N2 = 375
· N3 = 205



2. Lean
2.1. Problema 1
   Preguntas de verdadero y falso:

  1. Al aplicar Six Sigma, primero nos enfocamos en reducir la variabilidad y posteriormente en mejorar el
     promedio.
     Solución: Verdadero

  2. La motivación principal del Heijunka es el mejoramiento de la calidad.
     Solución: Falso, tiene como motivación equilibrar los tamaños de lotes producidos y las condiciones de
     proceso para aumentar la frecuencia de producción y disminuir lotes e inventarios

  3. El andón es la forma que tiene el sistema productivo de Toyota de encontrar a la persona responsable del
     problema de calidad.
     Solución: Falso, es el una forma que toma el sistema a fin de avisar de una falla y poder solucionarlo.

2.2. Problema 2
    Supóngase que un hospital privado especializado en una cirugı́a en particular tiene demanda de 16 opera-
ciones al dı́a y que la sala de operación está abierta ocho horas por dı́a,Calule el takt time.

    Solución: Tiempo Takt es un ı́ndice de demanda para un proceso que se calcula dividiendo el tiempo de
producción entre la cantidad de productos que el cliente demanda en tal tiempo. En el caso de la sala de
operaciones, el tiempo de producción es 8 × 60 minutos, dividido entre 16 cirugı́as que deben hacerse en ese
tiempo; lo que da un Takt de 30 minutos.

2.3. Problema 3
   Defina que es el desperdicio o muda, y mencione los principales ejemplos.

   Solución:

                                                       5
   Cualquier cosa o actividad que genera costos pero que no agrega valor al producto se considera un desperdicio
o muda. En Ohno (1988) se identifi can siete tipos de desperdicio: sobreproducción, esperas, transportación,
sobreprocesamiento, inventarios, movimientos y retrabajos.


3. Bodegas y CD
3.1. Problema 1
    Usted está a cargo de las operaciones de un CD de una marca de cervezaas conocidas como ING. Dentro
de sus planes, usted considera optimizar los procesos dentro del CD. En primer lugar desea diseñar una bodega
con pallets a piso para los SKU dispuestos en la siguiente tabla. La bodega recibirá pallets de 1.3 m x 1.1 m
en invierno y 1.4 m x 1.4 m en verano, los que se ubican de modo que la cara más agosta de hacia el pasillo, el
que se encuentra a un solo lado y tiene un ancho de 5 metros. En invierno se reciben packs de cervezas chicas
en botella (A), six packs de latas 330 cc (B), galones de cerveza (c) y packs de botellas de litro retornable (D).
En cambio en verano se reciben galones (c), packs de botellas de litro retornables (D) y packs de cervezas de
latas de 470 cc (E). La cantidad ordenada y la altura máxima de apilado se muestran a continuación:

                         SKU     Cantiad Ordenada (pallet)       Altura apilado (pallets)
                          A                 29                              4
                          B                 13                              7
                          C                  7                              4
                          D                 15                              2
                          E                 12                              3


  a) Para cada SKU determine la profundidad óptima para asegurar el guardado de los productos en cada
     periodo.

  b) Para todas las SKU, determine una profundidad óptima única para cada temporada.

  c) Construya un gráfico para las profundidades calculadas en verano, donde el eje x será SKU y el eje y
     será la profundidad.

  d) Determine la configuración óptima de la bodega de modo de optimizar el uso del espacio en verano.

   Solución: a)                                            r
                                                                α i
                                                P rofi =         ·
                                                                2 i
Donde, α = anchopasillo
            anchopallet , qi = Dda ordenada del SKUi y zi = altura de apilado. Es importante mencionar que
para deteminar el valor de α se debe utilizar el largo de la otra cara.
   Se obtiene:

     SKU     Profundidad INV     # pallet necesarios INV        Profundidad VER    # pallet necesarios VER
      A            3.73                     4                           -                      -
      B            1.89                     2                           -                      -
      C            1.83                     2                         1.77                    2
      D            3.80                     4                         3.66                    4
      E              -                      -                         2.67                    3



                                                        6
b)                                                  v
                                                    u
                                                    uα 1 X i
                                                             i
                                            P rof = t  · ·
                                                      2 n    i i

Con n = númerodeSKU

                                     P rofIN V = 2,97 y P rofV ER = 2,80
     c)




                                      Figura 1: Altura de pallet verano

d) Con los resultados obtenidos en pregunta b) se puede obtener la siguiente configuración:




                                      Figura 2: Configuración de Bodega


                                 Sup = (3x1,4m + 5m)x(6x1,4m) = 77,28m2

                                                       7
3.2. Problema 2
    Para la operacioón de su CD de operación de verano, suponga que le toma 1.2 minutos hacer un pick en la
zona frontal y 1.6 minutos hacer un pick en la zona de reserva. Se decide que se podrán hacer picks de cajas
y pallets completos en la zona frontal. Por otro lado, la reposición toma 3.5 minutos y cada posición tiene
una profundidad de 3 pallets. Calcule los beneficios, rankings y ubicaciones de cada SKU. Considere que sólo
dispone de 12 posiciones para pick.

           SKU     Picks   Dda(pallets)   Dda pallets completos          #Min(Pallets)   #Max(Pallets)
            A       250        24                  14                         4              22
            B       070        06                  18                         1              08
            C       147        13                  24                         2              13
            D       093        21                  04                         5              25

   Solución: li = minimo cantidad de posiciones necesarias ui = máxima cantidad de posiciones necesarias
   Ambos para una profundidad de 3 pallets.

                                                    Li       Ui
                                                    2        8
                                                    1        3
                                                    1        5
                                                    2        9

                                               Tabla 1: Caption

   Lo cual se calcula con el número de pallet (max y min) sobre la profundidad de 3 pallets.
   Para cada SKU proseguimos en calcular lo siguiente:
                                                             si · Pi − Cri · di
                                       Beneficio-min =
                                                                     Li
                                                        si · Di + Cri · di
                                    Beneficio-adicional =
                                                             U i − Li
                                                         si · (Pi + Di )
                                     Beneficio-maximo =
                                                                Ui
    Donde si corresponde al ahooro de tiempo por pick, Cr i corresponde al tiempo necesario para reponer, di
es la demanda y Di corresponde a la demanda de pallets completos

                                  Beneficio   Mı́nimo        Adicional     Máximo
                                     A           8            14.93         13.20
                                     B           7            14.10         11.73
                                     C         13.3           13.78         13.68
                                     D        -18.15          10.73         4.31

                                               Tabla 2: Caption

   Luego se ordenan por beneficio, dónde para cada SKU solo puede estar el máximo o el mı́nimo y el adicional.
Las ubicaciones necesarias son L si es mı́nimo, U si es máximo y U-L si es adicional.
   Luego como disponemos solamente de 12 posiciones para pick frontal nos quedamos con las tres primeras
categorı́as de la tabla.

                                                         8
                                                    Beneficio         Ubicación
                                         A Adic      14.93                6
                                         B Adic      14.10                2
                                         C Adic      13.78                4
                                         C Max       13.68                5
                                         C Min       13.30                1
                                         A Max       13.20                8
                                         B Max       11.73                3
                                         D Adic      10.73                7
                                         A Min        8.00                2
                                         B Min        7.00                1
                                         D Max        4.31                9
                                         D Min       -18.15               2


3.3. Problema 3
    Finalemente, el CD dispone de un volumen de 1.900 m3, en un área de picking rápido que se surte de un
área de reserva. Por polı́ticas de la empresa todos los SKU deben ingresar a esta área y actividad está dada de
la siguiente manera:

                                 SKU    Pick/mes      un/mes      un/caja          m3/caja
                                  A        780         4,600        25               4.5
                                  B        610         1,150        17                4
                                  C        300         2,100        11                3
                                  D        480         2,900        20                2


     a) ¿Cuánto espacio se le asigna a cada una?

     b) ¿Con qué frecuencia se deben reponer si se hace al mismo tiempo?

     c) Explique cómo varı́an los resultados obtenidos si ahora se asignan los SKU con igual espacio e igual
        tiempo.

      Solución: a)
                                                      un/mes m3
                                               fi =          ·
                                                      un/caja caja
Determinamos el flujo de cada SKU

                                                      fi
                                                Vi = P · VT otal
                                                       fi
      Determinamos el espacio de cada producto.
      LOs resultados los tabulamos en la siguiente tabla:
b)
                                                                 fi
                                                      f reci =
                                                                 Vi
    c) Al asignar el mismo espacio a cada producto, debemos dividir el volumen total por la cantidad de SKU
que tengamos, de esta forma obtenemos el volumen por SKU. COn esta nueva información podemos volver a
calcular las frecuencias y ver que ocurre con los resultados.

                                                            9
                                        SKU      Flujo m3/mes     Volúmen m3
                                         A            828            634.35
                                         B           270.58          362.73
                                         C           572.72          527.58
                                         D            290            375.42

                                     Tabla 3: Flujos y volúmenes de cada SKU

                                               SKU    Frecuencia rep/mes
                                                A             1.3
                                                B            0.74
                                                C            1.08
                                                D            0.77

                                                  Tabla 4: Frecuencias

                                               SKU    Frecuencia rep/mes
                                                A            1.74
                                                B            0.56
                                                C             1.2
                                                D            0.61

                                                  Tabla 5: Frecuencias


3.4. Problema 4
    Dadas las polı́ticas de optimización de procesos ING desea diseñar un nuevo CD. En este trabajarán 12
personas, 8 horas al dı́a, 250 dı́as al año. La tasa de servicio de cada operador es de 9 minutos por pallet. Por
razones de logı́stica usted desea mantener, en promedio, una rotación de 1.5 meses. Los pallets miden 1.4 X
1.2 X 1 m3, ancho largo y alto, respectivamente. Sin embargo por razones de seguridad, la altura no puede
sobrepasar los 5 m de altura.

     a) Calcule la tasa de servicio del CD.

     b) Capacidad de pallet en CD.

     c) Calcule el área del terreno que comprará.

     d) Calcule la capacidad del CD en m3, sin considerar pasillos.

      Solución:
a)
                                           hora              dı́a   1pallet           pallet
                           λ = 12per · 8        · dı́a · 250      ·         = 160,000
                                            per              año 9/60horas            año
      b)
                                                    rotaciones
                                                      8
                                                       año
                                                       λ
                                      Capacidad =            = 20,000pallets
                                                  rotaciones


                                                           10
   c)
                      Superf icie = Capacidad/Alturaxanchopalletxlargopallet = 6, 720m2
   d)
                                   V olumen = Superf iciexaltura = 33, 600m3

3.5. Problema 5
   Describa ventajas y desventajas del almacenamiento compartido sobre el dedicado.

   Solución:

   Ventajas:

        Mayor aprovechamiento de espacio disponible: al no tener posiciones reservadas para cada producto, al
        desocuparse una posición se puede reasignar a otro producto, sin tener que esperar por el tiempo de
        reposición.

        Un producto puede estar en más de una posición, ocupando superficies menores en cada posición. Permi-
        tiendo que se desocupen posiciones de forma más frecuente, las que son reasignadas.

   Desventajas:

        Las posiciones de los productos cambian: los trabajadores tienen mayores dificultades con aprender las
        posiciones, por lo que deben ser guiados por el sistema informático de la bodega.

        Mayor complejidad de administrar: ya que agrega otros factores a considerar, como: elegir la posición a
        la que conviene ir a buscar un producto (el más cercano, el con menor cantidad, entre otros), trade-off
        entre reducir tiempo o espacio, etc. Esto exige mejores sistemas informáticos y mayor disciplina de los
        trabajadores para que funcione correctamente. (Bartholdi, Warehouse Distribution Science, página 15)

3.6. Problema 6
    Usted está diseñando una bodega de pallets a piso cuyos pasillos son de 4,2 m de ancho. Los pallets son de
1,2 m x 1 m y se ubican con la cara más angosta hacia el pasillo. Asuma que cada SKU tiene una demanda
constante y es reordenado de acuerdo al ciclo de pedido a continuación:

   SKU       Cantidad de pallest pedidos       Altura de apilado(pallets)      Ciclo de pedido(semanas)
    A                    32                                1                               5
    B                    28                                2                               4
    C                    14                                3                               6

  1. Para cada SKU determina la profundidad óptima para ser guardado

  2. Para todas las SKU determine una profundidad óptima única

   Solución 1:

   Usando la formula:                                         r
                                                                  a ∗ qi
                                            prof undidadi =
                                                                  2 ∗ zi

                                                        11
Donde a representa la razón entre el ancho del pasillo y el ancho del pallet (el largo de la cara que no da hacia
el pasillo), qi es la cantidad ordenada, y zi es la altura de los pallets. Se obtienen los siguientes resultados:

                                                Tabla 6: Resultados

                                                SKU       Profunidad
                                                 A           7.48
                                                 B           4.95
                                                 C           2.86

  Solución 2:
Ahora la profundidad óptima es la siguiente:
                                                          v
                                                          u      N
                                                          ua ∗ 1 X qi
                                          prof undidadi = t
                                                            2∗n    zi
                                                                     i=1

En esta parte, como el ciclo de pedido es distinto para cada SKU, debemos encontrar un mı́nimo común múltiplo
para los ciclos, en este caso 60, y ponderar de acuerdo a eso. Si todos tuviesen el mismo ciclo, se utiliza la fórmula
y el n serı́a igual a 3 (porque tenemos 3 SKU).
                                         r
                                            3,5 ∗ 1        32        28        14
                          prof unidad =             ∗ 12 ∗    + 15 ∗    + 10 ∗     = 4, 3227
                                            2 ∗ 60         1         2          3

3.7. Problema 7
   Varias preguntas conceptuales:


   1. Verdadero o Falso: Una bodega bajo un esquema de asignación de espacio dedicada u organizada tiene
      una utilización levemente superior al 50
      Solución: Falso, Una asignación dedicada tiene siempre una eficiencia del 50

   2. Verdadero o Falso:En una zona de pickeo rápido se recomienda tener todos los SKU de alta rotación.

      Solución: Falso, se recomienda aquellos convenientes; los SKU de alta rotación pero con pickeos volumi-
      nosos respecto del tamaño de pallet es mejor tenerlos en ubicaciones especiales separadas.

   3. Verdadero o Falso:La externalización de actividades de bodega es conveniente cuando el mercado es
      inestable en su demanda y los requerimientos del cliente no son exigentes en cuanto a las entregas.
      Solución: Verdadero

3.8. Problema 8:
   Describa supuestos de las fórmulas de profundidad óptima global para varios SKU.

   Solución:
   1. No considera restricciones fı́sicas de la bodega.

   2. Considera un ancho único para el pasillo y la bodega.

                                                          12
3. Hace cálculos basado en el número de pallets completos, no por unidades o pick.

4. Asume que las tasas de ventas relativas de los distintos SKU son iguales.(Bartholdi, Warehouse Distri-
   bution Science, página 58)




                                                   13
