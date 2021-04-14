base = int(input("Informe a base: "))
expo = int(input("Informe o expo: "))

prod = 1
cont = 1
while cont <= expo:
    prod *= base
    cont += 1

print("{} elevado a {} = {}".format(base, expo, prod))

    
    
                
