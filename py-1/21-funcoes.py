
# 1- Função que imprime "hello world"
def wellcome():
    print(f'Hello World!')

wellcome()

# 2- Função para somar dois números
def somar_valores(num1, num2):
    print(num1 + num2)

somar_valores(2,10)

# 3- Função para cadastrar 4 jogos em uma lista
games_list = []

def create_game():
    for i in range(4):
        name = input('Digite o nome do jogo para cadastrar: ')
        games_list.append(name)
        print(f'{games_list}')

create_game()