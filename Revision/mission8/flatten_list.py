def flatten(l):
    new_l = []
    for elm in l:
        if isinstance(elm, list):
            new_l += flatten(elm)
        else:
            new_l.append(elm)
    return new_l

l = [1,[2,3],4,[5,[6,7]],8]
print(flatten(l))