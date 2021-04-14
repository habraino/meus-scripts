#iniciando com poo
#trabalhando com class

class meu_objeto:
    def __init__(self):
        self.nome = 'John Lee'
        self.idade = 34
        self.sexo = 'Masculino'
        print("Chamando o construtor")

    def imprima(self, **kwargs):
        for k, v in kwargs.items():
            print('{}: {}'.format(k, v))


teste = meu_objeto()
pessoa = {'Nome':teste.nome, 'Idade':34, 'Sexo':'Masculino'}

teste.imprima(**pessoa)

