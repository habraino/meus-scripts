nomes = []

while True:
	print('1 → adicionar')
	print("2 → listar")
	print("3 → remover")
	print("4 → sair")
	user = int(input("O que desejas fazer? "))
	if user == 1: 
		nome = input("Informe o seu nome: ")
		if nome not in nomes:
			nomes.append(nome)
		else:
			print("O nome ja esta na lista. ")
	if user == 2:
		for n in nomes:
			print(n)
	if user == 4:
		break

