class Matriz(object):
    name_class = "My Matriz"

    def __init__(self, n, m):
        self.matriz = [[None for i in range(m)] for j in range(n)]
        self.line = n
        self.column = m
    
    def __getitem__(self, i):
        return self.matriz[i]
    
    def __add__(self, b):
        c = Matriz(self.line, self.column)

        for i in range(self.line):
            for j in range(self.column):
                c[i][j] = self[i][j] + b[i][j]
        return c

    @staticmethod
    def name():
        print(Matriz.name_class)

