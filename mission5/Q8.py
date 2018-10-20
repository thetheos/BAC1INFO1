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
        
    if list_of_courses[middle][1] != "":
        return list_of_courses[middle][1]
    else:
        return []

l = [('LINFO1101', ['Jean', 'Pierre']),('LINFO1110', ['Jean']), ('LINFO1111', ['Jean']), ('LINFO1112', ['Jacques', 'Pierre']), ('LINFO1113', ['Pierre'])]


print(binary_search("LINFO01110",l))