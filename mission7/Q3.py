l = [(2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]

d = {2.0: [5.0], 8.0: [12.0, 50.0, 50.0], 10.0: [40.0]}

def create_dict(l):
    d = {}
    for elmt in l:
        if elmt[0] in d:
            d[elmt[0]].append(elmt[1])
        else:
            d[elmt[0]] = [elmt[1]]
    
    return d
    #return dict(l)

print(create_dict(l))

