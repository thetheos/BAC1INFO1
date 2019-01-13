def fibonnaci(n):
    F0 = 0
    F1 = 1
    F2= F0 +F1 
    for i in range(n+1):
        F0 = F1
        F1 = F2
        F2 = F1 + F0
    return(F2)

print(fibonnaci(6))
