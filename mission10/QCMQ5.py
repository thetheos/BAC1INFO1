class E :

    cvar = 0   # variable de classe

    def __init__(self,v):
        self.var = v

    def m1(self):
        self.var += 1

    def m2(self):
        self.cvar += 1

    @classmethod
    def m3(cls):
        cls.var += 1

    @classmethod
    def m4(cls):
        pass
e = E(5)   # création d'une instance e de la classe E
e.m2()