def greatest_common_divisor(a,b):
    if b == 0 :
        return a

    return greatest_common_divisor(b, a%b)

print(greatest_common_divisor(34,512))