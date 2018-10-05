
s = int(input("Veuillez entrer un nombre netier \n"))
while s == '': #verrifie que la valeur entrée est non null
    s = int(input("Veuillez entrer un nombre netier \n"))


while s != 1: #la suite de sytacuse ne vaut que pour les entier positifs non nuls
    if s % 2 == 0:
        s = s//2
    else:
        s = 3 * s + 1 
    print(s)