"""
1- Antecessor e Sucessor de um número:
    -> Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.

2- Média de 4 notas
    -> Escreva um programa em Python que leia quatro números e calcule a média entre esses números
"""

# Desafio 1
numeroPrograma = int(input("Digite um número: "))

print(f"Antecessor do número {numeroPrograma} é: {numeroPrograma - 1} e o Sucessor do número é: {numeroPrograma + 1}")

# Desafio 2
note1 = float(input("Digite a primeira nota: "))
note2 = float(input("Digite a segunda nota: "))
note3 = float(input("Digite a terceira nota: "))
note4 = float(input("Digite a quarta nota: "))

media = (note1 + note2 + note3 + note4) / 4

print(f"A média das notas é {media}")