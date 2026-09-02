                   Pontificia Universidad Católica de Chile
                   Escuela de Ingenierı́a
                   Departamento de Ingenierı́a Industrial y de Sistemas
                   Profesores: Alejandro Mac Cawley y Jorge Morales
                   Ayudantes: Alberto Busch (atbusch@uc.cl) y Francisco Lira (fvlira@uc.cl)



1     Procesos
Problema 1
La empresa de comida rápida Churrasco King permite que el empleado pueda escoger que añadirle al chur-
rasco. Para esto uno tiene que pedir la orden, se tiene que cortar y tostar el pan, luego añadir los condimentos
escogidos para finalmente envolver el churrasco y entregarlo. El gerente de la empresa quiere que los pedidos
sean entregados de la manera más rápida posible. Para esto está dispuesto a invertir y contratar nuevos
empleados si es necesario. El esquema de la producción se encuentra a continuación.




Los costos de los empleados varı́an según su posición. Un cajero tiene un sueldo de $300.000, los cocineros
encargados de las carnes y que también cortan y tuestan el pan son los con más experiencia, por lo que
tienen un sueldo de $500.000. Los cocineros aprendices son los que añaden los condimentos, estos tienen un
sueldo de $400.000 y finalmente para envasar y entregar se utiliza a un cajero que no atiende las ordenes.
a) ¿Cuál es la capacidad máxima de churrascos a servir de Churrasco King durante un dı́a? Considere que
el local está abierto 16 horas y que los tiempos son por churrasco. Considere que para un dı́a existen dos
turnos, por lo que se tienen 8 empleados al dı́a. La demanda es constante a lo largo del dı́a.
b) La gerencia de la empresa calcula que el local a estudiar tendrá una demanda de 480 churrascos al dı́a.
Con las capacidades actuales, ¿Se puede satisfacer la demanda? ¿Qué estación o estaciones son el cuello de
botella para esta demanda?
c) La empresa puede contratar más aprendices y cocineros con experiencia. Se pueden combinar trabajadores
en las diferentes estaciones y los rendimientos relevantes serian:
    • Destinar dos aprendices en cortar y tostar, lo que dejará un tiempo de 2 minutos el proceso.
    • Tener un aprendiz y un cocinero en los condimentos lo que dejará el tiempo de proceso en 2 minutos.
    • Tener dos aprendices en condimentos, con un tiempo de 2,5 minutos.
    • Tener dos cocineros en condimentos, con un tiempo de 1 minuto.
    • Tener dos cocineros en cortar y tostar, con un tiempo de 1,5 minutos.
Determine cual combinación permite cumplir con la demanda, además calcule los costos asociados a esta
medida.
d) Si un churrasco promedio cuesta $1.800 pero $1.500 sirven para cubrir costos de ingredientes y costos fijos
del local (sin considerar sueldos), ¿Es rentable expandir la capacidad?

Solución

a) Debido a que la estación de condimentos es la más lenta, esta es la que determina la capacidad del
local.


                                                       1
                                 1 orden    min      hora
                                 5 min ∗ 60 hora ∗ 16 dia = 192 churrascos

b) Debido a que la demanda es de 480 churrascos al dı́a, se puede calcular cada cuantos minutos se pide un
churrasco.

                                480 churrascos
                                       dia
                                                 1 dia
                                               ∗ 16        1 hora   1 churrasco
                                                    hora ∗ 60 min = 2    min

Lo que equivale a 2 minutos por churrasco. De este modo la estación de tostado y la de condimentos no
soportan la capacidad de demanda.

c) Debemos darnos cuenta de que la demanda es de un churrasco cada 2 minutos y lo más barato serı́a
contratar a un aprendiz. Luego, destinar dos aprendices a cortar y tostar y un aprendiz con un cocinero
en los condimentos dejando el resto igual. Notar que, si bien otras opciones son posibles para cubrir la
demanda, son más costosas.

d) Primero calculamos los sueldos con los nuevos empleados, se tiene:
   • 2 cajeros por turno, un total de 4 cajeros = 4 * $300.000
   • 3 aprendices por turno, un total de 6 aprendices= 6 * $450.000
   • 1 cocinero por turno, un total de 2 cocineros= 2 * $550.000
El total gastado en sueldos es de $5.000.000. Por otro lado los ingresos por churrasco son de $300, ya que
$1.500 pagan los ingredientes y costos fijos del local, por eso al mes se tiene de ingreso: 300*480*30 =
$4.320.000. Por lo que no se alcanza a cubrir los sueldos. La alternativa para cubrir la demanda no es
rentable para la empresa.

Problema 2
La siguiente figura muestra el esquema de una estación de lavado de automóviles. Esta consiste de dos
túneles de lavado paralelos con rodillos rotatorios y ventiladores para secar, y dos estaciones de limpieza
y secado final donde los automóviles son además aspirados. Por supuesto, los autos deben eventualmente
esperar por el servicio cuando llegan a la estación y eventualmente esperar frente al área de limpieza. Cada
túnel tarda 3 minutos en lavar un auto, pero caben simultáneamente dos autos en promedio en cada túnel
(van uno detrás del otro) y este tiempo es bastante exacto. Por otro lado, la limpieza y secado final de un
auto requiere de 4 minutos en promedio y se utilizan dos personas por vehı́culo.




a) Calcule la capacidad promedio de atención de los túneles de lavado de autos, de la estación de secado y
limpieza, y del sistema como un todo.
b) En el área de espera por limpieza y secado no caben más de 4 autos en espera. El tiempo de limpieza
es de 4 minutos promedio pero puede tener una varianza muy significativa según el nivel de pulcritud del


                                                       2
dueño y del tamaño del auto. Explique qué impacto puede tener esto en la hora punta del servicio, cuando
la demanda promedio de llegada de clientes es de 30 autos
                                                     hora .
c) Proponga un cambio estructural en el sistema que mejore el Performance. Explique en qué sentido habrá
mejoras. (Hint: Procesos y Layout)
d) Explique qué puede hacerse para mejorar el balance de la lı́nea y aumentar el throughput. Indique igual-
mente qué se puede hacer para disminuir la variabilidad del tiempo de limpieza de los vehı́culos.

Solución


a)

     • Capacidad de cada túnel de lavado: 0, 67 autos
                                                  min

     • Capacidad secado-limpieza:0, 5 autos
                                       min

     • Throughput Sistema: 0, 5 autos
                                 min (Igual al del cuello de botella).

b) En hora punta llegan 30 autos           autos
                                hora = 0,5 min por lo que el sistema está a capacidad, al haber variabilidad
el área de espera se va a llenar rápidamente y el sistema se bloqueará, se detendrá el lavado. Por lo tanto el
Throughput será menor al calculado en a).
c) Hay que separar secado de limpieza y ordenar la lı́nea con la limpieza primero, el lavado y finalmente el
secado. Se deberı́a ampliar el área de espera. Ası́ el cuello de botella controlará el flujo lo que evitará el
bloqueo de túneles. De esta manera se logra efectivamente el Throughput calculado en a).
d) Para esto hay que aumentar la tasa de producción del cuello de botella, es decir limpieza. Se puede incor-
porar más personal. Para disminuir la variabilidad: entrenamiento personal, mejorar coordinación, mejorar
tecnologı́a de limpieza.


Problema 3
Rockness Recycling reacondiciona a estudiantes de administración agotados. El proceso utiliza una banda
transportadora que lleva a cada estudiante por los cinco pasos del proceso en secuencia. Los cinco pasos son:


          Pasos               Descripción               Tiempo requerido por estudiante (min)
            1       Desempacar y poner en la cinta                        1,0
            2          Deshacer de malos hábitos                         1,5
            3            Tallar y limpiar mente                           0,8
            4        Introducir métodos modernos                         1,0
            5               Pulir y empacar                               1,2


Un miembro del cuerpo docente ha sido asignado a cada uno de estos pasos. Los docentes trabajan 40 horas
a la semana y rotan de puesto cada semana. El Sr. Rockness ha estado trabajando en un contrato con
General Electric que requiere la entrega de 2.000 estudiantes reacondicionados por semana.
a) ¿Cúal es el cuello de botella del sistema?
b) Un representante del departamento de recursos humanos acaba de llamar para quejarse de que la compañı́a
no ha estado recibiendo el número de estudiantes convenido. Cuando el Sr. Rockness revisa el inventario de
bienes terminados encuentra que no quedan existencias. ¿Qué está ocurriendo?
c) ¿Cuánto tendrá que ser el tiempo promedio por estudiante para poder cumplir con el contrato? ¿Es
lograble arreglando solo uno de los pasos del proceso?



                                                         3
Solución


a) Deshacer de malos hábitos es el cuello de botella, ya que tiene una capacidad de 1,5 minutos a diferencia
de todos los otros procesos que requieren de menos tiempo.
b)
                    salida = tiempo       horas      min    estudiante       estudiantes
                              ciclo = 40 semana ∗ 60 hora ∗ 1,5minutos = 1600 semana

El proceso más largo determina la salida del proceso completo, por lo que esta lı́nea no puede producir 2000
estudiantes por semana
c)
                         salida = 2000 estudiantes
                                         semana
                                                         horas
                                                   = 40 semana      min
                                                               ∗ 60 hora ∗ estudiantes
                                                                              xmin
                                                 x = 1, 2 min
Sı́, es posible arreglar el proceso solo modificando el paso 2 y que de esta manera tenga una mayor capacidad
de procesamiento de estudiantes.

Problema 4
El Festival Lollapalooza que será este fı́n de semana ha sido cancelado de forma inesperada tres dı́as antes
de su realización. Por ello, el SERNAC ha dispuesto de oficinas especiales para que quienes habı́an com-
prado sus entradas puedan resolver sus dudas. Cada una de estas sucursales cuenta con una sola autoridad
dispuesta a solucionar las consultas. Si quienes tenı́an entradas para este evento llegan a una tasa de 100
por hora y permanecen media hora en la sucursal. ¿Cuántas sillas deben haber en promedio para que todos
esperen sentados? Asuma que nadie se retira del sistema sin haber realizado su consulta.

Solución



                             L = λW = 100 asistentes
                                             hora    ∗ 5 horas = 50 asistentes

Por ende, se requiere contar con 50 asientos para que nadie espere de pie ser atendido.

Problema 5
Considere un sistema de producción de 4 etapas como el de la figura. Una unidad de D requiere una de C, y
cada unidad de C requiere una de A y una de B. Los tiempos de ciclo de las etapas B y C están entre 1 min  u
y 20 min
      u , es decir,1 ⩽ x ⩽ 20 y 1 ⩽ y ⩽ 20. Indique y justifique dónde está el cuello de botella del sistema
para todos los posibles valores de x e y. Además indique el respectivo throughput del sistema.




Solución




                                                       4
                X          Y             Cuello de botella      Troughput (unidades/hora)
              [1, 10[    [1, 10[                A                           6
              [1, 20]   ]10, 20]   y>x           C                        60/y
             ]10, 20]    [1, 20]   x>y           B                        60/x
                10         10                A, B y C                       6
                10       [1, 10[               AyB                          6
              [1, 10[      10                  AyC                          6
             ]10, 20]   ]10, 20]   x=y         ByC                     60/x o 60/y



En la tabla se muestra el comportamiento del cuello de botella y throughput para todos los intervalos posibles.

Tambı́en se puede ver en el gráfico que muestra donde ocurren los cuellos de botella.




Problema 6
Considere el caso de una panaderı́a (ver Figura) la cual opera 24 horas. Este proceso tiene una cierta veloci-
dad (throughput rate). ¿Cuál es el valor? ¿Por qué? Calcule el tiempo de proceso (throughput time) total
de un lote de 100 panes. Justifique muy bien cada paso de su respuesta.




                                                      5
Solución


Primero, el throughput rate o velocidad está limitado por el cuello de botella del proceso, que en este caso
es el empaquetado.
Por lo tanto:
                                                      1
                                  throughput rate = tciclo = 43 = 133, 333
Para un lote de 100 panes, primero hay que notar que independiente de que la tasa de producción de los 2
hornos pueda generar 200 panes/hr, esto no implica que 100 panes serán horneados en 30 minutos. Esto nos
entrega el primer término para el throughput time que esta compuesto por:
                     T hrought time = Thorno + W IP (tiempo inventario) + Tempaque
El tiempo en empaquetado es conocido y será 0,75 horas para 100 panes. Por lo tanto, se debe determinar
el WIP: *Si se asume que desde T=0 hrs. la fábrica tiene inventario acumulado ya antes del empaquetado,
podemos decir que en 24 hrs. la producción total de la panaderı́a estará dada por: (depende de la tasa del
cuello de botella)
                                 P roduccion T otal = 133, 333 ∗ 24 = 3200
Luego, una producción de 3200 panes es producida por los hornos en un tiempo de:
                                              T = 3200
                                                   200 = 16 h

Si gráficamos el inventario WIP, notemos que la tasa de acumulación durante las primeras 16 hrs. es la
diferencia entre la tasa de entrada y la tasa de salida (200 - 133,33333 = 66,66666 panes/h). Posteriormente,
la tasa corresponde a la de empaquetamiento:




Tenemos que el inventario promedio es de 533,333 panes. Luego, podemos usar Little para determinar el
tiempo promedio de espera, considerando la tasa del sistema:


                                                     6
                                              W = 533,333
                                                  133,333 = 4 h

Finalmente:

                                T hroughput time = 1h + 4h + 0, 75h = 5, 75h

Problema 7
La empresa Jot Wilz fabrica autos de juguete de distintos tamaños y colores. Para ello utiliza dos insumos:
aluminio (para la carrocerı́a) y ruedas. Actualmente trabajan 8 horas al dı́a, 5 dı́as a la semana y cada parte
del proceso lo realiza una maquina diferente:




En primer lugar se vierte una unidad de aluminio en el molde de plantilla creado por los diseñadores, para
darle forma a los autos y luego se llevan a una cámara de enfriado. A continuación se ensamblan las 4 ruedas
en los ejes y se pinta el auto. Finalmente se empacan en cajas para ser distribuidos. Un 10 porciento de
los autos son testeados antes de ser empaquetados. Todo el proceso funciona como una lı́nea de producción
continua, donde cada una de las máquinas tiene una capacidad promedio de trabajo, indicado en la siguiente
tabla:

                      Proceso       Capacidad Máquina (autos/hora)            Máquinas
                       Molde                      55                               6
                      Enfriado                    79                               5
                     Ensamblaje                   65                               4
                       Pintura                    100                              2
                       Testeo                     48                               1
                      Empaque                     110                              4


El precio de una unidad de aluminio es de CLP 500 y cada rueda tiene un precio de CLP 100. La empresa
tiene un mismo proveedor para ambos insumos, que demora 2 dı́as hábiles en entregar los pedidos requeridos.
Cada orden tiene un costo de CLP 50.000 y el costo de mantener inventario a la semana es un 10 porciento
del precio de cada insumo. Cada auto de juguete vendido genera una utilidad de CLP 350. Responda las
siguientes preguntas:
a) Determine la capacidad máxima que la fábrica puede procesar al dı́a. ¿Cuál es el cuello de botella? ¿Cuál
es la utilidad semanal de la empresa?
b) Los gerentes han decidido realizar una mejora en la cadena de producción y le han pedido ayuda para
determinar qué procesos deberı́an aumentar su capacidad y en cuánto (cantidad de máquinas extra) para
poder satisfacer una demanda diaria de 2.400 autos. ¿Cuánto estarı́an dispuestos a pagar los gerentes por
este cambio en el sistema?

Solución


a) Tenemos:
El cuello de botella es Pintura, porque solo puede producir 200 autos por hora.


                                                       7
   Proceso       Capacidad Máquina (autos/hora)            Máquinas      Capacidad total (autos/hora)
    Molde                      55                               6                      330
   Enfriado                    79                               5                      395
  Ensamblaje                   65                               4                      260
    Pintura                    100                              2                      200
    Testeo                     48                               1                 =48*1/0,1=480
   Empaque                     110                              4                      440



                     Capacidad maxima diaria = Capcuello botella = 200 ∗ 8 = 1600 autos
                                                                                   dia
                             U tilidad Semanal = 1600 ∗ 350 ∗ 5 = 2.800.000

Para suplir una demanda de 2400 autos/dı́a se necesita que la tasa de producción durante las 8 horas sea de
300 autos/hora. Actualmente es de 200 autos/hora, ya que la Pintura es el cuello de botella. Luego, si se
agrega 1 máquina de pintura, la capacidad de esa tarea sube a 300 autos/hora, pero el nuevo cuello de botella
es Ensamblaje, con 260 autos/hora. Por lo tanto, se debe también agregar 1 máquina de Ensamblaje para
que su capacidad sea 325 autos/hora, y ası́, el cuello de botella sea Pintura con 300 autos/hora cumpliendo
con la demanda diaria. Estarı́amos dispuestos a pagar a lo más los nuevos ingresos:
                             N uevos Ingresos = (2400 − 1600) ∗ 350 = 280.000

Problema 8
La producción de cobre consta de varios procesos desde que se extrae el mineral desde la mina hasta poder
producir lingotes de cobre. En primer lugar, el mineral se debe llevar a un proceso de molienda con el fin
de reducir su tamaño. Luego, este mineral se lleva a la concentradora donde se obtiene concentrado de
cobre. Posteriormente, se lleva a fundición que consta en procesar el concentrado para obtener cobre blı́ster.
Especı́camente, el concentrado es llevado a hornos de fundición, donde se puede obtener escoria o cobre
blı́ster. La escoria se lleva a un horno de limpieza de escoria, el cual también entrega cobre blı́ster, y luego
éste se lleva a un proceso de moldeado que finalmente entrega los lingotes. Suponga que en una mina se
tienen 2 molinos para procesar el mineral y 2 hornos de fundición. Además, considere los siguientes datos:

                          Capacidad de procesamiento molino            2800 ton/h
                             Capacidad de procesamiento
                                                                       5000 ton/h
                                     concentradora
                             Porcentaje de mineral que se
                                                                           3%
                              transforma en concentrado
                                  Capacidad de hornos             90 tonconcentrado /h
                              Porcentaje de concentrado
                                                                          30%
                                transformado en blı́ster
                              Porcentaje de concentrado
                                                                          70%
                                transformado en escoria
                           Capacidad horno de limpieza de
                                                                       100 ton/h
                                        escorias
                          Porcentaje de escorias transformado
                                                                           8%
                                    en cobre blı́ster
                             Capacidad área de moldeado              1400 ton/dia


Considere que el mineral puede ser tratado en cualquiera de los 2 molinos, que el concentrado de mineral
puede entrar en cualquiera de los 2 hornos de fundición, que toda escoria debe pasar por el horno de limpieza


                                                       8
de escorias y que la escoria restante se desecha.
a) Dibuje el diagrama de tratamiento de mineral.
b) Determine el cuello de botella.
c) ¿Cuál es la máxima cantidad de mineral que se puede extraer al dı́a (24 hrs)?

Solución


a) Tenemos:




b) Para determinar los cuellos de botella se debe calcular la capacidad para cada una de las etapas del
procesos. Llamaremos ”ton” a toneladas de mineral totales, es decir, el equivalente que se puede procesar
de las toneladas de material inicial:
                                   Capacidad M olinos = 2800 ∗ 2 = 5600 ton
                                                                         h
                                    Capacidad Concentradora = 5000 tonh
                                                         90
                                   Capacidad Hornos = 0,03  ∗ 2 = 6000 ton
                                                                        h

Para el horno de limpieza de escorias, notar que para llevar a unidades de toneladas iniciales equivalentes,
el 70 porciento que ya venı́a desde el concentrado es el que pasa por esta máquina:
                                                               100
                         Capacidad Horno Limpieza Escoria = 0,03∗0,7 = 4761, 6 ton
                                                                                h
                                                        1400/24
                          Capacidad M oldeado = 0,03∗0,3+0,08∗0,7∗0,03 = 5461, 92 ton
                                                                                   h

Por lo tanto, el cuello de botella es el Horno de limpieza de escorias.
c) Tenemos:

                             T oneladas M aximas = 4761, 9 ∗ 24 = 114285, 6 tons

Problema 9
El Gerente General del Aeropuerto Internacional Antonio Carlos Jobim de Rı́o de Janeiro, le solicita ayuda
para evaluar sus procesos. Esto, con el fin de poder satisfacer la alta demanda que existirá en Junio y Julio
de este año por la Copa Mundial de Fútbol. Joao Goulart, le explica cuál es el procedimiento al que se
expone un pasajero desde que llega al aeropuerto hasta que se sube al avión: ”Una vez que llega un pasajero
al aeropuerto debe realizar el check-in con una de las tres azafatas que están en el mostrador (cada una
se demora tres minutos en atender a un pasajero). Ahı́ los pasajeros entregan sus maletas y reciben su
boarding pass (pase que será solicitado por otras azafatas en la última etapa). Luego debe pasar por policı́a
internacional, que tiene dos procesos consecutivos. Primero, el chequeo del pasaporte que es llevado a cabo
por uno de los tres policı́as de investigaciones que registran el egreso del paı́s y analizan si está todo en orden
para poder salir, todo esto en cuatro minutos. Después revisan las maletas de mano a través de una máquina
de rayos-x, mientras los pasajeros pasan por debajo del detector de metales, existen cuatro máquinas que
trabajan en paralelo demorándose en promedio tres minutos por pasajero. Por último, una de dos azafatas lo
estará esperando para atenderlo y darle la bienvenida en la puerta de su avión, demorándose solo un minuto
en revisar e ingresar su boarding pass al sistema.” También le dice que para efectos de su estudio asuma que
cada servidor atiende a un solo pasajero y que no hay tiempo de traslado entre un proceso y otro. Además,


                                                         9
se han despreciados procesos intermedios como comprar en el DutyFree.

a) Dibuje el diagrama de flujo, indique claramente cuánto es el tiempo de atención por proceso
b) ¿Cuál es el actual cuello de botella?
c) ¿Cuántos pasajeros son atenidos, actualmente, por hora?
d) El Gerente General, comprendió lo crı́tico de esta situación por lo que desea adquirir una nueva tecnologı́a
que disminuye a la mitad el tiempo de Chequeo de Maletas de Mano y Detector de Metales. ¿Usted re-
comendarı́a que adopte esta nueva tecnologı́a?
e) Otra medida que está evaluando es la contratación de más personal, ¿en qué estación usted le recomendarı́a
agregar un servidor y cuál serı́a su bene
    cio?
f) ¿Cuál será el cuello de botella, una vez que el Gerente General tome en consideración todas sus observa-
ciones? ¿Cuántos pasajeros serán atendidos por hora?

Solución


a) Tenemos:

                                    Tiempo de
                                                       Cantidad de         Tiempo de
                      Proceso        atención
                                                        servidores       Atención (min)
                                  (min/servidor)
                          1              3                    3                  1,0
                          2              4                    3                  1,3
                          3              3                    4                  0,8
                          4              1                    2                  0,5




b) El cuello de botella se ubica en el segundo proceso (chequeo de pasaporte), ya es el proceso que demora
más tiempo en desocupar un servidor con 1,333 minutos.
c) Los pasajeros atendidos son 45, ya que el proceso se encuentra sujeto al cuello de botella que atiende a
1,333 pasajeros por minuto, es decir, en 60 minutos atenderá a 60/1,333 = 45 pasajeros.


                                                       1
                                 P asajeros al Dia = 1,333 ∗ 60 = 45 pasajeros
                                                                       hora

d) La adaptación de esta nueva tecnologı́a disminuirá el tiempo de atención de 0,8 minutos a 0,4 minutos
en la tercera etapa (chequeo de maletas de mano y detector de metales) convirtiéndose en la etapa más
veloz. Sin embargo, no afecta a la cantidad de pasajeros atendidos ya que no estamos mejorando el cuello de
botella. Solo va a producir que se haga cola en la última etapa. No recomendarı́a realizar dicha inversión.
e) Agregar 1 servidor en la etapa que es cuello de botella, es decir, la etapa 2 correspondiente al chequeo del
pasaporte. Con ello disminuirá su tiempo de atención a 1 minuto en desocupar un servidor. Por lo tanto,
ahora se atenderán 60 pasajeros/hora, aumentando en 15 pasajeros la capacidad del sistema.
f) El nuevo cuello de botella serán las dos primeras etapas atendiendo a 60 pasajeros por hora, como
calculamos en el punto anterior. Seguimos sin pensar en invertir en la nueva tecnologı́a ya que sigue sin
afectar la capacidad del sistema.



                                                       10
Problema 10
Reflejos S.A. es una empresa dedicada a la fabricación de espejos de alta calidad. El proceso de producción,
mostrado en la figura, por lo general tiene una altı́sima eficiencia. Sin embargo, debido al descuido de los
dueños de la empresa, ninguna de las etapas que componen este proceso está a plena capacidad, como se
describirá a continuación. La primera etapa del proceso consiste en el lavado y pulido de las láminas de vidrio
mediante una pulidora industrial, la cual es capaz de pulir las láminas a una tasa de 400 m2 /h. Un 50% del
vidrio es correctamente pulido, mientras que el porcentaje restante, llamado vidrio sucio, es destinado a una
pulidora de potencia aumentada. Esta última trabaja con una capacidad de 150 m2 /h y deja pulido un 95%
del vidrio sucio. El 5% restante se destina a otros usos. Luego, el vidrio pulido se dirige a 2 plateadoras,
que depositan sobre las láminas una fina pelı́cula de plata, la cual cumple la función refractaria (es decir, de
espejo). Cada plateadora tiene una capacidad de 150 m2/h, y procesa correctamente un 80% del material,
dejándolo como pre-espejo.
Finalmente, el pre-espejo se hornea y limpia para quedar como espejo listo. Éste se empaqueta en el mismo
lugar del horneado y la limpieza. El horneado, limpieza y empaquetado tiene una capacidad de 8400 m2/dı́a,
y transforma todo el pre-espejo que le llega a espejo (asuma un dı́a de 24 horas de trabajo).




A partir de esta información:
a) Determine el cuello de botella. ¿Cuál es la máxima cantidad de láminas de vidrio en m2/h que es posible
procesar en la pulidora? ¿Cuál es la producción en m2/dı́a de espejos?
b) Suponga que en el mercado se cotiza a $1000 el m2 de espejo. ¿Cuál serı́a el ingreso diario de la empresa?
c) A Reflejos S.A. le llegaron más recursos, y está pensando en mejorar sus procesos. Es por esto que
decidieron aumentar la capacidad del cuello de botella encontrado en a). Este aumento de capacidad debe
ser de tal manera que ningún otro punto del proceso se convierta en un nuevo cuello de botella.¿Cuál serı́a
la nueva capacidad del cuello de botella, en m2/h de láminas de vidrio?
d) Suponiendo que aumentar la capacidad del cuello de botella tiene un costo diario, ¿cuánto serı́a el máximo
que los gerentes de Reflejos S.A. estarı́an dispuestos a pagar? Suponga que el precio del espejo se mantiene
a $1000 el m2
Solución


a) Primero se calculan las capacidades equivalentes. En este caso, se toma como referencia las láminas de
vidrio. De esta forma:
                                                                 2
                                              P ulidora = 400 mh
                                                                          m2
                               P ulidora P otencia Aumentada = 150
                                                                 0,5 = 300 h
                                                                            2
                                                      150∗2
                                    P lateadoras = 0,5+0,5∗0,95 = 307, 7 mh
                                                      8400/24                     2
                              Horno, Limp, Emp = 0,8∗(0,5+0,5∗0,95) = 448, 7 mh



                                                       11
Por lo tanto, el cuello de botella es la Pulidora de Potencia Aumentada.
Pueden ingresar a lo más 300 m2/h de láminas de vidrio al sistema (a la pulidora, a causa del cuello de
botella). A las plateadoras llega 0,5*300 + 0,5*0,95*300 = 292,5 m2/h de vidrio pulido. El primer término
corresponde a lo que llega a las plateadoras directo de la pulidora, el segundo corresponde a lo que viene
desde la pulidora de potencia aumentada. Al proceso final llega un 80% de lo anterior, o sea, 292,5*0,8 =
234 m2/h.
En un dı́a, se obtienen 234*24 = 5616 m2 de espejo.
b)Tenemos:
                                                                            $
                              Ingresos Diarios = 1.000 ∗ 5.616 = 5.616.000 dia

c) Para que ningún nuevo punto se convierta en cuello de botella, la capacidad del actual cuello de botella
debe alcanzar a la capacidad de la etapa de proceso más cercana. Es decir, debemos aumentar la capacidad
de la Pulidora de Potencia Aumentada a 307,7 m2/h.
d) Se pagarı́a la diferencia entre los ingresos diarios en cada situación. Ya calculamos para la situación sin
aumentar el cuello de botella.
Si se repite el cálculo para la nueva situación hipotética tendrı́amos:
0,5*307,7 + 0,5*0,95*307,7 = 300 m2/h de vidrio pulido. Al final llega un 80% de lo anterior, o sea, 240
m2/h.
En un dı́a se tiene 240*24= 5.760 m2 de espejo, es decir, una ganancia diaria de $5.760.000.
Finalmente:
                                                                                 $
                       Delta Ingresos Diarios = 5.760.000 − 5.616.000 = 144.000 dia




                                                      12
2    Pronósticos
Problema 1
Suponga que es contratado en una heladerı́a para realizar un pronóstico de la demanda que habrá durante
el año. La demanda mensual de la heladerı́a durante el 2018 se muestra a continuación:

                                          Mes               Demanda
                                          Enero             500
                                          Febrero           450
                                          Marzo             400
                                          Abril             200
                                          Mayo              150
                                          Junio             100
                                          Julio             50
                                          Agosto            50
                                          Septiembre        100
                                          Octubre           100
                                          Noviembre         200
                                          Diciembre         400


a) Haga un pronóstico mensual usando los métodos de: valor anterior, media anual, media móvil de 3 meses,
media móvil de 3 meses ponderada (wt−3 = 0.2, wt−2 ,= 0.3, wt−1 = 0.5), suavizamiento exponencial con α
= 0.3 y pronóstico de Enero igual a la media anual.
b) ¿Cuál resulta mejor estimador según el criterio de MAD?
c)¿En base a la estructura de la demanda de la heladerı́a, qué tipo de demanda tiene? ¿Qué método se le
ocurre utilizar para un mejor pronóstico?

Solución

a)
Recordemos que las fórmulas para calcular los distintos pronósticos son:

Valor anterior: utilizar la demanda del perı́odo anterior.
Media anual: sacar el promedio de las demandas desde enero diciembre.
Media móvil de tres meses: sacar el promedio de los últimos tres perı́odos.
Media móvil de 3 meses ponderada: promedio ponderado de los últimos tres meses, en que el más
reciente es el que más cuenta.
Suavizamiento exponencial: la fórmula es Ft = Ft−1 + α(At−1 − Ft−1 ) ,
donde Ft es el pronóstico calculado, Ft−1 es el pronóstico del perı́odo anterior, At−1 es la demanda del
perı́odo anterior y α es el coficiente de suavización, que va entre 0 y 1.

A continuación se muestra la tabla con los pronósticos calculados con cada método, mediante sus fórmulas
respectivas.




                                                       13
        Mes       Demanda       Media Anual     Valor anterior     3 Meses    Ponderada     Exp
        Enero       500         225                                                         225
       Febrero      450         225             500                                         308
       Marzo        400         225             450                                         350
        Abril       200         225             400                450        435           365
        Mayo        150         225             200                350        310           316
        Junio       100         225             150                250        215           266
        Julio       50          225             100                150        135           216
       Agosto       50          225             50                 100        85            166
     Septiembre     100         225             50                 66.67      60            131
      Octubre       100         225             100                66.67      75            122
     Noviembre      200         225             100                83.33      90            115
     Diciembre      400         225             200                133.33     150           141



b) Para calcular el MAD, debemos calcular la sumatoria de los errores absolutos (pronóstico - demanda)
para cada perı́odo:

                                Error absoluto
                                Media     Valor
                      Mes                              3 Meses   Ponderada     Exp
                                Anual Anterior
                  Enero         275                                            275
                  Febrero       225     50                                     143
                  Marzo         175     50                                     50
                  Abril         25      200            250       235           165
                  Mayo          75      50             200       160           166
                  Junio         125     50             150       115           166
                  Julio         175     50             100       85            166
                  Agosto        175     0              50        35            116
                  Septiembre    125     50             33        40            31
                  Octubre       125     0              33        25            22
                  Noviembre     25      100            117       110           85
                  Diciembre     175     200            267       250           259




                                                  14
                               Σ Error absoluto
                               Media     Valor
                    Mes                                 3 Meses    Ponderada   Exp
                               Anual Anterior
                 Enero         275                                             275
                 Febrero       500     50                                      418
                 Marzo         675     100                                     467
                 Abril         700     300              250        235         632
                 Mayo          775     350              450        395         798
                 Junio         900     400              600        510         964
                 Julio         1075    450              700        595         1130
                 Agosto        1250    450              750        630         1246
                 Septiembre    1375    500              785        670         1278
                 Octubre       1500    500              817        695         1300
                 Noviembre     1525    600              933        805         1384
                 Diciembre     1700    800              1200       1055        1644


Finalmente dividimos la sumatoria final por la cantidad de datos pronosticados en cada perı́odo.


                               Media        Valor
                                                        3 Meses    Ponderada   Exp
                               Anual      Anterior
                Diciembre      142        73            133        117         137


Por lo tanto, la mejor predicción es la del valor directamente anterior.




                                                   15
Problema 2
La demanda semanal de Fajitas a la que se enfrenta un vendedor de la entrada de nuestro campus se muestra
a continuación:

                             Semana      1       2        3       4       5       6         7
                             Número
                                         450     480      440     520     600     550       500
                              Fajitas


Hacer pronósticos de la semana 5 en adelante utilizando:

a) Media móvil de 4 semanas
b) Suavizamiento exponencial con α = 0,1 con inicialización con el promedio simple de las 4 semanas
c) Suavizamiento exponencial con α = 0,8 con inicialización con el promedio simple de las 4 semanas
d) Calcule el MAD y TS.
e) ¿Qué modelo prefiere? ¿Por qué?

Solución

a, b, c) Se usan las fórmulas del ejercicio anterior, obteniendo:


                    Semana               1       2        3       4       5           6           7
                    Número
                                         450     480      440     520     600         550         500
                    Fajitas
                    MM
                                             -       -        -       -   472,5       510         527,5
                    4 semanas
                    Suav. Exp. 0,1           -       -        -       -   472,5       485,25      491,725
                    Suav. Exp. 0,8           -       -        -       -   472,5       574,5       554,9


   d) El MAD se calcula de la misma manera en que se hizo en el ejercicio anterior (promedio de los errores
absuloutos entre los pronósticos y la demanda real).
La Señal de Rastreo (conocida también como Tracking Signal o TS) es una medida de desempeño que permite
medir la desviación del pronóstico respecto a variaciones en la demanda. Análogamente se puede interpretar
como el número de MAD (Desviación Media Absoluta o Mean Absolute Deviation) que el pronóstico está
sobre o bajo la demanda real. La fórmula para calcular el TS corresponde a:

                                                          Σ(At − Ft )
                                        Tracking signal = 1
                                                          n Σ |At − Ft |

Los resultados usando estas fórmulas son:

                               MM 4 semanas              Suav. Exp. 0,1           Suav. Exp. 0,8
                     MAD       65                        66,84                    68,97
                     TS        2,15                      3




                                                           16
   e) Es preferible la Media Móvil pues tiene menor MAD.


Problema 3
En una central de llamado se ha registrado el número de llamadas diarias en los últimos 8 dı́as:

                         Dı́a          1     2       3        4     5       6      7       8
                         Llamadas      92    127     103      165   132     111    174     97

a) Prepare un pronóstico de media móvil de 3 dı́as e indique el error en cada dı́a.
b) Prepare un pronóstico de media móvil ponderada de 3 dı́as con w1 = 0,5 w2 , = 0,3 y w3 = 0,2 , donde
w1 representa el perı́odo más reciente.
c) ¿Cuál de los dos métodos es mejor?
d) ¿Qué supuestos hay detrás de cada modelo?


Solución

   a)
Las medias móviles desde el dı́a 4 (antes no se pueden sacar) utlizando la fórmula usada anteriormente es:

                               Dı́a      4           5         6           7       8
                               Error     107,33      131,66    133,33      136     139

   Los errores es la diferencia entre la demanda real que hubo un perı́odo y el pronósticos para ese:

                                 Dı́a       4         5         6         7       8
                                 Error      -57,67    -0,33     22,33     -38     42

    b)
Un pronóstico con media móvil ponderado se calcula ponderando los dı́as anteriores diferente. En este caso
el pronóstico del dı́a 4 se calcula como
F4 = 0, 2 ∗ 92 + 0, 3 ∗ 127 + 0, 5 ∗ 103 = 108, y ası́ sucesivamente. Queda de la siguiente manera.

                             Dı́a            4       5         6          7        8
                             Pronóstico     108     138,8     136,1      128,1    146,7

   c)

Utilizando las fórmulas anteriores se pueden calcular ambos.
MAD Media Móvil = 32,067, MAD Media Móvil Ponderada = 36,9.
Por lo tanto es mejor la Media Móvil Ponderada.

   d)

Media Móvil: El valor futuro se puede pronosticar según lo ocurrido en los “k” últimos perı́odos mediante
un promedio.
Media Móvil Ponderada: El valor futuro se puede pronosticar según lo ocurrido en los “k” últimos
perı́odos mediante un promedio ponderado en el cual se asigna más importancia a lo que ocurrió en los
perı́odos más recientes.


                                                        17
Problema 4
Una compañı́a ha usado tres diferentes métodos para pronosticar sus ventas en los últimos 5 meses. Utilice
MAD y TS (Señal de rastreo) para evaluar el desempeño de los tres métodos.
¿Cuál método de pronóstico es más preciso? ¿Qué información entrega MAD? ¿Qué información entrega
TS?

                       Perı́odo      Actual    Método A      Método B        Método C
                       1             10        10             9                8
                       2             8         11             10               11
                       3             12        12             8                10
                       4             11        13             12               11
                       5             12        14             11               12

Solución


                                                          MAD      TS
                                            Método A     1,4      5
                                            Método B     1,8      5
                                            Método C     1,4      5

Se ecoge el método A o C, pues tienen menor MAD.
MAD indica cuánto es el error de mi pronóstico en términos de módulo, cuánto me alejo en promedio del
valor real en valor absoluto, “por arriba o por abajo”.
TS indica el sesgo de mi pronóstico, si es positivo tengo un sesgo a la alza, es decir en general mi pronóstico
sobreestima el valor que predice, si es negativo ocurre lo contrario.

Problema 5
La empresa XYZ sufrió una inundación y perdió parte de sus datos de pronósticos. Hay que reconstruir los
datos existentes utilizando suavizamiento exponencial y :
M ADt = α ∗ |At ∗ Ft | + (1 − α)∗ M ADt−1 (Use esta fórmula recursiva para calcular el MAD puesto que
hay muchos periodos anteriores que no se incluyen en la tabla). Calcule el valor de los parámetros a, b, c,
d, e, f.

                                              Ft
                          Perı́odo    At                 et = At - Ft   M ADt      T St
                                              α = 0, 3
                          0                                             10
                          1           120     100        20             f          1,5
                          2           140     106        34             19,3       e
                          3           160     a          b              c          d

Solución

Los valores son:

   • a = 116,2
   • b = 43
   • c = 26,65



                                                         18
   • d = 3,65
   • e = 2,77
   • f = 13

Problema 6
Asuma un valor inicial de pronóstico Ft = 100 unidades, una tendencia de 10 unidades, α = 0, 2 y δ = 0,
3. Si la demanda resultó ser de 115 unidades, en vez de las 100 proyectadas, calcule el pronóstico para el
próximo periodo.

Solución

   Al sumar el pronóstico inicial y la tendencia, tenemos:


                                   F ITt−1 = Ft−1 + Tt−1 = 100 + 10 = 110

   El valor actual o real de la demanda (At−1 ) es de 115. De este modo,


                                     Ft−1 = F ITt−1 + α(At−1 + F ITt−1 )

                                       Ft = 100 + 0.2(115 - 110) = 111

                                         Tt = Tt−1 + δ (Ft − F ITt−1 )

                                       Tt = 10 + 0.3 (111 - 110) = 10.3

                                    F ITt = Ft + Tt = 111 + 10.3 = 121.3

Por lo tanto, el pronóstico para el próximo periodo serı́a de 121.3 unidades.

Problema 7
Restorán Don Fabricio quiere estimar la demanda del plato Congrio Frito a lo pobre para el lunes de la
siguiente semana.
La demanda durante la semana anterior es la siguiente:

              Dı́a         Lunes    Martes    Miércoles   Jueves   Viernes       Sábado   Domingo
              Demanda      25       26        19           40       50            52        30

    Mediante suavizamiento exponencial con tendencia calcule la demanda para el dı́a lunes siguiente. Ini-
cialice la tendencia considerando los dı́as de lunes a jueves y el pronóstico como un promedio simple entre
los 7 dı́as de la semana. Considere α = 0,15 y δ = 1.


Solución

   Sabemos que:


                                                F ITt = Ft + Tt


                                                      19
                                      Ft = αAt + (1 − α)(Ft−1 + Tt−1 )

                                      Tt = (δ(Ft − Ft−1 ) + (1 − δ)Tt−1 )

   Para calcular la tendencia, se deben tomar en cuenta los primeros 4 dı́as de la semana:


                                   Tviernes = (40−19)+(19−26)+(26−25)
                                                         3            =5

   Por otro lado, el pronóstico se calcula como el promedio simple entre los 7 dı́as de la semana, obteniendo
un valor de 34,57.
Entonces:


                                  F ITviernes = Fviernes + Tviernes = 39, 57

De esta forma:

   Dı́a          Lunes     Martes     Miércoles      Jueves        Viernes       Sábado   Domingo   Lunes
   Demanda       25        26         19              40            50            52        30
   Tt                                                               5             6,6       6,8       2,6
   Ft                                                               34,6          43,7      51        46,7
   F ITt                                                            39,6          50,3      57,8      49,3
   | error |                                                        10,4          1,7       27,8

   Luego, la demanda esperada será de 49,3 platos.

Problema 8
El DT del Real Madrid, Zinedine Zidane, está muy preocupado por el rendimiento de su equipo, que ha
tenido una muy mala temporada. Una de sus preocupaciones es su temerario defensa: Sergio Ramos. A
Zidane le preocupa que siga haciendo muchas faltas por partido y que lo terminen expulsando.
Para esto le encarga que pronostique utilizando el método de suavizamiento exponencial con tendencia
el número de faltas que cometerá en el próximo partido. Para inicializar, considere un promedio simple
entre los 2 primeros partidos para F3 . Para la tendencia inicial considere los 2 primeros partidos también.
(α = 0, 4; δ = 0, 2)
A continuación se muestran las faltas en los últimos 7 partidos:

                                                                    5
                             Partido     1      2     3        4              6     7
                                                                    (Derby)
                             Faltas      15     22    11       18   40        22    27

Solución

   Para esta solución, siguiendo las fórmulas que aparecen en clases y/o en el problema anterior, tenemos:


                                                T3 = 22 − 15 = 7

                                               F3 = 15+22
                                                      2   = 18, 5

                                             F IT3 = 18, 5 + 7 = 25, 5

                                  T4 = 7 + 0, 4 ∗ 0, 2 ∗ (11 − 25, 5) = 5, 84


                                                          20
                                     F4 = 25, 5 + 0, 4 ∗ (11 − 25, 5) = 19, 7

                                         F IT4 = 19, 7 + 5, 84 = 25, 54

... y ası́ continuamos aplicando iterativamente las fórmulas hasta llegar a que:


                                                  F IT8 = 35, 5

Problema 9
¿Por qué se dice que el modelo de suavizamiento exponencial es un modelo que “tiene memoria” y en especial
una memoria a infinito? Realizar la derivación matemática.


Solución

   La fórmula del modelo es la siguiente:


                          Ft = Ft−1 + α(At−1 − Ft−1 ) → Ft = At−1 · α+(1 - α)Ft−1
   donde,


                                         Ft−1 = α · At−2 +(1 - α)Ft−2
   De este modo,
            Ft = α · At−1 +(1 - α)[α · At−2 +(1 - α)Ft−2 ] → α · At−1 + α(1 - α)At−2 + (1 − α)2 Ft−2

   Siguiendo el mismo proceso, se puede expresar como serie

                                       P∞          k                  ∞
                                Ft =    k=0 (1 − α) αA(t−1−k) +(1 − α) Ft−∞

   Como 0 < α < 1 =⇒ lim(n→∞) (1 − α)n = 0

   El problema es que no hay datos infinitos hacia atrás, por lo que se debe inicializar el modelo. Por lo
tanto, en la realidad la memoria del modelo llega solo hasta la inicialización.

Problema 10
Se sabe que en el Hospital del Trabajador, la demanda de camillas al año ha seguido el siguiente patrón:

                                               Año    Demanda
                                               2014      750
                                               2015      800
                                               2016      815
                                               2017      850
                                               2018      875

   Estime con una confianza del 85% el intervalo que contiene el pronóstico del número de camillas que se
requerirán en el hospital para el año 2018, usando los siguientes 3 modelos:



                                                       21
a) Suavizamiento exponencial con tendencia, con α = 0.8 y δ = 0.4, se sabe que en el 2012 se utilizaron 690
camillas y en el 2013, 720. Además se sabe que el pronóstico realizado hace 5 años para el 2014 era de 740
camillas.
b) Media móvil de 3 periodos.
c) Modelo de regresión Y = 690 + 40 ∗ X, donde X corresponde a ı́ndice del año (1 para el 2014) e Y
representa la demanda anual de camillas.

     ¿Qué método es preferible?


Solución

   El intervalo de confianza se define mediante la siguiente relación:
Ft ± zσ ∗ σ = P (zσ ) , donde 1.25 ∗ zσ = zM AD y z es el parámetro de una distribución normal estándar.
a) Para inicializar el primer método se calcula la tendencia inicial:


                                            T1 = (720−690)+(750−720)
                                                          2          = 30

                                                      F1 = 740

De este modo,

                          Año       A(t)    FIT(t)     F(t)      T(t)    Error   MAD
                          2014       750       770      740        30       20      20
                          2015       800      776,6     754       23,6    -22,4    21,2
                          2016       815     826,29    795,52     30,77   11,29    17,9
                          2017       850     844,41    817,26     27,16   -5,59   14,82
                          2018       875     877,83    848,88     28,94    2,83   12,42

    Utilizando la tabla normal estándar obtenemos el z para una confianza de 85%. Se revisa en la tabla el
valor z que entrega una probabilidad de (1 - 0.85) / 2 = 0.075 (debido a que el margen es por ambos lados),
lo que da un z = 1.44. Con lo que se obtiene el parámetro zM AD = 1.8. De este modo, el intervalo de un
85% de confianza para el parámetro será:
                                            F IT2018 ± M AD2018 ∗ zM AD

                                       877.83 ± 22.356 → (855.474, 900.186)

b)


                                     Año     A(t)    F(t)       Error    MAD
                                     2014     750
                                     2015     800
                                     2016     815
                                     2017     850     788,33     -61,67   61,67
                                     2018     875     821,67     -53,33   57,5

     Y su intervalo asociado será


                                        821.67 ± 103, 5 → (718.17, 925.17)


                                                         22
   c)


                                   Año     A(t)   F(t)    Error    MAD
                                   2014     750    730      -20      20
                                   2015     800    770      -30      25
                                   2016     815    810       -5     18,33
                                   2017     850    850       0      13,75
                                   2018     875    890       15      14

   Y su intervalo asociado será


                                          890 ± 17.5 → (872.5, 907.5)

    El método escogido es el que tiene un menor rango, que a su vez corresponde al método de menor MAD,
es decir, el de la letra a)




                                                      23
