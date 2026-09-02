# Interrogación 2 — Gestión de Operaciones (ICS3213)
## Semestre: 1er Semestre 2026
**Profesores:** Alejandro Mac Cawley
**Escuela de Ingeniería, Pontificia Universidad Católica de Chile**

---

### Instrucciones:
* Responder en letra legible, en lápiz pasta o bolígrafo y poner nombre a todas las hojas.
* No debe descorchetear la prueba y responda en el espacio asignado.
* Esta sección de la prueba tiene 60 puntos, dura 60 minutos.
* Se leerá la prueba al comienzo de clases y después se permitirán preguntas en voz alta. Posteriormente en la mitad de la prueba se volverá a permitir preguntas en voz alta. No se permitirán preguntas fuera de estos intervalos. Si su duda persiste indique el supuesto y continúe.
* Al final de la prueba los alumnos deberán subir su prueba a CANVAS. Dispondrán de 15 minutos para escanear pruebas hoja por hoja y subirlas. Al final de subir la prueba deberán dejarla en el mismo puesto. Si por alguna razón hay un problema al subir la prueba, avisen al profesor/ayudante y dejen su prueba.
* Este curso adscribe el Código de Honor establecido por la Escuela de Ingeniería el que es vinculante. Todo trabajo evaluado en este curso debe ser propio. En caso de que exista colaboración permitida con otros estudiantes, el trabajo deberá referenciar y atribuir correctamente dicha contribución a quien corresponda. Como estudiante es su deber conocer la versión en línea del Código de Honor (http://ing.puc.cl/codigodehonor).

---

## PARTE DESARROLLO (60 Puntos)

### Pregunta 1: Planificación Agregada y MRP (20 Puntos)

Usted es el analista de operaciones de **AgriDrone S.A.**, una empresa ensambladora de drones para monitoreo agrícola. Se le ha encargado conectar la planificación de mediano plazo de la familia de drones con las órdenes de compra de corto plazo para un componente crítico importado: el **Módulo de Cámara Multiespectral (MCM)**.

#### Datos de Planificación Agregada:
* **Demanda agregada proyectada** para la familia de drones para el último trimestre del año:
  * **Octubre:** 800 unidades
  * **Noviembre:** 1.200 unidades
  * **Diciembre:** 1.600 unidades
* **Estrategia a seguir:** "Nivelación" (Fuerza de trabajo constante).
* **Productividad de cada trabajador:** 10 drones terminados por semana. (Se asume un mes de exactamente 4 semanas para todos los meses, totalizando 12 semanas en el trimestre).
* **Costo de mantener inventario:** $50 dólares por dron al mes (se cobra sobre el inventario final de cada mes).
* **Inventario inicial** a fines de septiembre: 0 unidades.
* **Faltantes (backorders):** No se permiten faltantes al final del trimestre.

#### Datos de Planificación MRP:
* El **modelo estrella** de la compañía representa exactamente el **50%** de la producción total agregada.
* Para la planificación semanal, se asume que la producción de este modelo estrella se distribuye uniformemente durante las 4 semanas de cada mes en el Programa Maestro de Producción (MPS).
* Para ensamblar cada dron estrella se requiere exactamente **1 unidad** del componente Módulo de Cámara Multiespectral (MCM).
* El registro de inventarios para el MCM indica lo siguiente al iniciar octubre:
  * **Inventario Inicial:** 50 unidades.
  * **Tiempo de Espera (Lead Time):** 2 semanas.
  * **Recepciones Programadas:** 200 unidades que llegarán al inicio de la Semana 1.
  * **Política de Tamaño de Lote:** Lote a Lote (L4L).

#### Se pide:
* **i.** (6 ptos) Determine el plan agregado mensual de producción requerida bajo la estrategia de Nivelación. Determine la cantidad de personal y calcule el costo total de mantención de inventario para el trimestre (octubre-diciembre). Muestre sus cálculos.
* **ii.** (9 ptos) Tomando los resultados de su plan agregado (calculado anteriormente) para el mes de octubre, desarrolle la tabla MRP de las semanas 1 a 4 de dicho mes para el componente MCM. Indique claramente en qué semanas deben emitirse las expediciones de Pedidos Planeados (*Planned Order Releases*).
* **iii.** (5 ptos) El Gerente de Finanzas está alarmado por la cantidad de órdenes de compra independientes que se están emitiendo bajo la política Lote a Lote (L4L) y le exige cambiar a una política de Cantidad Económica de Pedido (EOQ) utilizando la demanda total del trimestre para calcular un tamaño fijo de lote. Basándose en la teoría de gestión de inventarios y MRP, fundamente cuál es el principal problema matemático o ineficiencia al usar el modelo EOQ clásico en un sistema MRP, y qué algoritmo de lotificación alternativo le recomendaría utilizar en su lugar. No determine los lotes, sólo explique los fundamentos que lo llevan a su decisión.

---

### Pregunta 2: Administración de Proyectos PERT/CPM (20 Puntos)

Una empresa llamada **Redd SpA** de distribución y comercio electrónico está evaluando la ejecución de un proyecto para implementar un nuevo sistema de gestión logística. El objetivo del proyecto es mejorar la trazabilidad de pedidos, reducir errores de despacho y aumentar la velocidad de respuesta hacia los clientes.

El proyecto se desarrollará por etapas, considerando las actividades técnicas, operativas y de capacitación interna. Dado que la empresa debe comprometer una fecha de entrega con la gerencia comercial y con sus principales clientes, se solicita realizar un análisis preliminar del proyecto.

La relación de dependencias entre las actividades y los tiempos estimados de duración, medidos en semanas, se presentan a continuación:

| Actividad | Predecesor | Tiempo Medio | Desv. Estándar |
| :---: | :---: | :---: | :---: |
| **A** | - | 3 | 0.667 |
| **B** | A | 5 | 0.667 |
| **C** | A | 4 | 1.000 |
| **D** | B | 6 | 1.333 |
| **E** | B, C | 5 | 0.667 |
| **F** | C | 7 | 1.000 |
| **G** | D, E | 4 | 0.667 |
| **H** | F, G | 3 | 0.333 |

#### Se pide:
* **i.** (8 ptos) Dibuje el diagrama PERT asociado al proyecto, respetando las relaciones de precedencia indicadas, determinando la Ruta Crítica, $E[T]$ y $\text{Var}[T]$.
* **ii.** (5 ptos) Determine la probabilidad de que el proyecto sea completado en 23 semanas y construya un intervalo de confianza al 95% (Con dos colas) para la duración del proyecto.
* **iii.** (4 ptos) La gerencia comercial de Redd SpA evalúa comprometer una fecha de entrega de 23 semanas para la implementación del nuevo sistema de gestión logística. Para incentivar el cumplimiento anticipado, se establece un bono de $1.5 millones si el proyecto termina en o antes del tiempo medio. Sin embargo, si el proyecto termina después de las 23 semanas, la empresa deberá pagar una penalización fija de $4 millones. ¿Aceptaría usted esta propuesta? Muestre sus cálculos y justifique su respuesta.
* **iv.** (3 ptos) Si el bono es ahora de $1.5 millones por cada semana de adelanto respecto a la fecha del tiempo medio y la penalización es de $4 millones por cada semana de atraso después de las 23 semanas. ¿Cómo cambia su respuesta anterior? Plantee la condición matemática que debe cumplirse para aceptar el contrato. No la desarrolle.

Nota: Recordar que la función de densidad de la normal estándar es: $\phi(t) = \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2}{2}}$

---

### Pregunta 3: Gestión de Capacidad y Variabilidad (20 Puntos)

Usted está a cargo de una oficina del Registro Civil y debe velar por el servicio que se entrega. Actualmente llegan a la oficina **20 personas por hora** a hacer sus trámites y este tiempo se distribuye de forma general, con un coeficiente de variación de los arribos $C_a = 0.5$.

Usted analiza el tiempo de atención y encuentra que, en promedio, las atenciones demoran **2.4 minutos** y se distribuyen también de forma general, con un coeficiente de variación del servicio $C_s = 1.5$.

#### Con esta información usted debe responder:
* **a)** (6 ptos) ¿Cuál es el nivel de utilización de la oficina? ¿Cuánto espera la gente en la cola para hacer el trámite? ¿Cuál debería ser el tamaño (número de asientos) promedio de la sala de espera?
* **b)** (7 ptos) Usted desea que los clientes no esperen más de 6 minutos en la cola para hacer el trámite y para ello piensa implementar un sistema de agenda digital y hacer agendamientos en bloques de 1 hora. ¿Cuántos clientes puede agendar por hora?
* **c)** (7 ptos) Para la situación inicial, usted debe decidir qué mejora hacer en el servicio. Usted tiene las siguientes dos opciones de mejora:
  * **i.** Realizar capacitación al personal y reducir el coeficiente de variación del servicio $C_s$ a $1.0$ a un costo total de $4,000.
  * **ii.** Digitalizar algunos servicios, lo que conllevaría a disminuir la tasa de llegada de personas a **15 personas por hora** con un costo total de $6,000.
  
  Si por cada minuto que reduce en la cola se genera un beneficio de $1,000. ¿Cuál de las dos opciones prefiere? Muestre sus cálculos.

---

## Formulario de Referencia

* **Aproximación de Kingman (Cola G/G/1):**
  $$W_q = \left( \frac{C_a^2 + C_s^2}{2} \right) \left( \frac{\rho}{1 - \rho} \right) \left( \frac{1}{\mu} \right)$$
* **Ecuación de Little:**
  $$L_q = \lambda \cdot W_q, \quad L = \lambda \cdot W$$
* **Estadístico Z (PERT):**
  $$Z = \frac{D - \sum_{i \in \text{RC}} E[T_i]}{\sqrt{\sum_{i \in \text{RC}} \text{Var}[T_i]}}$$

---

## Tabla de Distribución Normal Estándar

La tabla muestra el valor de la probabilidad acumulada $\Phi(z) = P(Z \le z)$.

| $z$ | 0.00 | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 | 0.06 | 0.07 | 0.08 | 0.09 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.0** | 0.5000 | 0.5040 | 0.5080 | 0.5120 | 0.5160 | 0.5199 | 0.5239 | 0.5279 | 0.5319 | 0.5359 |
| **0.1** | 0.5398 | 0.5438 | 0.5478 | 0.5517 | 0.5557 | 0.5596 | 0.5636 | 0.5675 | 0.5714 | 0.5753 |
| **0.2** | 0.5793 | 0.5832 | 0.5871 | 0.5910 | 0.5948 | 0.5987 | 0.6026 | 0.6064 | 0.6103 | 0.6141 |
| **0.3** | 0.6179 | 0.6217 | 0.6255 | 0.6293 | 0.6331 | 0.6368 | 0.6406 | 0.6443 | 0.6480 | 0.6517 |
| **0.4** | 0.6554 | 0.6591 | 0.6628 | 0.6664 | 0.6700 | 0.6736 | 0.6772 | 0.6808 | 0.6844 | 0.6879 |
| **0.5** | 0.6915 | 0.6950 | 0.6985 | 0.7019 | 0.7054 | 0.7088 | 0.7123 | 0.7157 | 0.7190 | 0.7224 |
| **0.6** | 0.7257 | 0.7291 | 0.7324 | 0.7357 | 0.7389 | 0.7422 | 0.7454 | 0.7486 | 0.7517 | 0.7549 |
| **0.7** | 0.7580 | 0.7611 | 0.7642 | 0.7673 | 0.7704 | 0.7734 | 0.7764 | 0.7794 | 0.7823 | 0.7852 |
| **0.8** | 0.7881 | 0.7910 | 0.7939 | 0.7967 | 0.7995 | 0.8023 | 0.8051 | 0.8078 | 0.8106 | 0.8133 |
| **0.9** | 0.8159 | 0.8186 | 0.8212 | 0.8238 | 0.8264 | 0.8289 | 0.8315 | 0.8340 | 0.8365 | 0.8389 |
| **1.0** | 0.8413 | 0.8438 | 0.8461 | 0.8485 | 0.8508 | 0.8531 | 0.8554 | 0.8577 | 0.8599 | 0.8621 |
| **1.1** | 0.8643 | 0.8665 | 0.8686 | 0.8708 | 0.8729 | 0.8749 | 0.8770 | 0.8790 | 0.8810 | 0.8830 |
| **1.2** | 0.8849 | 0.8869 | 0.8888 | 0.8907 | 0.8925 | 0.8944 | 0.8962 | 0.8980 | 0.8997 | 0.9015 |
| **1.3** | 0.9032 | 0.9049 | 0.9066 | 0.9082 | 0.9099 | 0.9115 | 0.9131 | 0.9147 | 0.9162 | 0.9177 |
| **1.4** | 0.9192 | 0.9207 | 0.9222 | 0.9236 | 0.9251 | 0.9265 | 0.9279 | 0.9292 | 0.9306 | 0.9319 |
| **1.5** | 0.9332 | 0.9345 | 0.9357 | 0.9370 | 0.9382 | 0.9394 | 0.9406 | 0.9418 | 0.9429 | 0.9441 |
| **1.6** | 0.9452 | 0.9463 | 0.9474 | 0.9484 | 0.9495 | 0.9505 | 0.9515 | 0.9525 | 0.9535 | 0.9545 |
| **1.7** | 0.9554 | 0.9564 | 0.9573 | 0.9582 | 0.9591 | 0.9599 | 0.9608 | 0.9616 | 0.9625 | 0.9633 |
| **1.8** | 0.9641 | 0.9649 | 0.9656 | 0.9664 | 0.9671 | 0.9678 | 0.9686 | 0.9693 | 0.9699 | 0.9706 |
| **1.9** | 0.9713 | 0.9719 | 0.9726 | 0.9732 | 0.9738 | 0.9744 | 0.9750 | 0.9756 | 0.9761 | 0.9767 |
| **2.0** | 0.9772 | 0.9778 | 0.9783 | 0.9788 | 0.9793 | 0.9798 | 0.9803 | 0.9808 | 0.9812 | 0.9817 |
| **2.1** | 0.9821 | 0.9826 | 0.9830 | 0.9834 | 0.9838 | 0.9842 | 0.9846 | 0.9850 | 0.9854 | 0.9857 |
| **2.2** | 0.9861 | 0.9864 | 0.9868 | 0.9871 | 0.9875 | 0.9878 | 0.9881 | 0.9884 | 0.9887 | 0.9890 |
| **2.3** | 0.9893 | 0.9896 | 0.9898 | 0.9901 | 0.9904 | 0.9906 | 0.9909 | 0.9911 | 0.9913 | 0.9916 |
| **2.4** | 0.9918 | 0.9920 | 0.9922 | 0.9925 | 0.9927 | 0.9929 | 0.9931 | 0.9932 | 0.9934 | 0.9936 |
| **2.5** | 0.9938 | 0.9940 | 0.9941 | 0.9943 | 0.9945 | 0.9946 | 0.9948 | 0.9949 | 0.9951 | 0.9952 |
| **2.6** | 0.9953 | 0.9955 | 0.9956 | 0.9957 | 0.9959 | 0.9960 | 0.9961 | 0.9962 | 0.9963 | 0.9964 |
| **2.7** | 0.9965 | 0.9966 | 0.9967 | 0.9968 | 0.9969 | 0.9970 | 0.9971 | 0.9972 | 0.9973 | 0.9974 |
| **2.8** | 0.9974 | 0.9975 | 0.9976 | 0.9977 | 0.9977 | 0.9978 | 0.9979 | 0.9979 | 0.9980 | 0.9981 |
| **2.9** | 0.9981 | 0.9982 | 0.9982 | 0.9983 | 0.9984 | 0.9984 | 0.9985 | 0.9985 | 0.9986 | 0.9986 |
| **3.0** | 0.9987 | 0.9987 | 0.9987 | 0.9988 | 0.9988 | 0.9989 | 0.9989 | 0.9989 | 0.9990 | 0.9990 |
| **3.1** | 0.9990 | 0.9991 | 0.9991 | 0.9991 | 0.9992 | 0.9992 | 0.9992 | 0.9992 | 0.9993 | 0.9993 |
| **3.2** | 0.9993 | 0.9993 | 0.9994 | 0.9994 | 0.9994 | 0.9994 | 0.9994 | 0.9995 | 0.9995 | 0.9995 |
| **3.3** | 0.9995 | 0.9995 | 0.9995 | 0.9996 | 0.9996 | 0.9996 | 0.9996 | 0.9996 | 0.9996 | 0.9997 |
| **3.4** | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9998 |
