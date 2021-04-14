par = []
impar = []

cont = 1
while cont <= 100:
    if cont % 2 == 0:
        par.append(cont)
    else:
        impar.append(cont)
    
    cont += 1


print(par)
print(impar)
