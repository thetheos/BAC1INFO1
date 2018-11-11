def count(n, l):
    cnt = 0
    for elm in l:
        if isinstance(elm,list):
            cnt += count(n,elm)
        elif elm == n:
            cnt += 1 
    return cnt