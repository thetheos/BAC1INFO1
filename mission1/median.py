a=5
b=3
c=1


if a>=b and a<=c or a<=b and a>=c:
    median=a
elif b>=a and b<=c or b<=a and b>=c:
    median=b
elif (c>=a and c<=b) or c<=a and c>=b: 
    median=c

print(median)