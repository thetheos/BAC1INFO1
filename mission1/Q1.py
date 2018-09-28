a = 2
b = 12
c = 10
median = c
if((a>=b and a<=c) or (a>=c and a<=b)):
    median = a
elif((b>=a and b<=c) or (b>=c and b<=a)):
    median = b

print(median)