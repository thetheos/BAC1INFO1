def is_in_lst(elmt, l):
    for i in l:
        if elmt == i:
            return True
    return False

def diff_count(lst):
    new_lst = []
    for i in lst:
        if i in new_lst:
            pass
        else:
            new_lst.append(i)
    
    return len(new_lst)


print(diff_count([1,3,4,1,1]))