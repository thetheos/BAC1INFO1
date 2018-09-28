"""
Réalise par Vanden Driessche Théo et Guillaume van der Rest

"""
c = 1
powSum = 0
while c != 11:
    powSum += c*c
    print(c, "\t", c*c, "\t", powSum, "\t", (c * (c + 1) * (2*c+1) // 6) )
    c += 1


    