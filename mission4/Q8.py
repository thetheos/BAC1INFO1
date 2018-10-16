def primes(max):
    prime_list = []
    for i in range(max+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

def is_prime(n):
    for i in range(2,n//2+1):
        if n == 2:
            return True
        elif n % i == 0:
            return False
        else:
            return True
    
print(primes(70))