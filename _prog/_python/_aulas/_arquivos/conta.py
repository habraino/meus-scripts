class Cliente:
    def __init__(self, nome, sobrenome, numBi):
        self.nome = nome
        self.sobrenome = sobrenome
        self.numBi = numBi


class Conta:
    def __init__(self, numero, cliente, saldo, limite):

        print('Inicializando uma conta!')

        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def criar(numero, titular, saldo, limite):
        conta = {'numero':numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
        return conta

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print('numero: {}\nsaldo: {}'.format(self.numero, self.saldo))

    def transferir(self, destino, valor):
        retirou = self.sacar(valor)
        if retirou == False:
            return False
        else:
            destino.saldo += retirou
            return True

