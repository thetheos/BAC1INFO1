def f():
    #return "Numéro: {0}".format(12+1/3)
    #return "Numéro: " + str(12) + "." + str(33)
    #return "Numéro: " + str(12.330)
    #return "Numéro: {0:.4f}".format ( 12 + 1/3 )
    #return "Numéro: {0:<.2}".format ( 12 + 1/3 )
    s = "abcdefegh"
    #return s[4:6]
    #return s[-5:-3]
    return s[-5:-3]

def ab(s):
  for c in s:
    if c in ["a","b"]:
      return True
  return False

def ranget2(n):
  return [ i * 2 for i in range(n+1) ]

print(ranget2(10))

print(f())