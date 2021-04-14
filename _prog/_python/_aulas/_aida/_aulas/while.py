'''
cont = 20

while (cont >= 1):
    print(cont)

    cont -= 1
'''

'''
cont = 0# contador
soma = 0# acumulador
media = 0

a = 1# controlador

while a <= 4:
    nota = float(input('Informe {}ª nota: '.format(a)))
    cont += 1
    soma += nota

    a += 1

media = soma / cont

print('Foram lidas {} notas.'.format(cont))
print('A soma total é: {}'.format(soma))
print('A média final é: {}'.format(media))
'''

'''
soma = 0
num = int(input('Informe um valor [999] para terminar: '))

while (num != 999):
    soma += num
    num = int(input('Informe outro valor [999] para terminar: '))

print('A soma total: {}'.format(soma))
'''

sair = True
soma = 0
num = 0

while (sair):
    #soma += num
    num = int(input('Digite qualquer número positivo: '))
    
    if num <= 0:
        sair = False
    else:
        soma += num
    
print('A soma total: {}'.format(soma))
