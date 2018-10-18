import math as mt

def solution(a, b, c):
    """
    pre:  a, b et c sont 3 nombres réels
    post: la valeur de retour de cette fonction dépend du nombre
          de solutions de l'équation ax^2 + bx + c = 0.
    - 0 solution: retourne la liste vide
    - 1 solution: retourne une liste contenant la solution de l'équation
    - 2 solutions: retourne une liste contenant les deux solutions,
                  la plus petite solution en première place
    """
    delta = b**2 - (4 * a * c)
    sol = []
    if delta < 0:
        return []
    sol.append( (-b + mt.sqrt(delta))/(2*a) )
    sol.append( (-b - mt.sqrt(delta))/(2*a) )
    sol.sort()
    return sol


def solveur(list):
    sol = [solution(l[0],l[1],l[2]) for l in list]
    return sol


print(solution(1,4,1))