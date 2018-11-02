def create_dictionary(filename):
    dico = {}
    f = open(filename,"r")
    for line in f:
        for word in line.split():
            if word in dico:
                dico[word] += 1
            else:
                dico[word] = 1
    return dico

def occ(dictionary,word):
    return dictionary.get[word, 0]