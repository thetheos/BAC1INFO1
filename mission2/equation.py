# Recherche des racines d'une équation x**a + y**b = z**c 
# Vanden Driessche Théo, octobre 2018

solutions = 0
a = int(input("Entrez la valeur de l'exposant a : "))
b = int(input("Entrez la valeur du l'exposant b : "))
c = int(input("Entrez la valeur du l'exposant c : "))
max = float(input("Entrez la valeur maximale pour x, y et z: "))

for x in range(0,max+1,0.1):
    for y in range(0,max+1):
        for z in range(0, max+1):
            if x**a + y**b == z**c:
                print("x =", x, " y =", y, " z =", z)
                solutions += 1

if solutions == 0:
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees") 