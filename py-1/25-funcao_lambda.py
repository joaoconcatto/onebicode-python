# 1- Função de potência de um número
power = lambda num: num ** 2

# 2- Função que verifica se o número é par
pair = lambda x: x % 2 == 0

# 3- Função que divide um número por outro
div_num = lambda x, y : x / y

# 4- Função que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(pair(10))
print(div_num(10, 2))
print(reverse('João'))