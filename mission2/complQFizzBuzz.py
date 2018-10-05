i = 2
if i % 3 == 0 :
    temp = "fizz"
if i % 5 == 0:
    temp= "buzz"
if i%5 == 0 and i % 3 == 0:
    temp = "fizzbuz"
if i%5 != 0 and i % 3 != 0:
    temp = "no"

print(temp)