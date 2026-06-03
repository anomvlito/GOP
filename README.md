# GOP 2026 - Repositorio de Estudio y Soluciones

Este repositorio contiene material de estudio, apuntes y resoluciones de pruebas anteriores para el curso de Gestion de Operaciones (GOP). Todo el material ha sido digitalizado y formateado en LaTeX para facilitar su lectura y estudio.

## Estructura del Repositorio

El repositorio se organiza en los siguientes directorios principales:

* llevar_a_i2/: Contiene todos los documentos PDF ya compilados y listos para estudiar. Incluye el resumen completo, los modulos divididos por tema y las soluciones de las pruebas pasadas. Es la carpeta principal para consultar el material final.
* resumen_i2/: Contiene el codigo fuente en LaTeX del resumen general completo (estudio_i2.tex) y los textos originales de cada seccion.
* resumen_por_partes/: Contiene el resumen general modularizado. Cada tema del curso (MRP, Proyectos, Colas, etc.) tiene su propia subcarpeta con un archivo LaTeX independiente. Estos archivos importan el texto original, generando PDFs cortos y enfocados en un solo tema para evitar desbordamientos de informacion.
* pruebas _anteriores/: Almacena los historiales de evaluaciones pasadas.
    * sol latex/: Soluciones oficiales de las pruebas transcritas a formato LaTeX. Todas siguen un formato pedagogico estandarizado que separa el enunciado original del desarrollo de la solucion.
    * markdown/: Transcripciones y apuntes crudos de las soluciones en formato Markdown.

## Como utilizar la Skill de GOP (tutor_gop)

El repositorio incluye una "Skill" estructurada para ser consumida por asistentes de inteligencia artificial. Esta skill dota a la IA del conocimiento metodologico exacto, el estilo de resolucion y los criterios de evaluacion especificos del curso.

Ubicacion de la skill: .claude/skills/tutor_gop/

Para utilizar la skill, el asistente o entorno compatible debe leer las instrucciones base en .claude/skills/tutor_gop/SKILL.md al inicio del contexto. Una vez activada, la skill permite a la IA:

1. Leer la teoria estandarizada del curso desde el directorio reference/ (que incluye apuntes clave de Planificacion Agregada, MRP, Proyectos PERT, Bodegas y Variabilidad).
2. Estudiar los ejemplos historicos de evaluacion desde el directorio examples/ para imitar el formato y nivel de exigencia de las pautas oficiales de años anteriores.
3. Actuar como un tutor estricto que modela problemas paso a paso, usando terminologia precisa (Lote a Lote, Silver-Meal, ecuacion Kingman VUT, etc.) e identificando "trampas" clasicas de las pruebas.

Si utilizas un cliente de terminal o IDE compatible con este estandar de skills, el asistente cargara automaticamente estas directrices cuando trabajes dentro de este repositorio, asegurando respuestas calibradas al nivel del curso.
