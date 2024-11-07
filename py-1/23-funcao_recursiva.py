"""
Fatorial:
    -> 3 - 3*2*1
    -> 5- 5*4*3*2*1
"""

# 1- Fatoral de um número
def factorial(num):
    if num == 1:
        return 1
    
    else:
        return (num*factorial(num-1))
    

number = int(input('Digite o número: '))
print(f'O fatorial de {number} é: {factorial(number)}')

# 2- Soma total de um número
def soma_factorial(num):
    if num == 1:
        return 1
    
    else:
        return (num+factorial(num-1))
    
number2 = int(input('Digite o número: '))
print(f'A soma do fatorial de {number2} é: {soma_factorial(number2)}')