is_prime = True
n = 73           #Un entier supérieur à 1    

for i in range(1,n+1):
    print(i)
    if (n % i == 0):
        if (i != 1 and i != n):
           is_prime = False
    elif(is_prime == True):
        is_prime = True
print( is_prime)