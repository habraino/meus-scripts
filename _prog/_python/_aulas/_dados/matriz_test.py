from matriz import Matriz

def sub(self, b):
    c = Matriz(self.line, self.column)

    for i in range(self.line):
        for j in range(self.column):
            c[i][j] = self[i][j] - b[i][j]
    return c


if __name__ == '__main__':
    a = Matriz(3, 3)
    b = Matriz(3, 3)
    print(Matriz.name())

    for i in range(a.line):
        for j in range(a.column):
            a[i][j] = i
            b[i][j] = j

    Matriz.__sub__ = sub

    c = a - b

    print(c.matriz)
    print(a.matriz)
    print(b.matriz)
