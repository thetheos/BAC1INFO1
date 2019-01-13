def line_count(filename):
    f = open(filename, "r")
    count = 0 
    for l in f:
        count +=1
    f.close()
    return count

def char_count(filename):
    f = open(filename,"r")
    lines = f.readlines()
    counter = 0
    for l in lines:
        counter += len(l.strip())
    f.close()
    return counter

def longuest_line(filename):
    f = open(filename, "r")
    lines = f.readlines()
    longest_line = ""
    for l in lines:
        if len(l) > len(longest_line):
            longest_line = l
    
    f.close()
    return longest_line.strip()

def space(filename,n):
    f = open(filename,"w")
    line = ""
    for i in range(n):
        line += " "
    f.write(line)
    f.close()    

def capitalize(filename_in, filename_out):
    f_in = open(filename_in,"r")
    lines_in = f_in.readlines()
    f_in.close()

    f_out = open(filename_out,"w")
    for line in lines_in:
        f_out.write(line.upper())
    f_out.close()





print(line_count("test.txt"))
print(char_count("test.txt"))
print(longuest_line("test.txt"))
space("caca.txt",10)
capitalize("test.txt","caca.txt")