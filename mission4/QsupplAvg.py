def average(list):
    if list == []:
        return
    pos = 0
    sum = 0
    for i in list:    
        if type(i) == int or type(i) == float:
            sum += i
            pos += 1

    return sum/pos