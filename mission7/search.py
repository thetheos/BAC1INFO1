global file_name


def readfile(filename):
    """
        Open the file, return a list of all the lines in this file
    """
    try:
        f = open(filename, "r")
        lines_lst = [line for line in f]
        f.close()
        return lines_lst
    except IOError:
        print("Error while opening the file")
        return -1
    except OSError:
        print("We can not locate the file")
        return -1
    except:
        print("An unknow error occured in the readfile def")
        return -1
    

def get_words(line):
    """
    Return a list of all the words in a line without punctionation
    """
    return [word.lower().strip(".!?%+-#,;: ") for word in line.split(" ")]


def create_index(filename):
    """
    Return an index dictionary of all the words contained in a file.
    In which line the words is contained
    """
    index = {}
    
    line_lst = readfile(filename)
    if line_lst == None or line_lst == [] or line_lst == -1:
        print("There is no list or list is empty")
        return -1
    try:
        for line_nbr, line in enumerate(line_lst):
            word_list = get_words(line.strip())
            for word in word_list:
                if word in index and line_nbr in index[word]:
                    index[word][line_nbr] += 1
                else:
                    if word not in index:
                        counts= {line_nbr: 1}
                        index[word] = counts
                    else:
                        index[word][line_nbr] = 1
        return index
    except ValueError:
        print("List is not manifold.")
        return 
    except:
        print("An unknow error has occured in def create_index")
        return 


def get_lines(words, index):
    """
    Takes a list of words and an index. Return the lines numbers where all the words contained in words list is in this line
    """
    for word in words:
        if word not in index:
            print("This word isn't in the index: " + word)
            return []
    line_pos_t = []
    test = True
    for pos in index[words[0]].keys():
        l = get_words_same_line(pos, index)
        for word in words:
            if word in l:
                next
            else:
                test = False
                break
        if test:
            line_pos_t.append(pos)
    return line_pos_t

def get_words_same_line(line, index):
    """
    Takes line number and an index. Return all the words that are in this line
    """
    keys_list = []
    for key in index:
        for i in index[key].keys():
            if i == line:
                keys_list.append(key)
    return keys_list


file_name = ""
while True:
    if file_name == "":
        cmds = []
        cmds = input("Enter the filename to begin or enter quit(to enter test mode enter test): ")
        cmds_list = [i for i in cmds.split(" ")]
        file_name = cmds_list[0]
        if readfile(file_name) == -1:
            file_name = ""
        if cmds_list[0] in ["q","quit","exit","exit()","test"]:
            print("Have a good night")
            break
    else:
        if cmds_list[0] in ["q","quit","exit","exit()","test"]:
            print("Have a good night")
            break
        words = input("Enter words separate by a space: ").split(" ")

        if words[0] in ["q","quit","exit","exit()"]:
            print("Have a good night")
            break
        index = create_index(file_name)
        line_lst = readfile(file_name)
        #print(index)
        for line_number in get_lines(words, index):
            print(line_lst[line_number].strip())

        #print(get_lines(words, create_index(file_name)))
        
    
 