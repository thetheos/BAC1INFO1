def recursive_min(l):
    nl = flatten_list(l)
    return nl[0] 

def flatten_list(l):
    new_list = []
    for elm in l:
        if isinstance(elm,list):
            new_list += flatten_list(elm)
        else:
            new_list.append(elm)

    new_list.sort()
    return new_list
        
l=[2, 9, [12, 13], 8, 6]

print(recursive_min(l))