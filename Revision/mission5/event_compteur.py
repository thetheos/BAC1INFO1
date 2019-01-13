events = [(0,1),(2,3),(0,1),(4,5),(1,2),(0,1),(1,1),(0,2),(1,1)]

def event_counter(events, i, j):
    count = 0 
    for x in events:
        if x == (i,j):
            count += 1

    return count

print(event_counter(events,0,1))