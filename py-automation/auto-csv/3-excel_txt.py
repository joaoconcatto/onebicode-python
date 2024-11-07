from openpyxl import Workbook

print('Lendo dados do arquivo de texto...')
print()


# 1- lendo o arquivo de texto e separando as linhas para iteração
file_txt = open('auto-csv/files/gastos.txt', 'r', encoding='utf-8').read()
list_data = file_txt.splitlines()


# 2- iterar os valores da lista e estruturar a lista
for i in range(0, len(list_data)):
    list_data[i] = list_data[i].split(',')


# 3- criar a planilha
wb = Workbook()
name = 'auto-csv/planilhas/planilha2.xlsx'

ws1 = wb.active
ws1.title = 'Planilha1'


for row in list_data:
    ws1.append(row)


wb.save('auto-csv/planilhas/gastos.xlsx')