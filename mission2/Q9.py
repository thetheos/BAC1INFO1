"""
Question:
# Place dans sum la somme des n premiers entiers pairs strictement positifs

n = some_value
sum = 0
for ___ in ___________:
    ______________
"""
some_value = 22
#Solution
n = some_value
sum = 0
for i in range(0,(n+1)*2,2):
    sum += i

print(sum)