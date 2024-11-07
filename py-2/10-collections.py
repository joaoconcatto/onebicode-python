from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1- Contar itens de uma lista
frutas = ["Banana", "Maçã", "Uva", "Pera", "Laranja", "Laranja", "Abacaxi", "Banana", "Banana", "Banana"]

print(frutas)
print(Counter(frutas))


# 2- Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
game1 = game('Fifa 23', 90.50, 8.5)
game2 = game('God of War', 220.00, 10)
print(game1)
print(game2)


# 3- Ordenando dicionários
studants = {"Pedro": 23, "Ana": 42, "Ronaldo": 72, "Janaina": 25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)


# 4- Utilizando fila com ambas extremidades
deq = deque([20, 30, 40, 60])
deq.appendleft(10)
deq.append(100)
print(deq)
deq.popleft()
deq.pop()
print(deq)