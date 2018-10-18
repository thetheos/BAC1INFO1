def sum(list):
    sum = 0
    for i in list:
        if type(i) == int or type(i) == float:
            sum += int(i)
        
    return sum

l = [1,2,3,"e"]
print(sum(l))