# file_name: return_v1.py

def dados(nome, idade=None):
    if idade is not None:
        return (f'Nome: {nome}\nIdade: {idade}')
    else:
        return (f'Nome: {nome}\nIdade: não informada!')

dados("Brayen")
dados("Brayen", 20)