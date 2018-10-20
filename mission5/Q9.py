def binary_search ( name, list_of_courses ):
    first = 0
    last = len(list_of_courses)-1
    found = False
    middle = 0
    if list_of_courses == []:
        return []
    while first<=last and not found:
        middle = (first + last)//2
        if list_of_courses[middle][0] == name:
            found = True
        else:
            if name < list_of_courses[middle][0]:
                last = middle-1
            else:
                first = middle+1
        print(middle)

    if list_of_courses[middle][1] != "":
        return list_of_courses[middle][1]
    else:
        return []

l = [('LINFO1101', ['Jean', 'Pierre']), ('LINFO1111', ['Jean']),\
 ('LINFO1110', ['Jean']), ('LINFO1112', ['Jacques', 'Pierre']), \
 ('LINFO1113', ['Pierre'])]

print(binary_search("LINFO1114",l))
#LINFO01110 2
#LINFO1112 2
#LINFO1111 2
#LINFO1114 3