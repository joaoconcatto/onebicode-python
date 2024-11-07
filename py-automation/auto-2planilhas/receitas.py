from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data_receitas = [
    ['Ano', 'Receita'],
    [2017, 60000],
    [2018, 70000],
    [2019, 85000],
    [2020, 55000],
    [2021, 89000],
    [2022, 95000]
]

for d in data_receitas:
    ws.append(d)


wb.save('auto-2planilhas/planilhas/receitas.xlsx')