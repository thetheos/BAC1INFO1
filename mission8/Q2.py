def sum(list):

    if list != []:
        if isinstance(list[0],(int,float)):
            return list[0] + sum(list[1:])
        else:
            return sum(list[1:])
    else:
        return 0

print(sum([1,2,3]))