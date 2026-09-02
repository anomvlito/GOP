# Soluciones - Ayudantías para examen

Fuente: `ayudantias/ayudantias_para_examen/*.pdf`.

Notas de uso:

- `Ayudantía_11.pdf` y `Ayudantía_11-1.pdf` son duplicados textuales; se resuelve una sola vez.
- En Ayudantía 10, Problema 2, la tabla y el agregado impreso `sum x_i^2` no coinciden. Para la pauta se privilegia el criterio de la pauta manuscrita, que identifica como fuera de control las muestras 20, 23 y 24.
- En problemas con convenciones no especificadas, se explicita el supuesto usado.

---

## Ayudantía 10 - Bodegas y Calidad

### Problema 1

Para asignar espacio al área de picking rápido se usa la regla de asignación proporcional a la raíz:

$$
v_i = V \frac{\sqrt{p_i f_i}}{\sum_j \sqrt{p_j f_j}},
\qquad
f_i = \frac{\text{unidades/mes}}{\text{unidades/caja}} \cdot \text{m}^3/\text{caja}.
$$

Los flujos volumétricos mensuales son:

| SKU | Picks/mes | Flujo \(f_i\) m3/mes | \(\sqrt{p_i f_i}\) | Espacio \(v_i\) m3 |
|---|---:|---:|---:|---:|
| A | 780 | 828.00 | 803.64 | 764.41 |
| B | 610 | 270.59 | 406.27 | 386.44 |
| C | 300 | 572.73 | 414.51 | 394.27 |
| D | 480 | 290.00 | 373.10 | 354.88 |

Por lo tanto, la asignación recomendada es:

$$
(v_A,v_B,v_C,v_D)=(764.41,\ 386.44,\ 394.27,\ 354.88)\ \text{m}^3.
$$

La frecuencia individual de reposición, medida en meses entre reposiciones, queda:

$$
T_i=\frac{v_i}{f_i}.
$$

| SKU | \(T_i\) meses | Días aproximados |
|---|---:|---:|
| A | 0.923 | 27.7 |
| B | 1.428 | 42.8 |
| C | 0.688 | 20.7 |
| D | 1.224 | 36.7 |

Si todos los SKU se reponen simultáneamente, el ciclo común que vacía el área completa es:

$$
T=\frac{1900}{828+270.59+572.73+290}=0.969\ \text{meses}\approx 29.1\ \text{días}.
$$

### Problema 2

Con \(n=27\) y \(\sum x_i = 9538\):

$$
\bar{x}=\frac{9538}{27}=353.26\ \text{g}.
$$

Usando los límites de la pauta manuscrita para 96% de confianza, \(z \approx 2.055\), se obtiene:

$$
LCI \approx 321.2,\qquad LCS \approx 385.4.
$$

Al comparar cada muestra contra esos límites, las muestras fuera de control son:

$$
20\ (320\text{ g}),\quad 23\ (397\text{ g}),\quad 24\ (319\text{ g}).
$$

Por lo tanto, el proceso no está bajo control inicialmente. Eliminando esas observaciones, se recalculan los límites con las muestras restantes:

$$
\bar{x}_{\text{sin outliers}}=354.25\ \text{g}.
$$

Con la tabla transcrita, la desviación estándar recalculada queda aproximadamente \(17.20\) g y los límites serían:

$$
LCI=318.90,\qquad LCS=389.60.
$$

Como la tabla y el agregado impreso del PDF no coinciden, el gráfico final debe construirse con el mismo criterio usado por la pauta: retirar 20, 23 y 24, recalcular media/desviación y repetir hasta que no queden puntos fuera.

### Problema 3

Las medias y recorridos de las cuatro muestras son:

| Fecha | Media | Recorrido |
|---|---:|---:|
| 24 junio | 0.45 | 0.30 |
| 25 junio | 0.50 | 0.20 |
| 26 junio | 0.60 | 0.20 |
| 27 junio | 0.50 | 0.00 |

Luego:

$$
\bar{\bar X}=0.5125,\qquad \bar R=0.175.
$$

Para \(n=4\), usando \(A_2=0.729\), \(D_3=0\), \(D_4=2.282\):

$$
LCS_X=\bar{\bar X}+A_2\bar R=0.6401,
\qquad
LCI_X=\bar{\bar X}-A_2\bar R=0.3849.
$$

Para recorridos:

$$
LCS_R=D_4\bar R=0.3994,
\qquad
LCI_R=D_3\bar R=0.
$$

La nueva muestra \((0.4,0.7,0.5,0.9)\) tiene:

$$
\bar X_{\text{nuevo}}=0.625,\qquad R_{\text{nuevo}}=0.9-0.4=0.5.
$$

El promedio cae dentro de los límites, pero el recorrido excede \(LCS_R=0.3994\). Por lo tanto, el proceso no está bajo control: el problema es variabilidad excesiva, no desplazamiento de la media.

Para el plan de muestreo con \(AQL=0.02\), \(LTPD=0.08\), \(\alpha=0.05\), \(\beta=0.10\), la pauta indica:

$$
n=99,\qquad c=4.
$$

Es decir, se toma una muestra de 99 unidades; si aparecen 4 o menos defectuosas se acepta el lote, y si aparecen 5 o más se rechaza.

---

## Ayudantía 11

### Problema 1

Para Kanban se usa:

$$
K_i=\left\lceil \frac{d\,(t_{p_i}+t_{k_i}+t_{v_i})}{C_i}\right\rceil.
$$

La demanda final buena es \(200\) tarjetas/hora. Como al final se descarta 15%, el flujo requerido antes del descarte es:

$$
d=\frac{200}{0.85}=235.29\ \text{tarjetas/hora}
=0.06536\ \text{tarjetas/seg}.
$$

| Proceso | \(C_i\) | Tiempo ciclo s | Kanban calculado | Kanban entero |
|---|---:|---:|---:|---:|
| P1 | 200 | 330 | 0.108 | 1 |
| P2 | 250 | 445 | 0.116 | 1 |
| P3 | 300 | 292 | 0.064 | 1 |

Se requiere 1 Kanban en cada etapa.

Para los datos de calidad de P3, con \(n=5\), \(A_2=0.577\), \(D_3=0\), \(D_4=2.114\):

| Día | Media | Recorrido |
|---|---:|---:|
| 1 | 60.6 | 21 |
| 2 | 64.0 | 23 |
| 3 | 56.6 | 28 |
| 4 | 53.2 | 20 |
| 5 | 55.8 | 17 |

Luego:

$$
\bar{\bar X}=58.04,\qquad \bar R=21.8.
$$

Límites:

$$
LCI_X=45.46,\quad LCS_X=70.62,
\qquad
LCI_R=0,\quad LCS_R=46.09.
$$

No hay medias ni recorridos fuera de control; por lo tanto, no se eliminan outliers bajo el criterio \(X\)-\(R\).

Para el día 6:

$$
\bar X_6=\frac{63+54+43+69+65}{5}=58.8,
\qquad
R_6=69-43=26.
$$

Ambos valores están dentro de los límites, por lo que la muestra del día 6 está bajo control estadístico.

Si el control reduce fallas a 5%, el flujo requerido antes del descarte baja a:

$$
d=\frac{200}{0.95}=210.53\ \text{tarjetas/hora}.
$$

Recalculando, los valores siguen siendo menores que 1 en todas las etapas; por redondeo, el número entero de Kanbans no cambia. La mejora sí reduce carga y desperdicio, aunque no cambia el mínimo entero.

### Problema 2

La demanda diaria es 22.800 unidades y se trabaja 8 horas:

$$
d=\frac{22800}{480}=47.5\ \text{unidades/min}.
$$

Con variación de 5%, se usa \(d'=47.5(1.05)=49.875\) unidades/min. Para lote \(C=100\):

$$
K=\left\lceil \frac{d' T}{C}\right\rceil.
$$

| Tramo | Tiempo relevante \(T\) min | Kanban calculado | Kanban entero |
|---|---:|---:|---:|
| M3 | \(100/120+2+6=8.833\) | 4.406 | 5 |
| M2 | \(100/55+2+6=9.818\) | 4.897 | 5 |
| M1 | \(100/100+2+6=9.000\) | 4.489 | 5 |
| Proveedor | \(15+3+10=28.000\) | 13.965 | 14 |

Por lo tanto, se necesitan 5 Kanbans entre máquinas y 14 con el proveedor.

Para fallas de M1:

$$
A=\frac{MTBF}{MTBF+MTTR}
=\frac{100}{100+25/60}=0.99585.
$$

La capacidad efectiva de M1 es:

$$
100(0.99585)=99.59\ \text{unidades/min}.
$$

La disponibilidad apenas cambia el tiempo de procesamiento del lote, por lo que los Kanbans enteros no cambian.

Si M1 produce 20% defectuoso y los defectos se detectan después de M3, para satisfacer la demanda buena se debe producir:

$$
d''=\frac{47.5(1.05)}{0.8}=62.34\ \text{unidades/min}.
$$

Recalculando:

| Tramo | Kanban calculado | Kanban entero |
|---|---:|---:|
| M3 | 5.507 | 6 |
| M2 | 6.121 | 7 |
| M1 | 5.611 | 6 |
| Proveedor | 17.456 | 18 |

El control de calidad conviene ubicarlo inmediatamente después de M1, porque ahí se generan los defectos. Así se evita procesar unidades malas en M2 y M3. Si el control elimina la causa de defecto, el sistema vuelve al caso base; si sólo detecta y descarta, reduce costos aguas abajo pero mantiene la necesidad de producir más antes de M1.

### Problema 3

Política descentralizada por mercado. Se usa:

$$
Q^*=\sqrt{\frac{2SD}{h}},\qquad
SS=z\sigma_L,\qquad
ROP=\mu_L+SS.
$$

Con \(S=60\), \(h=0.27\), \(z=1.88\), \(L=1\) semana y 52 semanas/año:

| Mercado | \(D\) anual | \(Q^*\) | Stock seguridad | ROP |
|---|---:|---:|---:|---:|
| 1 | 2163.2 | 980.5 | 16.17 | 57.77 |
| 2 | 1955.2 | 932.2 | 14.29 | 51.89 |

El costo anual descentralizado aproximado, incluyendo transporte de \(1.05\) por unidad, es:

$$
C_D \approx 2540.47+2308.51=4848.98.
$$

Centralizando:

$$
\mu=41.6+37.6=79.2,
\qquad
\sigma=\sqrt{8.6^2+7.6^2}=11.48.
$$

Entonces:

$$
D=4118.4,\quad Q^*=1352.9,\quad SS=21.58,\quad ROP=100.78.
$$

El costo anual centralizado, incluyendo transporte de \(1.10\) por unidad, es:

$$
C_C\approx 4901.35.
$$

Bajo estos datos conviene mantener despacho descentralizado, porque el ahorro por pooling de inventario no compensa el mayor costo unitario de transporte.

Modelo general para decidir centralización con \(N\) productos y \(M\) mercados:

$$
\min \sum_{i=1}^N \sum_{m=1}^M (1-y_i) C_{im}^{D}
+ \sum_{i=1}^N y_i C_i^{C}
$$

sujeto a:

$$
y_i\in\{0,1\}\qquad \forall i.
$$

Donde \(y_i=1\) si el producto \(i\) se centraliza, \(C_{im}^{D}\) es el costo anual descentralizado del producto \(i\) en el mercado \(m\), y \(C_i^C\) es el costo anual centralizado del producto \(i\).

---

## Ayudantía 12

### Problema 1

Sea \(F\) el flujo de arándanos frescos en kg/h y \(M\) el flujo de masa base. Tras secado, 80% va a molido y 20% a azucarado. En azucarado se pierde 10%, por lo que los arándanos que llegan a mezcla son:

$$
0.8F+0.2F(0.9)=0.98F.
$$

Las restricciones principales son:

$$
F\le 300,\quad 0.8F\le 280,\quad 0.2F\le 65,\quad M\le 600,
$$

$$
M+0.98F\le 800,\qquad M+0.98F\le 850.
$$

Como mezcla es el cuello de botella efectivo, se ocupa \(M=600\) y:

$$
600+0.98F=800
\Rightarrow F=204.08\ \text{kg/h}.
$$

Después del control final se pierde 3%, luego:

$$
\text{capacidad final}=0.97(800)=776\ \text{kg/h de galletas}.
$$

Con 1 turno de 8 horas, 240 días/año:

$$
\text{arándanos frescos}=204.08(8)(240)=391836.73\ \text{kg/año},
$$

$$
\text{masa base}=600(8)(240)=1152000\ \text{kg/año}.
$$

Si se pueden duplicar dos máquinas, conviene duplicar mezclado y cocido. La nueva mezcla máxima viene dada por:

$$
F=300,\qquad M=600,
\qquad M+0.98F=894.
$$

Luego la capacidad final es:

$$
0.97(894)=867.18\ \text{kg/h}.
$$

Para envases, con demanda mensual \(D=50000\), \(S=90000\), \(h=1.5\), \(\sigma=\sqrt{2500}=50\), \(z=1.645\):

Política de período fijo de 1 mes:

$$
S_T=D(T+L)+z\sigma\sqrt{T+L}.
$$

Con \(T=1\) mes y \(L=0.25\) meses:

$$
S_T=62591.96\ \text{envases}.
$$

Se ordena mensualmente, antes del inicio del mes cubierto, hasta llevar la posición de inventario a unas 62.592 unidades.

Política de revisión continua:

$$
Q^*=\sqrt{\frac{2DS}{h}}
=77459.67\ \text{envases},
$$

$$
ROP=D L+z\sigma\sqrt{L}
=12541.13\ \text{envases}.
$$

Para Wagner-Whitin con demandas \((49000,53000,47000)\), setup \(S=90000\) y holding \(h=1.5\), los costos óptimos son:

$$
F_1=90000,\quad F_2=169500,\quad F_3=250500.
$$

La política óptima es ordenar en el mes 1 para cubrir meses 1 y 2, y ordenar en el mes 3 para cubrir mes 3:

$$
Q_1=102000,\qquad Q_2=0,\qquad Q_3=47000.
$$

Costos comparables:

- Período fijo mensual: tres setups más stock de seguridad mensual.
- Revisión continua: costo EOQ mensual/anualizado según horizonte usado.
- Wagner-Whitin 3 meses: \(250500\) pesos para setup y holding determinístico.

El máximo a pagar por el contrato es la diferencia entre el menor costo sin contrato y el costo Wagner-Whitin bajo contrato, usando el mismo horizonte y los mismos componentes de costo.

### Problema 2

Revisión continua por producto:

$$
Q_i^*=\sqrt{\frac{2SD_i}{h_i}},
\qquad
ROP_i=d_iL+z\sigma_i\sqrt{L}.
$$

Con \(z=1.645\), \(L=10\) días y 365 días/año:

| Insumo | \(D_i\) anual | \(h_i\) | \(Q_i^*\) | ROP | Pedidos/año | Días entre pedidos | Costo anual |
|---|---:|---:|---:|---:|---:|---:|---:|
| U1 | 2190 | 20 | 148.0 | 65.20 | 14.80 | 24.66 | 2959.73 |
| U2 | 1460 | 14 | 144.4 | 43.38 | 10.11 | 36.11 | 2021.88 |

El costo anual total de manejar ambos independientemente es:

$$
C\approx 4981.61.
$$

Para una política conjunta de período fijo, usando un despacho común:

$$
T^*=\sqrt{\frac{2S(365)}{\sum_i h_i d_i}}
=20.37\ \text{días}.
$$

Las cantidades por pedido son:

$$
Q_1=6(20.37)=122.20,
\qquad
Q_2=4(20.37)=81.46.
$$

Los puntos objetivo de protección para \(T+L\) son:

$$
R_1=6(30.37)+1.645(1)\sqrt{30.37}=191.26,
$$

$$
R_2=4(30.37)+1.645(0.65)\sqrt{30.37}=127.36.
$$

El costo anual conjunto aproximado es:

$$
C\approx 3584.41.
$$

Conviene la política de período fijo conjunto, porque aprovecha el costo fijo único de despacho para ambos insumos.

### Problema 3

Se modela cada bloque como \(G/G/c\). Cada taxi atiende en promedio un viaje de 20 minutos, por lo que:

$$
\mu=3\ \text{viajes/hora por taxi}.
$$

La utilización es:

$$
\rho=\frac{\lambda}{c\mu}.
$$

La aproximación de Sakasegawa entregada es:

$$
W_q \approx
\left(\frac{CV_a^2+CV_s^2}{2}\right)
\frac{\rho^{\sqrt{2c+2}-1}}{c(1-\rho)\mu}.
$$

Los resultados actuales son:

| Bloque | Duración h | Demanda | Taxis | \(\lambda\) viajes/h | \(\rho\) | \(W_q\) h | \(W_q\) min |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 35 | 4 | 5.83 | 0.486 | 0.494 | 29.66 |
| 2 | 2 | 27 | 6 | 13.50 | 0.750 | 1.464 | 87.86 |
| 3 | 7 | 85 | 6 | 12.14 | 0.675 | 1.538 | 92.26 |
| 4 | 9 | 45 | 3 | 5.00 | 0.556 | 0.139 | 8.32 |

El bloque más congestionado por espera es el bloque 3, aunque el bloque 2 tiene la mayor utilización. La política de 90% no se está saturando; todos los bloques están bajo 90%. Se podría reasignar capacidad desde bloques con baja espera hacia bloques 2 y 3 si el objetivo operacional es reducir espera.

Si se aceptan viajes fuera de zona, la demanda total aumenta 20%. La demanda base total es:

$$
35+27+85+45=192,
\qquad
\Delta=38.4.
$$

Distribuyendo el aumento según el enunciado, las nuevas demandas por bloque son:

| Bloque | Nueva demanda | \(\lambda\) viajes/h |
|---|---:|---:|
| 1 | 40.76 | 6.79 |
| 2 | 32.76 | 16.38 |
| 3 | 104.20 | 14.89 |
| 4 | 52.68 | 5.85 |

Si todos esos viajes se atienden bajo condición fuera de zona, la tasa de servicio baja a:

$$
\mu=1.5\ \text{viajes/hora por taxi}.
$$

Con la flota original, las utilizaciones superan 1 en todos los bloques, por lo que la política no es factible sin aumentar taxis o separar flota por tipo de viaje.

Una asignación mínima para mantener \(\rho\le 0.9\) es:

$$
c_b \ge \left\lceil \frac{\lambda_b}{0.9\mu}\right\rceil.
$$

Con \(\mu=1.5\):

| Bloque | \(\lambda\) | Taxis mínimos |
|---|---:|---:|
| 1 | 6.79 | 6 |
| 2 | 16.38 | 13 |
| 3 | 14.89 | 12 |
| 4 | 5.85 | 5 |

La flota requerida sube fuertemente; por lo tanto, aceptar viajes fuera de zona sólo es razonable si el margen adicional cubre el costo de más taxis y el aumento de espera.

Modelo matemático:

Variables:

$$
k_b \in \mathbb{Z}_+,\quad
z\in\{0,1\},\quad
\rho_b\ge 0,\quad
W_{q,b}\ge 0.
$$

Donde \(k_b\) es el número de taxis en bloque \(b\) y \(z=1\) indica aceptar viajes fuera de zona.

Demanda:

$$
\lambda_b(z)=\frac{D_b+z\Delta s_b}{H_b}.
$$

Utilización:

$$
\rho_b=\frac{\lambda_b(z)}{k_b\mu(z)}.
$$

Restricciones operacionales:

$$
\rho_b\le 0.9,\qquad k_b\in\mathbb{Z}_+,\qquad z\in\{0,1\}.
$$

Función objetivo:

$$
\min \sum_b C_q \lambda_b(z) W_{q,b}
+ \sum_b C_u(0.9-\rho_b)
+ \sum_b C_k k_b.
$$

Con:

$$
W_{q,b}\ge
\left(\frac{CV_{a,b}^2+CV_{s,b}^2}{2}\right)
\frac{\rho_b^{\sqrt{2k_b+2}-1}}{k_b(1-\rho_b)\mu(z)}.
$$

El modelo decide simultáneamente si salir fuera de zona y cuántos taxis asignar por bloque.
