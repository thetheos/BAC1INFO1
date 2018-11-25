class E:
    def m(self):
        print("E 1")
    def n(self):
        print("E 2")
    def p(self):
        self.n()   # appel à la méthode m1 sur la même instance

class F(E):
   def q(self):
       print("F 1")
   def n(self):
       super().n() # appeler la méthode définie sur la classe mère
       print("F 2")
   def r(self):
        self.m() # appel à la méthode m1 sur la même instance

"""
La fonction super() appele la classe mère directe de la classe dans laquelle elle est appelée

"""

f = F()
f.q()#F 1
f.m()#E 1
f.r()#E 1
f.n()#E 2, F 2
f.p()#E 2, F 2