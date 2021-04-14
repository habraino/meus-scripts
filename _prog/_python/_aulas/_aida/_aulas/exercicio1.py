cont = 0
soma = 0
b = float(input("Digite uma altura: "))
while b > 0:
    cont += 1
    soma += b 
    b = float(input("Digite outra altura: "))
    
print("A soma é: {}".format(soma))

