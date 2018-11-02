
def test_error():
    try:
        f = open('integers.txt') #erreur 
        s = f.readline()     #unexpected indent
        i = int(s.strip())   #unexpected indent
    except IOError:
        print("IOError")
    except ValueError:
        print("Impossible de convertir en int")
    except:
        print("An unknow error occured")
        

def getMax(filename)
try:
    f = open(filename, "r")
    previous_i = -1
    for line in f.readlines():
        try:
            i = int(strip(line))
        except:
            next
        if i > previous_i and i => 0:
            previous_i = i
    return previous_i
except IOError:
    print("error in the file")
    return -1
except ValueError:
    print("Unable to convert to int")
    return -1
except:
    print("Unknow error")
    return -1







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
            
