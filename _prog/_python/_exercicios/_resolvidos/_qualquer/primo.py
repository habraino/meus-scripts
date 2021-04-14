a = int(input("Informe um valor inteiro: "))

cont = 0
i = 0
while i < a:
    if a % (i + 1) == 0:
        cont += 1
    i += 1

if cont == 2:
    print("Primo")
else:
    print("Composto")
