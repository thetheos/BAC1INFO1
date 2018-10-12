def greatest_divisor(a):
    import math
    pgcd = 1
    if a == 0 or a == 1:
        return
    for i in range(2,a//2+1):
        if a % i == 0:
            pgcd = i

    return pgcd