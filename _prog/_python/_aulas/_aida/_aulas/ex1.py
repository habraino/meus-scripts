print('*'*40)
print('\tBem-vindos ao meu programa')
print('*'*40)
idades = list()
cres = list()
decres = list()
a = 1

while a <= 5:
    idade = int(input("Informe a idade da {}ª pessoa: ".format(a)))
    idades.append(idade)
    a += 1
idades.sort()
print("Em ordem crescente: {}".format(idades))
idades.sort(reverse=True)
print("Em ordem decrescente: {}".format(idades))

print("A maior idade lida é: {} anos.".format(max(idades)))
