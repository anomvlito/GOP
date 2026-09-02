Pontificia Universidad Cat´olica de Chile
Departamento Ingenier´ıa Industrial y de Sistemas
ICS3213 – Gesti´on de Operaciones
Profesor Alejandro Mac Cawley - Rodrigo Carrasco (Secci´on 1, 2 y 3)
Primer Semestre del 2026
Ayudant´ıa 11
Ayudante: Juan Pablo Garc´ıa – jgarca@uc.cl
1.
Calidad: Control de Procesos
El Control de Procesos es una herramienta del departamento de control de calidad que
comprende la verificaci´on de una muestra aleatoria de salidas de un proceso para determinar si
este produce art´ıculos con caracter´ısticas dentro de un rango aceptable o de tolerancia.
Esta evaluaci´on se basa principalmente en los Gr´aficos de Control, los cuales permiten
estudiar la variaci´on de un proceso, mostrar si est´a bajo control o no, indicar resultados que
requieren explicaci´on y definir los l´ımites de capacidad del sistema.
Existen dos metodolog´ıas de c´alculo dependiendo del tama˜no de la muestra (n):
1.1.
Para muestras grandes (m´as de 25 unidades)
Se asume una distribuci´on normal y se utiliza el promedio (x) y la desviaci´on est´andar (σ).
La desviaci´on est´andar del promedio se calcula como:
σx = σ
√n
L´ımite de Control Superior (LCS):
LCS = x + Z · σ
L´ımite de Control Inferior (LCI):
LCI = x −Z · σ
1.2.
Para muestras peque˜nas (menos de 25 unidades) - Gr´aficos X y
R
Cuando la muestra es peque˜na, no se usa Z, sino factores estad´ısticos de tabla (A2, D3, D4).
1. Se obtiene la media de cada muestra (X) y el recorrido de cada muestra (R, que es la
diferencia entre el valor m´aximo y el m´ınimo).
17-06-2026
ICS3213 – Ayudant´ıa 11
P´agina 1 de 6

2. Se calcula el promedio de todas las medias (X) y el promedio de todos los recorridos (R).
3. L´ımites para el promedio (X):
LCSX = X + A2 · R
LCIX = X −A2 · R
4. L´ımites para el recorrido (R):
LCSR = D4 · R
LCIR = D3 · R
Nota: Para que el proceso est´e controlado, cada submuestra debe caer dentro de los l´ımites tanto
en el gr´afico de X como en el de R.
1.3.
Variabilidad y Capacidad del Proceso (Cp y Cpk)
Cp (Capacidad Potencial): Mide si el proceso es capaz de cumplir con las tolerancias. Un
Cp bajo indica que los datos est´an muy dispersos y se salen de los l´ımites aceptables.
Cp = USL −LSL
6σ
Cpk (Capacidad Real): Se utiliza cuando la distribuci´on de los datos no est´a centrada (es
decir, la media est´a desviada del objetivo). Si el proceso est´a descentrado, la probabilidad
de un mal resultado aumenta dr´asticamente. Se calcula como el valor m´ınimo entre:
Cpk = m´ın
USL −Media
3σ
, Media −LSL
3σ

2.
Coordinaci´on en las Cadenas de Abastecimiento
El problema fundamental en la cadena de suministro es que, normalmente, cada agente
optimiza su propio beneficio de forma local (fabricante, marketing, transporte, etc.). Estas
decisiones descentralizadas generan ineficiencias globales.
2.1.
El problema: La Cadena Descentralizada vs. Centralizada
Para entender esto, se plantea un modelo entre un Proveedor (que define un precio de venta
w y tiene un costo de producci´on c) y un Comprador/Retailer (que enfrenta una demanda del
mercado Q = a −bP).
Soluci´on Descentralizada (Doble Marginalizaci´on): El proveedor ofrece un precio w
y el comprador selecciona la cantidad Q para maximizar su propia utilidad. Al hacer esto
secuencialmente, el proveedor cobra w = a+c
2
y el retailer compra una cantidad Q = a−c
4b .
Esto lleva a un problema llamado Doble Marginalizaci´on, que provoca que la utilidad
total de la cadena sea sub´optima.
Soluci´on Centralizada: Si la cadena actuara como un solo due˜no (integrada), maxi-
mizar´ıan la ganancia global. Al hacerlo, la cantidad vendida sube exactamente al doble:
Q = a−c
2b . Esto resulta en un precio de mercado m´as bajo y una utilidad total para la cadena
mucho mayor.
17-06-2026
ICS3213 – Ayudant´ıa 11
P´agina 2 de 6

2.2.
Contratos de Coordinaci´on
Como las cadenas rara vez est´an integradas como una sola empresa, se utilizan contratos
para coordinar a los agentes. El objetivo de un contrato es obtener utilidades lo m´as cerca posi-
ble del ´optimo centralizado, dividir de forma flexible estas utilidades, mantener bajos costos de
administraci´on y aplicar justicia.
Existen distintos tipos de contratos:
1. Tarifa de dos partes: Busca extraer rentas.
2. Descuentos por cantidad: Busca incentivar el aumento de la cantidad ordenada (Q).
3. Compartir utilidades (Revenue Sharing): Reduce la doble marginalizaci´on.
4. Contratos de retro-compra (Buy-back): Aumentan la cantidad al compartir el riesgo.
2.3.
Profundizaci´on: Compartir Utilidades (Franquicias / Ej: Netflix)
En este esquema, el retailer acepta compartir con el proveedor una fracci´on (α) de sus ingresos.
Para que matem´aticamente la cadena alcance la cantidad ´optima global (Q de la cadena
centralizada), el proveedor debe venderle al retailer el producto por debajo de su costo
de producci´on: w = αc.
A cambio, el retailer se queda solo con una porci´on de la utilidad (α) y transfiere el resto al
proveedor.
Dado que la utilidad total que genera este acuerdo es mayor (ya que simula a la cadena
centralizada), es posible encontrar un punto de negociaci´on α (por ejemplo, entre 0.25 y 0.5)
donde ambos ganan m´as dinero que en el escenario descentralizado.
2.4.
Eficiencia
El nivel de ´exito de la coordinaci´on en la cadena se mide mediante la Eficiencia, que es la
raz´on entre el Beneficio Total obtenido y el Beneficio Total ´Optimo de la cadena:
Eficiencia =
Π
Πopt
=
Beneficio Total
Beneficio Total ´Optimo
17-06-2026
ICS3213 – Ayudant´ıa 11
P´agina 3 de 6

Problema 1
La empresa Tarjetas ABC desea establecer un plan de producci´on JIT. La demanda diaria
registrada es de 200 tarjetas telef´onicas por hora. El proceso de producci´on de estas tarjetas pasa
por 3 grandes operaciones antes del control de calidad ubicado al final de la l´ınea: impresi´on de
las leyendas (P1), la inclusi´on del chip (P2) y cortado de la tarjeta (P3).
P1
P2
P3
Control de calidad
La empresa cuenta con un registro de los tiempos promedios de procesamiento (tpi) por ope-
raci´on, adem´as de los tiempos de env´ıo de los Kanbans (tki) y tiempos de env´ıo de los lotes (tvi).
Operaci´on
Lote (C)
tpi (seg)
tki (seg)
tvi (seg)
P1
200
85
45
200
P2
250
78
67
300
P3
300
50
92
150
Por su parte, los registros hist´oricos del control de calidad indican que en promedio un 15 %
de las unidades son descartadas.
a) (10 ptos) A partir de los datos anteriores, calcule el n´umero de Kanbans necesarios en el
proceso productivo.
Las investigaciones de la empresa han determinado que el proceso P3 es el que est´a actual-
mente generando el 15 % del descarte de las tarjetas, las cuales no est´an saliendo con los tama˜nos
adecuados. Se realiz´o un muestreo del largo de las tarjetas de 5 lotes recibidos durante los ´ultimos
5 d´ıas. Los resultados se muestran a continuaci´on:
D´ıa
Largo (mil´ımetros)
1
70
56
49
67
61
2
65
47
70
70
68
3
70
49
42
68
54
4
50
47
52
67
50
5
48
65
51
50
65
A partir de lo anterior:
b) (8 ptos) Calcule los l´ımites de control, eliminando los outliers. Realice los gr´aficos corres-
pondientes.
c) (2 ptos) Si el d´ıa 6 usted toma una muestra con los siguientes resultados: 63, 54, 43, 69 y
65. ¿Qu´e puede decir de la muestra? ¿Est´a el proceso bajo control?
17-06-2026
ICS3213 – Ayudant´ıa 11
P´agina 4 de 6

d) (5 ptos) El implementar el control reduce las fallas del sistema a solo un 5 %. Con esta
informaci´on ¿cambia el n´umero Kanbans? Argumente.
Problema 2
Suponga el siguiente proceso que funciona mediante el uso de Just in Time y Kanbans. El
sistema productivo produce un producto P1 y se produce a trav´es de 3 m´aquinas que funcionan
en serie y sus capacidades se indican en unidades por minuto, las cuales no tienen variabilidad.
Proveedor
M1
100 Uni./Min
M2
55 Uni./Min
M3
120 Uni./Min
Cliente
Kanban
Kanban
Kanban
a) (10 ptos) La empresa ha establecido que los lotes de producci´on sean de 100 unidades y
el tiempo que se demora un Kanban en arribar de una m´aquina a otra es de 2 minutos y
el tiempo en que se demora el lote de moverse de una m´aquina a otra es de 6 minutos. El
Kanban desde M1 al proveedor demora 3 minutos en llegar, el proveedor demora en producir
el lote 15 minutos y 10 minutos en entregar el Kanban a la empresa. Si la demanda del cliente
es de 22.800 unidades al d´ıa, con una variaci´on de 5 %, y se trabaja un turno de 8 hrs al d´ıa.
¿Cu´al ser´ıa el n´umero ´optimo de Kanbans entre cada m´aquina y el proveedor?
b) (7 ptos) M1 presenta fallas. El tiempo entre una falla y otra es de 100 hrs y cuando falla, la
reparaci´on demora en promedio 25 minutos. ¿Afecta esto el n´umero de Kanban y cu´al ser´ıa
del n´umero ´optimo?
c) (8 ptos) Se le informa a usted que M1 tambi´en produce un 20 % de unidades defectuosas que
son descubiertas una vez que pasan el proceso de M3. Estas unidades deben ser desechadas.
Con esta informaci´on ¿cu´al ser´ıa del n´umero ´optimo de Kanbans? Si puede colocar un control
de calidad en el proceso ¿En qu´e parte lo colocar´ıa y cu´al ser´ıa su efecto en las unidades
producidas y costo? Si elimina los defectos ¿Cu´al ser´ıa su efecto en las unidades producidas
y el costo?
17-06-2026
ICS3213 – Ayudant´ıa 11
P´agina 5 de 6

Problema 3
Usted est´a a cargo de la log´ıstica de una empresa que vende al retail. Actualmente la empresa
cuenta con un producto y dos mercados en los que vende su producci´on (1 y 2). Usted determina
que el costo de cada orden es de $60 por orden y el costo de mantener inventario es de $0,27 por
unidad a la semana. El gerente le pide un nivel de servicio de un 97 % (z = 1, 88). La f´abrica tiene
un tiempo de respuesta o lead time de 1 semana.
Semana
Mercado
1
2
3
4
5
Promedio
Desv. Est.
1
33
45
37
38
55
41,6
8,6
2
46
35
41
40
26
37,6
7,6
Se despacha directamente a cada mercado independientemente y usted est´a analizando la posi-
bilidad de centralizar el despacho. Usted ha determinado que el costo de transporte descentralizado
es de $1,05 por unidad y centralizado es de $1,10 por unidad y el precio de venta del producto es
$1. Con esta informaci´on usted debe:
a) (10 ptos) Determinar la pol´ıtica de inventario descentralizada para cada mercado. Determine
el costo anual.
b) (10 ptos) Determinar la pol´ıtica de inventario centralizada. Determine el costo anual.
c) (10 ptos) ¿Qu´e recomendar´ıa usted? Construya un modelo matem´atico que permita deter-
minar la decisi´on ´optima para N productos y M mercados.
17-06-2026
ICS3213 – Ayudant´ıa 11
P´agina 6 de 6

