l2 = [['Olivier', 40], ['Peter', 53], ['Yves', 68]]
l =[['Charles', 99], ['Siegfried', 65], ['Kim', 81]]
def merge(first_list, second_list):
    new_list = sorted(first_list + second_list, key=lambda l : l[1])
    return new_list

print(merge(l,l2))