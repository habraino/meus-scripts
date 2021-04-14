class Pessoa:

    def __init__(self, n, i, s):
        self.nome = n
        self.idade = i
        self.sexo = s

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getSexo(self):
        return self.sexo

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setSexo(self, sexo):
        self.sexo = sexo

    def read(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Sexo: {self.sexo}')

