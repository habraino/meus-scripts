import time, os

def letraHora():
    arq = open("captura.txt", "a+")
    if os.path.isfile('captura.txt') == True:
        print(os.path.getsize('captura.txt'))
    if(os.path.getsize("captura.txt") <= 2):
        cap = input("Insira o texto: ")
        #arq.write(cap+"\nO calendario do dia arquivo foi salvo: "+time.asctime())
        arq.write(cap)
    else:
        dividir = "="*50
        cap = input("Insira o texto: ")
        arq.write("\n"+dividir+"\n"+cap+"\nO calendario do dia arquivo foi salvo: "+time.asctime())

letraHora()
