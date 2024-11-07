game_name = input('Digite o nome do jogo: ')
qtd_rating = 0
total_rating = 0
rating = True
average = 0

while(rating):
    rating = float(input('Digite a nota do jogo: '))

    if(rating != -1):
        total_rating += rating
        qtd_rating += 1
        average = total_rating / qtd_rating
        
    else:
        break

print(f'A média do jogo {game_name} é: {average:.2f} pontos.')