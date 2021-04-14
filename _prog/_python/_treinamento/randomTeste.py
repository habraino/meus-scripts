from random import *

s = SystemRandom()

print([s.randrange(9) for i in range(11)])

lista = ['ana', 'marta', 'joana', 'maria']
print(sample(lista, 2))
