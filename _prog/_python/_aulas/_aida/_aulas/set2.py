lista1 = ['Silvania', 'Sonilsa', 'Fábio', 'Fábio', 'Anita','Teclado', 'Rato']
lista2 = ['Computador', 'Monitor', 'Rato', 'Teclado', 'Sonilsa']

setter1 = set(lista1) # crio um novo set
setter2 = set(lista2)

'''
print(setter1)
# serve para adicionar novo elemento
setter1.add('Aida')
print(setter1)

print('******************************************************************************')

copia = setter1.copy()
setter1.add('Hebraino')

print("Cópia de Setter1:",copia)

print("Set1:",setter1)
'''

# retorna diferença entre os sets
#print(setter2.difference(setter1))

# intersecção entre os sets
#print("Intersecção:",setter1.intersection(setter2))

#  união entre os sets
print("União:",setter1.union(setter2))

print(setter1.pop())

