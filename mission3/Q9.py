"""
Realised by Vanden Driessche Théo. Octobre 2018
Turtle program who print the European flag following the normalized size format
L=3/2 H , R_(stars) =  1/3 Heigt, R_(star) = 1/9 Height

Pour la réalisation de ce programme j'ai découpé le drapeau suivant ce schéma:
-base du drapeau
-dodecagone régulier
-étoile

Plus d'autre fonction de positionnement afin que l'ensemble soit correcte.
Conclusion: Le drapeau est dessiné grace a une suite de fonction se déroulant dans un certain ordre
Bien que cet orde pourrait être différent

"""

import turtle
import math

def drapeau(t, drp_lenght, drp_fill_color):
    """
    pre: turtle instance, lenght of flag, fill up color of flag
    post: create a base flag with the previous parameters
    """
    t.setheading(0)
    t.color(drp_fill_color, drp_fill_color)
    t.begin_fill()
    t.forward(drp_lenght)
    t.left(90)
    t.forward((drp_lenght*2)//3)
    t.left(90)
    t.forward(drp_lenght)
    t.left(90)
    t.forward((drp_lenght*2)//3)
    t.end_fill()
    drp_center(t, drp_lenght) #call fonction to position to center
   

def drp_center(t,drp_lenght):
    """
    pre: turtle instance
    post: go to center of flag
    """
    t.penup()
    t.left(90)
    t.forward(drp_lenght//2)
    t.left(90)
    t.forward((drp_lenght*2)//6)
    drp_draw_stars(t, drp_lenght) #call draw stars

def drp_draw_stars(t,drp_lenght):
    """
        pre: turtle instance, size>0 drp_lenght
        post: position the turtle in a dodecagon
    """
    radius = (2/9) * drp_lenght
    t.right(90) #position the turtle where the circle has to be drawn
    t.forward(radius)
    t.left(90)
    t.color("yellow")
    for i in range(0,12): #the 12 corner for the 12 stars
        draw_star(t, drp_lenght)
        t.circle(radius,30)
    return

def draw_star(t, size):
    """
        pre: turtle instance, size>0 (lenght of the flag)
        post: draw a yellow start where the turtle is with the branch pointing up
    """
    size = (size/35.343458848) # (27×(1+cos(72))) = 35.34 represents 1/9 of the height
    previous_heading = t.heading()
    t.setheading(-10) #Make the star look 12 o clock
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.right(72-120)
    t.end_fill()
    t.setheading(previous_heading)
    return


wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
alex.setheading(225) #position more in the down left corner
alex.forward(300) 
alex.setheading(0)
drapeau(alex, int(input("Enter lenght of the flag")),"blue") #ask the user to set lenght of the flag


wn.mainloop()