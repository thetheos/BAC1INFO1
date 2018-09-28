#Donne le nombre de diviseur entier
n = 1218
for i in range(1,10000):
    if (n % i) == 0:
        print(i)
