def fat(x):
    if not isinstance(x, int):
        print('Fatorial é só para inteiros.')
        return None
    if x < 0:
        print('Fatorial é só para números positivos.')
        return None
    if x == 0:
        return 1
    else:
        return x * fat(x - 1)

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

def isPar(x):
    if x % 2 == 0:
        return True
    else:
        return False

def pow(x, y):
    return x ** y


def ack(m ,n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m -1, ack(m, n + 1))

# method that return sqrt one number 'x'
def sqrt(a):
    X = 3 # this is my const
    while True:
        y = (X + a / X) / 2
        if X == y:
            break
        X = y
    return X


