# Enunciados transcritos - Ayudantías para examen

> Fuente: PDFs en `ayudantias/ayudantias_para_examen`. Transcripción base generada con `pdftotext -layout`. `Ayudantía_11.pdf` y `Ayudantía_11-1.pdf` son duplicados textuales; se conserva una sola versión.


---

## ayudantia_10_gop

                        Pontificia Universidad Católica de Chile
                        Escuela de Ingenierı́a
                        Departamento de Ingenierı́a Industrial y de Sistemas
                        ICS3213 – Gestión de operaciones
                        Profesores Alejandro Mac Cawley - Rodrigo Carrasco
                        Primer Semestre 2026



                                    Ayudantı́a 10
                                  Bodegas y Calidad
                        Ayudante: Alonso Parada Frigerio (alonso.parada@uc.cl)


Problema 1
El CD dispone de un volumen de 1.900 m3 en un área de picking rápido que se surte desde un área de
reserva. Todos los SKU deben ingresar a esta área. Se entrega la siguiente información:

                            SKU      Pick/mes    un/mes     un/caja   m3 /caja
                             A          780       4600        25        4.5
                             B          610       1150        17        4.0
                             C          300       2100        11        3.0
                             D          480       2900        20        2.0


Se pide:

 (a) ¿Cuánto espacio se le asigna a cada SKU?
 (b) ¿Con qué frecuencia se deben reponer si todos los SKU se reponen al mismo tiempo?


Problema 2
Usted decide que quiere implementar un sistema de control estadı́stico en su panaderı́a, ya que ha recibido
muchas quejas de que sus paquetes de panes tienen un peso distinto al que aparece en el etiquetado. Por
lo mismo, decide hacer un esquema de 27 muestras de paquetes, a los cuales les mide su peso en gramos.
Los resultados de las muestras se muestran en la siguiente tabla:

                           Muestra    Peso   Muestra      Peso    Muestra   Peso
                             1        342      10         342       19      376
                             2        356      11         366       20      320
                             3        381      12         371       21      359
                             4        322      13         340       22      378
                             5        355      14         370       23      397
                             6        359      15         365       24      319
                             7        368      16         354       25      347
                             8        341      17         353       26      374
                             9        333      18         326       27      324


También se sabe que:
                                                X
                                                    X̂ = 9538

                                             X
                                                 X̂ 2 = 3376759


                                        V ar[X] = E[X 2 ] − E[X]2
 (a) Calcule la media y la desviación estándar de la muestra.
 (b) Establezca los lı́mites de control del proceso para un 96% de confianza.

 (c) Presente el gráfico con los lı́mites de control encontrados.
 (d) Determine si el proceso se encuentra en control o no. En caso de no estarlo, ¿qué muestras se
     encuentran fuera de los lı́mites? ¿Cómo queda el gráfico sin estos datos?


Problema 3
Usted es el gerente de calidad de una empresa metalmecánica y se encuentra estableciendo un sistema
de aseguramiento de la calidad. Para el proceso A, usted decide tomar muestras y obtiene el siguiente
resultado:

                                  Fecha        Valores de las Muestras (mm)
                               24 de Junio     0.5 0.6 0.4          0.3
                               25 de Junio     0.5 0.5 0.4          0.6
                               26 de Junio     0.7 0.5 0.5          0.7
                               27 de Junio     0.5 0.5 0.5          0.5


 (a) Con esta información encuentre los lı́mites para el promedio y, a su vez, para la diferencia entre el
     máximo y mı́nimo.

 (b) Si hoy toma una muestra la cual entrega los siguientes resultados: 0.4 mm, 0.7 mm, 0.5 mm y 0.9
     mm. Basándose en la gráfica anteriormente realizada, ¿qué puede decir del proceso?
 (c) Usted cree que debe controlar mejor lo que recibe como insumo, para lo cual desea proponer un
     sistema de muestreo. Para ello define un AQL de 0.02 y un LPTD de 0.08, con un α de 0.05 y un β
     de 0.1. Indique y explique el plan de muestreo.

---

## Ayudantía_11

                    Pontificia Universidad Católica de Chile
                    Departamento Ingenierı́a Industrial y de Sistemas
                    ICS3213 – Gestión de Operaciones
                    Profesor Alejandro Mac Cawley - Rodrigo Carrasco (Sección 1, 2 y 3)
                    Primer Semestre del 2026



                                   Ayudantı́a 11
                            Ayudante: Juan Pablo Garcı́a – jgarca@uc.cl




1.      Calidad: Control de Procesos
    El Control de Procesos es una herramienta del departamento de control de calidad que
comprende la verificación de una muestra aleatoria de salidas de un proceso para determinar si
este produce artı́culos con caracterı́sticas dentro de un rango aceptable o de tolerancia.
    Esta evaluación se basa principalmente en los Gráficos de Control, los cuales permiten
estudiar la variación de un proceso, mostrar si está bajo control o no, indicar resultados que
requieren explicación y definir los lı́mites de capacidad del sistema.
    Existen dos metodologı́as de cálculo dependiendo del tamaño de la muestra (n):

1.1.     Para muestras grandes (más de 25 unidades)
     Se asume una distribución normal y se utiliza el promedio (x) y la desviación estándar (σ).

       La desviación estándar del promedio se calcula como:
                                                       σ
                                                  σx = √
                                                         n

       Lı́mite de Control Superior (LCS):

                                              LCS = x + Z · σ

       Lı́mite de Control Inferior (LCI):

                                              LCI = x − Z · σ

1.2.     Para muestras pequeñas (menos de 25 unidades) - Gráficos X y
         R
     Cuando la muestra es pequeña, no se usa Z, sino factores estadı́sticos de tabla (A2 , D3 , D4 ).

  1. Se obtiene la media de cada muestra (X) y el recorrido de cada muestra (R, que es la
     diferencia entre el valor máximo y el mı́nimo).

17-06-2026                           ICS3213 – Ayudantı́a 11                            Página 1 de 6
  2. Se calcula el promedio de todas las medias (X) y el promedio de todos los recorridos (R).
  3. Lı́mites para el promedio (X):
                                           LCSX = X + A2 · R
                                           LCIX = X − A2 · R
  4. Lı́mites para el recorrido (R):
                                              LCSR = D4 · R
                                              LCIR = D3 · R
Nota: Para que el proceso esté controlado, cada submuestra debe caer dentro de los lı́mites tanto
en el gráfico de X como en el de R.

1.3.     Variabilidad y Capacidad del Proceso (Cp y Cpk )
       Cp (Capacidad Potencial): Mide si el proceso es capaz de cumplir con las tolerancias. Un
       Cp bajo indica que los datos están muy dispersos y se salen de los lı́mites aceptables.
                                                 U SL − LSL
                                            Cp =
                                                      6σ
       Cpk (Capacidad Real): Se utiliza cuando la distribución de los datos no está centrada (es
       decir, la media está desviada del objetivo). Si el proceso está descentrado, la probabilidad
       de un mal resultado aumenta drásticamente. Se calcula como el valor mı́nimo entre:
                                                                           
                                             U SL − Media Media − LSL
                                Cpk = mı́n                  ,
                                                  3σ              3σ

2.      Coordinación en las Cadenas de Abastecimiento
   El problema fundamental en la cadena de suministro es que, normalmente, cada agente
optimiza su propio beneficio de forma local (fabricante, marketing, transporte, etc.). Estas
decisiones descentralizadas generan ineficiencias globales.

2.1.     El problema: La Cadena Descentralizada vs. Centralizada
   Para entender esto, se plantea un modelo entre un Proveedor (que define un precio de venta
w y tiene un costo de producción c) y un Comprador/Retailer (que enfrenta una demanda del
mercado Q = a − bP ).
       Solución Descentralizada (Doble Marginalización): El proveedor ofrece un precio w
       y el comprador selecciona la cantidad Q para maximizar su propia utilidad. Al hacer esto
       secuencialmente, el proveedor cobra w = a+c
                                                 2
                                                    y el retailer compra una cantidad Q = a−c
                                                                                            4b
                                                                                               .
       Esto lleva a un problema llamado Doble Marginalización, que provoca que la utilidad
       total de la cadena sea subóptima.
       Solución Centralizada: Si la cadena actuara como un solo dueño (integrada), maxi-
       mizarı́an la ganancia global. Al hacerlo, la cantidad vendida sube exactamente al doble:
       Q = a−c
             2b
                . Esto resulta en un precio de mercado más bajo y una utilidad total para la cadena
       mucho mayor.

17-06-2026                          ICS3213 – Ayudantı́a 11                           Página 2 de 6
2.2.     Contratos de Coordinación
    Como las cadenas rara vez están integradas como una sola empresa, se utilizan contratos
para coordinar a los agentes. El objetivo de un contrato es obtener utilidades lo más cerca posi-
ble del óptimo centralizado, dividir de forma flexible estas utilidades, mantener bajos costos de
administración y aplicar justicia.
    Existen distintos tipos de contratos:

  1. Tarifa de dos partes: Busca extraer rentas.

  2. Descuentos por cantidad: Busca incentivar el aumento de la cantidad ordenada (Q).

  3. Compartir utilidades (Revenue Sharing): Reduce la doble marginalización.

  4. Contratos de retro-compra (Buy-back): Aumentan la cantidad al compartir el riesgo.

2.3.     Profundización: Compartir Utilidades (Franquicias / Ej: Netflix)
   En este esquema, el retailer acepta compartir con el proveedor una fracción (α) de sus ingresos.

       Para que matemáticamente la cadena alcance la cantidad óptima global (Q de la cadena
       centralizada), el proveedor debe venderle al retailer el producto por debajo de su costo
       de producción: w = αc.

       A cambio, el retailer se queda solo con una porción de la utilidad (α) y transfiere el resto al
       proveedor.

       Dado que la utilidad total que genera este acuerdo es mayor (ya que simula a la cadena
       centralizada), es posible encontrar un punto de negociación α (por ejemplo, entre 0.25 y 0.5)
       donde ambos ganan más dinero que en el escenario descentralizado.

2.4.     Eficiencia
    El nivel de éxito de la coordinación en la cadena se mide mediante la Eficiencia, que es la
razón entre el Beneficio Total obtenido y el Beneficio Total Óptimo de la cadena:
                                            Π        Beneficio Total
                            Eficiencia =        =
                                           Πopt   Beneficio Total Óptimo




17-06-2026                           ICS3213 – Ayudantı́a 11                            Página 3 de 6
Problema 1
    La empresa Tarjetas ABC desea establecer un plan de producción JIT. La demanda diaria
registrada es de 200 tarjetas telefónicas por hora. El proceso de producción de estas tarjetas pasa
por 3 grandes operaciones antes del control de calidad ubicado al final de la lı́nea: impresión de
las leyendas (P1), la inclusión del chip (P2) y cortado de la tarjeta (P3).



                      P1                  P2                   P3

                                                                           Control de calidad




    La empresa cuenta con un registro de los tiempos promedios de procesamiento (tpi ) por ope-
ración, además de los tiempos de envı́o de los Kanbans (tki ) y tiempos de envı́o de los lotes (tvi ).

                     Operación     Lote (C)         tpi (seg)      tki (seg)    tvi (seg)
                           P1             200             85           45           200
                           P2             250             78           67           300
                           P3             300             50           92           150

    Por su parte, los registros históricos del control de calidad indican que en promedio un 15 %
de las unidades son descartadas.

  a) (10 ptos) A partir de los datos anteriores, calcule el número de Kanbans necesarios en el
     proceso productivo.

    Las investigaciones de la empresa han determinado que el proceso P3 es el que está actual-
mente generando el 15 % del descarte de las tarjetas, las cuales no están saliendo con los tamaños
adecuados. Se realizó un muestreo del largo de las tarjetas de 5 lotes recibidos durante los últimos
5 dı́as. Los resultados se muestran a continuación:

                                    Dı́a        Largo (milı́metros)
                                      1         70   56   49   67     61
                                      2         65   47   70   70     68
                                      3         70   49   42   68     54
                                      4         50   47   52   67     50
                                      5         48   65   51   50     65

   A partir de lo anterior:
  b) (8 ptos) Calcule los lı́mites de control, eliminando los outliers. Realice los gráficos corres-
     pondientes.

  c) (2 ptos) Si el dı́a 6 usted toma una muestra con los siguientes resultados: 63, 54, 43, 69 y
     65. ¿Qué puede decir de la muestra? ¿Está el proceso bajo control?

17-06-2026                           ICS3213 – Ayudantı́a 11                                    Página 4 de 6
  d) (5 ptos) El implementar el control reduce las fallas del sistema a solo un 5 %. Con esta
     información ¿cambia el número Kanbans? Argumente.

Problema 2
    Suponga el siguiente proceso que funciona mediante el uso de Just in Time y Kanbans. El
sistema productivo produce un producto P1 y se produce a través de 3 máquinas que funcionan
en serie y sus capacidades se indican en unidades por minuto, las cuales no tienen variabilidad.



                                M1                     M2                      M3
       Proveedor                                                                          Cliente
                            100 Uni./Min            55 Uni./Min            120 Uni./Min
                   Kanban                  Kanban                 Kanban




  a) (10 ptos) La empresa ha establecido que los lotes de producción sean de 100 unidades y
     el tiempo que se demora un Kanban en arribar de una máquina a otra es de 2 minutos y
     el tiempo en que se demora el lote de moverse de una máquina a otra es de 6 minutos. El
     Kanban desde M1 al proveedor demora 3 minutos en llegar, el proveedor demora en producir
     el lote 15 minutos y 10 minutos en entregar el Kanban a la empresa. Si la demanda del cliente
     es de 22.800 unidades al dı́a, con una variación de 5 %, y se trabaja un turno de 8 hrs al dı́a.
     ¿Cuál serı́a el número óptimo de Kanbans entre cada máquina y el proveedor?

  b) (7 ptos) M1 presenta fallas. El tiempo entre una falla y otra es de 100 hrs y cuando falla, la
     reparación demora en promedio 25 minutos. ¿Afecta esto el número de Kanban y cuál serı́a
     del número óptimo?

  c) (8 ptos) Se le informa a usted que M1 también produce un 20 % de unidades defectuosas que
     son descubiertas una vez que pasan el proceso de M3. Estas unidades deben ser desechadas.
     Con esta información ¿cuál serı́a del número óptimo de Kanbans? Si puede colocar un control
     de calidad en el proceso ¿En qué parte lo colocarı́a y cuál serı́a su efecto en las unidades
     producidas y costo? Si elimina los defectos ¿Cuál serı́a su efecto en las unidades producidas
     y el costo?




17-06-2026                           ICS3213 – Ayudantı́a 11                                Página 5 de 6
Problema 3
   Usted está a cargo de la logı́stica de una empresa que vende al retail. Actualmente la empresa
cuenta con un producto y dos mercados en los que vende su producción (1 y 2). Usted determina
que el costo de cada orden es de $60 por orden y el costo de mantener inventario es de $0,27 por
unidad a la semana. El gerente le pide un nivel de servicio de un 97 % (z = 1, 88). La fábrica tiene
un tiempo de respuesta o lead time de 1 semana.


                                     Semana
                  Mercado       1    2   3    4    5    Promedio     Desv. Est.
                       1       33   45   37   38   55      41,6           8,6
                       2       46   35   41   40   26      37,6           7,6


    Se despacha directamente a cada mercado independientemente y usted está analizando la posi-
bilidad de centralizar el despacho. Usted ha determinado que el costo de transporte descentralizado
es de $1,05 por unidad y centralizado es de $1,10 por unidad y el precio de venta del producto es
$1. Con esta información usted debe:

  a) (10 ptos) Determinar la polı́tica de inventario descentralizada para cada mercado. Determine
     el costo anual.

  b) (10 ptos) Determinar la polı́tica de inventario centralizada. Determine el costo anual.

  c) (10 ptos) ¿Qué recomendarı́a usted? Construya un modelo matemático que permita deter-
     minar la decisión óptima para N productos y M mercados.




17-06-2026                          ICS3213 – Ayudantı́a 11                           Página 6 de 6

---

## Ayudantía_12

                  Pontificia Universidad Católica de Chile
                  Departamento Ingenierı́a Industrial y de Sistemas
                  ICS3213 – Gestión de Operaciones
                  Profesor Alejandro Mac Cawley - Rodrigo Carrasco (Sección 1, 2 y 3)
                  Primer Semestre del 2026



                                  Ayudantı́a 12
                            Ayudante: Juan Pablo Garcı́a – jgarca@uc.cl




Problema 1
    Usted se encuentra a cargo del proceso de producción de una gran empresa productora de
galletas. Su producto estrella son las galletas de arándanos y para la producción de estas galletas
se requiere de la masa base y los arándanos. A continuación se detalla el proceso:


                                              Control
                               Azucarado
                                              Calidad

     Arándanos
                   Secado
      Frescos

                                 Molido                     Mezclado      Cocido    Control Calidad



     Masa Base                  Amasado




    Los arándanos frescos llegan de los proveedores y son sometidos a un proceso de secado, con
una capacidad de 300 kg/hr. Posteriormente el 80 % de los arándanos va a un proceso de molido,
con una capacidad de 280 kg/hr, en donde se transforma en polvo de arándano. El restante 20 %
de los arándanos secos sigue a un proceso de azucarado, con una capacidad de 65 kg/hr, en donde
se les coloca una capa de azúcar y posteriormente se controla la calidad y un 10 % de los arándanos
azucarados debe ser desechado por no cumplir con el standard de calidad. Por otro lado, la masa
base pasa a la máquina de amasado, con una capacidad de 600 kg/hr. Posteriormente la masa
base pasa junto a los arándanos azucarados y el polvo de arándano a la mezcladora, que tiene una
capacidad de 800 kg/hr, posteriormente la mezcla pasa al cocido que tiene una capacidad de 850
kg/hr para finalmente someterse a un control de calidad, en donde el 3 % no cumple el estándar
y debe ser desechado.


  a) ¿Cuál es la máxima capacidad productiva del proceso en términos de kilogramos de galletas
     por hora?


24-06-2026                           ICS3213 – Ayudantı́a 12                          Página 1 de 5
  b) Si el proceso funciona a 1 turno de 8 hrs. al dı́a por 240 dı́as al año. ¿Qué cantidad anual
     de arándanos frescos y masa base debe comprar?

  c) Si usted puede duplicar la capacidad productiva de solo 2 máquinas en el proceso. ¿Qué dos
     máquinas duplicarı́a? ¿Cuál serı́a la capacidad productiva nueva?


La empresa tiene dificultades para estimar la cantidad de envases que debe solicitar a su proveedor
para almacenar sus galletas. De acuerdo a la información registrada en los últimos 6 meses, se
estima que la demanda promedio es de 50.000 unidades. Además, suponga que el costo de inventario
es de $1,5 unidad/mes, el costo por unidad es de 60 pesos, el costo de la orden es de $90.000 y
el proveedor se demora 1 semana en entregar el pedido. Considerando una varianza de 2.500 con
un nivel de servicio de 95 % para no tener problemas con los minoristas. Calcule el pedido óptimo
de envases para el próximo mes. Considere que tiene una polı́tica de periodo fijo de 1 mes y los
pedidos llegan siempre antes de que comience el mes para el cual se requieren.


  d) ¿Cuál es la cantidad óptima de pedido y las fechas en que debe ordenar?

  e) Si ahora se considera una polı́tica de revisión continua. ¿Cuál serı́a la nueva cantidad óptima
     de pedido y el punto de re orden?

  f) El proveedor le ofrece firmar un contrato para asegurar la provisión de envases para los próxi-
     mos 3 meses. Usted estima que las cantidades de envases para los próximos 3 meses serı́an
     49.000, 53.000 y 47.000 respectivamente. ¿Cuál es la cantidad óptima de pedido mensuales
     y en qué meses ordenarı́a? (Hint: Utilice método Wagner-Whitin)

  g) Calcule el costo de inventario de los 3 sistemas. Si el proveedor le cobra un costo fijo por el
     contrato ¿Cuánto seria lo máximo que estarı́a dispuesto a pagar?




24-06-2026                          ICS3213 – Ayudantı́a 12                             Página 2 de 5
Problema 2
    Usted utiliza dos insumos en su proceso productivo U1 y U2 , los cuales los debe adquirir al
mismo proveedor. U1 tiene un costo de $100 por unidad y U2 tiene un costo de $70 por unidad.
La demanda diaria de U1 ha sido de 6 unidades con una desviación estándar de 1 unidad diaria y
la de U2 ha sido de 4 unidades con una desviación estándar de 0,65 unidades diarias.
    El costo anual de mantener inventarios es de un 20 % del valor del artı́culo y usted tiene
capacidad infinita de guardar U1 y U2 . El proveedor le cobra una cantidad fija de $100 por cada
despacho de U1 , U2 o ambas, independiente de la cantidad, y demora 10 dı́as en completar el
pedido tanto de U1 como el de U2 . Usted trabaja los 365 dı́as del año y desea mantener un nivel
de servicio de un 95 %.
    Hint: Recuerde que es posible solicitar los dos productos (U1 y U2 ) en el mismo despacho.

  a) Las cantidades óptimas a pedir, puntos de reorden, números de pedidos anuales, tiempo entre
     pedidos y costos anuales de la polı́tica para U1 y U2 si se utiliza una polı́tica de revisión
     continua.

  b) Las cantidades óptimas a pedir, puntos de reorden, números de pedidos anuales, tiempo entre
     pedidos y costos anuales de la polı́tica para U1 y U2 si se utiliza una polı́tica de periodo fijo.

  c) ¿Por cuál polı́tica de inventario se decide?




24-06-2026                          ICS3213 – Ayudantı́a 12                             Página 3 de 5
Problema 3
    Alfa es una empresa que se dedica al transporte de pasajeros entre Santiago y el aeropuerto de
esa ciudad. Comenzó su actividad hace dos años y está formada por 4 amigos que han invertido en
9 autos/taxi. Se han organizado para cubrir zonas en Santiago y hacen transportes al aeropuerto.
La disponibilidad de los automóviles es variable durante el dı́a, al igual que los pedidos que reciben.
Dado que sus zonas son especialmente las comerciales céntricas y de oficinas, durante el fin de
semana no brindan servicios.

En la tabla se muestran algunos datos relevados desde sus planillas de trabajo:

                                    Demanda media     # Autos que
     Bloque
                Franja horaria       (# viajes) en  cubren el servicio CVa                   CVs
     horario
                                    Zona en franja en la franja horaria
         1         8:00 a 14:00           35                 4          2                      5
         2        14:01 a 16:00           27                 6          2                      5
         3        16:01 a 23:00           85                 6          2                      7
         4         23:00 a 8:00           45                 3          1                     1.5


En la tabla se indica la variabilidad del tiempo de arribo de las solitudes de los clientes (CVa) y la
variabilidad que presentan los viajes (CVs). En promedio cada taxi demora 20 minutos por cada
viaje. Sakasegawa (1977) propone una aproximación al tiempo de espera para sistemas G/G/c
dada por:
                                                       √
                                          CVa2 + CVs2 ρ( 2c+2)−1 1
                                       
                                  Wq ≈
                                               2         c(1 − ρ) µ

Aunque inicialmente todos atendı́an zonas bien demarcadas, con el correr del tiempo los clientes
han empezado a cambiar los puntos de partida y salida. Eso les ha llevado a sea posible hacer
viajes FUERA DE ZONA, donde las condiciones de tránsito, seguridad y accesos, son dispares.
El salir FUERA DE ZONA lleva a un aumento en un 20 % de la demanda media. Estos viajes se
distribuyen: un 15 % en la franja 1, 15 % en la franja 2, 50 % en la 3 y el 20 % en la 4. Los tiempos
FUERA DE ZONA cambian por los factores mencionados, permitiendo que un auto FUERA DE
ZONA pueda atender solo 1.5 viajes por hora.

Los socios tienen como polı́tica que sus autos/taxis estén un 90 % utilizados, ya que eso permite
dar un buen servicio y tener viajes. Actualmente están evaluando si el salir fuera de la zona es
una adecuada polı́tica; pero no saben si tomar una medida definitiva sobre esto tendrá impactos
negativos sobre su negocio.

Por ende, le piden a usted que responda las siguientes preguntas:

  a. ¿Cuál es la tasa de ocupacion de los taxis? Determine los tiempos promedios de espera para
     el bloque más congestionado. ¿Se sigue la polı́tica de utilización de Alfa? ¿Deberı́a cambiar
     la asignación de taxis por franja? ¿Por qué?

  b. Si los socios deciden hacer viajes FUERA DE ZONA ¿Cuál es la tasa de ocupacion de los
     taxis si no se cambia el número de autos en servicio? Suponga que los tiempos de espera para

24-06-2026                           ICS3213 – Ayudantı́a 12                             Página 4 de 5
     cada franja horaria deben mantenerse similares a los del punto a, en un rango de +/-30 %.
     ¿Que flota de taxis asignarı́a para cada franja horaria? Recalcule los Wq y en caso de hacer
     supuestos defı́nalos claramente.

  c. Si los socios determinan que el costo de espera de cada cliente es de Cq [$/min] pesos
     por minuto esperando. Por otro lado, determinan que cada unidad porcentual (1 %) de
     disminución en su nivel de utilización tiene costo Cu [$/(unidad %)] y es posible aumentar el
     número de taxis por bloque a un costo de Ck [$/taxi/bloque], lo que claramente aumentarı́a
     el nivel de servicio. Plantee un modelo de programación matemática que permita: determinar
     el número óptimo de taxis a tener por bloque horario, nivel de utilización optimo y también
     determinar si debemos o no hacer viajes FUERA DE ZONA.




24-06-2026                         ICS3213 – Ayudantı́a 12                           Página 5 de 5
