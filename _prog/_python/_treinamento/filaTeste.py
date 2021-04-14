#programa baseado em fila, lista e pilhas
from collections import deque#usamos está biblioteca para trabalhar com filas

def p_f_l():
    lista = deque(["PHP", "Javascript", "Ruby", "Python", "C#", "C", "Java", "GO"])
    while True:
        print(list(lista))
        opcao = str(input("O que queres? Adicionar(a), Recuperar ultimo(ru) ou Recuperar Primeiro(rp): "))

        if(opcao.lower() == "a"):
            lista.append(str(input("Insira o último valor: ")))
        elif(opcao.lower() == "ru"):
            rec = lista.pop()
            print(f"O valor recuperado foi {rec}")
        else:#se não digitar nada a lista sempre vai remover o primeiro
            rec = lista.popleft()
            print(f"O valor recuperado foi {rec}")

        sair = str(input("O queres continuar? Sim ou Não?: "))

        if(sair.lower() == "não" or sair.lower() == "nao"):
            return False

p_f_l()