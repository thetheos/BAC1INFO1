def flatten(l):
    new_lst = []
    for elm in l:
        if isinstance(elm, list):
            new_lst += flatten(elm)
        else:
            new_lst.append(elm)
    return new_lst