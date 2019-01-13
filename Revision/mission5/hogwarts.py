import math

trace1 = [(1.0,(10.10,20.0)),(3.0,(10.50,20.30)),(5.0,(11.0,21))]
trace2 = [(1.0,(15.00,15.0)),(2.0,(12.00,17.00)),(3.0,(10.50,20)),(4.0,(12.0,21.0))]
trace3 = [(1.0,(15.00,15.0)),(3.0,(16.0,21.0)),(5.0,(20.0,21.0))]
l = [trace1,trace2,trace3]

def matrixfor_traces(l, theta_1, theta_2):
    matrix2 = []
    for i in l:
        rowl = []
        for j in l:
            if traces_are_crossing(i,j,theta_1,theta_2):
                rowl.append(1)
            else:
                rowl.append(0)
        matrix2.append(rowl)
    return matrix2

def traces_are_crossing(t1, t2, theta_1, theta_2):
    for l in t1:
        for i in t2:
            if absolute(l[0],i[0]) <= theta_1 and euclidian_distance(l[1],i[1])<= theta_2:
                return True
    return False 


def search_time(l, t):
    for pos,i in enumerate(l):
        if i[0]>= t:
            return pos
    return len(l)


def absolute(v1, v2):
    return abs(v1-v2)


def euclidian_distance(c1,c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)



print(euclidian_distance((0,0),(4,3)))
print(absolute(10,12))
print(search_time(trace1,4.0))
print(traces_are_crossing(trace1,trace2,0,1.0))
print(matrixfor_traces(l,0.0,1.0))
