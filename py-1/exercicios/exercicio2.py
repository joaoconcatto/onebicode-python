"""
1- Substituir caracter repetido:
    -> Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências
    de seu primeiro caractere foram alteradas para $, exceto o próprio caractere.
    Ex.: Fifa 23 -> Fi$a 23

2- Troca de caracteres:
    -> Escreva um programa Python para obter uma única string de duas strings fornecidas separadas por um espaço
    e troque os dois primeiros caracteres de cada string.
    Ex.: abc xyz -> xyc abz
"""

# Desafio 1
name = "League of Legends"

char = name[1].lower()
new_name = name.replace(char, '$')
new_name = char + new_name[1:]
print(new_name)