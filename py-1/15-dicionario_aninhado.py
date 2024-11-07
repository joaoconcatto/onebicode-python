import pprint

games_dict = {
    "Resident Evil 4": {
        'year_launch': 2023,
        'classification': 9.8,
        'genre': ['ação','terror']
    },

    "Mario Odyssey": {
        'year_launch': 2017,
        'classification': 10.0,
        'genre': ['aventura','3d']
    },

    "Donkey Kong Country": {
        'year_launch': 1995,
        'classification': 9.5,
        'genre': ['aventura', '2d']
    }
}

# Identando o output no terminal
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games_dict)

print(games_dict["Mario Odyssey"]['genre']) # 1- Buscar informações dentro de um dicionário aninhado
games_dict['Mario Odyssey']['players'] = 1 #  2- Adicionar novo item no dicionario aninhado
print(games_dict['Mario Odyssey'])
del games_dict["Resident Evil 4"] #           3- Excluir um dicionario do dicionario aninhado
pp.pprint(games_dict)