import os
import re

dir_path = "/home/fabian/src/gop_2026/pronostico_examen/tarjetas pdf/materia"

for filename in os.listdir(dir_path):
    if not filename.endswith(".tex"): continue
    filepath = os.path.join(dir_path, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    def replacer(match):
        cmd = match.group(1) # tarjetavf o tarjetaabierta
        tema = match.group(2) # Tema
        
        t_lower = tema.lower()
        if "meta" in t_lower:
            new_tag = "Examen (La Meta)"
        elif "tps" in t_lower or "lean" in t_lower:
            new_tag = "Examen (60\\% Mat. Nueva)"
        elif "casos" in t_lower or "hospitales" in t_lower or "barilla" in t_lower or "zara" in t_lower:
            new_tag = "Examen (60\\% Mat. Nueva)"
        elif "látigo" in t_lower or "cadena" in t_lower or "suministro" in t_lower:
            new_tag = "Examen (60\\% Mat. Nueva)"
        elif "calidad" in t_lower:
            new_tag = "Examen (60\\% Mat. Nueva)"
        elif "bodegas" in t_lower or "localización" in t_lower:
            new_tag = "Examen (60\\% Mat. Nueva)"
        elif "colas" in t_lower or "variabilidad" in t_lower or "little" in t_lower:
            new_tag = "Examen (40\\% I2)"
        elif "proyectos" in t_lower or "mrp" in t_lower or "inventarios" in t_lower or "eoq" in t_lower:
            new_tag = "Examen (40\\% I1)"
        else:
            new_tag = "Examen"

        return f"\\{cmd}{{{tema}}}{{{new_tag}}}"

    new_content = re.sub(r'\\(tarjetavf|tarjetaabierta)\{([^}]+)\}\{([^}]+)\}', replacer, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Tags updated")
