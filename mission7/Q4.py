d = {2.0: 5.0, 8.0: 50.0, 10.0: 40.0}
l = [(2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]


def create_dict_max(l):
    d = {}
    for elmt in l:
        if elmt[0] in d and elmt[1] > d[elmt[0]]:
            d[elmt[0]] = elmt[1]
        else:
            d[elmt[0]] = elmt[1]
    return d

print(create_dict_max(l))

