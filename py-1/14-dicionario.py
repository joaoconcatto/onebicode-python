game_1 = {
    'name': 'Fifa 23',
    'year_launch': 2022,
    'game_price': 90.50,
    'classification': 8.5,
    'genre': [
        'esporte',
        'um jogador',
        'multijogador',
        'modo história'
    ]
}

print(game_1)
print(game_1.get('genre')) #   1- Recuperar um elemento do dicionario
print(game_1.keys()) #         2- Buscar apenas as chaves do dicionario
print(game_1.values()) #       3- Buscar apenas os valores do dicionario
print(game_1.items()) #        4- Buscar itens do dicionario com chave e valor
game_1['players'] = 2 #        5- Adicionando itens no dicionario
print(game_1)
game_1.update({'players':1}) # 6- Atualizar itens no dicionario
print(game_1)
game_1.pop('players') #        7- Remover os itens do dicionarios
print(game_1)