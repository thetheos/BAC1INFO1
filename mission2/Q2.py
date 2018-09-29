a = 0
b = 1
c = 2

a = b       # ligne 1 1,1,2
a = a*2     # ligne 2 1,1,2
b = 17      # ligne 3 1,17,2
c = a+b     # ligne 4 1,17,19
a = b-c     # ligne 5 -2,17,19
c = a+b+c+a # ligne 6 -2,17,32
print(a, b, c)