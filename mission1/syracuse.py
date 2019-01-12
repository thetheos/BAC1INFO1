s=11

print(int(s))

while True:
    if s%2 == 0:
        s= s/2
    else:
        s=3*s+1
    print(int(s))
    if s == 1:
        break
    