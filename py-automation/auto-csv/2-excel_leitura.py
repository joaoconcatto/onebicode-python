from openpyxl import load_workbook


# 1- leitura do arquivo e buscando o sheet
wb = load_workbook(filename='auto-csv/planilhas/planilha1.xlsx')
planilha1 = wb['Planilha1']


# 2- acessando um determinado valor
ano_2023 = planilha1['A4'].value
print(ano_2023)


# 3- iterando valores por meio de um loop
for i in range(2, 5):
    ano =   planilha1['A%s' %i].value
    lucro = planilha1['B%s' %i].value
    custo = planilha1['C%s' %i].value

    print("{0} teve {1} de lucro, com um custo de {2}.".format(ano, lucro, custo))

