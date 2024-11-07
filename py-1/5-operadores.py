num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Aritméticos
print("\n####### Aritméticos #######")

somarValores = num1 + num2
subtrairValores = num1 - num2
dividirValores = num1 / num2
multiplicarValores = num1 * num2
restoValores = num1 % num2
exponenciarValores = num1 ** num2

print(somarValores)
print(subtrairValores)
print(dividirValores)
print(multiplicarValores)
print(restoValores)
print(exponenciarValores)

# Comparação
print("\n####### Comparação #######")

maior = num1 > num2
menor = num1 < num2
igual = num1 = num2
diferente = num1 != num2
maior_igual = num1 >= num2
menor_igual = num1 <= num2

print(maior)
print(menor)
print(igual)
print(diferente)
print(maior_igual)
print(menor_igual)

# Atribuição
print("\n####### Atribuição #######")

num1 += 1
print(num1)

num1 -= 1
print(num1)

num1 *= 1
print(num1)

num1 /= 1
print(num1)
