def maximum_index(l):
    if isinstance(l,list) == False or l == []:
        return None
    max = 0
    index = 0 
    for pos,i in enumerate(l):
        if i > max:
            max = i
            index = pos 
    return index

print(maximum_index("papa"))