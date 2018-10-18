def diff_count(lst):
    if lst == 0:
        return

    tmp_lst = []
    divergence = 0

    for i in lst:    
        if i not in tmp_lst:
            tmp_lst.append(i)
            divergence += 1
    
    return divergence