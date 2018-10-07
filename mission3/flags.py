import turtle                # module des graphiques tortue


tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed(2)      # tracé rapide
wn = turtle.Screen()

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.
    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()


def rectangle(widht, height, color):
    """Trace un rectancle de largeur 'wifth' et de hauteur 'height' et de couleur 'color' .
    pre: 
        `color` spécifie la couleur du rectangle.
        `widht`: largeur, `height`: hauteur .
        La tortue est positionnée à un sommet du rectagle et orientée en direction d'un coté 
        du rectangle.
    post:
        Le rectangle a été tracé sur la gauche du premier coté.
        La tortue est de retour à sa position et orientation d'origine.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(widht)
        tortue.left(90)
        tortue.forward(height)
        tortue.left(90)
    tortue.end_fill()
    tortue.penup()


def three_color_flag(width, color1, color2, color3):
    """Trace un drapeau tricolore `color1`,`color2`,`color3`. De largeur `width`, 
    le rapport L/H = 3/2.
    pre: 
        `widht`: largeur du drapeau.
        `color1`,`color2`,`color3`: les couleurs du drapeau de gauche à droite.
        La tortue est positionnée à un sommet du drapeau (Le coin inférieur gauche).
        la tortue pointe vers le coté de la largeur du drapeau.
    post: 
        Le drapeau tricolore est dessiné dans le quart supérier droit par rapport à la tortue.
        La tortue est de retour en position et orientation d'origine dans le coin inferieur gauche 
        du drapeau.
    """
    for color in [color1,color2,color3]:
        rectangle(width/3, (2*width)/3, color)
        tortue.forward(width/3)
    
    tortue.right(180)
    tortue.forward(width)
    tortue.right(180)


def hv_three_color_flag(width, color1, color2, color3, disposition):
    """Trace un drapeau tricolore `color1`,`color2`,`color3` horizontalement ou verticalement `disposition`. De largeur `width`, 
    le rapport L/H = 3/2.
    pre: 
        `widht`: largeur du drapeau.
        `color1`,`color2`,`color3`: les couleurs du drapeau de gauche à droite ou de bas en haut.
        `disposition`: définit l'orientation des couleurs du drapeau "h":horizontal ou "v": vertical.
        La tortue est positionnée à un sommet du drapeau (le coin inférieur droit).
        la tortue pointe vers le coté de la largeur du drapeau.
    post: 
        Le drapeau tricolore est dessiné dans le quart supérier droit par rapport à la tortue
        La tortue est de retour en position et orientation d'origine dans le coin inferieur gauche 
        du drapeau
    """
    if disposition == "v":
        for color in [color1, color2, color3]:
            rectangle(width/3, (2*width)/3, color)
            tortue.forward(width/3)

        tortue.right(180)       #Repositionne la tortue à son point d'origine de création du drapeau
        tortue.forward(width)
        tortue.right(180)
    elif disposition == "h":
        for color in [color1, color2, color3]:
            rectangle(width, (2*width)/9, color)
            tortue.left(90)
            tortue.forward((2*width)/9)
            tortue.right(90)

        tortue.right(90)       #Repositionne la tortue à son point d'origine de création du drapeau
        tortue.forward((2*width)/3)
        tortue.left(90)


def belgian_flag(width):
    """Trace le drapeau belge de largeur width. Le rapport L/H = 3/2.
    pre: 
        `widht`: largeur du drapeau.
        La tortue est positionnée à un sommet du drapeau
        la tortue pointe vers le coté de la largeur du drapeau
    post:
        Le drapeau  est dessiné dans le quart supérier droit par rapport à la tortue
        La tortue est de retour en position et orientation d'origine dans le coin inferieur gauche 
        du drapeau
    """
    for color in ["black","yellow","red"]:
        rectangle(width/3, (2*width)/3, color)
        tortue.forward(width/3)
    
    tortue.right(180)
    tortue.forward(width)
    tortue.right(180)


def dutch_flag(width):
    """Trace le drapeau des Pays-Bas de largeur width. Le rapport L/H = 3/2.
    pre: 
        `widht`: largeur du drapeau.
        La tortue est positionnée à un sommet du drapeau
        la tortue pointe vers le coté de la largeur du drapeau
    post:
        Le drapeau  est dessiné dans le quart supérier droit par rapport à la tortue
        La tortue est de retour en position et orientation d'origine dans le coin inferieur gauche 
        du drapeau
    """
    hv_three_color_flag(width,"blue","white","red","h")


def new_belgian_flag(width):
    """Trace le drapeau belge de largeur width. Le rapport L/H = 3/2.
    pre: 
        `widht`: largeur du drapeau.
        La tortue est positionnée à un sommet du drapeau
        la tortue pointe vers le coté de la largeur du drapeau
    post:
        Le drapeau  est dessiné dans le quart supérier droit par rapport à la tortue
        La tortue est de retour en position et orientation d'origine dans le coin inferieur gauche 
        du drapeau
    """
    hv_three_color_flag(width,"black","yellow","red","v")


def german_flag(width):
    """Trace le drapeau allemand de largeur width. Le rapport L/H = 3/2.
    pre: 
        `widht`: largeur du drapeau.
        La tortue est positionnée à un sommet du drapeau
        la tortue pointe vers le coté de la largeur du drapeau
    post:
        Le drapeau  est dessiné dans le quart supérier droit par rapport à la tortue
        La tortue est de retour en position et orientation d'origine dans le coin inferieur gauche 
        du drapeau
    """
    hv_three_color_flag(width,"yellow","red","black","h")


#rectangle(300,100,"green")
#belgian_flag(300)
#three_color_flag(300,"black","yellow","red")
#hv_three_color_flag(300,"black","yellow","red","h")
dutch_flag(300)
new_belgian_flag(300)
german_flag(300)

wn.mainloop()