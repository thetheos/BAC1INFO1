def interests(base, y, x):
    for i in range(x):
        base = base*(1+(y/100))
    return(base)

print(interests(100,10,1))