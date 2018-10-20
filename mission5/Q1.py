#compliqué mais drole

def count(events, i, j):
    cnt = 0 
    l = [1 for evt in events if evt[0] == i and evt[1] == j]
    return len(l)

"""
def count(events, i, j):
    count = 0
    for evt in events:
        if evt[0] == i and evt[1] == j:
            count += 1
    return count
"""
print(count([(0,1),(2,3),(0,1),(4,5),(1,2),(0,1),(1,1),(0,2),(1,1)],1,1))