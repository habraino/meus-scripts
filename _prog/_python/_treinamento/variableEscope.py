def counter():
    num = 0

    def increment():
        nonlocal num
        num += 1
        return num
    return increment

c = counter()
print(c())
print(c())
print(c())
