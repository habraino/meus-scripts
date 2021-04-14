class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Ponto({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "{}, {}".format(self.x ** 2, self.y ** 2)


if __name__ == '__main__':
    p1 = Ponto(5, 10)
    p2 = eval(repr(p1))

    print(p1)
    print("quadrado:",p2)

