class A:

    def __init__(self,s,n):
        self.s = s
        self.n = n

    def m(self) :
        return self.n * self.n

class B(A) :
    def __init__(self,s,n) :
        A.__init__(s, n)
        self.n2 = n;

    def m(self) :
        return ( A.m() + self.n2 * self.n2 )


n = A(10,10)
print(n.m())
d = B(n)
print(B.m())