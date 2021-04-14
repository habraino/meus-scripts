#!/usr/bin/python3
# Problema da sequência de Fibonacci

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

n = int(input('Informe um valor: '))

if n >= 0 and n <= 40:
    #print(fibo(n))
    fib = list()
    cont = 0
    a, b = 0, 1
    fib.append(a)

    while cont < n:
        b += fib[a]
        fib.append(b)
        a = cont

        cont += 1
    print(fib)


