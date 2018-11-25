class A:
  def m1(self):
      print("A 1")
  def m2(self):
      print("A 2")
  def m3(self):
      self.m1()   # appel à la méthode m1 sur la même instance
  def nom(self):
      return "A"

class B(A):
  def m2(self):
      print("B 2")

class C(A):
    def m1(self):
        print("C 1")
    def nom(self):
        return "C"

class D(C):
    def m2(self):
        print("D 2")

"""
Le mot self pointe vers l'instance d'un objet de cette classe.






"""


a = A()
print(a.nom()) #A
a.m1()#A 1
a.m2()#A 2
a.m3()#A 1
b = B()
print(b.nom())#A
b.m1()#A 1
b.m2()#B 2
b.m3()# A 1
c = C()
print(c.nom())#C
c.m1()#C 1
c.m2()#A 2
c.m3()#C 1
d = D()
print(d.nom())#C
d.m1()#C 1
d.m2()# D 2 
d.m3()#C 1
