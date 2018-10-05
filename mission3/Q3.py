def croix(char, height):
    """
    pre: n nombre impair
    post: affiche une croix de hauteur, et largeur "hauteur" dans le prompteur
    """
    space = " "
    for i in range(height ):
        if i == height//2:
            print(char * height)
        else:
            print(space * ((height//2)-1),char)

hauteur = int(input("Hauteur de la croix: "))
print()
croix('X', hauteur)
    