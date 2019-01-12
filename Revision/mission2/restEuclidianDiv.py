a =128
b = 63
rest = 0

while True:
    max_substraction = b
    count = 2
    if b == 0:
        rest = None
        break
    if b > a:
        rest = a
        break
    while max_substraction < a:
        max_substraction = b * count
        count += 1

    max_substraction = max_substraction - b
    rest  = a - max_substraction
    break

print(rest)
