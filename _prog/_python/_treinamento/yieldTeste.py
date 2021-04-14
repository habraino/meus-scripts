def foo():
    yield 1

print(foo())


def foo1(x):
    print(x)

get = lambda x = 'My name is Brayen': foo1(x)
print(get())

