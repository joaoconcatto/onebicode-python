gameDescription = """
EA FC 25 é um jogo de futebol desenvolvido pela Ea Sports single e multiplayer para os
fanáticos do mundo dos games esportivos.
"""
gameName = "Ea Football 25"

print(gameName.upper()) #           1- Retornar string em maiúsculo
print(gameName.lower()) #           2- Retornar string em minúsculo
print(gameName.capitalize()) #      3- Retornar a primeira letra da string em maiúsculo
print(gameName.title())
print(gameName.center(12,'-')) #    4- Retornar a string centralizada
print(gameName.find("a")) #         5- Procurar por um caractere na string
print(gameName.count("a"))#         6- Retorna a contagem do número de caracteres
print(gameName.replace("Ea", "E"))# 7- Altera um determinado valor da string por outro
print(gameName.split(','))#         8- Quebra as strings em valores menores, útil para análise de dados