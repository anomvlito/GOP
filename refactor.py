import os
import re

base_dir = "/home/fabian/src/gop_2026/pruebas _anteriores/sol latex"
out_dir = "/home/fabian/src/gop_2026/ejercicios_por_tema"

files = [
    os.path.join(base_dir, "I2_2020", "I2_2020_Solucion.tex"),
    os.path.join(base_dir, "I2_2022", "I2_2022_Solucion.tex"),
    os.path.join(base_dir, "I2_2023_1", "I2_2023_1_Solucion.tex"),
    os.path.join(base_dir, "I2_2024_1", "I2_2024_1_Solucion.tex"),
    os.path.join(base_dir, "I2_2025_1", "I2_2025_1_Solucion.tex")
]

# Create output directories
topics = {
    "01_planificacion_agregada": [],
    "02_mrp_e_inventarios": [],
    "03_proyectos_pert_cpm": [],
    "04_variabilidad_colas": [],
    "05_localizacion_bodegas": []
}

for topic in topics.keys():
    os.makedirs(os.path.join(out_dir, topic), exist_ok=True)

def extract_preamble(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"(.*?\\begin{document})", content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

preamble = extract_preamble(files[0])

# Mapping substrings in subsection to topic
mapping = {
    "Planificación Agregada": "01_planificacion_agregada",
    "Producción de Vacunas": "01_planificacion_agregada",
    "Programación Matemática para MRP": "02_mrp_e_inventarios",
    "MRP de Bicicletas": "02_mrp_e_inventarios",
    "Gestión de Inventarios": "02_mrp_e_inventarios",
    "Wagner-Whitin": "02_mrp_e_inventarios",
    "Requerimiento de Materiales (MRP)": "02_mrp_e_inventarios",
    "Administración de Proyectos": "03_proyectos_pert_cpm",
    "Riesgo en Proyectos (PERT)": "03_proyectos_pert_cpm",
    "Planificación de Proyectos": "03_proyectos_pert_cpm",
    "Control de Proyectos": "03_proyectos_pert_cpm",
    "Variabilidad": "04_variabilidad_colas",
    "Localización": "05_localizacion_bodegas",
}

for fpath in files:
    if not os.path.exists(fpath):
        print(f"Skipping {fpath} (not found)")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all \subsection*{...} that start with Pregunta or Opción
    # Use split to separate the document into parts
    parts = re.split(r"(\\subsection\*\{(?:Pregunta|Opción).*?\})", content)
    
    # parts[0] is everything before the first subsection
    # Then parts[1] is the subsection title, parts[2] is its content, etc.
    # Exclude \newpage at the end of the content
    
    for i in range(1, len(parts), 2):
        title = parts[i]
        text = parts[i+1]
        
        # Clean up text (remove trailing \end{document} if present)
        text = text.replace(r"\end{document}", "").strip()
        # Remove trailing \newpage
        if text.endswith(r"\newpage"):
            text = text[:-8].strip()
            
        found_topic = None
        for key, topic in mapping.items():
            if key.lower() in title.lower():
                found_topic = topic
                break
                
        if found_topic:
            # Prepend exam source to title for context
            exam_name = os.path.basename(os.path.dirname(fpath))
            clean_title = title.replace(r"\subsection*{", "").replace("}", "")
            new_title = f"\\subsection*{{[{exam_name}] {clean_title}}}"
            topics[found_topic].append(f"{new_title}\n{text}\n\n\\newpage\n\n")
        else:
            print(f"Could not map: {title}")

# Write the new files
topic_titles = {
    "01_planificacion_agregada": "Planificación Agregada",
    "02_mrp_e_inventarios": "MRP e Inventarios",
    "03_proyectos_pert_cpm": "Proyectos PERT y CPM",
    "04_variabilidad_colas": "Variabilidad y Teoría de Colas",
    "05_localizacion_bodegas": "Localización de Bodegas"
}

for topic, contents in topics.items():
    if not contents:
        continue
        
    out_file = os.path.join(out_dir, topic, f"{topic}.tex")
    
    custom_preamble = preamble.replace(
        r"\fancyhead[L]{\small\textbf{GOP ICS3213} --- Pauta Interrogación 2 (1er Semestre 2020)}",
        f"\\fancyhead[L]{{\\small\\textbf{{GOP ICS3213}} --- Compendio de Ejercicios: {topic_titles[topic]}}}"
    )
    
    title_page = f"""
% ════════════════════════════════════════════════════════════════════════════
% PORTADA
% ════════════════════════════════════════════════════════════════════════════
\\begin{{titlepage}}
  \\centering
  \\vspace*{{2cm}}
  {{\\Huge\\bfseries\\color{{gopcyan}} Compendio de Ejercicios\\par}}
  \\vspace{{0.4cm}}
  {{\\LARGE\\bfseries {topic_titles[topic]}\\par}}
  \\vspace{{0.3cm}}
  {{\\large Gestión de Operaciones (ICS3213)\\par}}
  \\vspace{{1.2cm}}
  \\rule{{\\textwidth}}{{0.4pt}}
  \\vspace{{0.4cm}}
  {{\\small Material extraído de pautas oficiales de Interrogaciones I2.\\par}}
  \\vspace{{0.4cm}}
  \\rule{{\\textwidth}}{{0.4pt}}
  \\vfill
\\end{{titlepage}}

\\newpage
"""
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(custom_preamble + "\n")
        f.write(title_page)
        f.write("\\section*{" + topic_titles[topic] + "}\n\n")
        for c in contents:
            f.write(c)
        f.write("\\end{document}\n")

print("Files generated successfully.")
