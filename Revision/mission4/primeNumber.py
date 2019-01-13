def is_prime(n):
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def primes(max):
    if max<= 0:
        return []
    prime_list = []
    for i in range(2,max+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


print(primes(18))

