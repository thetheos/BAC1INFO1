e = 12
n = 6
divisor_count  = 0
for nbr in range(1,n+1):
    divisor_count = 0
    for i in  range(1,nbr):
        if nbr % i == 0:
            divisor_count += 1
    print("nombre: {}, diviseurs: {}".format(nbr,divisor_count))        
