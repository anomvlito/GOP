       Pontificia Universidad Católica de Chile
       Departamento de Ingeniería Industrial y Sistemas
       ICS3213 Gestión de Operaciones
       Profesores: Alejandro Mac Cawley – Isabel Alarcón




                           Guía de Ejercicios 6: PERT y Localización

Max Garafulic (mgarafulic1@uc.cl)
Gonzalo Vargas (grvargas@uc.cl)

Problema 1 (Guía I2 2014-1)
Considerando la siguiente información:
                                                    Tiempo por Tarea (semanas)
                 Tarea                       Optimista   Más probable     Pesimista
           Tarea precedente                  (a)         (m)              (b)
             A          -                         3              4              5
             B          -                         5              7              9
             C          -                         4             12             14
             D          A                         1              3             11
             E          A                         3              6              9
             F          B                         1              4              7
             G          C                         3              6              9
             H          C                         2              5              8
             I          D                         5             10             21
             J         E,F                        1              3             11
             K          G                         1              2              3
             L         J,K                        3              8             19
            M           H                         1              5             15

a) Dibuje el grafo de las actividades y calcule e idenetifique la ruta crítica del proyecto
indicando los valores de ES, EF, LS, LF para cada actividad.
b) ¿Cuál es la probabilidad de que el proyecto termine en 26 semanas o menos?¿Y en 32
semanas o menos?
c) ¿Cómo cambia su respuesta anterior si para la tarea G los tiempos mínimo, medio y
máximo cambiaran a 1, 2 y 9 semanas, respectivamente?
d) Como cambia su respuesta en b) si para la tarea B los tiempos mínimo, medio y máximo
cambiaran a 1, 2 y 9 semanas, respectivamente?
Solución:
a) El grafo es:




La duración de actividades se considera como la media. La holgura de las actividades es la
diferencia entre el término medio más el tardío menos el temprano de la actividad. La
                                a + 4m + b                        b-a
media de las actividades es µ =            y su varianza es s 2 =     . Así:
                                     6                             6




La ruta crítica es aquella que pasa por todas las actividades que no tienen holgura y que, por
lo tanto, un atraso en alguna de ellas genera un atraso en la duración del proyecto completo.
En este caso, la ruta es CGKL.
b) La duración del proyecto X sigue una distribución normal, que se estandariza como
     X -µ
 Z=            N (0,1) , con µ = 28;s = 3,3 . Luego, las probabilidades pedidas son:
       s
                                   æ     26 - 28 ö    -1
                    P( X £ 26) = P ç Z £         ÷ = F (-2 / 3.3) = 0, 27
                                   è       3.3 ø
                                   æ     32 - 28 ö    -1
                    P( X £ 32) = P ç Z £         ÷ = F (4 / 3.3) = 0,89
                                   è       3.3 ø
c) Se recalcula sólo para G, y se ve si se afecta la ruta crítica. La ruta crítica no cambia,
pero cambian la media y la varianza. Con los nuevos valores obtenidos se recalculan las
probabilidades. Con los nuevos valores la duración media del proyecto cambia a 25
semanas, y la desviación a 3,4:




Realizando los mismos cálculos para la distribución de la duración del proyecto, se
obtienen probabilidades:
                                   æ     26 - 25 ö    -1
                    P( X £ 26) = P ç Z £         ÷ = F (1/ 3.4) = 0, 291
                                   è       3.4 ø
                                   æ     32 - 25 ö    -1
                    P( X £ 32) = P ç Z £         ÷ = F (7 / 3.4) = 0,98
                                   è       3.4 ø
d) La respuesta no cambia, pues B no forma parte de la ruta crítica, y por ende, cualquier
cambio en su duración afecta la holgura de la actividad, pero no la duración del proyecto.
Problema 2 (Guía I2 2015-1)
Un proyecto consta de las siguientes actividades, que toma llevarlas un tiempo U (a, b) :
                                                      Parámetros
                                                        U(a,b)
                                     Tarea
                        Tarea     precedente        a        b
                          A             -           3        5
                          B            A            0        6
                          C            A            1        3
                          D            B            3        7
                          E           B,C           1        1
                          F            C            1        5
                          G           E,F           3        5
                          H           E,D          1,5      6,5
                          I           H,G           5        7

a) Dibuje el diagrama correspondiente e identifique la ruta crítica, indicando ES, EF, LS,
LF.
b) ¿Cuál es la probabilidad de que el proyecto termine en 19,75 días o menos?
c) ¿Cómo cambia su respuesta anterior si los nuevos parámetros de la tarea C son 0 y 2?¿Y
los de la tarea D 2 y 4?
Solución:
a) El diagrama es:




                                       a + b 2 (b - a)2
Para una distribución U (a, b) , µ =        ,s =        , por lo que:
                                         2        12




Luego, la ruta crítica es ABDHI.
b) La duración media del proyecto es µ = 22 días y su desviación es s = s R2 = 3 . Luego,
                                                         X -µ
la duración X del proyecto se estandariza como Z =                N (0,1) . Así,
                                                           s
                                    æ     19, 75 - 22 ö    -1
                 P( X < 19, 75) = P ç Z <             ÷ = F (-0, 75) = 0, 226
                                    è          3      ø
c) Si los parámetros de C cambian la ruta crítica no es afectada y por tanto no se afecta la
duración del proyecto (tampoco su varianza). Si los parámetros de D cambian, se tiene:




Con media µ = 20 y desviación s = 2,84 . Así,
                                    æ     19, 75 - 20 ö
                 P( X < 19, 75) = P ç Z <             ÷ = F -1 (-0, 09) = 0, 464
                                    è        2,84 ø

Problema 3
Considere la información del siguiente proyecto:
                                      Normal                       Acelerado
                                             Costo                         Costo
        Tarea Predecesor Duración(días) ($)                 Duración(días) ($)
           A         -              4            100              2           200
           B         -              2             50              1           150
           C        A,B             1            200              1           200
           D        A,C             3            100              2           140
           E         B              5            200              3           300
           F        D,E             4             50              3           130
           G         F              1            120              1           120
           H         F              2            100              1           250

a) Calcule el costo de aceleración de cada actividad por día y la duración y costo normales
del proyecto.
b) Dibuje el diagrama del proyecto.
c) Calcule ES, EF, LS y LF y la holgura de cada actividad del proyecto no acelerado.
Identifique la ruta crítica.
d) Suponga que el proyecto parte con 3 días de retraso y el costo por día de retraso de
finalización del proyecto es de 90 ($/día), basado en la duración normal del proyecto.
Determine la estrategia de aceleración óptima que minimiza el costo total del proyecto.
Solución:
a) Considerando que las actividades C y G no se pueden adelantar, el costo por adelantar es
 ca - cn
         :
 dn - da
                                            Costo
                                    Tarea ($/día)
                                      A         50
                                      B        100
                                      C          -
                                      D         40
                                       E        50
                                       F        80
                                      G          -
                                      H        150

Por otro lado, la duración normal del proyecto es de 14 días y su costo normal $ 920.
b) Tenemos lo siguiente:




c) Haciendo los cálculos pertinentes, se tiene:
                              Tarea ES EF LS LF H
                                A       0     4 0 4 0
                                B       0     2 1 3 1
                                C       4     5 4 5 0
                                D       5     8 5 8 0
                                E       2     7 3 8 1
                                F       8 12 8 12 0
                                G      12 13 13 14 1
                                H      12 14 12 14 0

La única ruta crítica es ACDFH.
d) La duración normal del proyecto es de 14 días y su costo normal $ 920. Tenemos las
siguientes opciones:
- No adelantar nada: Tenemos tres días de retraso, y por tanto un costo de $ 270.
- Adelantar un día, adelantando la actividad con costo más barato de aceleración en la ruta
crítica, es decir, la actividad D con costo $ 40 por día. Luego, el costo es $ 180 + $ 40 = $
220. Notemos que al adelantar D, las actividades B y D se vuelven críticas y existen dos
rutas críticas: ACDFH y BEFH.
- Adelantar un segundo día, considerando las dos rutas críticas ACDFH y BEFH. Las
mejores combinaciones (menor costo) son {A,E} con costo $ 100, {F} con costo $ 80 y
{H} con costo $ 150 (costos por día). En este caso, lo mejor es elegir adelantar F, que tiene
un menor costo que la penalización por atraso ($ 90 por día). Así, el costo total es $ 90 + $
40 + $ 80 = $ 210. Notemos que al adelantar F se mantienen ambas rutas críticas anteriores.
- Adelantar un tercer día, considerando las mismas rutas críticas. En este caso, las mejores
opciones son {A,E} con costo $ 100 y {H} con costo $ 150 (costos por día). En este caso,
no es óptimo adelantar ninguna (es menos costoso atrasar el proyecto de costo $ 90 por
día).
Por lo tanto, conviene adelantar el proyecto dos días. El proyecto tendrá un día de retraso y
el costo total es $ 920 + $ 210 = $ 1.130.

Problema 4 (Guía I2 2015-1)
Una empresa está localizada en la VII región y cuenta con 5 sitios de producción y 3 sitios
de venta. Se quiere instalar un centro de distribución que disminuya los gastos logísticos de
la empresa. Considere la siguiente información:
                  Unidades                 Costo transporte
    Plantas       transportadas            ($/transp)                Coord X Coord Y
    Producción 1            120                         8                90         50
    Producción 2            200                         6                30         90
    Producción 3             60                         5                85         20
    Producción 4            100                         9                70         70
    Producción 5             50                         7               100         90
    Venta 1                 180                         5                60         85
    Venta 2                 200                         4                50         50
    Venta 3                 150                         6                30         60

Las zonas están divididas de acuerdo a la siguiente tabla de valores mínimos y máximos:
                                 Zonas (x,X) (y,Y)
                                       1 0,50        0,50
                                       2 50,100 0,50
                                       3 0,50 50,100
                                       4 50,100 50,100

a) ¿Dónde ubicaría el centro de distribución?
b) Se piensa habilitar una nueva zona en el origen, que presenta un aumento en ventas que
debe ser suministrado por el centro de producción más cercano, es decir, debe aumentar la
capacidad productiva de ese centro. El costo de transporte de esta nueva ubicación es de 8
($/transp.). ¿Cuál es la producción límite para que no se cambie de zona el centro de
distribución?
c) Para decidir la empresa constructora se le presentan las siguientes alternativas donde
usted debe decidir cuál de estas utilizar, a sabiendas que el mejor pronóstico del próximo
año entrega 100 unidades:


                              Costos fijos        Costos variables
                      Empresa ($)                 ($)
                            1      500                     3
                            2      510                     3
                            3       10                    10
                            4      200                     5
                            5       10                    15

Solución:
a) Con el modelo de centro de gravedad:
                                     C X = 58,1458
                                          CY = 67, 6704
b) El centro más cercano corresponde al sitio de producción 3 (distancia en línea recta de
85). Por lo tanto, la ecuación queda, para la coordenada x:
                            366900 + 425 x               2056
                                              ³ 50 ® x £      » 228
                             6310 + 8 x + 5 x              9
En tanto, para la coordenada y:
                            427000 + 100 x               2230
                                              ³ 50 ® x £      » 203
                             6310 + 8 x + 5 x             11
Por lo que la producción mínima es 203 unidades.
c) Se descarta la alternativa de las empresas 2 y 5, ya que las superan las demás. Graficando
las alternativas restantes:




Se tiene que para 100 unidades conviene la empresa 4, con un costo de 700.
Usted está a cargo de un nuevo proyecto que necesita que sea completado en 24
semanas. En base a los tiempos normales de duración de cada actividad, indique qué
actividades hay que apurar, y cuál sería el costo adicional del proyecto. Haga el
grafo del proyecto también.

Actividad   Predecesor   Tiempo        Costo Total      Tiempo        Costo Total en tiempo
                         Normal        Normal           Mínimo        mínimo
   A            -             4             $4.000           3                 $4.500
   B            A             6             $9.000           6                 $9.000
   C            A             5             $1.500           3                 $2.000
   D           B,C            3             $6.000           2                 $9.000
   E            D             4             $8.000           2                $16.000
   F            E             6             $3.000           5                 $3.500
   G            E             8             $4.000           6                 $6.000
   H           F,G            3             $3.600           2                 $4.800



Problema 5 (Ayudantía 6 2016-1)

Una empresa necesita encontrar la localización adecuada para su nuevo centro de
distribución. Para ello se cuenta con las coordenadas de los puntos de ventas de la empresa
y el volumen de bienes a transportar hacia ellos.

    Lugar      Coordenadas        Volumen
      1          (325;75)          1500
      2         (400;150)           250
      3         (450;350)           450

a) Determinar la localización optima del centro de distribución. ¿Cuál es el mayor problema
de este método?
b) Si se abre otro punto de venta que requiere un volumen de 300 unidades ¿Cuáles deben
ser sus coordenadas para que el nuevo CD sea localizado en (380,150)?

Solución
a) Se utiliza el método de centro de gravedad. El principal problema es que considera las
distancias euclidianas entre los lugares y el centro de distribución, lo que no necesariamente
refleja las diferencias entre los costos de transporte a cada lugar. Tampoco considera otros
costos totales ni otros factores.

                          325 ∗ 1500 + 400 ∗ 250 + 450 ∗ 450
                     𝐶" =                                    = 359,09
                                  1500 + 250 + 450
                          75 ∗ 1500 + 150 ∗ 250 + 350 ∗ 450
                     𝐶. =                                   = 139,77
                                  1500 + 250 + 450
b)
                    325 ∗ 1500 + 400 ∗ 250 + 450 ∗ 450 + 𝑧 ∗ 300
                                                                 = 380
                              1500 + 250 + 450 + 300
                    75 ∗ 1500 + 150 ∗ 250 + 350 ∗ 450 + 𝑤 ∗ 300
                                                                 = 150
                              1500 + 250 + 450 + 300

El nuevo punto de venta debería estar en las coordenadas (533,33 ; 225).


Problema 6 (Guía I2 2016-1)

Se ha establecido que un proyecto tiene las siguientes actividades y tiempos estimados
con distribución beta para terminarlas.

                                         Tiempo           Tiempo más     Tiempo
            Actividad   Predecesor       Optimista (a)    Probable (m)   Pesimista (b)

               A            -                 1                 4               7
               B            A                 2                 6               7
               C           A,D                3                 4               6
               D            A                 6                12              14
               E            D                 3                 6              12
               F           B,C                6                 8              16
               G           E,F                1                 5               6

a) Calcule el tiempo esperado y la varianza para cada actividad.
b) Dibuje el diagrama de la ruta crítica.
c) Calcular ES, LS, EF, LF, las holguras de las actividades y el tiempo estimado de
duración del proyecto. ¿Cuál es la ruta crítica?
d) ¿Qué probabilidad existe de que el proyecto quede concluido en 34 semanas?



Solución:
a)
                                     𝑎 + 4𝑚 + 𝑏                𝑏−𝑎
                              𝜇=                ,         𝜎=
                                          6                     6

                                 Actividad         µ          𝜎;
                                     A               4        1
                                     B              5.5     0.694
                                     C             4.17      0.25
                                     D            11.33     1.778
                                     E              6.5      2.25
                                     F               9      2.778
                                     G              4.5     0.694
b)




c)
             Actividad      𝐸𝑆          EF          LS          LF           H
                 A           0            4           0           4          0
                 B           4           9.5         14         19.5        10
                 C         15.33        19.5       15.33        19.5         0
                 D           4         15.33          4        15.33         0
                 E         15.33       21.83         22         28.5       6.67
                 F          19.5        28.5        19.5        28.5         0
                 G          28.5         33         28.5         33          0

El proyecto dura 33 semanas, su ruta crítica es ADCFG.
d)
                                    34 − 33
              𝑃 𝑋 ≤ 34 = 𝑃 𝑧 ≤                  = 𝑃 𝑧 ≤ 0.3922 = 65.17%
                                    2.5495

Problema 7

La empresa Ford había decidido construir una fábrica de autos en México, ya que sus
analistas decían que, con las ventas esperadas, era el lugar con menores costos. Ellos habían
elegido la ciudad de San Luis de Potosí, pero el costo total era igual al de poner la planta en
Toluca.

Después de las amenazas de Donald Trump de agregar un impuesto a las importaciones de
un 40%, los gerentes decidieron estudiar nuevamente la mejor localización de la planta.

   Ciudad         Costo Fijo ($) Costo Variable ($)
   San Luís         25.000.000          5.000
    Toluca          20.000.000          6.000
   Detroit          20.000.000          6.600
   Iquique          50.000.000          2.500
Para este ejercicio suponga que el impuesto se cobra solo sobre el costo variable.

a) Determine el lugar que deberían elegir para la nueva planta. Cuantifique los efectos
económicos para Ford bajo el nuevo escenario.
b) Determine las condiciones necesarias para que Ford decida poner su fábrica en Iquique,
considerando el anuncio de subida de impuestos.
Solución:

Primero debemos conocer la cantidad que esperan vender. Del enunciado sabemos que en
el caso inicial el costo total de poner la planta en San Luis es igual al de Toluca:

                    25.000.000 + 5.000 ∗ 𝑥 = 20.000.000 + 6.000 ∗ 𝑥
                                      𝑥 = 5.000

Con este volumen de ventas el costo total es de $50.000.000.

El nuevo escenario considera que el costo variable de San Luís y Toluca sube:
                    𝐶𝑜𝑠𝑡𝑜 𝑣𝑎𝑟𝑖𝑎𝑏𝑙𝑒 𝑆𝑎𝑛 𝐿𝑢í𝑠 = 1,4 ∗ 5.000 = 7.000
                     𝐶𝑜𝑠𝑡𝑜 𝑣𝑎𝑟𝑖𝑎𝑏𝑙𝑒 𝑇𝑜𝑙𝑢𝑐𝑎 = 1,4 ∗ 6.000 = 8.400
Con los nuevos costos y el mismo volumen esperado tenemos:

 Ciudad      Costo Total
 Detroit     53.000.000
 Iquique     62.500.000
 San Luís    60.000.000
  Toluca     62.000.000

Bajo este nuevo escenario se debe elegir Detroit por tener el menor costo total. El costo
sube $3.000.000 para Ford.

b) Para esto se debe buscar un volumen que hace que el costo total de Iquique sea menor a
los otros. En este caso se compara con el costo total de Detroit.

                    50.000.000 + 2.500 ∗ 𝑥 < 20.000.000 + 6.600 ∗ 𝑥
                                 𝑥 > 7.317,07 ≈ 7.318

Para ese volumen se evalúa en otras ciudades para asegurar que es el mínimo costo total:

  Ciudad      Costo Fijo ($)

 Detroit      68.298.800
 Iquique      68.295.000
 San Luís     76.226.000
  Toluca      81.471.200

El volumen debe ser mayor o igual a 7.318 para que sea la mejor opción poner la planta en
Iquique.
