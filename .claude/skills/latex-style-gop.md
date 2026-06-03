# Skill: Estilo LaTeX — Estudio GOP ICS3213

Genera documentos LaTeX que repliquen **exactamente** el estilo visual del "Estudio I1 2026" de Gestión de Operaciones (ICS3213, PUC Chile). Este es el estilo canónico del autor (Fabián Ortega Llantén).

---

## Preamble completo

```latex
\documentclass[11pt, a4paper]{article}

% ── Codificación y Lenguaje ──────────────────────────────────────────────────
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish, es-tabla]{babel}

% ── Geometría ───────────────────────────────────────────────────────────────
\usepackage[top=2.5cm, bottom=2.5cm, left=2.5cm, right=2.5cm]{geometry}

% ── Matemáticas ─────────────────────────────────────────────────────────────
\usepackage{amsmath, amssymb, amsthm}
\usepackage{mathtools}       % \underbrace mejorado, etc.

% ── Colores y Cajas ─────────────────────────────────────────────────────────
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\tcbuselibrary{skins, breakable, theorems}

% ── Tablas ──────────────────────────────────────────────────────────────────
\usepackage{booktabs}
\usepackage{array}
\usepackage{multirow}

% ── Listas ──────────────────────────────────────────────────────────────────
\usepackage{enumitem}

% ── Encabezado y Pie de Página ──────────────────────────────────────────────
\usepackage{fancyhdr}

% ── Hipervínculos y TOC ─────────────────────────────────────────────────────
\usepackage[colorlinks=true, linkcolor=gopblue, urlcolor=gopblue]{hyperref}

% ── Gráficos y Diagramas ────────────────────────────────────────────────────
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\usepackage{graphicx}

% ── Columnas múltiples (formulario) ─────────────────────────────────────────
\usepackage{multicol}

% ── Espaciado ───────────────────────────────────────────────────────────────
\usepackage{setspace}
\setlength{\parskip}{4pt}
\setlength{\parindent}{0pt}
```

---

## Paleta de colores (definir DESPUÉS de xcolor)

```latex
% ── Paleta GOP ──────────────────────────────────────────────────────────────
\definecolor{gopblue}{RGB}{31, 78, 121}       % Azul oscuro: secciones y links
\definecolor{gopcyan}{RGB}{70, 130, 180}      % Azul claro: título principal
\definecolor{gopgreen}{RGB}{0, 100, 0}        % Verde oscuro: cajas Formulas
\definecolor{gopgreenlight}{RGB}{230, 255, 230} % Fondo verde claro
\definecolor{goporange}{RGB}{200, 100, 0}     % Naranja: TIP PRUEBA
\definecolor{goporangelight}{RGB}{255, 245, 210} % Fondo naranja/crema
\definecolor{gopred}{RGB}{160, 0, 0}          % Rojo: TRAMPA/ADVERTENCIA
\definecolor{gopredlight}{RGB}{255, 230, 230} % Fondo rojo claro
\definecolor{gopgray}{RGB}{90, 90, 90}        % Gris: Ejercicio (header)
\definecolor{gopgraylight}{RGB}{245, 245, 240} % Fondo ejercicio
\definecolor{gopbluedef}{RGB}{0, 70, 140}     % Azul: Definicion (header)
\definecolor{gopbluedeflight}{RGB}{220, 235, 255} % Fondo definición
```

---

## Entornos tcolorbox (los 5 tipos de caja)

```latex
% ── 1. DEFINICION (azul) ─────────────────────────────────────────────────────
\newtcolorbox{definicion}[1]{
  enhanced,
  breakable,
  colback=gopbluedeflight,
  colframe=gopbluedef,
  fonttitle=\bfseries\small,
  title={Definicion: #1},
  coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=6pt},
  boxed title style={colback=gopbluedef, colframe=gopbluedef, sharp corners},
  sharp corners=south,
  top=4mm,
  before skip=6pt,
  after skip=6pt,
}

% ── 2. FORMULAS (verde) ──────────────────────────────────────────────────────
\newtcolorbox{formulas}[1]{
  enhanced,
  breakable,
  colback=gopgreenlight,
  colframe=gopgreen,
  fonttitle=\bfseries\small,
  title={Formulas: #1},
  coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=6pt},
  boxed title style={colback=gopgreen, colframe=gopgreen, sharp corners},
  sharp corners=south,
  top=4mm,
  before skip=6pt,
  after skip=6pt,
}

% ── 3. TIP PRUEBA (naranja) ───────────────────────────────────────────────────
\newtcolorbox{tipprueba}[1]{
  enhanced,
  breakable,
  colback=goporangelight,
  colframe=goporange,
  fonttitle=\bfseries\small,
  title={TIP PRUEBA: #1},
  coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=6pt},
  boxed title style={colback=goporange, colframe=goporange, sharp corners},
  sharp corners=south,
  top=4mm,
  before skip=6pt,
  after skip=6pt,
}

% ── 4. TRAMPA / ADVERTENCIA (rojo) ───────────────────────────────────────────
\newtcolorbox{trampa}[1]{
  enhanced,
  breakable,
  colback=gopredlight,
  colframe=gopred,
  fonttitle=\bfseries\small,
  title={TRAMPA/ADVERTENCIA: #1},
  coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=6pt},
  boxed title style={colback=gopred, colframe=gopred, sharp corners},
  sharp corners=south,
  top=4mm,
  before skip=6pt,
  after skip=6pt,
}

% ── 5. EJERCICIO (gris, envuelve TIP PRUEBA dentro) ──────────────────────────
\newtcolorbox{ejercicio}[1]{
  enhanced,
  breakable,
  colback=gopgraylight,
  colframe=gopgray,
  fonttitle=\bfseries\small\color{black},
  title={Ejercicio: #1},
  attach boxed title to top left={yshift=-2mm, xshift=6pt},
  boxed title style={colback=gopgray!40, colframe=gopgray, sharp corners},
  sharp corners=south,
  top=4mm,
  before skip=6pt,
  after skip=6pt,
}

% ── 6. RESUMEN TEMARIO (azul título-página) ───────────────────────────────────
\newtcolorbox{resumentemario}{
  enhanced,
  colback=gopbluedeflight,
  colframe=gopbluedef,
  fonttitle=\bfseries,
  title={Resumen del Temario},
  coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=6pt},
  boxed title style={colback=gopbluedef, colframe=gopbluedef, sharp corners},
}

% ── 7. ESTRUCTURA PRUEBA (naranja título-página) ──────────────────────────────
\newtcolorbox{estructuraprueba}{
  enhanced,
  colback=goporangelight,
  colframe=goporange,
  fonttitle=\bfseries,
  title={Estructura de la Prueba},
  coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=6pt},
  boxed title style={colback=goporange, colframe=goporange, sharp corners},
}
```

---

## Encabezado y pie de página

```latex
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\textbf{GOP ICS3213} --- Estudio \texttt{<PRUEBA>} \texttt{<AÑO>}}
\fancyhead[C]{\small\thepage}
\fancyhead[R]{\small\nouppercase{\rightmark}}   % nombre de sección actual
\fancyfoot[C]{\footnotesize Documento generado a partir de ayudantías \texttt{<AÑO>}, pruebas pasadas 2014--2023 y wiki GOP}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
```

---

## Estilo de secciones

Las secciones usan color `gopblue` con una regla inferior:

```latex
\usepackage{titlesec}

\titleformat{\section}
  {\color{gopblue}\Large\bfseries}
  {\color{gopblue}\thesection.}
  {0.5em}{}
  [\color{gopblue}\titlerule]

\titleformat{\subsection}
  {\color{gopblue}\normalsize\bfseries}
  {\color{gopblue}\thesubsection.}
  {0.5em}{}

\titleformat{\subsubsection}
  {\color{gopblue}\small\bfseries}
  {\color{gopblue}\thesubsubsection.}
  {0.5em}{}
```

---

## Página de título

```latex
\begin{document}

\begin{titlepage}
  \centering
  \vspace*{3cm}
  {\Huge\bfseries\color{gopcyan} Estudio \texttt{<PRUEBA>}\par}
  \vspace{0.4cm}
  {\LARGE\bfseries Gestión de Operaciones\par}
  \vspace{0.3cm}
  {\large ICS3213 --- PUC Chile --- \texttt{<AÑO>}\par}
  \vspace{1.5cm}
  \rule{\textwidth}{0.4pt}
  \vspace{0.5cm}

  {\normalsize \texttt{<Día> de <Mes> <AÑO>}\par}
  \vspace{0.2cm}
  {\small Prof.\ Alejandro Mac Cawley\par}
  \vspace{0.2cm}
  {\small\textbf{Autor:} Fabián Ignacio Ortega Llantén\par}
  \vspace{0.5cm}
  \rule{\textwidth}{0.4pt}
  \vspace{1.5cm}

  \begin{resumentemario}
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
      \item Materia de clase: desde \texttt{<módulo inicio>} hasta \texttt{<módulo fin>}
      \item \textbf{La Meta} Capítulos \texttt{<X>--<Y>} (inclusive)
      \item \textbf{Caso 1:} \texttt{<Caso A>} y \textbf{Caso 2:} \texttt{<Caso B>}
      \item Cápsula: \texttt{<Tema cápsula>}
    \end{itemize}
  \end{resumentemario}

  \vspace{0.8cm}

  \begin{estructuraprueba}
    \begin{itemize}[leftmargin=1.2em, itemsep=3pt]
      \item \textbf{Etapa Digital:}
        \begin{itemize}[leftmargin=1.2em, itemsep=1pt]
          \item 10 preguntas selección múltiple (materia)
          \item 10 preguntas V/F de La Meta (si Falso, argumentar)
          \item 1 pregunta de desarrollo
        \end{itemize}
      \item \textbf{Descanso intermedio}
      \item \textbf{Etapa Desarrollo --- APUNTES LIBRES:}
        \begin{itemize}[leftmargin=1.2em, itemsep=1pt]
          \item Se permite el uso de cualquier documento o manual impreso.
          \item Ejercicios de cálculo (\texttt{<temas desarrollo>})
        \end{itemize}
    \end{itemize}
  \end{estructuraprueba}

  \vfill
\end{titlepage}
```

---

## Tabla de contenidos

```latex
\tableofcontents
\newpage
```

El TOC se genera automáticamente. Los links se colorean en `gopblue`.

---

## Tabla de frecuencia histórica (Análisis del Temario)

```latex
\begin{center}
\small
\begin{tabular}{lcccccccc}
  \toprule
  \textbf{Tema} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17}
                & \textbf{18} & \textbf{19} & \textbf{23} & \textbf{Prior.} \\
  \midrule
  Análisis CB proceso multi-etapa & $\checkmark$ & $\checkmark$ & \ldots & & & & & \textbf{7/7} \\
  \bottomrule
\end{tabular}
\end{center}
```

---

## Tablas V/F

```latex
\begin{center}
\small
\begin{tabular}{@{}clp{9cm}@{}}
  \toprule
  $\#$ & R & Afirmación y corrección \\
  \midrule
  1 & \textbf{F} & ``Afirmación falsa.'' --- Falso: corrección breve. \\
  2 & \textbf{V} & ``Afirmación verdadera.'' \\
  \bottomrule
\end{tabular}
\end{center}
```

---

## Fórmulas matemáticas con anotaciones

Usar `\underbrace` para anotar componentes de costos:

```latex
\[
  \mathbf{CT} = \underbrace{D \cdot C}_{\text{Costo Producto}}
              + \underbrace{\frac{D}{Q} \cdot S}_{\text{Costo Pedir}}
              + \underbrace{\frac{Q}{2} \cdot H}_{\text{Costo Mantener}}
\]
```

---

## Diagrama de flujo de proceso (tikz)

```latex
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, fill=blue!15, minimum width=2.5cm, minimum height=1cm,
              text centered, font=\small},
  arr/.style={-Stealth, thick}
]
  \node[box] (A) {Etapa 1\\(cap u/h)};
  \node[box, right=1.5cm of A] (B) {Etapa 2\\(cap u/h)};
  \draw[arr] (A) -- (B) node[midway, above]{\small flujo};
\end{tikzpicture}
\end{center}
```

---

## Formulario de Referencia (2 columnas compactas)

```latex
\section{Formulario de Referencia}

\begin{multicols}{2}
\small

\textbf{\color{gopblue} PROCESOS}
\begin{align*}
  L &= \lambda W \\
  \text{WIP} &= \text{TH} \times W \\
  T_N &= \tau + (N-1) \cdot \tfrac{1}{\text{CB}}
\end{align*}

\columnbreak

\textbf{\color{gopblue} INVENTARIOS DETERMINÍSTICOS}
\begin{align*}
  Q^*_{\text{EOQ}} &= \sqrt{\tfrac{2DS}{H}} \\
  Q^*_{\text{POQ}} &= \sqrt{\tfrac{2DS}{H(1-d/p)}}
\end{align*}

\end{multicols}
```

---

## Convenciones tipográficas

| Elemento | Formato |
|---|---|
| Primer uso de término clave | `\textbf{término}` |
| Intuición / explicación secundaria | `\textit{texto}` |
| Siglas técnicas | Mayúsculas, p.ej. CB, EOQ, WIP |
| Nombres de modelos | Normal, no cursiva |
| Valores numéricos con unidades | `$100\,\text{kg/hr}$` |
| Resultado final de ejercicio | `\textbf{resultado}` |
| Referencia a sección | `Sección~\ref{sec:xxx}` |

---

## Estructura de un Ejercicio completo

```latex
\begin{ejercicio}{Nombre del Ejercicio (Fuente — Nivel)}

  \begin{tipprueba}{TIP PRUEBA: ¿Cuándo usar este enfoque?}
    \textbf{Identificación:} Descripción de cuándo aparece este tipo de problema.\\
    \textbf{Qué aplicar:} Método a usar y por qué.
  \end{tipprueba}

  \textbf{Datos:} $D = \ldots$; $S = \ldots$; $H = \ldots$.

  \medskip
  \textbf{Desarrollo:}

  Explicación paso a paso con cálculos:
  \[
    Q^* = \sqrt{\frac{2DS}{H}} = \sqrt{\frac{2 \times \ldots \times \ldots}{\ldots}} \approx \textbf{XXX}
  \]

  \textbf{Conclusión:} Una oración con la interpretación del resultado.

\end{ejercicio}
```

---

## Cierre del documento

```latex
\end{document}
```

---

## Checklist antes de compilar

- [ ] `lualatex` o `pdflatex` (dos pasadas para TOC y referencias)
- [ ] Verificar que todos los `\begin{...}` tienen su `\end{...}` correspondiente
- [ ] Los colores de las cajas coinciden con el tipo: azul=definición, verde=fórmulas, naranja=tip, rojo=trampa, gris=ejercicio
- [ ] Las fórmulas usan `\mathbf` para vectores/matrices y `\text` para unidades
- [ ] Los ejercicios siempre empiezan con un `\begin{tipprueba}` anidado dentro de `\begin{ejercicio}`
