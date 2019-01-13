class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __eq__ (self, p):
        """
        @pre     -
        @post   Retourne true si la paire p est égale à l'objet.
                Retourne false sinon
        """
        if p == None:
            return False
        if self.a == p.a and self.b == p.b:
            return True
        else:
            return False


p = Pair(1,2)
q = Pair(1,2)
c = Pair(1,3)

print(p==q)
print(p==c)
