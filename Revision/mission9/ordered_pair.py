class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return "{}, {}".format(self.a, self.b)

    def opposite(self):
        return Pair(-self.a,-self.b)



class OrderedPair:
    '''
    Représente une paire de deux entiers.
    Cette paire est considérée comme ordonnée si a est plus petit ou égal à b
    '''

    def __init__(self):
        self.p = Pair(0, 0)
        self.ordered = True

    def set_a(self, n_a):
        """
        @pre -
        @post donne au premier élément de la paire la valeur n_a
        """
        self.p.a = n_a
        if self.p.a <= self.p.b:
            self.ordered = True
        else:
            self.ordered = False
        

    def set_b(self, n_b):
        """
        @pre -
        @post donne au second élément de la paire la valeur n_b
        """
        self.p.b = n_b
        if self.p.b < self.p.a:
            self.ordered = False
        else:
            self.ordered = True

    def __str__(self):
        return str(self.ordered)


p = OrderedPair()   
p.set_b(2)
print(p)     