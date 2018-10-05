import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

def downstair(t,n_steps, height):
    t.color("blue")
    t.forward(height)
    for i in range(0, n_steps):
        t.right(90)
        t.forward(height)
        t.left(90)
        t.forward(height)

downstair(alex,3,20)
wn.mainloop()