
l = [(2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]
def create_dict_max(l):
    dico = {}
    for elm in l:
        if elm[0] in dico:
            dico[elm[0]].append(elm[1])
        else:
            dico[elm[0]] = [elm[1]]
    return dico


print(create_dict_max(l))
