Nombre: _______________________________ email UC: ______________________ Sección:_____

# Pontificia Universidad Católica de Chile
## Escuela de Ingeniería
## Departamento de Ingeniería Industrial y de Sistemas

# Pauta Examen
# Enunciados

**ICS 3213 Gestión de Operaciones**
**Sección 1 y Sección 2 – 1er semestre 2020**
**Prof. Martin Garcia**
**Prof. Alejandro Mac Cawley**

**Instrucciones:**

* Responder en letra legible, en lápiz pasta o bolígrafo y poner nombre a todas las hojas.
* Responder las preguntas en orden e indicar claramente la pregunta (I, II o III).
* Esta sección de la prueba tiene 50 puntos, dura 50 minutos y consta de 3 preguntas.
* Se leerá la prueba al comienzo de clases y después se permitirán preguntas en voz alta. Posteriormente en la mitad de la prueba se volverá a permitir preguntas en voz alta. No se permitirán preguntas fuera de estos intervalos. Si su duda persiste indique el supuesto y continúe.
* Al final de la prueba los alumnos deberán mantener online y se dividirán los alumnos en distintos break rooms numeradas, cada una de las cuales tiene un ayudante o profesor a cargo. Dispondrán de 15 minutos para escanear pruebas hoja por hoja y subirlas. Para subir las pruebas, los alumnos deberán subir su prueba I2 en la web de CANVAS en la Tarea con el número de su breakup-room. Es decir, si fui asignado al breakup-room 1, debo subir mi I2 en la tarea que dice I2 Breakup-Room 1. Al final de los 15 minutos el ayudante o profesor revisara las pruebas en el sistema e indicara si están OK y se podrán desconectar. Si por alguna razón hay un problema al subir la prueba, podrán mandarla por mail al profesor.
* Este curso adscribe el Código de Honor establecido por la Escuela de Ingeniería el que es vinculante. Todo trabajo evaluado en este curso debe ser propio. En caso de que exista colaboración permitida con otros estudiantes, el trabajo deberá referenciar y atribuir correctamente dicha contribución a quien corresponda. Como estudiante es su deber conocer la versión en línea del Código de Honor (http://ing.puc.cl/codigodehonor).

¡Muy Buena Suerte

Página 1 de 6

---

Nombre: _______________________________ email UC: ______________________ Sección:_____

**Responda todas las siguientes preguntas cortas de ejercicio.**

**I. (15 puntos)** Se le ha encomendado el determinar la capacidad óptima del cuello de botella de un proceso productivo. El proceso se caracteriza por dos máquinas en serie: M1 y CB, en que CB es el cuello de botella, y que el producto pierde calidad desde que entra al proceso en M1 hasta que este no es ingresado a la maquina cuello de botella. A continuación, se detalla un esquema:

*(Diagrama: M1 (Capacidad: CM1 Min/Unid) $\rightarrow$ Espera $\rightarrow$ CB (Capacidad: CCB Min/Unid))*

Si por cada minuto que el producto espera a ser procesado por CB (Tanto en proceso en M1 como en la cola de espera) se pierden $CE pesos por minuto. Por otro lado, M1 requiere de CM1 minutos para terminar cada trabajo, con una distribución general del proceso y con un coeficiente de variación de VM1. La máquina cuello de botella tiene una capacidad inicial de CCB min/unidad pero se puede reducir el tiempo de procesamiento a un costo lineal $ICB pesos por cada minuto reducido. El CB tiene una distribución general del proceso y un coeficiente de variación del proceso de VCB, independiente de la capacidad. Si el tiempo medio de llegada entre las ordenes al proceso es de LL minutos entre orden, distribuidos general y con un coeficiente de variación de VLL. Con esta información construya un modelo de optimización que permita determinar la capacidad óptima del cuello de botella.
La variable de decisión es la cantidad de minutos que vamos a reducir el tiempo de procesamiento en CB, que se define como CMR minutos, y también la variable Tq que es el tiempo de espera entre M1 y CB

**S/A**
$$ \min [ CE * (Tq + CM1) + ICB * CMR ] $$

$$ Tq = (CCB - CMR) * \left( \frac{\rho}{1 - \rho} \right) * \left( \frac{CV_{M1}^2 + VCB^2}{2} \right) $$

$$ CV_{M1}^2 = VM1^2 \rho_1^2 + VLL^2(1 - \rho_1^2) $$

$$ 0 \leq CMR < CCB $$

$$ \rho = \frac{(CCB - CMR)}{LL} $$

$$ \rho_1 = \frac{CM1}{LL} $$

**II.** Usted decide controlar el proceso de producción de pan y decide hacer un esquema de muestra de 30 panes a los cuales les mide el peso en grms. Los resultados de los 27 grupos de muestra se detallan a continuación, con el respectivo promedio de cada muestra, recorrido, promedio de todas las muestras y recorrido; y finalmente la suma de todos los promedios y los recorridos:

| # | Promedio | Recorrido | # | Promedio | Recorrido | # | Promedio | Recorrido |
|---|---|---|---|---|---|---|---|---|
| 1 | 8,67 | 1,6 | 10 | 9,52 | 1,1 | 19 | 9,61 | 1,2 |
| 2 | 9,70 | 1,5 | 11 | 10,61 | 1,2 | 20 | 11,65 | 1,6 |
| 3 | 9,73 | 2 | 12 | 11,56 | 0,6 | 21 | 11,00 | 0,9 |
| 4 | 10,00 | 0,1 | 13 | 10,10 | 1,1 | 22 | 10,72 | 1,5 |
| 5 | 9,55 | 1,3 | 14 | 9,46 | 0,3 | 23 | 9,41 | 1,8 |
| 6 | 10,67 | 1,5 | 15 | 10,18 | 0 | 24 | 8,67 | 1,3 |
| 7 | 10,90 | 0 | 16 | 11,26 | 0,6 | 25 | 12,30 | 0 |
| 8 | 9,91 | 1,8 | 17 | 8,03 | 0,4 | 26 | 9,28 | 1,2 |
| 9 | 9,91 | 1,8 | 18 | 10,81 | 0,6 | 27 | 9,93 | 0,9 |

Usted también sabe que: $\sum promedios = 273,14$, $\sum recorrido = 27,9$, $\sum (promedios)^2 = 2788,03$
$\sum (recorrido)^2 = 38,67$ Hint: $\sigma^2 = \frac{1}{n} \sum (X^2) - \bar{X}^2 = E[X^2] - E[X]^2$

**a)** (10 ptos) Con esta información desarrolle los gráficos de control del proceso para un control 96%. 

Como son 30 muestras de panes y 27 grupos de muestra se utiliza normalidad. Utilizamos la fórmula de varianza = $2788,03/27 - (273,14/27)^2 = 0,921$. Promedio = $273,14/27 = 10,116$. Z para 98% = 2,05
Determinamos los limites de control superior e inferior $LCS = 10,116 + 2,05*\sqrt{0,978} = 12,084$, $LCI = 10,116 - 2,05*\sqrt{0,978} = 8,148$. 

Página 2 de 6

---

Nombre: _______________________________ email UC: ______________________ Sección:_____

Se elimina la muestra 25 y la 17. 
Se vuelven a calcular la suma de promedio = $273,14 - 8,03 - 12,3 = 251,81$ y Suma de cuadrados = $2788,03 - 8,03^2 - 12,3^2 = 2572,26$ 
Calculamos la varianza = $2572,26/25 - (251,81/25)^2 = 0,793$. Media = $251,81/25 = 10,112$
Determinamos los límites de control superior e inferior $LCS = 10,112 + 2,05*\sqrt{0,793} = 11,738$, $LCI = 10,112 - 2,05*\sqrt{0,793} = 8,486$. 

Todo se encuentra dentro de rango, por lo que esa serían los límites.

**III.** Usted es el representante de la nueva franquicia Burger Mac, la cual produce hamburguesas y recién se ha establecido en Chile. Usted esta tratando de determinar el “mejor” tipo de contrato con sus franquiciados, con el objetivo de alinear la cadena. Para ello, usted determina que la función de demanda mensual por hamburguesas que enfrenta cada local, la cual es P = 80-2Q, siendo P el precio de venta de la hamburguesa y Q la cantidad vendida. Los costos asociados a la operación de cada local ascienden a $4 por cada hamburguesa que se vende. Si para usted el costo de insumos de cada hamburguesa ascienden a $8. Determine:
a) (10 ptos) Si desea coordinar la cadena y ofrece un contrato de arriendo. ¿Cuál sería el precio mínimo de arriendo y el precio máximo que le podría cobrar al franquiciado? ¿Para el precio de arriendo mínimo y máximo, cuál sería la utilidad operacional del franquiciado, la suya y la de la cadena?
b) (5 ptos) Si desea coordinar la cadena y ofrece un contrato en que el franquiciado le entregue un 50% de sus ventas. ¿A qué precio y que cantidad de hamburguesas vendería el franquiciado? ¿A qué precio le vendería usted los insumos? ¿Cuál sería la utilidad del franquiciado, la suya y la de la cadena?
c) (5 ptos) Si usted coordina la cadena puede negociar un contrato de arriendo de $300 mensuales. ¿Qué contrato prefiere: arriendo ($300) o el 50% de las ventas? ¿Qué arriendo lo deja indiferente entre las dos opciones?

**a)** Debo primero calcular la cadena no coordinada para ver los limites inferiores de negociación. 
La función de demanda hay que dejarla en términos de Q. Q = 40 - P/2. Primero expresamos la función de utilidad del franquiciado: $UT(P) = Q*(P - 4 - w) = $ Reemplazamos en Q la función $UT(P) = (40 - P/2)*(P - 4 - w) = 40P - 160 + 40w - P^2/2 + 2P + Pw/2$. Derivamos con respecto a P y se obtiene = $40 - P + 2 + w/2$. Igualamos a 0 y obtenemos $P = 42 + w/2$.

Planteamos la función de la Franquicia = $Q(w - 8) = (40 - P/2)*(w - 8)$. Reemplazamos el P anterior. Se obtiene = $(40 - (42 + w/2)/2)*(w - 8) = (19 - w/4)*(w - 8) = 19w - 152 - w^2/4 + 2w$. Derivamos por w y se obtiene = $19 - w/2 + 2$. Igualamos a 0 y se obtiene $w = 42$. 

Ingresamos w en la función de P y se obtiene un P de 63 con eso se determina una cantidad Q de 8.5. Esto entrega una utilidad al franquiciado de $UTV = 8.5*(63 - 4 - 42) = 144.5$, la utilidad de la Franquicia es $UTF = 8.5*(42 - 8) = 289$. La utilidad de la cadena es 433.5 para el caso no coordinado.

Para la cadena integrada se determina la utilidad de su integración $UTI = Q(P - 4 - 8) = (40 - P/2)*(P - 12) = 40P - 480 - P^2/2 + 6P$. Derivamos por P y obtenemos $= 40 - P + 6$ igualamos a 0 y obtenemos $P = 46$ y $Q = 17$, eso lleva a que la utilidad de la cadena sea $17*(46 - 12) = 578$. Por ende, le debo vender el producto al costo al franquiciado, es decir a $8 y cobrarle un arriendo que vaya de un mínimo de $289 (Que sería mi utilidad) y el franquiciado tendría una utilidad de $289 hasta un máximo de $(578 - 144.5) = $433.5 que sería mi utilidad y la del franquiciado sería de 144.5.

**b)** Al establecer un esquema de porcentaje de las ventas, se debe vender a bajo el costo, a un valor w = $\alpha*c$. Por ende el valor de venta sería $0,5*8 = 4$. Si utilizamos este valor en la función del franquiciado quedaría de la siguiente forma $UT(P) = (40 - P/2)*(P - 4 - 4) = 40P - 320 - P^2/2 + 4P$. Si derivamos obtenemos $40 - P + 4 = 0$ por ende $P = 44$. Esto lleva a que el Q sea 18. Por ende, la venta del retailer es $18*44 = 792$. De esto el dueño de la franquicia recibe $396 y debe “pagar” 18*4 por vender bajo el costo = $ 324. La utilidad final del franquiciado seria $792 - 396 - 18*8 = 252$. La utilidad de la cadena es $576. Como es posible ver el total se reduce levemente de $578 a $576.

**c)** Usted prefiere el contrato de porcentaje de ventas, ya que recibe $324 mientras que en el contrato de arriendo recibe solo una utilidad de $300. Debria pedir un arriendo de $324 para ser indiferente.

Página 3 de 6

---

Nombre: _______________________________ email UC: ______________________ Sección:_____

# Formulario

$$ P(Z \leq z) = \int_{-\infty}^{z} f(t) dt $$

**Tabla de distribución normal estándar**

| z | 0.00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.0 | .5000 | .5040 | .5080 | .5120 | .5160 | .5199 | .5239 | .5279 | .5319 | .5359 |
| 0.1 | .5398 | .5438 | .5478 | .5517 | .5557 | .5596 | .5636 | .5675 | .5714 | .5753 |
| 0.2 | .5793 | .5832 | .5871 | .5910 | .5948 | .5987 | .6026 | .6064 | .6103 | .6141 |
| 0.3 | .6179 | .6217 | .6255 | .6293 | .6331 | .6368 | .6406 | .6443 | .6480 | .6517 |
| 0.4 | .6554 | .6591 | .6628 | .6664 | .6700 | .6736 | .6772 | .6808 | .6844 | .6879 |
| 0.5 | .6915 | .6950 | .6985 | .7019 | .7054 | .7088 | .7123 | .7157 | .7190 | .7224 |
| 0.6 | .7257 | .7291 | .7324 | .7357 | .7389 | .7422 | .7454 | .7486 | .7517 | .7549 |
| 0.7 | .7580 | .7611 | .7642 | .7673 | .7704 | .7734 | .7764 | .7794 | .7823 | .7852 |
| 0.8 | .7881 | .7910 | .7939 | .7967 | .7995 | .8023 | .8051 | .8078 | .8106 | .8133 |
| 0.9 | .8159 | .8186 | .8212 | .8238 | .8264 | .8289 | .8315 | .8340 | .8365 | .8389 |
| 1.0 | .8413 | .8438 | .8461 | .8485 | .8508 | .8531 | .8554 | .8577 | .8599 | .8621 |
| 1.1 | .8643 | .8665 | .8686 | .8708 | .8729 | .8749 | .8770 | .8790 | .8810 | .8830 |
| 1.2 | .8849 | .8869 | .8888 | .8907 | .8925 | .8944 | .8962 | .8980 | .8997 | .9015 |
| 1.3 | .9032 | .9049 | .9066 | .9082 | .9099 | .9115 | .9131 | .9147 | .9162 | .9177 |
| 1.4 | .9192 | .9207 | .9222 | .9236 | .9251 | .9265 | .9279 | .9292 | .9306 | .9319 |
| 1.5 | .9332 | .9345 | .9357 | .9370 | .9382 | .9394 | .9406 | .9418 | .9429 | .9441 |
| 1.6 | .9452 | .9463 | .9474 | .9484 | .9495 | .9505 | .9515 | .9525 | .9535 | .9545 |
| 1.7 | .9554 | .9564 | .9573 | .9582 | .9591 | .9599 | .9608 | .9616 | .9625 | .9633 |
| 1.8 | .9641 | .9649 | .9656 | .9664 | .9671 | .9678 | .9686 | .9693 | .9699 | .9706 |
| 1.9 | .9713 | .9719 | .9726 | .9732 | .9738 | .9744 | .9750 | .9756 | .9761 | .9767 |
| 2.0 | .9772 | .9778 | .9783 | .9788 | .9793 | .9798 | .9803 | .9808 | .9812 | .9817 |
| 2.1 | .9821 | .9826 | .9830 | .9834 | .9838 | .9842 | .9846 | .9850 | .9854 | .9857 |
| 2.2 | .9861 | .9864 | .9868 | .9871 | .9875 | .4878 | .9881 | .9884 | .9887 | .9890 |
| 2.3 | .9893 | .9896 | .9898 | .9901 | .9904 | .9906 | .9909 | .9911 | .9913 | .9916 |
| 2.4 | .9918 | .9920 | .9922 | .9925 | .9927 | .9929 | .9931 | .9932 | .9934 | .9936 |
| 2.5 | .9938 | .9940 | .9941 | .9943 | .9945 | .9946 | .9948 | .9949 | .9951 | .9952 |
| 2.6 | .9953 | .9955 | .9956 | .9957 | .9959 | .9960 | .9961 | .9962 | .9963 | .9964 |
| 2.7 | .9965 | .9966 | .9967 | .9968 | .9969 | .9970 | .9971 | .9972 | .9973 | .9974 |
| 2.8 | .9974 | .9975 | .9976 | .9977 | .9977 | .9978 | .9979 | .9979 | .9980 | .9981 |
| 2.9 | .9981 | .9982 | .9982 | .9983 | .9984 | .9984 | .9985 | .9985 | .9986 | .9986 |
| 3.0 | .9987 | .9987 | .9987 | .9988 | .9988 | .9989 | .9989 | .9989 | .9990 | .9990 |
| 3.1 | .9990 | .9991 | .9991 | .9991 | .9992 | .9992 | .9992 | .9992 | .9993 | .9993 |
| 3.2 | .9993 | .9993 | .9994 | .9994 | .9994 | .9994 | .9994 | .9995 | .9995 | .9995 |
| 3.3 | .9995 | .9995 | .9995 | .9996 | .9996 | .9996 | .9996 | .9996 | .9996 | .9997 |
| 3.4 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9997 | .9998 |

**Formulario**

$$ CT = DC + \frac{D}{Q} S + \frac{Q}{2} H $$

$$ Q^* = F^{-1} \left( \frac{C_u}{c_o + C_u} \right) $$

$$ EF = ES + t $$
$$ LS = LF - t $$

$$ Q_{eoq} = \sqrt{\frac{2 \times D \times S}{H}} $$

$$ R = d \times L $$

$$ \mu = \frac{a + 4m + b}{6} \quad \sigma = \frac{b - a}{6} \quad Z = \frac{D - T_E}{\sqrt{\sum \sigma_i^2}} $$

$$ R = d \times L + z_\alpha \sigma \sqrt{L} $$

Página 4 de 6

---

Nombre: _______________________________ email UC: ______________________ Sección:_____

$$ Q^* = d \times (T + L) + z_\alpha \sigma \sqrt{(T + L)} - I_{\text{existente}} $$
$$ Q = T_P \times p $$
$$ I = T_P \times (p - d) $$
$$ T_P = \frac{Q}{p} $$

$$ P = \sqrt{ \binom{a}{2} \binom{q}{z} } \quad P = \sqrt{ \binom{a}{2} \binom{1}{n} \left( \sum_{i=1}^n \frac{q_i}{z_i} \right) } \quad ef = \frac{k}{k + 1} $$

$$ Ben = sp_i - c_r d_i \quad Ben = s(p_i + D_i) $$

$$ Beneficio_{min\_A} = \frac{s * p_i - c_r * d_i}{l_i} \quad Restocks = \frac{f_i}{V_i} \quad \text{Restocks/tiempo} $$

$$ Beneficio_{adic\_A} = \frac{s * D_i + c_r * d_i}{u_i - l_i} \quad \text{Costo Total} = \text{Costo Fijo} + \text{Costo Variable} \times \text{Volumen} $$

$$ v_i^* = \left( \frac{\sqrt{f_i}}{\sum_{j=1}^n \sqrt{f_j}} \right) V \quad \frac{p_i}{\sqrt{fi}} \quad Cx = \frac{\sum d_{ix} V_i}{\sum V_i} \quad Cy = \frac{\sum d_{iy} V_i}{\sum V_i} $$

$$ \rho = \frac{\lambda}{\mu} \quad \rho = \frac{\lambda}{c\mu} \quad L = \lambda \times W \quad c_T = \frac{\sigma}{t} = \frac{\sqrt{Var(T)}}{E(T)} $$

$$ L = \frac{\rho}{1 - \rho} , \quad W = \frac{1}{\mu(1 - \rho)} \quad L_q = \frac{\rho^2}{1 - \rho} , \quad W_q = \frac{\rho}{\mu(1 - \rho)} $$

$$ WIP = TH \times TC \quad L = \lambda * W $$

$$ A = \frac{m_f}{m_r + m_f} \quad t_e = \frac{t_o}{A} \quad \sigma_e^2 = \left( \frac{\sigma_o^2}{A} \right) + \frac{(m_r + \sigma_r^2)(1 - A)t_o}{A m_r} $$

$$ c_e^2 = \frac{\sigma_e^2}{t_e^2} = c_o^2 + (1 + c_r^2)A(1 - A) \frac{m_r}{t_o} $$

$$ t_e = t_o + \frac{t_s}{N_s} \quad \sigma_e^2 = \sigma_o^2 + \frac{\sigma_s^2}{N_s} + \frac{N_s - 1}{N_s^2} t_s^2 \quad c_e^2 = \frac{\sigma_e^2}{t_e^2} $$

$$ (c_S)^2 \approx \rho^2(c_e)^2 + (1 - \rho^2)(c_a)^2 \quad CT_q = \underbrace{\left( \frac{C_a^2 + C_e^2}{2} \right)}_{V} \underbrace{\left( \frac{\rho}{1 - \rho} \right)}_{U} \underbrace{t_e}_{T} $$

$$ L = \frac{\rho}{1 - \rho} - \frac{(b + 1)\rho^{b+1}}{1 - \rho^{b+1}} \quad \lambda' = \lambda \left( \frac{1 - \rho^b}{1 - \rho^{b+1}} \right) $$

Página 5 de 6

---

Nombre: _______________________________ email UC: ______________________ Sección:_____

$$ L_q = \frac{\rho}{1 - \rho} \times Prob(N > c) \quad W_q = \frac{\rho}{\lambda(1 - \rho)} \times Prob(N > c) $$

$$ F_t = w_1 A_{t-1} + w_2 A_{t-2} + w_3 A_{t-3} + \dots + w_n A_{t-n} \quad T(t, t-1) = A_t - A_{t-1} $$
$$ F_{t+1} = \alpha A_t + (1 - \alpha) F_t \quad \hat{y} = a + bx \quad \sum_{i=1}^n w_n = 1 \quad T = \frac{\sum_{i=1}^n T(t-i, t-i-1)}{n} $$

$$ TS_k = \frac{\sum_{t=1}^k e_t}{MAD_k} \quad F_t = \frac{A_{t-1} + A_{t-2} + A_{t-3} + \dots + A_{t-n}}{n} \quad e_t = F_t - A_t $$
$$ \sigma = 1,25 * MAD \quad MAD_k = \frac{1}{k} \sum_{t=1}^k |e_t| \quad b = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2} $$

$$ FIT_t = \underbrace{F_t}_{\text{Pronóstico}} + \underbrace{T_t}_{\text{Tendencia}} \quad L = t_k + t_p + t_v \quad a = \frac{\sum y}{n} - b \frac{\sum x}{n} = \bar{y} - b\bar{x} $$

$$ F_t = FIT_{t-1} + \alpha(A_{t-1} - FIT_{t-1}) $$
$$ T_t = T_{t-1} + \alpha\delta(A_{t-1} - FIT_{t-1}) \quad LCS = \bar{x} + Z * \sigma \quad N = \frac{D \times L}{C} $$
$$ LCI = \bar{x} - Z * \sigma $$

$$ N = \frac{D \times L}{C} (1 + \varepsilon) $$

| c | LTPD/AQL | n*AQL |
|---|---|---|
| 0 | 44,890 | 0,052 |
| 1 | 10,946 | 0,355 |
| 2 | 6,509 | 0,818 |
| 3 | 4,890 | 1,366 |
| 4 | 4,057 | 1,97 |
| 5 | 3,549 | 2,613 |
| 6 | 3,206 | 3,286 |
| 7 | 2,957 | 3,981 |
| 8 | 2,768 | 4,695 |
| 9 | 2,618 | 5,426 |

$$ p_0 \pm 3 \sqrt{\frac{p_0(1 - p_0)}{n}} $$

$$ C_p = \frac{USL - LSL}{6\sigma} $$

$$ LCS\ \bar{X} = \bar{\bar{X}} + A_2 * \bar{R} $$
$$ LCI\ \bar{X} = \bar{\bar{X}} - A_2 * \bar{R} $$
$$ LCS\ R = D_4 * \bar{R} $$
$$ LCI\ R = D_3 * \bar{R} $$

$$ C_{pk} = \frac{USL - Media}{3\sigma} $$
$$ C_{pk} = \frac{Media - LSL}{3\sigma} $$

| Tamano Muestra | A2 | d2 | D3 | D4 |
|---|---|---|---|---|
| 2 | 1.880 | 1.128 | 0 | 3.267 |
| 3 | 1.023 | 1.693 | 0 | 2.574 |
| 4 | 0.729 | 2.059 | 0 | 2.282 |
| 5 | 0.577 | 2.326 | 0 | 2.114 |
| 6 | 0.483 | 2.534 | 0 | 2.004 |
| 7 | 0.419 | 2.704 | 0.076 | 1.924 |
| 8 | 0.373 | 2.847 | 0.136 | 1.864 |
| 9 | 0.337 | 2.970 | 0.184 | 1.816 |
| 10 | 0.308 | 3.078 | 0.223 | 1.777 |
| 11 | 0.285 | 3.173 | 0.256 | 1.744 |
| 12 | 0.266 | 3.258 | 0.283 | 1.717 |
| 13 | 0.249 | 3.336 | 0.307 | 1.693 |
| 14 | 0.235 | 3.407 | 0.328 | 1.672 |
| 15 | 0.223 | 3.472 | 0.347 | 1.653 |
| 16 | 0.212 | 3.532 | 0.363 | 1.637 |
| 17 | 0.203 | 3.588 | 0.378 | 1.622 |
| 18 | 0.194 | 3.640 | 0.391 | 1.608 |
| 19 | 0.187 | 3.689 | 0.403 | 1.597 |
| 20 | 0.180 | 3.735 | 0.415 | 1.585 |
| 21 | 0.173 | 3.778 | 0.425 | 1.575 |
| 22 | 0.167 | 3.819 | 0.434 | 1.566 |
| 23 | 0.162 | 3.858 | 0.443 | 1.557 |
| 24 | 0.157 | 3.895 | 0.451 | 1.548 |
| 25 | 0.153 | 3.931 | 0.459 | 1.541 |

Página 6 de 6
