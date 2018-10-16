"""
Réalise par Théo Vanden Driessche et Simon Van Roy en octobre 2018
"""

def is_adn(s):
    if s =="":
        return False
    for c in s:
        if c in "atgcATGC": #['a','t','g','c','A','T','G','C']
            next
        else:
            return False
    return True


def positions(s, p):
    """
    pre: `s`: une chaine de caractère, `p`: la chaine à trouver dans `s`
    post: Retourne une liste contenant la position de la chaine `s` dans `p´
    """
    s = s.lower()
    p = p.lower()
    occurences = []
    pos= 0
    while pos < len(s):
        if s[pos:(pos+len(p))] == p: #Verifie si la chaine en partant de c, de longeur len(p) correspond au string p
            occurences.append(pos)
            pos += len(p)
        else:
            pos += 1
    return occurences


def distance_h(s, p):
    """
    pre: `s` et `p`: de chaine de caractère de même longeur
    post: retourne la distance de Hamming
    """
    dist = 0
    pos = 0
    if len(s) != len(p):
        return
    while pos < len(s):
        if s[pos] != p[pos]:
            dist += 1
        pos+=1

    return dist

#print(is_adn(""))
print(positions("atgcatgatgatg","ATG"))
print(distance_h("atgac","aggag"))
