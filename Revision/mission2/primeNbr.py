is_prime = True
n = 4
for i in range(2,n):
    if n == 1:
        break
    if n%i == 0:
        is_prime = False
        break

print(is_prime)