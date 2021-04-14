from pessoa import Pessoa

# declaração das variáveis
p = dict()
cont = 1
nome = ''
idade = 0
sexo = ''

# pega dados de quatro pessoas
while cont <= 2:
    print('\n-------- %dª PESSOA -------'%cont)
    nome = input('Informe o seu nome: ').strip().title()
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo: ').strip().upper()[0]

    pessoa = Pessoa(nome, idade, sexo)

    p['Nome'] = pessoa.getNome()
    p['Idade'] = pessoa.getIdade()
    p['Sexo'] = pessoa.getSexo()

    cont += 1

print(p)

