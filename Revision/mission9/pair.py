class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return "{}, {}".format(self.a, self.b)

    def opposite(self):
        return Pair(-self.a,-self.b)


p = Pair(10, -2)
print(p)            # affiche "10, -2"
p.a = 12
print(p)            # affiche "12, -2"
q = p.opposite()
print(p)            # affiche "12, -2"
print(q)            # affiche "-12, 2"