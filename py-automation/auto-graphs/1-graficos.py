from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, series


wb = Workbook()
ws = wb.active


data = [
    ['Ano', 'Lucro', 'Custos'],
    [2017, 40, 30],
    [2018, 35, 25],
    [2019, 30, 20],
    [2020, 10, 10],
    [2021, 15, 10],
    [2022, 25, 15]
]

for d in data:
    ws.append(d)


# criação do Gráfico
chart = AreaChart()
chart.title = 'Lucro x Custos por Ano'
chart.style = 12
chart.x_axis.title = 'Ano'
chart.y_axis.title = 'Porcentagem'

categorias = Reference(
    ws,
    min_col=1,
    min_row=1,
    max_row=7
)

dados = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_col=3,
    max_row=7
)

chart.add_data(dados, titles_from_data=True)
chart.set_categories(categorias)
ws.add_chart(chart, 'A8')

wb.save('graphs/planilhas/chart.xlsx')
