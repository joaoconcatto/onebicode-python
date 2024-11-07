gameDescription = """
EA FC 25 é um jogo de futebol desenvolvido pela Ea Sports single e multiplayer para os
fanáticos do mundo dos games esportivos.
"""
gameName = "EA FC 25"

"""
    Slice de strings:
    -> string[início:fim] - índice começa na posição 0 | índice final -1
    -> string[início:fim:passo] - passo determina o incremento
"""

# 1- Busque toda a string a partir da primeira posição
print(gameName[0:])

# 2- Busque toda a string até a última posição
print(gameName[:8])

# 3- Busque toda a string da terceira até a última posição
print(gameName[2:])

# 4- Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5- Busque toda a string nos índices ímpares
print(gameName[1::2])

# 6- Inverter uma string
print(gameName[::-1])