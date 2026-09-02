import fitz
import os
import glob

pdfs = glob.glob('*.pdf')
for pdf in pdfs:
    md_name = pdf.replace('.pdf', '.md')
    print(f"Converting {pdf} to {md_name}...")
    doc = fitz.open(pdf)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    with open(md_name, "w") as f:
        f.write(text)
    print(f"Saved {md_name}")
