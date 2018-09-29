n = 10
sum = 0
for i in range(1, n+1):
    reste = n%i
    if reste == 0:
        sum = sum + i

print(sum)