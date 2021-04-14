import os

def listar():
    #tratamento de erro
    try:
        while True:
            os.system('dir *.db' if os.name == 'ns' else 'ls *.txt')
            break
    except OSError as e:
        print(e)
        print("Não existe nenhum ficheiro no diretorio.")

listar()

