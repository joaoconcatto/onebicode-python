# 1- Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(fname, lname):
    print(f'Nome completo: {fname} {lname}')

full_name('João', 'Dos Reis')


# 2- Crie uma função que some dois números dos parâmetros
def somar_valores(a,b):
    print(a + b)

somar_valores(3,4)

# 3- Argumentos default em uma função
def address(country="Brasil"):
    print(f'País: {country}')

address()
address("Canadá")

# 4- Avaliação e média do jogo
def rating_game(qtdRating):
    game_name = input('Nome do jogo: ')
    sum = 0

    for i in range(qtdRating):
        rating = float(input("Digite a nota do jogo: "))
        sum += rating

    print(f'{game_name} tem {sum:.2f} pontos totalizados')
    print(f'Média de: {sum/qtdRating:.2f} pontos')

rating_game(4)