import PyPDF2
import os 

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
print(lista_arquivos)

