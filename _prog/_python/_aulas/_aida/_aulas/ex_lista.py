lista = list()
nome = ''
while nome.lower() != "q": 
    nome = input("Informe um nome: ")
    if nome.lower() == "q":
        break
    
    if nome not in lista:
        lista.append(nome)
    else:
        print("já está na lista!")
    
print(lista)        

        
