# module fibonacci

def fibo(n):
    """ write the sequency of fibonacci to n"""
    a, b = 0, 1

    while b < n:
        print(b)
        a, b = b, a + b
        
def fibo2(n):
    """ Return the sequency of fibonacci to n"""

    result = []

    a, b = 0, 1

    while b < n:
        result.append(b)

        a, b = b, a + b
    print(result)

if __name__ == '__main__':
    fibo2(100)
