def lineCount(file):
    cont = 0
    for _ in open(file):
        cont += 1
    return cont

print("Line Size:", lineCount("teste.txt"))


def input_number(n, e=None):
    while True:
        try:
            return float(input(n))
        except ValueError:
            if e is not None:
                print(e)

a = input_number("Informe um valor: ", 'não é um número')
print(a)



