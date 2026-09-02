with open('04_calidad.tex', 'r') as f:
    lines = f.readlines()

# find indices
algo2_idx = -1
ejemplo1_idx = -1

for i, line in enumerate(lines):
    if "\\subsection{Algoritmo 2: Capacidad de Proceso" in line:
        algo2_idx = i
    if "Ejemplo Práctico Directo (Examen 2024" in line:
        ejemplo1_idx = i - 2 # grab the \vspace and \begin{tcolorbox}

# split
part1 = lines[:algo2_idx] # everything before Algoritmo 2
algo2_block = lines[algo2_idx:ejemplo1_idx] # Algoritmo 2
ejemplo1_block = lines[ejemplo1_idx:] # Ejemplo 1

ejemplo2_str = r"""
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

new_lines = part1 + ejemplo1_block + ["\n"] + algo2_block + [ejemplo2_str]

with open('04_calidad.tex', 'w') as f:
    f.writelines(new_lines)
