import re

with open('04_calidad.tex', 'r') as f:
    content = f.read()

# 1. Split the content
# We know the markers:
algo2_start = r"\\subsection{Algoritmo 2: Capacidad de Proceso \(\$C_p\$ y \$C_\{pk\}\$\)}"
ejemplo1_start = r"\\vspace\{0.4cm\}\n\\begin\{tcolorbox\}\[colback=white,colframe=green!60!black,title=\{Ejemplo Práctico Directo \(Examen 2024 - PII.b\)\}\]"

# Find Algoritmo 2 and Ejemplo 1 indices
idx_algo2 = re.search(algo2_start, content).start()
idx_ejemplo1 = re.search(ejemplo1_start, content).start()

# Parts:
# Before Algo 2
part1 = content[:idx_algo2]
# Algo 2 text
algo2_text = content[idx_algo2:idx_ejemplo1]
# Ejemplo 1 text
ejemplo1_text = content[idx_ejemplo1:]

# Create Ejemplo 2 text
ejemplo2_text = r"""

\vspace{0.4cm}
\begin{tcolorbox}[colback=white,colframe=green!60!black,title={Ejemplo Práctico Directo (Basado en Examen 2016 - Vasos Térmicos)}]
\textbf{Enunciado:} Usted es el titular de una empresa de café preparado. Ha determinado que los vasos térmicos deben tolerar un mínimo de $90^\circ\text{C}$ (Límite Inferior de Especificación, $EI$) para ser seguros. Por otro lado, su proveedor actual le entrega vasos que, en las muestras de recepción, tienen una resistencia térmica promedio de $95^\circ\text{C}$ ($\bar{\bar{X}}$) con una desviación estándar del proceso de $2^\circ\text{C}$ ($\hat{\sigma}$).

\textbf{Pregunta:} Evalúe la capacidad del proceso del proveedor utilizando el índice de capacidad real ($C_{pk}$). ¿Es el proveedor capaz de cumplir con las exigencias?

\textbf{Resolución paso a paso según el Algoritmo:}
\begin{enumerate}
    \item \textbf{Identificación de Parámetros:} 
    Promedio del proceso: $\bar{\bar{X}} = 95^\circ\text{C}$.
    Desviación estándar: $\hat{\sigma} = 2^\circ\text{C}$.
    Especificación Inferior: $EI = 90^\circ\text{C}$.
    Especificación Superior ($ES$): No existe un límite superior (mientras más resista el vaso, mejor).
    \item \textbf{Cálculo del $C_{pk}$ (Capacidad Real):} Dado que solo existe una especificación inferior, el índice de capacidad real se calcula evaluando únicamente la distancia del centro hacia ese límite:
    $$ C_{pk} = \frac{\bar{\bar{X}} - EI}{3\hat{\sigma}} = \frac{95 - 90}{3(2)} = \frac{5}{6} \approx 0.833 $$
    \item \textbf{Diagnóstico Final:} 
    Puesto que $C_{pk} = 0.833 < 1$, se concluye matemáticamente que el proceso del proveedor \textbf{no es capaz} de asegurar consistentemente que todos los vasos resistirán al menos $90^\circ\text{C}$. Una fracción significativa de los vasos fallará por debajo de este estándar de seguridad, lo cual justifica las quejas de los clientes. Se debe exigir al proveedor centrar su proceso (aumentar $\bar{\bar{X}}$) o reducir su variabilidad ($\hat{\sigma}$).
\end{enumerate}
\end{tcolorbox}
"""

# Reassemble
new_content = part1 + ejemplo1_text + "\n\n" + algo2_text.strip() + ejemplo2_text

with open('04_calidad.tex', 'w') as f:
    f.write(new_content)

