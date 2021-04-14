numero = 42
tent = 3
chance = 1

while(chance <= tent):
    print("Tentativas de {} de {}".format(chance, tent))
    chute = int(input("Chute um número -> "))
    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if(acertou):
        print("Você acertou!")
        break
    elif(maior):
        print("Você errou! Chute um número menor!")
    elif(menor):
        print("Você errou! Chute um número maior!")
    chance += 1
print("Fim do Jogo")

