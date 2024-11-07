user_infos1 = [
    'João', 
    22,
    1.73,
    59,
    'Caxias do Sul',
    'Rio Grande do Sul',
    'Técnico de Informática'
]

print(len(user_infos1)) #                   1- Tamanho da lista
print(user_infos1.index("Caxias do Sul")) # 2- Recuperar um item na lista pelo índice
user_infos1.append(2500) #                  3- Adicionar um item ao final da lista
print(user_infos1)
# user_infos1.sort() #                      4- Ordenar a lista (Só funciona para strings)
user_infos2 = user_infos1.copy() #          5- Copiar os itens de uma lista para outra
print(user_infos2)
user_infos2.remove(2500) #                  6- Remover um item de uma lista
print(user_infos2)