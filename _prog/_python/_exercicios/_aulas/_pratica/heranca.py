class Pai:

    def __init__(self, nome, apelido):
        self._nome = nome
        self._apelido = apelido

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if len(nome) > 1:
            self._nome = nome
        else:
            print('Nome inválido!')


class Filho(Pai):
    def __init__(self, nome, apelido, idade):
        super().__init__(nome, apelido)
        self._idade = idade
