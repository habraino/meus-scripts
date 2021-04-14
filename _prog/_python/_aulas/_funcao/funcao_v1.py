# file_name: funcao_v1.py

def dado(nome, idade=None):
    print(f"Nome: {nome}")

    if idade is not None:
        print(f"Idade: {idade}")
    else:
        print(f"Idade: idade não informada!")

dado("Brayen")
