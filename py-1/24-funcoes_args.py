"""
*args - Utilizamos ele quando não temos certeza do número de argumentos
      - Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também as chaves para cada argumento
         - Os argumentos são passados como um dicionário
"""

# 1- Soma de números
def soma_total(*num):
    total = 0 
    for n in num:
        total += n

    print(f'Soma total é: {total}')

soma_total(7,9,12,18,23)

# 2- Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')

curso_python = presentation(name="Python", category="Back-End", level="Iniciante")
print()
curso_js = presentation(name="JavaScript - React", category="Front-End", level="Avançado" )