""" Programme initial
n = input("n = ? ") #la fonction input retourne une chaine de caractère et non un entier
print("n^2 =", n ** 2) #l'opération mathématique ci-contre ne peut s'effectuer avec un String
"""
#Correction du code:
n = int(input("n = ? ")) #convertir le string en int
print("n^2 =", n ** 2)