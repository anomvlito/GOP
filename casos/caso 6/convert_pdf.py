import fitz # PyMuPDF

pdf_path = "/home/fabian/src/gop_2026/casos/caso 6/Zara_SPA.pdf"
md_path = "/home/fabian/src/gop_2026/casos/caso 6/Zara_SPA.md"

try:
    doc = fitz.open(pdf_path)
    with open(md_path, "w", encoding="utf-8") as f:
        for page in doc:
            text = page.get_text()
            f.write(text)
            f.write("\n\n---\n\n")
    print("Conversión completada con PyMuPDF.")
except Exception as e:
    print(f"Error con PyMuPDF: {e}")
    import subprocess
    try:
        subprocess.run(["pdftotext", pdf_path, md_path])
        print("Conversión completada con pdftotext.")
    except Exception as e2:
        print(f"Error con pdftotext: {e2}")

