def counts(events, n, m):
    matrix = [[ 0 for i in range(m)] for l in range(n)]
    for evt in events:
        if evt[0]<=m and evt[1] <= n:
            matrix[evt[0]][evt[1]] += 1
    print(matrix)
    return matrix

events = [(0,1),(2,3),(0,1),(4,5),(1,2),(0,1),(1,1),(0,2),(1,1)]
counts(events,2,3)