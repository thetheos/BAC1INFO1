def chiffres_pairs(n):
    i = 1
    count = 1
    while n // 10 != 0:
        i = i * 10
        n = n //10
        count += 1

    if count % 2 == 0:
        return True
    else:
        return False
    return not int(len(str(n))) % 2

n = 0
while True :
    n = int ( input (" Entrez un nombre ( -1 pour arrêter) : "))
    if n < 0:
        break
    if chiffres_pairs (n) :
        print (n, " a un nombre pair de chiffres dans sa repr é sentation dé cimale ")
    else :
        print (n, " a un nombre impair de chiffres dans sa repr é sentation dé cimale ")
