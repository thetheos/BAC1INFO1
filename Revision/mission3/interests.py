def interests(base,y,x):
    for i in range(x):
        base = base + (base*(y/100))

    return base

print(interests(100,2,5))