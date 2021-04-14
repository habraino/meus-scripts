# declaração das variáveis
lista = []
soma = 0
mult = 0
media = 0
num = 0

# faz a leitura dos 7 números
for i in range(0, 7):
    num = int(input('Informe o {}º num: '.format(i+1)))
    lista.append(num)
    soma = soma + num

media = soma / len(lista) # calcula a média aritmétrica

print('*'*35)
print("Soma total: {}".format(soma))
print("Média aritmétrica: {:.2f}".format(media))

# faz a multiplicação dos num
for j in range(0, len(lista)):
    mult = j * lista[j]
    print('Multiplicação do elem: {} * {} = {}'.format(j, lista[j], mult))
    
