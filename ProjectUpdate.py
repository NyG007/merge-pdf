from pypdf import PdfWriter
import os

writer = PdfWriter()

lista_arquivos = sorted(os.listdir("arquivos"))

for arquivo in lista_arquivos:
    if arquivo.lower().endswith(".pdf"):
        caminho = f"arquivos/{arquivo}"
        writer.append(caminho)

with open("PDF Final.pdf", "wb") as f:
    writer.write(f)