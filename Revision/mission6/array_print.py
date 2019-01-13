def table(f_in, f_out, width):
    header= "+"
    for i in range(width):
        header += "-"
    header += "+\n"
    f = open(f_in,"r")
    lines = f.readlines()
    f.close()
    f_o = open(f_out, "w")
    f_o.write(header)
    for line in lines:
        f_o.write("|{0:<{1}}|\n".format(line.strip(),width))
    f_o.write(header)

table("test.txt","caca.txt", 8)