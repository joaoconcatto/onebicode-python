import re

text = "OneBitCode: Transformamos pessoas em programadores sem limites"

# 1- Íncide inicial e final de palavras
# O 'r' siginifica que estamos trabalhando com uma string bruta [row string]

match1 = re.search(r'pessoas', text)

print('Índice inicial ', match1.start())
print('Índice final ', match1.end())


# 2- Buscar o índice que possui o ponto
site = 'https://onebitcode.com'

match2 = re.search(r'\.', site)
print(match2)


# 3- Buscar uma lista de caracteres dentro de uma frase
pattern = '[a-m]'
result = re.findall(pattern, text)
print(text)
print(result)


# 4- Verifcar o início de uma string
rule_start = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']

for f in phrases:
    if re.match(rule_start, f):
        print(f'Corresponde: {f}')
    
    else:
        print(f'Não corresponde: {f}')

print()
print()

# 5- Verificar o final de uma string
rule_end = r'!$'
phrases = ['A casa está suja', 'O dia está lindo!', 'Vamos passear']

for f in phrases:
    if re.search(rule_end, f):
        print(f'Corresponde: {f}')

    else:
        print(f'Não corresponde: {f}')