num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação a realizar (+ - * /): ')


if operacao == '+':
    result = num1 + num2

elif operacao == '-':
    result = num1 - num2

elif operacao == '*':
    result = num1 * num2

elif operacao == '/':
    result = num1 / num2

else:
    print('Erro Calculadora')
    result = 0

print(f'O resultado do cálculo é: {result:.2f}')