class Cliente:
    def __init__(self, nome, numBI):
        self._nome = nome
        self._numBI = numBI


class Conta:

    #__slots__ = ['_saldo', '_titular', '_limite']

    _total_conta = 0
    _id = 0

    def __init__(self, saldo, cliente, limite=1000.0):
        self._saldo = saldo
        self._titular = cliente
        self._limite = limite
        Conta._total_conta += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(self._saldo < 0):
            print('saldo não pode ser negativo')
        else:
            self._saldo = saldo

    @classmethod
    def get_total_conta(cls):
        return Conta._total_conta

    @classmethod
    def getId(cls):
        Conta._id += 1
        if Conta.__new__(cls):
            return Conta._id
