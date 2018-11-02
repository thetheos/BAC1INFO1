def readfile(filename):
    try:
        f = open(filename, "r")
        lines_lst = [line for line in f]
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
    return [word.lower().strip(". ") for word in line.split(" ")]


def create_index(filename):
    """
    Return an index dictionary of all the words contained in a file.
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
    keys_list = []
    for key in index:
        for i in index[key].keys():
            if i == line:
                keys_list.append(key)
    return keys_list

#print(readfile("episodeIV_dialog.txt"))


print(get_words("Turmoil has engulfed the Galactic Republic."))

print(create_index("test_example_1.txt"))
#print(get_words_same_line(1, create_index("test_example_1.txt")))
print(get_lines(["this","has","coco"], create_index("test_example_1.txt")))