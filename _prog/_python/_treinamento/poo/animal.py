class Animal:

    def __init__(self, cor, patas):
        self._cor = cor
        self._patas = patas

    @property
    def pata(self):
        return self._patas

    @pata.setter
    def pata(self, patas):
        if self._patas < 2:
            print('animais têm duas patas no mínimo.')
        else:
            self._patas = patas

class Cachorro(Animal):

    def __init__(self, cor, patas, raca, nome):
        super().__init__(cor, patas)
        self._raca = raca
        self._nome = nome

