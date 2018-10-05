v1 = [1,0,-3]
v2 = [-2,5,1]
v3 = [3,1,1]
vr =[0,0,0]

for i in range(0,3):
    vr[i] = 2*v1[i] - 3*(v2[i] - v3[i])

print(vr)