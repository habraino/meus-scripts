numero = 42

chute = int(input("Chute um número -> "))

acertou = chute == numero
maior = chute > numero
menor = chute > numero

if(acertou):
    print("Você acertou!")
elif(maior):
    print("Você errou! Chute um número menor!")
elif(menor):
    print("Você errou! Chute um número maior!")
