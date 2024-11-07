from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data_despesa = [
    ['Ano', 'Despesa'],
    [2017, 45000],
    [2018, 50000],
    [2019, 64000],
    [2020, 75000],
    [2021, 56000],
    [2022, 90000]
]

for d in data_despesa:
    ws.append(d)


wb.save('auto-2planilhas/planilhas/despesas.xlsx')