try:
    num = int(input("Informe um valor inteiro: "))
except ValueError:
    num = int(input("Informe um valor inteiro: "))
finally:
    print(num)
