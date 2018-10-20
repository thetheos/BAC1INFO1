matrix = [[0 for j in range(4)] for i in range(3)]
for i in range(3):
    for j in range(4):
        matrix[i][j] = i + j

print(matrix)

l = [("Jean",1), ("Charles",3), ("Marc", 5)]
for a, b in l:
  print (a)

def pos_index(matrix):
  l = []
  for i in range(len(matrix)):
    ligne = matrix[i]
    for j in range(len(ligne)):
      if ligne[j] == 1:
        l.append((i, j))
  return l
def nest(l):
    new_l = []
    new_ll = []
    for v in l[1:]:
        if v == 0:
            new_l.append(new_ll)
            new_ll = []
        else:
            new_ll.append(v)
    return new_l
print(nest([0,1,2,3,4,0,1,3,4,0,0,5,6,0,4,5,0]))

def binary_search(name, list_of_names):
  first = 0
  last = len(list_of_names)-1
  found = False

  while first<=last and not found:
    middle = (first + last)//2
    print(middle)                   # Ligne ajoutée!
    if list_of_names[middle] == name:
      found = True
    else:
      if name < list_of_names[middle]:
        last = middle-1
      else:
        first = middle+1

  return found
binary_search( "7", ["1","3","5","8","9","12","13"])