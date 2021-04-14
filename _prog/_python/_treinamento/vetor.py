import math

class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return ("%s, %s" %(self.x, self.y))

    def from_point(self, P1, P2):
        return Vetor(P2[0] - P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude


