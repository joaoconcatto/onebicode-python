from openpyxl import Workbook 

# 1 - criando o workbook
wb = Workbook()
name = 'auto-csv/planilhas/planilha1.xlsx'


# 2- utilizando o worksheet
ws1 = wb.active
ws1.title = 'Planilha1'


# 3- adicionando os dados
data = [
    ['Ano', 'Lucro', 'Custos'],
    [2021, '25%', '40%'],
    [2022, '45%', '50%'],
    [2023, '15%', '10%']
]

for line in data:
    ws1.append(line)


ws2 = wb.create_sheet(title='Planilha2')
ws2['D2'] = 3.14

wb.save(filename=name)