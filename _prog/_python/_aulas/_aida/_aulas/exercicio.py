cont = 0
b = 0
c = 0.0
a = int(input("Informe uma idade: "))

while a >= 0:
    cont += 1
    b = b + a
    a = int(input("Informe outra idade: "))
   
c = b / cont
print("Foram lidas {} idade.".format(cont))
print("A soma total é {} ".format(b))
print("A media final é: {:.2f} ".format(c))

    
    
    
