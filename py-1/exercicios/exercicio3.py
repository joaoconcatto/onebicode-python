"""
1- Cálculo de distância
    -> Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
    Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 
    para viagens mais longas.

2- Aumento salário funcionário
    -> Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
    Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""


# Desafio 1
usuario_km = float(input("Quantos quilômetros (km) deseja percorrer: "))

if(usuario_km <= 0):
    print(f'O valor da quilometragem não é válido')

elif(usuario_km <= 200):
    print('Viagem curta')
    preco_passagem = usuario_km * 0.5

elif(usuario_km > 200):
    print('Viagem longa')
    preco_passagem = usuario_km * 0.35

print(f'O preço da passagem é de R$ {preco_passagem}')


# Desafio 2
salario_func = float(input("Digite o salário do funcionário: "))

if(salario_func <= 0):
    print(f'O valor do salário está inválido...')

elif(salario_func <= 1250):
    salario_aumento = salario_func * 15/100
    salario_correcao = salario_func + (salario_func * 15/100)


elif(salario_func > 1250):
    salario_aumento = salario_func * 10/100
    salario_correcao = salario_func + (salario_func * 10/100)


print(f'O aumento de salário do funcionário que recebe {salario_func} é de: R$ {salario_aumento}, totalizando {salario_correcao}')