games_list = [
    'Fifa 23',
    'Star Wars',
    'GTA V',
    'E-Football',
    'Dota 2',
    'God of War',
    'I-Racing',
    90.50
]


# 1- Iterando valores dentro de uma collection
for game in games_list:
    print(game)


# 2- Quando a condição for atendida, o loop será encerrado
for game in games_list:
    if game == 'Dota 2':
        break

    print(game)


# 3- Quando a condição for atendia, o loop vai pular para a próxima iteração
for game in games_list:
    if game == 'GTA V':
        continue

    print(game)


# 4- Avaliação do jogo
game_name = input('Digite o nome do jogo: ')
game_rating = int(input('Digite quantas avaliações deseja fazer no jogo: '))

sum = 0

for i in range(game_rating):
    note = float(input('Digite a nota para o jogo: '))
    sum += note

print(f'A média de avaliação do jogo {game_name} é: {sum/game_rating:.2f} pontos.')