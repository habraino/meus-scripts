nome = "Brayen Strong"

#print(nome.count("a"))

#print(nome.upper())

#print(nome.lower())

nomes = ['Abner', 'Admilson', 'Aida', 'Amilton']
num = [1, 2, 3, 4]

for i in range(0, len(nomes)):
    for j in range(0, len(num)):
        print("Nome: {} ----> Nº{}".format(nomes[j], num[j]))
    break

