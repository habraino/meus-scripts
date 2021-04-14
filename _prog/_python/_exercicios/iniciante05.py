#!/usr/bin/python3.6
# Problema da conjectura de Goldbach

print('*'*50)
print('\t\tPROBLEMA DA CONJECTURA DE GOLDBACH')
print('*'*50)

# método para verificar se num é primo
def testaPrimo(n):
    cont = 1
    for i in range(2, n):
        if n % i == 0:
            cont += 1

    if cont != 1:
        return False
    else:
        return True

# método para verificar se num é par
def isPar(n):
    return True if n % 2 == 0 else False


# pede para usuário informar um número inteiro
num = int(input('Informe um número par: '))

# obriga o usuário a informar um número par
while isPar(num) == False:
    num = int(input('Informe um número par: '))

# crio uma lista para armazenar os números primos
primo = list()

# pega os possíveis num primo
for j in range(2, num):
    if testaPrimo(j) == True: # caso j for primo
        primo.append(j)
    else:
        pass

# fatia o num para retornar 2 resultados primos
for i in primo[:]:
    res = num - i
    if testaPrimo(res) == True: # caso resultado for primo
        print('Resultado em primo: ', end='')
        print(i, end=', ')
        print(res)
        break




