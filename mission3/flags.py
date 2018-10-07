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
    """Trace un rectancle de larheur 'wifth' et de hauteur 'height' et de couleur 'color'

    pre: color spécifie la couleur du rectangle
        widht: largeur, height:hauteur
        La tortue est positionnée à un sommet du rectagle
        la tortue pointe vers le coté de la hauteur du rectangle
    post: le rectangle a été tracé sur la droite du premier coté
        La tortue est de retour à sa position et orientation d'origine 
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(widht)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def belgian_flag(width):
    """Trace le drapeau belge de rapport 3/2 et de largeur width
    pre: width largeur du drapeau
        La tortue est positionnée à un sommet du drapeau
        la tortue pointe vers le coté de la hauteur du drapeau
    post: Le drapeau a été déssine à la droite du premier coté
        La tortue est de retour en position et orientation d'origine
    """
    for color in ["black","yellow","red"]:
        rectangle(width/3, (2*width)/3, color)
        tortue.forward(width/3)
    
    tortue.right(180)
    tortue.forward(width)
    tortue.right(180)

def three_color_flag(width, color1, color2, color3):
    """Trace le drapeau de rapport 3/2 et de largeur width avec les couleurs definies
    pre: width largeur du drapeau
        La tortue est positionnée à un sommet du drapeau
        la tortue pointe vers le coté de la hauteur du drapeau
    post: Les 3 parties du drapeau ont été déssinées à la droite du premier coté
        La tortue est de retour en position et orientation d'origine
    """
    for color in [color1,color2,color3]:
        rectangle(width/3, (2*width)/3, color)
        tortue.forward(width/3)
    
    tortue.right(180)
    tortue.forward(width)
    tortue.right(180)

def hv_three_color_flag(width, color1, color2, color3, disposition):
    """Trace un drapeau tricolore de rapport 3/2 et de largeur width avec les couleurs definies 
    horizontalement ou veticalemnt 
    pre: width largeur du drapeau
        disposition: définit l'orientation des parties du drapeau "h":horizontal ou "v": vertical
        Les couleurs doivent être données de gauche à droite ou de bas en haut.
        La tortue est positionnée à un sommet du drapeau
        la tortue pointe vers le coté de la hauteur du drapeau
    post: Les 3 parties du drapeau ont été déssinées à la droite du premier coté
        La tortue est de retour en position et orientation d'origine
    """
    if disposition == "v":
        for color in [color1, color2, color3]:
            rectangle(width/3, (2*width)/3, color)
            tortue.forward(width/3)
    elif disposition == "h":
        for color in [color1, color2, color3]:
            rectangle(width, (2*width)/9, color)
            tortue.left(90)
            tortue.forward((2*width)/9)
            tortue.right(90)

    #tortue.right(180)
    #tortue.forward(width)
    #tortue.right(180)

#rectangle(300,100,"green")
#belgian_flag(300)
three_color_flag(300,"black","yellow","red")
hv_three_color_flag(300,"black","yellow","red","h")

wn.mainloop()