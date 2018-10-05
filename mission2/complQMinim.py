a = 5
b = 3
c = 15
if a <= b and a <= c:
    minima = a
elif b <= c and b <= a:
    minima = b
else:
    minima = c

print(minima)