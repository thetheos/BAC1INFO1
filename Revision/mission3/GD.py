def greatest_divisor(n):
    pgcd = None
    for i in range(2,(n//2)+2):
        if n%i == 0:
            pgcd = i

    return pgcd

print(greatest_divisor(257))