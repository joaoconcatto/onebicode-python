import random

# 1- Sorteando um valor aleatório de uma lista
list1 = [7,6,123,4,412,12,32,1,2,90]

print(random.choice(list1))


# 2- Gera um número aleatório em um intervalo de valores
r1 = random.randint(5,15)
print(r1)


# 3- Seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)


# 4- Seleciona mais de um valor aleatório
# Sintaxe: random.sample(sequencia, tamanho)

print(random.sample(list1, 4))