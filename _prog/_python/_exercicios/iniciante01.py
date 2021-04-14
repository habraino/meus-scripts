#!usr/bin/python3.6
# Problema da soma

n = int(input('Desejas ler quantos números? '))

if n > 0 and n < 1000:
    a = 1
    soma = 0
    somaPares = 0
    somaImpares = 0
    while a <= n:
        num = int(input(f"Informe o {a}º número: "))

        # Calcula a soma dos valores lidos
        soma += num
        if num % 2 == 0:
            somaPares += num # calcula todos os pares lidos
        elif num % 2 == 1:
            somaImpares += num # calcula todos os ímpares lidos

        a += 1
    print("A soma total é:",soma)
    print("A soma dos pares é:",hex(somaPares)[2::])
    print("A soma dos ímpares é:", oct(somaImpares)[2::])
print('Fim')
