# Pontificia Universidad Católica de Chile
Escuela de Ingeniería
Departamento de Ingeniería Industrial y de Sistemas

# PAUTA Examen
# Enunciados

**ICS 3213 Gestión de Operaciones**
**Sección 1 y Sección 2 – 1er semestre 2022**
**Prof. Patricio Gahona**
**Prof. Alejandro Mac Cawley**

**Nombre:** _______________________________ **email UC:** ______________________ **Sección:**_____

**Instrucciones:**
*   Responder en letra legible, en lápiz pasta o bolígrafo y poner nombre a todas las hojas.
*   No debe des corchetear la prueba y responda en el espacio asignado.
*   Esta sección de la prueba tiene 60 puntos, dura 70 minutos y consta de 2 secciones.
*   Se leerá la prueba al comienzo de clases y después se permitirán preguntas en voz alta. Posteriormente en la mitad de la prueba se volverá a permitir preguntas en voz alta. No se permitirán preguntas fuera de estos intervalos. Si su duda persiste indique el supuesto y continúe.
*   Al final de la prueba los alumnos deberán subir su prueba a CANVAS. Dispondrán de 15 minutos para escanear pruebas hoja por hoja y subirlas. Al final de subir la prueba deberán dejarla en el mismo puesto. Si por alguna razón hay un problema al subir la prueba, avisen al profesor/ayudante y dejen su prueba.
*   Este curso adscribe el Código de Honor establecido por la Escuela de Ingeniería el que es vinculante. Todo trabajo evaluado en este curso debe ser propio. En caso de que exista colaboración permitida con otros estudiantes, el trabajo deberá referenciar y atribuir correctamente dicha contribución a quien corresponda. Como estudiante es su deber conocer la versión en línea del Código de Honor (http://ing.puc.cl/codigodehonor).

¡Muy Buena Suerte!

---

**PARTE I (20 Puntos): Responda UNA de las siguientes DOS preguntas de ejercicio.**

a) Usted está a cargo del proceso productivo que produce un producto (P) el cual usa solo un insumo (I). Para producir una unidad de P se requiere una unidad de I. El proceso se compone de dos máquinas que trabajan en serie. La máquina A toma el insumo I y lo procesa a una tasa de 1 segundo por unidad, produciendo un producto semiterminado. Este producto semi terminado se almacena en una cámara de temperatura controlada, para posteriormente ser procesado por la máquina B a una tasa de 50 unidades por minuto. El proceso opera 24 hrs al día los 365 días del año.
El producto final P se vende al mercado premium en $150 por unidad. El problema que usted enfrenta es que el producto terminado es perecible y si no es vendido durante el día, debe ser liquidado en un mercado secundario a un precio de $80 por unidad. Si la demanda por el producto se distribuye normalmente, siendo esta de 68.000 unidades al día en promedio con una desviación standard de 12.000 unidades. El costo total del producto terminado es de $100 por unidad (Incluye el proceso y los insumos). El costo de almacenamiento anual es de $17 por unidad por día para el producto final, de $15 por unidad al año para el producto semiterminado y de $7,3 por unidad para el insumo I. El costo de emitir una orden al proveedor es de $200.000 por orden de insumo I y el proveedor demora 5 días en entregar el pedido, independiente de su tamaño.

Con esta información:
i. (7 puntos) Determine la cantidad diaria a producir del producto final y la cantidad de inventario a mantener del producto terminado.
ii. (6 puntos) Cuál es el lote óptimo de pedido del Insumo I y su punto de reorden.
iii. (7 puntos) Si solo la maquina A tiene un costo de setup, el cual es función de la cantidad a producir, el cual está dado por CT_Setup=300.000/Q, siendo Q la cantidad o lote a producir. Desarrolle una forma funcional para el costo total de pedido del producto semiterminado y plantee la ecuación que permite determinar el lote óptimo.

b) Usted ya ha establecido un carro de comida y determina que el costo total de los clientes en el sistema es CE(Ws), depende del tiempo total (Ws) que éstos están en el sistema y la ecuación que describe este costo es CE(Ws) = 10+2000Ws.
Actualmente tengo una capacidad de atender a 15 clientes por hora con un coeficiente de variación de la atención es de 1, la cual no puedo variar.
Usted debe decidir la cantidad de dinero invertir en marketing para atraer a clientes y a su vez, dar un buen servicio. Para ello se realiza un estudio de mercado el cual me indica que por cada $12 que yo coloque en Marketing, mi tasa de llegada de clientes aumenta en 1 cliente por hora. Es decir, si deseo tener 10 clientes por hora deberé invertir $120 en marketing. También usted determina que cada cliente atendido le entrega un margen operacional de $20, que NO incluye el costo de marketing.

i. (7 puntos) Con esta información plantee un modelo de optimización que le permita determinar la cantidad óptima de marketing que debe implementar en su emprendimiento para tener un buen servicio y atraer a la máxima cantidad de clientes. HINT: un sistema con coeficiente de variación de arribo y servicio de 1 se comporta como un M/M/1.
ii. (6 puntos) Determine la inversión óptima en marketing que debe realizar.
iii. (7 puntos) Si usted puede también variar la capacidad de atención de clientes. ¿Cómo cambia el modelo planteado en i)? ¿Qué información adicional debe disponer? Con esta información plantee el modelo de optimización que le permita determinar el valor de estas variables.

---

**A**
i) Se debe analizar la demanda final utilizando el modelo del vendedor de diarios.
Se obtiene la utilidad de P en mercado premium Ut = 150 -100 = $50 y la perdida por venta en mercado secundario Pe = 100-80 =$20
Se obtiene el fractal optimo P() = 50/(50+20) = 0,7142. Se busca en tabla Z y obtiene 0,57.
La cantidad que demanda el mercado es Q= 68.000 + 0,57 * 12.000 = 74.840 .- Es lo que demanda el mercado diariamente.

Si analizamos la capacidad del proceso: A procesa a 1 segundo por unidad y diariamente la capacidad es es 24*60*60*1 = 86.400
El proceso B es 50*60*24 = 72.000.-
Somo podemos ver el CB esta en B en 72.000 unidades por día y la demanda es de 74.840.- Por lo que se produce a capacidad máxima, es decir 72.000.
Dado que se produce y se vende inmediatamente el inventario es 0.

ii) La demanda es de 72.000 diario, el costo de almacenamiento es de 7,3/365=0,02
Utilizando el Q de Wilson Raiz (2*D*S/H) = Raiz(2*72.000*0,02/200.000) = 1.200.000
L=72.000*5= 360.000

iii) Acá debemos usar la formula con tasa de entrega, pero tiene cambios en el costo de emitir una orden.

Original:
$$CT(Q) = D \cdot C + (D/Q) \cdot S + (Q/2) \cdot H$$

Como el inventario no llega a Q se utiliza $I = q \cdot (p/(p-d))$ y $S = 30.000/Q$. Por ende la ecuación queda como:

$$CT = DC + \frac{300.000 D}{Q^2} + \frac{1}{2}\left(1 - \frac{d}{p}\right)QH$$

$$CT(Q) = 0 - 2 \cdot \frac{300.000 D}{Q^3} + \frac{1}{2}\left(1 - \frac{d}{p}\right)H = 0$$

$$Q = \sqrt[3]{\frac{2 \cdot D \cdot 2 \cdot 300.000}{H}} \sqrt[3]{\frac{p}{p - d}} = 0$$

**b)**
El tiempo en el sistema esta dada por la ecuación
$$W_s = \frac{1}{(\mu - \lambda)}$$

Por ende la función objetivo ahora busca determinar la cantidad optima de MKTG (X) que es lo mismo que el $\lambda$ optimo, dado que $\lambda = X * 1$

La función objetivo es maximizar la utilidad total. Por ende UT = Ingreso clientes - Costo MKTG - Costo Espera
$$Max \ 20\lambda - 12\lambda - (10 + 2000 W_s)$$
S/A
$$W_s = \frac{1}{(\mu - \lambda)}$$
$$0 \leq \lambda \leq \mu$$

$$Max \ 8\lambda - (10 + 2000 W_s)$$
S/A
$$W_s = \frac{1}{(\mu - \lambda)}$$
$$0 \leq \lambda \leq \mu$$

Finalmente queda:
$$Max \ 8\lambda - \left(10 + 2000 \frac{1}{(\mu - \lambda)}\right)$$
$$0 \leq \lambda \leq \mu$$

ii) Si colocamos que $\mu=15$ y derivamos.

$$8 - \left(2000 \left(-1 \cdot \frac{1}{(225 - 15\lambda)^2} \cdot -1\right)\right) = 0$$

Despejando $\lambda = 13,9$

iii)
Si ahora debemos determinar la capacidad de atención tenemos a $\mu$ como incógnita y por ende, debemos colocar el costo adicional del servicio (CS) como un costo

$$Max \ 20\lambda - CS \cdot \mu - 12\lambda - (10 + 2000 W_s)$$
S/A
$$W_s = \frac{1}{(\mu - \lambda)}$$
$$0 \leq \lambda \leq \mu$$

Derivamos con respecto a $\lambda$ y $\mu$. Obtenemos el optimo.

---

**PARTE II. Responda las siguientes dos preguntas.**

**P1 (20 puntos)** Usted se encuentra en el proceso de evaluar las operaciones de sus bodegas y centros de distribución.
A.- Para su primer paso debe determinar la cantidad máxima de demanda anual que puede manejar la bodega. Si los operadores de montacargas trabajan turnos de 8 hrs. por 250 días al año, con un sueldo mensual de $20 mil. El tiempo medio total del proceso, desde la recepción a bodega y a despacho, es de 20 minutos. Si usted actualmente dispone de 2.800 Mt2 de bodega y cada pallet utiliza 4 mt2 de piso en la bodega (Ya que pueden ser apilados). Para la operación usted dispone de 12 trabajadores a tiempo completo.
i. (2 ptos.) Determine las rotaciones de inventario que un operario puede hacer al año.
ii. (3 ptos.) Determine la cantidad máxima de pallets anuales que puede manejar.
iii. (5 ptos.) Si usted pudiera variar el tamaño de la bodega, arrendando espacio a un costo de $E el Mt2 y pudiera variar la cantidad de personal. Plantee el problema de optimización para determinar el tamaño y dotación óptima.

B.- Usted debe determinar la profundidad óptima de los pallets en una bodega que tiene unos pasillos de 3.5 metros de ancho. Para ello considera una demanda constante y que los pallets tienen una medida de 1 × 1 metros. Usted recopila la información de los 4 SKU que maneja.

| SKU | # Pallets Demandados | Max. Altura de Apilado |
| :---: | :---: | :---: |
| A | 24 | 3 |
| B | 20 | 4 |
| C | 10 | 2 |
| D | 12 | 2 |

i. (3 ptos.) Determine la profundidad óptima para cada SKU individualmente.
ii. (3 ptos) Determine la profundidad óptima para todos en conjunto en el cual hay un pasillo y no se comparte. Muestre sus cálculos
iii. (4 ptos.) Si ahora puede tener 2 profundidades distintas y comparten el pasillo. ¿Cuáles serían estas profundidades? ¿Mejora el uso de espacio y por qué?

**Parte 1**
Los minutos anuales disponibles por operador = 60 * 8 * 250 = 120.000 minutos

Dado que tenemos 2800 mt2 de bodega, podemos almacenar 2.800 / 4 = 700 pallets

Como se demora 20 minutos en mover un pallet, son 6.000 pallets que puede mover al año, por ende 1 opear es capaz de rotar (6.000/700) = 8.57 rotaciones/año.

Si utilizamos la formula de flujo Q=A*v. Disponemos de la cantidad máxima de pallets a almacenar 700, por ende puedo manejar Q=700*8.57*12=71.988 pallets es lo máximo que puedo manejar

Si planteamos el modelo de optimización tenemos el espacio como variable (A) y los trabajadores (T) por ende nuestro modelo es minimizar el costo que permita manejar la demanda (D)

$$Min \ E \cdot A + 20.000 \cdot 12 \cdot T$$
$$Q = A_p \cdot v$$
$$v = 8.57 \cdot T$$
$$A_p = A/4$$
$$Q \geq D$$
$$A, T \geq 0$$

**Pregunta B**
Determinamos la profundidad optima de cada SKU individual, tomamos que el pallet comparte el pasillo. Es decir 3,5/1=3,5 unidades de pallet ocupa el pasillo. Por ende las profundidades optimas son:

| SKU | # Pallets Demandados | Max. Altura de Apilado | Prof. | Efectiva |
| :---: | :---: | :---: | :---: | :---: |
| A | 24 | 3 | 3,74165739 | 4 |
| B | 20 | 4 | 2,95803989 | 3 |
| C | 10 | 2 | 2,95803989 | 3 |
| D | 12 | 2 | 3,24037035 | 4 |

Si obtenemos la profundidad optima, ahora no se divide a por 2

| SKU | # Pallets Demandados | Max. Altura de Apilado | Espacio |
| :---: | :---: | :---: | :---: |
| A | 24 | 3 | 8 |
| B | 20 | 4 | 5 |
| C | 10 | 2 | 5 |
| D | 12 | 2 | 6 |
| | | **24** | |
| **Prof** | | **4,58257569** | |

Por ende para este caso la profundidad optima es 5. Ya que no se comparte el pasillo.

Observando los resultados individuales, es conveniente agrupar los SKU con profundidaddes parecidas, por ende colocamos juntos A y D y por otro lado B y C.
Esto da profundidades de:

| SKU | # Pallets Demandados | Max. Altura de Apilado | Espacio | | SKU | # Pallets Demandados | Max. Altura de Apilado | Espacio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | 24 | 3 | 8 | | B | 20 | 4 | 5 |
| D | 12 | 2 | 6 | | C | 10 | 2 | 5 |
| | | **14** | | | | | **10** | |
| **Prof**| | **3,5** | | | **Prof**| | **2,95803989** | |

Entrega una profundidad de 4 y otra de 3. El uso de espacio es más eficiente!

---

**P2 (20 puntos)** Usted se encuentra en el proceso de negociación para transformarse en un franquiciado de una empresa dedicada al rubro de comida rápida y en específico de hamburguesas. Realizando un estudio de mercado usted ha determinado que la demanda mensual por hamburguesas (Q) está dada por el precio al mercado de la hamburguesa (P), la cual está dada siguiente función de demanda P=150-0,5Q. Usted tiene dos costos variable relevantes: personal e infraestructura. Si el costo variable por hamburguesa es de $2 por concepto de personal y el de infraestructura es $3 por hamburguesa. Actualmente tiene dos ofertas de franquicias que quiere evaluar.
OPCION 1 “BurgerDon”: le ofrece un contrato en el cual le debe pagar un monto fijo anual de $12.000 y le ofrece venderle los insumos de cada hamburguesa a $12 por hamburguesa.
OPCION 2 “MacKing”: Le ofrece un contrato en el cual ellos le entregan toda la infraestructura y por ende ya no debe pagar este costo, pero le ofrece un contrato en el cual le pide el 50% de sus ventas y le vende los insumos de cada hamburguesa a $8 por unidad.
i. (10 puntos) Con esta información, como franquiciado, determine el precio al que vendería la hamburguesa con cada contrato ¿Qué contrato seleccionaría usted (Opción 1 u Opción 2) y por qué? Muestre todos sus cálculos.
ii. (10 puntos) Si usted determina que el costo de producción de cada hamburguesa para “BurgerDon” y “MacKing” es de $10 por hamburguesa. Para el contrato seleccionado en i) ¿Este contrato coordina o maximiza el valor para la cadena? ¿Cuál es la eficiencia de la cadena para el contrato? ¿Qué precio de venta de los insumos para la elaboración de la hamburguesa y qué monto fijo o porcentaje de ventas (dependiendo del contrato seleccionado) coordina o maximiza el valor de la cadena?

i.- Debemos determinar el precio de venta para cada contrato que maximice las utilidades.

OPCION 1
$$UT = Q(P - 5 - 10) = (300 - 2P)(P - 15) = 300P - 4500 - 2P^2 + 30P$$

Derivamos e igualamos a cero y Obtenemos que P es 82,5, eso lleva a que Q sea 135 y finalmente la utilidad total es 9112,5 mensual y como la franquicia se lleva 1000, la utilidad final es de 8112,5.

Opción 2
$$UT = Q \cdot (P \cdot 0,5 - 2 - 8) = (300 - 2P)(0,5P - 10) = 150P - 3000 - P^2 + 20P$$

Derivamos e igualamos a cero y Obtenemos que P es 85, eso lleva a que Q sea 130 , Las ventas totales son 11050, de lo cual el franquiciado se queda con el 50% 5525 y el costo es 10*130 = 1040 y por ende la utilidad para el franquiciado es de 4225
Prefiuere el contrato 1.

ii.- Debemos ver la cadena integrada

$$UT = Q \cdot (P - 2 - 3 - 10) = (300 - 2P)(P - 15) = 300P - 2250 - 2P^2 + 30P$$

Derivamos e igualamos a cero y Obtenemos que P es 82,5, eso lleva a que Q sea 135 y finalmente la utilidad total es 9112,5. Si lo comparamos con la opción 1 el contrato coordina la cadena. La eficiencia para la cadena completa es de un 100%. Por ende el monto seleccionado de $12.000 permite coordinar y es el único que debe implementarse.

---

**Formulario**

$$Q_w = \sqrt{\frac{2 C_0 D}{C_h}}$$

$$CT = DC + \frac{D}{Q}S + \frac{Q}{2}H$$

$$R = d \times L + z_\alpha \sigma \sqrt{L}$$

$$R = d \times L$$

$$Q^* = d \times (T + L) + z_\alpha \sigma \sqrt{(T + L)} - I_{existente}$$

$$C_x = \frac{\sum d_{ix} V_i}{\sum V_i}$$

$$C_y = \frac{\sum d_{iy} V_i}{\sum V_i}$$

$$c_T = \frac{\sigma}{t} = \frac{\sqrt{Var(T)}}{E(T)}$$

$$\rho = \frac{\lambda}{\mu}$$

$$\rho = \frac{\lambda}{c\mu}$$

$$L = \lambda \times W$$

$$c_T = \frac{\sigma}{t} = \frac{\sqrt{Var(T)}}{E(T)}$$

$$L = \frac{\rho}{1 - \rho}$$

$$W = \frac{1}{\mu(1 - \rho)}$$

$$L_q = \frac{\rho^2}{1 - \rho}$$

$$W_q = \frac{\rho}{\mu(1 - \rho)}$$

$$WIP = TH \times TC$$

$$L = \lambda * W$$

$$A = \frac{m_f}{m_r + m_f}$$

$$t_e = \frac{t_o}{A}$$

$$\sigma^2_e = \left(\frac{\sigma^2_o}{A}\right) + \frac{(m_r + \sigma^2_r)(1 - A)t_o}{A m_r}$$

$$c^2_e = \frac{\sigma^2_e}{t_e^2} = c^2_o + (1 + c^2_r)A(1 - A)\frac{m_r}{t_o}$$

$$t_e = t_o + \frac{t_s}{N_s}$$

$$\sigma^2_e = \sigma^2_o + \frac{\sigma^2_s}{N_s} + \frac{N_s - 1}{N_s^2} t^2_s$$

$$c^2_e = \frac{\sigma^2_e}{t_e^2}$$

$$CT_q = \left(\frac{c_a^2 + c_e^2}{2}\right)\left(\frac{\rho}{1 - \rho}\right) t_e$$

$$(c_S)^2 \approx \rho^2(c_e)^2 + (1 - \rho^2)(c_a)^2$$

$$L_q = \frac{\rho}{1 - \rho} \times Prob(N > c)$$

$$L = \frac{\rho}{1 - \rho} - \frac{(b + 1)\rho^{b+1}}{1 - \rho^{b+1}}$$

$$\lambda' = \lambda \left(\frac{1 - \rho^b}{1 - \rho^{b+1}}\right)$$

$$W_q = \frac{\rho}{\lambda(1 - \rho)} \times Prob(N > c)$$

---

**Tabla de distribución normal estándar**

| z | 0.00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.0** | .5000 | .5040 | .5080 | .5120 | .5160 | .5199 | .5239 | .5279 | .5319 | .5359 |
| **0.1** | .5398 | .5438 | .5478 | .5517 | .5557 | .5596 | .5636 | .5675 | .5714 | .5753 |
| **0.2** | .5793 | .5832 | .5871 | .5910 | .5948 | .5987 | .6026 | .6064 | .6103 | .6141 |
| **0.3** | .6179 | .6217 | .6255 | .6293 | .6331 | .6368 | .6406 | .6443 | .6480 | .6517 |
| **0.4** | .6554 | .6591 | .6628 | .6664 | .6700 | .6736 | .6772 | .6808 | .6844 | .6879 |
| **0.5** | .6915 | .6950 | .6985 | .7019 | .7054 | .7088 | .7123 | .7157 | .7190 | .7224 |
| **0.6** | .7257 | .7291 | .7324 | .7357 | .7389 | .7422 | .7454 | .7486 | .7517 | .7549 |
| **0.7** | .7580 | .7611 | .7642 | .7673 | .7704 | .7734 | .7764 | .7794 | .7823 | .7852 |
| **0.8** | .7881 | .7910 | .7939 | .7967 | .7995 | .8023 | .8051 | .8078 | .8106 | .8133 |
| **0.9** | .8159 | .8186 | .8212 | .8238 | .8264 | .8289 | .8315 | .8340 | .8365 | .8389 |
| **1.0** | .8413 | .8438 | .8461 | .8485 | .8508 | .8531 | .8554 | .8577 | .8599 | .8621 |
| **1.1** | .8643 | .8665 | .8686 | .8708 | .8729 | .8749 | .8770 | .8790 | .8810 | .8830 |
| **1.2** | .8849 | .8869 | .8888 | .8907 | .8925 | .8944 | .8962 | .8980 | .8997 | .9015 |
| **1.3** | .9032 | .9049 | .9066 | .9082 | .9099 | .9115 | .9131 | .9147 | .9162 | .9177 |
| **1.4** | .9192 | .9207 | .9222 | .9236 | .9251 | .9265 | .9279 | .9292 | .9306 | .9319 |
| **1.5** | .9332 | .9345 | .9357 | .9370 | .9382 | .9394 | .9406 | .9418 | .9429 | .9441 |
| **1.6** | .9452 | .9463 | .9474 | .9484 | .9495 | .9505 | .9515 | .9525 | .9535 | .9545 |
| **1.7** | .9554 | .9564 | .9573 | .9582 | .9591 | .9599 | .9608 | .9616 | .9625 | .9633 |
| **1.8** | .9641 | .9649 | .9656 | .9664 | .9671 | .9678 | .9686 | .9693 | .9699 | .9706 |
| **1.9** | .9713 | .9719 | .9726 | .9732 | .9738 | .9744 | .9750 | .9756 | .9761 | .9767 |
| **2.0** | .9772 | .9778 | .9783 | .9788 | .9793 | .9798 | .9803 | .9808 | .9812 | .9817 |
| **2.1** | .9821 | .9826 | .9830 | .9834 | .9838 | .9842 | .9846 | .9850 | .9854 | .9857 |
| **2.2** | .9861 | .9864 | .9868 | .9871 | .9875 | .4878 | .9881 | .9884 | .9887 | .9890 |
| **2.3** | .9893 | .9896 | .9898 | .9901 | .9904 | .9906 | .9909 | .9911 | .9913 | .9916 |
| **2.4** | .9918 | .9920 | .9922 | .9925 | .9927 | .9929 | .9931 | .9932 | .9934 | .9936 |
| **2.5** | .9938 | .9940 | .9941 | .9943 | .9945 | .9946 | .9948 | .9949 | .9951 | .9952 |
| **2.6** | .9953 | .9955 | .9956 | .9957 | .9959 | .9960 | .9961 | .9962 | .9963 | .9964 |
| **2.7** | .9965 | .9966 | .9967 | .9968 | .9969 | .9970 | .9971 | .9972 | .9973 | .9974 |
| **2.8** | .9974 | .9975 | .9976 | .9977 | .9977 | .9978 | .9979 | .9979 | .9980 | .9981 |
| **2.9** | .9981 | .9982 | .9982 | .9983 | .9984 | .9984 | .9985 | .9985 | .9986 | .9986 |
| **3.0** | .9987 | .9987 | .9987 | .9988 | .9988 | .9989 | .9989 | .9989 | .9990 | .9990 |
| **3.1** | .9990 | .9991 | .9991 | .9991 | .9992 | .9992 | .9992 | .9992 | .9993 | .9993 |
| **3.2** | .9993 | .9993 | .9994 | .9994 | .9994 | .9994 | .9994 | .9995 | .9995 | .9995 |
| **3.3** | .9995 | .9995 | .9995 | .9996 | .9996 | .9996 | .9996 | .9996 | .9996 | .9997 |
| **3.4** | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9998 |
