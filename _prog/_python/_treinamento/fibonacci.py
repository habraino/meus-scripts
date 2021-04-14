def fibonacci(n):
    def step(a, b):
        return b, a+b

    a, b = 0, 1
    for i in range(n):
        a, b = step(a, b)

    return a

fib = fibonacci(20)
print(fib)

