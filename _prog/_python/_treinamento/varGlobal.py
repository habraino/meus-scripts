a = 5

def test():
    global a
    a += 1
    return a

print(test())