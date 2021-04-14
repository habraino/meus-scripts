
#calcula a soma da lista mesmo com listas alinhadas
def nosted_sum(t):
    s = 0
    for i in t:
        if type(i) == list:
            for j in i:
                s += j
        elif type(i) == int:
                s += i
    print("Soma total é:",s)

# calcula comutativa
def cumsum(t):
    l = list()
    item = 0
    for j in range(len(t)):
        item += t[j]
        l.append(item)

    print("Soma comutativa:",l)

# apaga o primeiro e o último elemento da lista
def middle(t):
    print("Itens do meio:",t[1:-1])

# verfica se existe duplicatas na lista
def has_duplicates(t):
    cont = 0
    for i in range(0, len(t)):
        for j in range(0, len(t)):
            if (t[i] == t[j]):
                cont += 1

    if cont > len(t):
        return True
    else:
        return False


if __name__ == '__main__':
    lista1 = [[1, 2], 3, [4, 5, 6], [2, 4, 5], 8, [4, 5, 6, 7], [2, 6, 7, 8, 9]]
    nosted_sum(lista1)

    lista2 = [2, 3, 4, 5]
    cumsum(lista2)

    lista3 = [1, 6, 3, 4]
    middle(lista3)

    lista4 = [3, 1, 2, 3]
    print(has_duplicates(lista4))


