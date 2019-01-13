def sum(list):
    summ = 0
    for elm in list:
        if isinstance(elm, int) or isinstance(elm, float):
            summ += elm

    return summ

print(sum([1,2,3]))