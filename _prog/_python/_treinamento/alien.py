#Alien Yks

def planeta(texto):
    cont = 0
    for x in range(len(texto)):
        if(texto[x] == texto[x].upper()):
            cont += 1

        print(f"Total de palavra são: {cont}")
planeta(str(input("E­scra o texto >> ")))