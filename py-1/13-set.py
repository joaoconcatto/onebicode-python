"""
- Não consegue recuperar valores via fatiamento ou slice 
"""

games_set = {
    'Fifa 23',
    'Star Wars',
    'GTA V',
    'E-Football',
    'Dota 2',
    'God of War',
    'I-Racing'
}

print(games_set)
print(len(games_set)) #         1- Buscar o tamanho do set

example_set = {'Fifa 23', True, 1, 90.50}
print(example_set) #            2- True e 1 são considerados valores booleanos
games_set.update(example_set) # 3- Adicionar valores de outros set
print(games_set)