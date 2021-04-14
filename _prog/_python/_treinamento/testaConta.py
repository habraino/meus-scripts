from conta import *

cl1 = Cliente('Brayen', 169791)
c1 = Conta(100, cl1)

cl2 = Cliente('John', 234567)
c2 = Conta(400, cl2)

cl3 = Cliente('Maria', 123456)
c3 = Conta(500, cl3)

# imprime os ids
print("ID Nº:",c1.getId())
print("ID Nº:",c2.getId())
print("ID Nº:",c3.getId())

# apresenta total de contas usando instância e a classe
print('Nº de conta usando instância:',c1.get_total_conta())
print('Nº de conta usando a classe: ', Conta.get_total_conta())

