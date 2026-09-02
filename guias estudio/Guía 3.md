FACULTAD DE INGENIERÍA                                                                                  Curso:   Gestión de Operaciones
Departamento de Industrias                                                                            Semestre:   I 2018
PONTIFICIA UNIVERSIDAD CATÓLICA DE CHILE                                                             Ayudante:   Josefina Elsaca
                                                                                                                  Rene Acuña



                           Guı́a Planificación 2018
 Problema 1 : Guı́a 2016
La compañı́a en la que usted trabaja acaba de terminar la construcción de su nueva bodega de 2.100 m2, y
le han pedido a usted que plantee un modelo que optimice el uso de espacio dentro de la esta. La bodega
será dividida en dos ya que existe un contrato de arriendo con otra empresa por $15/m2 por un mı́nimo de
750 m2 , y además, se debe asignar espacio a los 25 diferentes productos propios de la propia compañı́a. Cada
producto genera un ingreso por ri y usa un espacio ei .
Finalmente le indican que debido a proyecciones de la demanda para los productos 3, 4, 5 y 6 debe considerar,
en conjunto, al menos 1000 unidades. El costo asociado al inventario en el espacio arrendado es ca (por m2 ),
y en el espacio usado por productos propios de la compañı́a cc (por m2 ). El costo total de mantención de
inventarios no puede superar los $3.000.

 Problema 1 .1.           Solución
Variables de decisión:

   ⇧     Xi = Cantidades de unidad de producto i (i = 1, 2, ...,25)

   ⇧     EA = Espacio asignado a arriendo en m2

Función Objetivo:

                                        25
                                        X                                   25
                                                                            X
                                  max         ri Xi + 15 ⇤ EA        cc ⇤         ei Xi    EA ⇤ c a
                                        i=1                                 i=1

Restricciones:
       Restricción de espacio:
                                                      25
                                                      X
                                                            ei Xi     EA  2100
                                                      i=1

       Restricción de demanda:
                                                   X3 + X4 + X5 + X6                1000


       Restricción de contrato:
                                                             EA >= 750


       Restricción de costos:
                                                            25
                                                            X
                                                     cc ⇤         e i Xi    EA ⇤ c a
                                                            i=1
     Naturaleza de las variables:
                                                Xi    0,   EA    0

Notar que para éste modelo no se incluyó como variable de decisión el espacioasignado al producto i, sino
que se considera la cantidad de unidades de ése producto. El espacio asignado se obtiene como Xi ei .

 Problema 2 : Guı́a 2016
Como gerente de operaciones de la planta de producción, se le ha encargado realizar la planificación de
producción para una nueva venta realizada por el área comercial. Los productos solicitados son F, y las
fechas de entrega acordadas con el cliente son:




Por otro lado usted dispone de la siguiente lista de materiales (BOM). Los números entre paréntesis indican
la cantidad del producto en el recuadro necesaria para producir una unidad del producto en el recuadro
superior.




Notar que los componentes necesarios para producir T1 y T2 se muestran sólo una vez en el diagrama. Usted
debe usarlos cada vez que requiera una unidad de T1 o de T2.
Los tiempos necesarios para la producción de cada producto o componente y los niveles iniciales de inventario
se muestran a continuación:
 Problema 2 .1.        Solución
Para obtener la planificación de producción asociado a esta venta se requiere realizar las tablas MRP. A
continuación se muestran las tablas MRP para la planificación, considerar que el primer cuadro muestra
el producto/componente, y los términos GR, OH y POR se refieren a la cantidad necesaria, el nivel de
inventario y cuando deben producir/comprar cada semana respectivamente.
 Problema 3 : I2 2016
Usted es el gerente de Operaciones de Papple, una empresa que produce productos tecnológicos. Actualmente
la empresa acaba de lanzar a la venta un nuevo producto, este necesita ciertas piezas para su producción. A
continuación, se detalla el BOM (el número indica las piezas necesarias) de este producto (P 1):




Además, el área de ventas ya tiene comprometido ventas para este producto. Estas ventas se detallan en la
siguiente tabla.

                                          Semana        10   11   12
                                        Demanda P1      15    0    7

Las disponibilidades de cada pieza, los tiempos de entrega y fabricación (semanas) y el tope de unidades por
pedido se detallan en la siguiente tabla.
  a)⇧ Desarrolle las tablas de MRP para cumplir con las ventas.

  b) Si su cliente desea adelantar los pedidos. Cuando es lo más temprano que le podrı́a cumplir.

Suponga ahora que existen costos de set-up/pedido para las piezas de $ Sk por cada set-up o pedido semanal
de pieza k. Además, los costos semanales de inventario son de $ Ik por cada unidad de pieza k mantenida
en inventario y el costo de producción es de $ Pk por cada unidad de pieza k producida. La demanda por
producto P1 es Dt . Finalmente, las piezas PO y PU comparten la máquina M1 y las piezas A y C comparten
la maquina M2, por lo que no pueden ser producidas en la misma semana.

  c) Con esta información plantee un problema de programación matemática que permita obtener el plan
     de producción de Papple. No considere la existencia de horas de sobretiempo para la producción de
     piezas.

 Problema 3 .1.        Solución
solución a)
solución b)


En base a las tablas de MRP desarrolladas se puede observar que lo más que se pueden adelantar los pedidos,
considerando también que también que no necesariamente deben ser la misma cantidad de pedidos, es: Esto

                                           Semana         7   8   9
                                         demanda P1      16   0   6

ocurre debido a que se necesitan 6 dı́as de adelanto, con tal de poder hacer los encargos y tener la pieza C
cuando es requerida.


solución c)
Parámetros:

   ⇧ Sk : Costo de pedido semanal por cada pieza k Ik : Costo de inventario semanal por cada unidad de
     pieza k

   ⇧ Pk : Costo de producción por cada unidad de pieza k producida

   ⇧ Dt : Demanda de la pieza P1 en el periodo (semana) t

   ⇧ Lk : Tiempo de entrega/fabricación de la pieza k

   ⇧ GRkt : Cantidad requerida de la pieza k en t

   ⇧ Rjk : Relación entre la pieza k y j. Cantidad de piezas k necesarias para producir una pieza j
   ⇧ T Pk : Tope de pedido de la pieza k

   ⇧ OHk : Inventario inicial de la pieza k

Variables de decisión:

   ⇧     P ORkt = Cantidades de piezas k pedidas en t

   ⇧     Ykt = Inventario de la pieza k al final del periodo t
               (
                 1 si se realiza un pedido de k en t
   ⇧     Bkt =
                 0 caso contrario

Función Objetivo:

                                  T X
                                  X   n               n
                                                      X            n
                                                                   X
                           min      (   P ORkt ⇤ Pk +   Ykt ⇤ Ik +   Bkt ⇤ Sk 15)
                                  t=1 k=1                  k=1                k=1

Restricciones:
       Restricción de demanda P1:

                                        YP 1,t+1 = YP 1,t + P ORP 1,t 1            Dt      8t


       Restricción de demanda general:

                                 Yk,t+1 = Yk,t + P ORP 1,t Lk         GRkt        8t, k,    k! = P 1


       Restricción de inventario inicial:
                                                         Yk0 = OHk


       Restricción de máquinas P0 y PU:

                                                   BP 0,t + BP U,t  1       8t


       Restricción de máquinas A y C:
                                                    BA,t + BC,t  1      8t


       Restricción capacidad de pedido:

                                                 P ORkt  T Pk ⇤ Bkt      8k, t


       Restricción insumos necesarios:

                                          GRkt     Rjk ⇤ P ORj,t      8j, k, t j! = k


       Naturaleza de las variables:
                                             Xkt    0,   Ykt     0,    Bkt 2 [0, 1]
 Problema 4 : Chase, Aquilano Jacobs (2009)
La siguiente tabla resume los costos de cuatro planes de producción agregada. Describa cada tipo de plan:




 Problema 4 .1.        Solución
   ⇧ Plan 1: Sigue la estrategia de ajuste. Busca igualar el nivel de producción con la demanda mediante
     el manejo de número de empleados. De esta forma no incurre en costos de inventarios ni faltantes.

   ⇧ Plan 2: Sigue la estrategia de nivel. Mantiene fuerza de trabajo estable y los ı́ndices de producción
     constantes. Absorbe los cambios en la demanda mediante fluctuación del nivel de inventario, los pedidos
     acumulados y las ventas perdidas.

   ⇧ Plan 3: Usa subcontratación. Produce a un nivel estable básico con fuerza de trabajo propia. Absorbe
     los cambios en la demanda mediante las decisiones en de subcontratación.

   ⇧ Plan 4: Mantiene fuerza de trabajo estable con horas de trabajo variables. Adecúa la producción con
     la demanda mediante horarios de trabajo flexibles y horas extras.

 Problema 5 : Guı́a 2 2014
Usted es el Gerente de Operaciones de una empresa que produce maquinarias para la agricultura. Actual-
mente la empresa vende dos tipos de máquinas M1 y M2, las cuales tienen ciertas piezas comunes entre sı́.
A continuación se detalla la BOM (El número indica las piezas necesarias) de las dos máquinas:
Por otro lado, ventas le indica que se han comprometido las siguientes ventas de cada modelo de máquina:

                                         Semana          8   9   10   11
                                       Máquina M1      10        7
                                       Máquina M2           4         8

Las disponibilidades de cada pieza y los tiempos de entrega o fabricación (semanas) se detallan a continuación:




Con esta información desarrolle las tablas de MRP para cumplir con las ventas.

 Problema 5 .1.          Solución
 Problema 6 : Guı́a 2016-1
Suponga que esta en cualquier caso de produccion, donde se manejan los pedidos y el inventario con el
modelo MRP y un BOM para los insumos. Se tienen 6 semanas de produccion, hay tiempos de produccion
y capacidades maximas de produccion.


Si existieran costos unitarios de fabricacion o setup de cj y costos de inventario hj , desarrolle un problema
de programacion matematica que permita determinar la cantidad optima y momento a producir o pedir.

 Problema 6 .1.         Solución
Para la modelación del problema se definen las siguientes variables:

   ⇧ xij producción del producto j en t

   ⇧ Iij cantidad de inventario de j al final del periodo t

   ⇧ ai tiempo requerido para producir el producto j

   ⇧ bij es el tiempo máximo de producción de j en el perı́odo t

   ⇧ dij demanda de j en el periodo t

Con las definición de las varaibles se tiene que el problema queda de la siguiente forma:
                                            6 X
                                            X   6          6
                                                           X
                                        min   (   cj xjt +   hj Ijt )
                                            t=1 j=1            j=1

Sujeto a:
                                              aj xij  bjt    8j, t
                                                  xjt     djt    8j, t
                                        Ijt = Ijt 1 + xjt            djt      8j, t
                                                  xjt , Ijt     08j, t

 Problema 7 : Guı́a 2017-1
A usted lo contratan para gestionar el inventario de una empresa fabricante de bebidas. Esta empresa fabrica
principalmente dos productos, la bebida normal y la light. Para ambas bebidas hay una lista de ingredientes
para obtener el producto final.


Los ingredientes, entregados en manera de diagrama se encuentran a continuacion:




Para las proximas semanas se tienen las siguientes ordenes de cada producto:

                            Semana      1     2    3      4      5       6       7    8    9
                            Normal                        10             12      12   15
                             Light                 15                    15                13

Ademas se tienen los siguientes niveles de inventario, los tiempos de produccion y el maximo pedido que se
puede hacer en una semana:

                 Ítem     Inventario       Tiempo de producción (Semanas)                Tope de Pedido
                Normal         23                         1
                 Light         20                         1
                 Agua          30                         1                                     20
               Aluminio        20                         3                                     10
                Azúcar        20                         4                                     16
               Sucralosa        5                         4                                      5

a) Con esta informacion desarrolle las tablas MRP para cumplir con las ventas. Justo en el momento de
entrega del informe con los planes de produccion se produce un problema con el productor de azucar, que
le dice que no podra cumplir con la produccion necesaria. Para arreglar este problema existen dos opciones,
estas se detallan a continuacion:
Opcion 1: Contratar otra empresa que tiene un tope de pedido de 8 y tiempo de produccion de 3 semanas.


Opcion 2: Comenzar a producir el azucar en la misma planta, lo que llevaria a tener un tope de pedi-
do/produccion de 11 y tiempo de produccion de 2 semanas.


b) Determine cual es la mejor opcion para la empresa. Fundamente su respuesta con calculos numericos.

 Problema 7 .1.         Solución
a) En este caso se deben completar las tablas MRP, considerando las restricciones de produccion y los tiempos
de entrega, las tablas completas estan a continuacion:

                           Normal      1           2            3        4           5      6             7         8        9
                            GR                                          10                  12           12        15
                            OH        23           23          23       13        13        1             0         0        0
                            POR                                                             11           15


                             Light     1           2            3       4        5         6         7        8          9
                              GR                               15                          15                           13
                              OH      20       20               5       5         5        0         0         0         0
                             POR                                                 10                           13


                             Agua     1        2               3        4         5         6        7          8        9
                              GR                                                 20        33        45        26
                              OH      30       30              38       58       58        45        20         0        0
                             POR                8              20       20       20        20        6


                           Aluminio        1           2            3        4         5         6        7          8       9
                             GR                                                       10        11        15        13
                             OH           20       20              20       20        16        15        10         0       0
                             POR                    6              10       10         3


                            Azúcar       1        2               3        4         5      6            7        8     9
                             GR                                                             22           30
                             OH        20          20           20       20          20     14            0        0     0
                             POR                   16           16


                             Sucralosa         1           2        3    4        5        6         7          8        9
                               GR                                                10                            13
                               OH              5           5        5    5        0        5         10         0        0
                               POR             5           5        5    3

b) En este caso se deben volver a calcular las tablas MRP del azucar, considerando el mismo inventario
inicial, pero con las nuevas restricciones.
                       Azúcar 1    -1   0    1    2      3    4      5     6      7   8   9
                         GR                                                 22    30
                         OH          -   -    20   22    28    34   40      24     0   0   0
                        POR          2   6     6    6    6      6

                           Azúcar 2     1     2    3     4     5      6     7    8    9
                             GR                                       22     30
                             OH          20   20   20     20   30     19     0    0    0
                            POR                    10     11   11


Se puede observar que en la opcion 1 no se alcanzan a completar las ordenes, ya que se necesita de una
semana 0 y una semana -1 que no se tiene. Debido a esto la opcion 2 es la unica posible, independiente de
cualquier factor que se pueda justificar.

 Problema 8 : Chase, Aquilano Jacobs (2009)
Desarrolle un plan de produccion y calcule el costo anual para una empresa cuyo pronostico de la demanda
es en otono, 10.000; en invierno, 8.000; en primavera, 7.000; en verano, 12.000. El inventario a principios de
otono es de 500 unidades. En este momento, principios de otono, tiene 30 trabajadores, pero planea contratar
trabajadores temporales a principios de verano y despedirlos al terminar esa estacion. Ademas, negocio con
el sindicato la opcion de utilizar la fuerza de trabajo regular en tiempo extra durante invierno o primavera,
en caso de que sea necesario para evitar que el inventario se agote al terminar cada uno de esos trimestres.
No hay tiempo extra durante el otono.


Los costos relevantes son: contratacion, 100 dolares por cada trabajador; despido, 200 dolares por cada
trabajador despedido; mantenimiento de inventario, 5 dolares por unidad-trimestre; pedidos demorados, 10
dolares por unidad; tiempo regular, 5 dolares por hora; tiempo extra, 8 dolares por hora. Suponga que la
productividad es de 0.5 unidades por hora de trabajador, con ocho horas al dia y 60 dias por temporada.

 Problema 8 .1.         Solución
Se desarrolla plan de produccion bajo las condiciones descritas en el enunciado. En otono se trabajan solo
las horas regulares:


                                Horas trabajadas = 30608 = 14,400 horas
                                                   u
                            P roducción = 0,5 ⇤       ⇤ 14,400 horas = 7200u
                                                 horas
                    Unidades demoradas = Demanda P roducción Inventario inicial
                            Unidades demoradas = 10000         7200        500 = 2300u
                                     Costos trabajo = 14400 ⇤ 5 = $72000
                                                             $10
                                   Costos demora = 2300u ⇤       = $23000
                                                              u
                                   Costos total = $23000 + $72000 = $95000
Para el invierno se propone no deber inventario. Se trabajan horas extras para terminar con inventario = 0.

                      Unidades a producir = Unidades atrasadas + Demanda = 11300
                                                          u
                           Producción regular = 0,5          ⇤ 14400horas = 7200u
                                                        horas
                                Producción extra = 11300u 7200u = 3100u
                                                    3100u
                                    Horas extra =         = 6200horas
                                                   0,5u/h
                              Costos trabajo = 14400 ⇤ 5 + 6200 ⇤ 8 = $121600
                                           Costo total = $121600
En la primavera no es necesario contratar horas extras. La produccion sobrante se deja para periodo siguiente:
                                                     u
                               Producción = 0,5         ⇤ 14400horas = 7200u
                                                   horas
                      Inventario periodo siguiente = P roducción     Demanda = 200u
                                  Costo mantenimiento = 5 ⇤ 200 = $1000
                                    Costos trabajo = 14400 ⇤ 5 = $72000
                                  Costo total = $1000 + $72000 = $73000
En el verano se busca satisfacer demanda total sin horas extra, solo contratando. Al finalizar temporada se
despiden contratados.

                 Unidades minimas a producir = Demanda          Inventario inicial = 11800u
                                                            u
                  Producción trabajadores actuales = 0,5 ⇤     ⇤ 14,400 horas = 7200u
                                                          horas
                    Producción minima nuevos trabajadores = 11800u 7200u = 4600u
                                                     4600u
                                                     0,5u/h
                    Trabajadores necesarios =             = 19,166 = 20trabajadores
                                              60 ⇤ 8horas
                                   N.Contrataciones = N.Despidos = 20
                                Costos CD = 20 ⇤ $100 + 20 ⇤ $200 = $6000
                        Producción trabajadores nuevos = 0,5 ⇤ 20 ⇤ 60 ⇤ 8 = 4800u
                                         Producción total = $12000
                              Costos trabajo = (14400 + 9600) ⇤ 5 = $120000
                      Intentario periodo siguiente = P roducción     Demanda = 200u
                                  Costo mantenimiento = 5 ⇤ 200 = $1000
                              Costo total = 120000 + 1000 + 8000 = $127000
                       Costo anual = 95000 + 121600 + 73000 + 127000 = $4136000
 Problema 9 : Guı́a 2017-1
En cierta empresa, usted es gerente de produccion. Usted quiere planificar la produccion de un conjunto N
(indexado por n) productos en un horizonte de tiempo dado por un conjunto T (indexado por t). Existe un
conjunto M (indexado por m) de materias primas. Cada producto requiere de algunas de estas.


La estructura de costos operacionales se detalla a continuacion. Los productos se pueden fabricar en un
conjunto de lineas de produccion, denotado por L (indexado por l). El costo de fabricar el producto n en
la linea l tiene un costo CPnl por unidad en cada etapa. Existen costos de inventario constantes a lo largo
del horizonte de planificacion para productos terminados, como para materias primas, denotados por CIn
,CHm por unidad en cada etapa. Tambien se considera un costo por faltante de cada producto, denotado
por CFn por unidad en cada etapa (no satisfaccion de la demanda de cada producto de la empresa).


Otros datos importantes son los siguientes. La capacidad de produccion de cada linea varia en cada periodo,
y viene dada por CAPlt . Se disponen inventarios iniciales de sn,0 para cada producto y de rn,0 para cada
materia prima. Por otro lado,existe un maximo de materia prima que puede ser comprada a proveedores en
cada periodo, denotado por maxmt . Considere que las materias primas compradas en un periodo t estan
disponibles a partir del mismo periodo. Finalmente, la demanda de cada producto esta dada por dnt , la que
puede ser satisfecha si hay suficiente inventario, o si no se incurre en un costo por faltante.


Por ultimo, considere un parametro unm que vale 1, si la materia prima m es usada para fabricar el producto
n , y 0 en otro caso. Su objetivo es minimizar los costos de fabricacion, inventario y faltante en todo el
horizonte de planificacion.


a) Plantee las variables del problema.


b) Escriba un modelo de programacion lineal que permita minimizar los costos de planificacion.


c) Suponga que si es que se hace un pedido (cualquiera sea la cantidad) de materia prima m en un periodo
t se incurre en un costo de set up de CSmt . Usted tambien desearia minimizar dichos costos ¿Como cambia
el modelo de la parte b)?


d) Suponga que se le exige que en la etapa final de planificacion el inventario debe ser, para cada producto,
una fraccion qn 2 [0, 1) de la demanda promedio del horizonte de planificacion. Agregue esta exigencia como
una restriccion a su modelo.

 Problema 9 .1.         Solución
a) Sea un periodo T = {1...T }, un conjunto de producto N , conjunto de materias primas M y una conjunto
de lı́neas L, planteamos las siguientes variables:

   ⇧ xnlt producción del producto n en la linea l en el periodo t

   ⇧ Ymt cantidad de materia prima m a comprar en el periodo t

   ⇧ zmt necesidad de materia prima m en el periodo t

   ⇧ Int balance de inventario del producto n en el periodo t 2 T [ {0}
      +
   ⇧ Int inventario fisico del producto n en elperiodo t
   ⇧ Int inventario faltante del producto n en elperiodo t

   ⇧ Mmt inventario final de materia prima m en el periodo t 2 T [ {0}

b) El modelamiento del problema se plantea de la siguiente forma:

                              X                       X                       X                    X
                                                                       +
              min CP lan =            CPnl ⇤ Xnlt +             CIn ⇤ Int +          CIf ⇤ Int +         CHm ⇤ Mmt
                              n,l,t                       n,l                  n,t                 m,t

Sujeto a las restricciones:                         X
                                         In,t 1 +           xnlt     dnt = Int       8n, t
                                                      l

                                         Hm,t 1 + Ymt              Zmt = Hmt         8m, t
                                                       +
                                                Int = Int           Int   8n, t
                                                    Hm,0 = rm,0           8m
                                                   In,0 = sn,0 8n
                                                   X
                                             zmt =      unm ⇤ xnlt 8m, t
                                                          n,l

                                               Ymt = maxmt 8m, t
                                               X
                                                 xnlt  CAPlt 8l, t
                                                n

c) Se define la siguiente variable:

   ⇧ wmt 1, si se pide al menos una unidad de la materia prima m en el periodo t; 0 en otro caso

A la funcion objetivo se le agregan los costos de set up de pedidos en el horizonte de planificacion, dados
por:                                          X
                                                  CSmt ⇤ wmt
                                                      m,t

Por otro lado se agrega la siguiente restricción:

                                             Ymt  maxmt ⇤ wmt                8m, t

d) Sea T la etapa final. Esto se puede representar como:
                                                       P
                                                         t dnt
                                          In,T = qn ⇤                           8n
                                                      card(T )
 Problema 10 : Guia 2014-1
A continuacion se detalla el BOM (Bill of materials) de un producto PF cuya elaboracion debe planificar.
Los nombres de las piezas se especifican con letras, y su cantidad con numeros:




Se indican tambien el inventario disponible de cada pieza e insumo (OH) y el tiempo requerido para su
produccion L (semanas):




Si la demanda es la siguiente (se indica en que semana se requiere el producto PF terminado):
a) Desarrolle las tablas MRP para cumplir con las ventas.


b) Si usted tiene una capacidad limitada de produccion semanal para cada pieza, dada por:




Indique lo mas temprano que podria terminar de producir el pedido establecido en a). Para ello usted debe
establecer las tablas MRP y determinar la fecha mas temprano que puede dar respuesta a los requerimientos
de su cliente.Nota: si requiere mas plazo de produccion, genere mas columnas en las tablas.

 Problema 10 .1.         Solucion
a) Las tablas MRP son las siguientes:
b) En este caso tenemos lo siguiente:
La fecha mas temprana es 12 semanas antes.
