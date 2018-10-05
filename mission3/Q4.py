def fact(n):
    """
    pre: n>0
    post: retourne la factorielle de n
    """
    if n<0: #verifie que n respecte pré
        return
    fact = 1
    for i in range(0,n):
        fact = fact * (n - i)
    print(fact)
    return fact

fact(int(input("Entrer une valeur: ")))