#Code réalisé le 4/10/2018 par Théo Vanden Driessche
#Ce code print le nombre de diviseur propre d'un nombre compris entre 0 et n
#n = int(input("Rentrer une valeur: "))
for i in  range(1,int(input("Rentrer une valeur: "))+1):
    compteur = 0
    for o in range(1,i):
        if i % o == 0 :
            compteur += 1
    print(i, "\t", compteur)
