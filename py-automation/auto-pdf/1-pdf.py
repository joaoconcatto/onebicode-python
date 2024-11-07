import PyPDF2 as pdf
from PyPDF2 import PdfReader


# 1- versão e métodos dessa biblioteca
print(pdf.__version__)
print(dir(pdf))


# 2- importando o arquivo pdf
file_pdf = open('auto-pdf/files/faturamento.pdf', 'rb')
reader = PdfReader(file_pdf)

info = reader.metadata


# 3- extraindo algumas informações
print(info.title)
print(info.creator)
print(info.author)
print(info.subject)
print(len(reader.pages))
print(reader.pages[0].extract_text())