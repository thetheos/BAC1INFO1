
def test_error():
    f = open('integers.txt') #erreur 
        s = f.readline()     
        i = int(s.strip())
    




def div_value():
    try:
        while True:
            try:
                value = int(input("Provide a value"))
                return 1/value
            except ValueError:
                print("Incorrect value")
    except ZeroDivisionError:
        print("Incorrect calculation")
        return -1

#print(div_value())
print(test_error())
            
