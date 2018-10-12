def fibonacci(n):
    fSecondPrevious = 0
    fPrevious = 1
    fterm = fSecondPrevious + fPrevious
    if n == 0 :
        return 0
    for i in range(n-1):
        fterm = fSecondPrevious + fPrevious
        fSecondPrevious = fPrevious
        fPrevious = fterm
    return(fterm)

print(fibonacci(10))