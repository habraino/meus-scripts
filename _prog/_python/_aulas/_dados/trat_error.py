num = 0
try:
    num = int(input('Informe um valor: '))
except ValueError:
    num = int(input('Informe um valor: '))
finally:
        print("O valor informado é: %d"%num)
    