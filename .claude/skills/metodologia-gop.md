# Skill: Metodología — Cómo crear un Estudio GOP

Guía completa para generar un documento "Estudio Ix" de Gestión de Operaciones (ICS3213, PUC Chile) desde cero. Cubre qué incluir, cómo ordenarlo, qué calidad exigir y cómo extraer valor de las fuentes disponibles.

---

## 1. Propósito del documento

El "Estudio" es un **apunte de estudio integral** para la prueba Ix de GOP. No es un resumen pasivo: es un documento operativo que:
- Analiza qué temas son más probables en base a histórico (2014–2023)
- Explica la teoría con **definiciones, fórmulas, trampas frecuentes y tips de prueba**
- Incluye ejercicios resueltos con identificación de patrón + desarrollo completo
- Termina con un formulario imprimible y un resumen de qué memorizar

---

## 2. Fuentes a consultar (en orden de prioridad)

| Fuente | Ubicación | Uso |
|---|---|---|
| Ayudantías del año | `ayudantias/` | Ejercicios resueltos más recientes, son los más representativos |
| Pruebas anteriores 2014–2023 | `pruebas _anteriores/` | Frecuencia histórica, patrones de preguntas, ejercicios reales |
| Resúmenes anteriores | `resumenes_anteriores/` | Estilo y contenido de referencia |
| Clases/diapositivas | `clases/` | Definiciones oficiales, fórmulas exactas |
| Casos | `casos/` | Contexto de Parcel Guard, LL Bean, etc. |
| Temario oficial | `temario.md` | Qué módulos entran en cada prueba |

**Regla de oro**: si un tema aparece en ≥ 5/7 pruebas históricas → **alta prioridad**, siempre incluir ejercicio resuelto.

---

## 3. Estructura fija del documento

Cada Estudio tiene exactamente estas secciones, en este orden:

```
0. Índice (automático)
1. Análisis del Temario y Probabilidad de Aparición
2. Módulo 1: [nombre]          ← un módulo por sección
   ...
N. Módulo N: [nombre]
N+1. La Meta (Capítulos X–Y): V/F Posibles
N+2. Casos: [Caso A] y [Caso B]
N+3. Módulo adicional / Otros Temas y Cápsulas   ← si aplica
N+4. Ejercicios Resueltos por Tema
N+5. Formulario de Referencia
     Resumen final: qué memorizar para la etapa digital
```

---

## 4. Sección 1: Análisis del Temario

### Qué incluir
1. **Tabla de frecuencia histórica**: filas = temas, columnas = años de prueba (ej. 14, 15, 16, 17, 18, 19, 23). Última columna = "Prior." con fracción X/N.
2. **Caja TIP PRUEBA naranja** con las 5–6 prioridades de estudio ordenadas por probabilidad.

### Cómo construirla
- Revisar cada PDF en `pruebas _anteriores/` y marcar qué temas aparecen
- Contar ocurrencias → calcular X/7 (o X/N según años disponibles)
- Temas con 7/7 o 6/7 → siempre aparecen, son el núcleo del estudio

### Temas históricos GOP I1 (referencia base)
| Tema | Prob. histórica |
|---|---|
| CB multi-etapa | 7/7 (100%) |
| Holt (tendencia) | 6/7 (86%) |
| V/F generales de materia | 6/7+ |
| EOQ y variantes | 5/7 (71%) |
| MAD/TS | 5/7 (71%) |
| Regresión lineal | 3/7 (43%) |
| Newsvendor | 3/7 (43%) |
| CPM/Crashing | variable |

---

## 5. Estructura de cada Módulo

Cada módulo sigue esta secuencia interna:

```
X.1  Glosario / Conceptos fundamentales     → caja azul "Definicion"
X.2  Métricas clave / Fórmulas principales  → caja verde "Formulas"
X.3  Subtemas específicos                   → definiciones + fórmulas + trampas
X.4  TIP PRUEBA: patrón invariable          → caja naranja si el tema siempre aparece igual
X.N  V/F frecuentes del módulo              → tabla con # / R / Afirmación y corrección
```

### Nivel de profundidad requerido

**No basta con listar fórmulas.** Cada concepto debe tener:
- **Definición** (caja azul): qué es, intuición en 2–3 oraciones
- **Fórmula** (caja verde): la ecuación con variables anotadas
- **Trampa** (caja roja): el error más frecuente en prueba sobre ese concepto
- **TIP** (caja naranja): cuándo/cómo identificar que este modelo aplica

---

## 6. Sección V/F: formato y calidad

Las tablas V/F son críticas (aparecen en la etapa digital). Formato:

```
#  |  R  |  Afirmación exacta entre comillas  — Corrección si es Falsa
```

### Reglas de calidad para V/F:
- Las afirmaciones **falsas** siempre incluyen la corrección exacta después del "—"
- Usar confusiones reales que han aparecido en pruebas: p.ej. TH vs Capacidad, Poka-Yoke vs Chaku-Chaku, EOQ continuo vs periódico
- Mínimo 5–6 V/F por módulo principal
- Las V/F de La Meta van en sección separada con ≥ 20 afirmaciones
- Incluir justificación en cursiva debajo de cada V/F de La Meta

---

## 7. Ejercicios resueltos: formato y calidad

### Estructura obligatoria de cada ejercicio

```
[Caja gris "Ejercicio: Nombre (Fuente — Nivel)"]
  [Caja naranja anidada "TIP PRUEBA: ¿Cuándo usar este enfoque?"]
    Identificación: descripción del patrón que activa este método
    Qué aplicar: qué fórmula/algoritmo usar y por qué
  [cierre caja naranja]

  Datos: todos los parámetros con unidades explícitas
  
  Desarrollo detallado:
  - Nombrar cada paso
  - Mostrar cálculo numérico completo (no saltarse pasos)
  - Resaltar en negrita el resultado final
  
  Conclusión: 1–2 oraciones interpretando el resultado en contexto
[cierre caja gris]
```

### Fuentes de ejercicios (en orden de preferencia)
1. Pruebas anteriores de I1 (mismo número de prueba que se estudia)
2. Ayudantías del año actual (son los más representativos del estilo actual)
3. Pruebas de I2/I3 si el tema aparece ahí con similar formato
4. Ejercicios propios calibrados con los datos históricos

### Qué ejercicios incluir siempre (I1)
- CB multi-etapa con rendimientos (diagrama + CB + producción + rebalanceo + LP)
- EOQ básico + POQ + EOQ con faltantes (del mismo contexto)
- ROP con incertidumbre (uno con SS negativo como trampa)
- Newsvendor (CR + Q* + análisis de precio de indiferencia)
- Holt paso a paso (con inicialización explícita)
- Problema integrador: combina ≥ 2 temas (ej. Regresión + Inventarios)

---

## 8. Sección La Meta

### Estructura
```
7.1  Personajes y contexto          → caja azul con personajes y sus roles
7.2  Conceptos clave Cap. X–Y       → cajas azules por capítulo/grupo temático
7.3  Cronología de ocurrencias      → tabla 3 columnas: fase / evento / teoría TOC
7.4  20+ afirmaciones V/F           → tabla con justificación en cursiva
```

### Las 5 ideas más preguntadas de La Meta
1. Meta = ganar dinero ahora y en el futuro (no producción)
2. Herbie = cuello de botella del sistema
3. Producir sin vender = Inventario, no Throughput
4. Maximizar eficiencia local ≠ eficiencia global
5. Lotes pequeños → mejor flujo (aunque aumenten los setups)

### Trampas clásicas de La Meta
- "Throughput es lo que se produce" → FALSO: es lo que se vende
- "Poner a Herbie al final" → FALSO: debe ir al frente
- "OE incluye materias primas" → FALSO: eso es Inventario
- "100% utilización en todos los recursos es óptimo" → FALSO

---

## 9. Sección Casos

Para cada caso incluir:
1. **Caja azul "Contexto"**: qué empresa es, qué decisión enfrenta, qué módulo conecta
2. **Lista de puntos clave evaluables**: qué conceptos del caso se han preguntado históricamente
3. **Tabla V/F del caso**: 4–6 afirmaciones con correcciones

### Casos frecuentes GOP
- **Parcel Guard** → Análisis de flujos, CB con rechazos, Ley de Little
- **LL Bean** → Newsvendor, Ratio Crítico, Postponement/Consolidación
- **Benihana Bar** → Layout, utilización, CB, batching
- **Sport Obermeyer** → Newsvendor con múltiples SKUs, variabilidad

---

## 10. Formulario de Referencia

### Formato
- **2 columnas** con `multicols`
- Sin explicaciones: solo las fórmulas clave con sus nombres
- Agrupar por tema con encabezados en color `gopblue`
- Incluir tabla de valores z (90%, 95%, 97.5%, 99%)
- Incluir "TRAMPAS FRECUENTES" al final como lista

### Siempre incluir
- Ley de Little, fórmula N unidades T = τ + (N-1)·TC
- Slope crashing
- SES, Holt (F, T, FIT), Holt-Winters
- MAD, TS, σ ≈ 1.25·MAD
- EOQ, POQ, Backorder, ROP+SS
- Newsvendor (CR, Q*)
- M/M/1 si entra en temario
- Inicialización Holt: F₀ = promedio, T₀ = (Aₖ - A₁)/(k-1)

---

## 11. Resumen Final: qué memorizar

Al final del formulario, agregar una **caja roja** con dos columnas:
- Izquierda: definiciones exactas + diferencias clave
- Derecha: La Meta — 5 ideas + fórmulas a recordar

Y una **caja verde** con consejos para la etapa de desarrollo:
- Llevar el formulario impreso
- Ejercicios más probables
- Patrón típico de la prueba (diagrama + CB + producción + rebalanceo)

---

## 12. Calibración de extensión

| Sección | Páginas aprox. |
|---|---|
| Portada + TOC | 3 |
| Análisis del temario | 1–2 |
| Módulo 1 (Estrategia/Intro) | 2 |
| Módulo 2 (Procesos) | 4–6 |
| Módulo 3 (Proyectos) | 2–3 |
| Módulo 4 (Pronósticos) | 4–5 |
| Módulo 5 (Inventarios) | 4–5 |
| La Meta | 6–8 |
| Casos | 2–3 |
| Ejercicios resueltos | 10–14 |
| Formulario | 2–3 |
| **Total** | **40–55 páginas** |

---

## 13. Proceso de trabajo recomendado

1. **Leer el temario oficial** (`temario.md`) → identificar módulos y casos de la prueba
2. **Revisar pruebas anteriores** de ese número (I1, I2, I3) → tabla de frecuencia
3. **Leer las ayudantías del año** → extraer ejercicios resueltos actualizados
4. **Redactar módulo a módulo** en LaTeX siguiendo el estilo canónico
5. **Generar V/F** a partir de confusiones reales encontradas en pruebas pasadas
6. **Resolver ejercicios** integrando datos de ayudantías, no inventar datos nuevos
7. **Compilar formulario** extrayendo las fórmulas de los módulos
8. **Revisar**: ¿tiene trampa roja por cada concepto importante? ¿tiene V/F por módulo?

---

## 14. Señales de un buen Estudio GOP

- Cada módulo tiene al menos 1 trampa roja
- Los ejercicios empiezan siempre con "Identificación" y "Qué aplicar"
- El análisis del temario tiene la tabla de frecuencia histórica completa
- El formulario cabe en 2–3 páginas imprimibles
- La sección La Meta tiene ≥ 20 afirmaciones V/F con justificación
- Los ejercicios son de pruebas o ayudantías reales, no inventados
- El resumen final dice explícitamente "qué memorizar" vs "qué llevar impreso"
