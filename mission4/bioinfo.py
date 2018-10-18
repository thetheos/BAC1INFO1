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
    pre: `s` et `p`: deux chaine de caractère de même longeur
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


def extract(text,n,x):
    """
    pre: extrait dans text apd la position x n characteres
    post:return le string conenant ces n carateres
    """
    
    extrait=text[(x):(n+x)]
    return(extrait) 
    
    
def palindrome(extrait):
    """
    pre: Verifie si extrait est un palindrome ou non
    pos: renvoit True si oui et False si non
    """
 
    max=len(extrait)
    a=max//2
    for x in range(a):
        if extrait[x] != extrait[-x-1]:
            return False
    return True


def plus_long_palindrome(text):
    """
    pre:cherche dans text le plus long palindrome
    post: return celui-ci
    """
    max=len(text)
    if max==0:
        return('')
    if max==1:
        return text
    max_2=max+1
    p_l_p=("")
    nb_ch=(0)
    for x in range (0,max):
        for n in range (2,max_2):
            if n+x>max:
                break
            if palindrome(extract(text,n,x))==True:
                if n>nb_ch:
                    p_l_p=extract(text,n,x)
                    nb_ch=n
    if nb_ch==0:
        return """Chaqu'une des lettres du mot est un palindrome d'un seul
charctère"""
    return p_l_p



#print(is_adn(""))
#print(positions("atgcatgatgatg","ATG"))
print(distance_h("atgac","aggag"))
