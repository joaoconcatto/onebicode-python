# for i in range(10):
#     if(i<4):
#         print(i)

# 1- Liste valores de 0 a 10 menor que 4
list_numbers = [i for i in range(10) if i<4]
print(list_numbers)

games_list = [
    "Mario Odyssey",
    "Dk Country",
    "Luigis Mansion",
    "Kirby"
]

# 2- Liste jogos que possuem a letra 'a'
new_list = [x for x in games_list if 'a' in x]
print(new_list)

# 3- Liste jogos que eu zerei
games_finished = [x for x in games_list if x != "Kirby"]
print(games_finished)