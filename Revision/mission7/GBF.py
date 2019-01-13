def topk_words(words, k):
    output = []
    dico = create_dico(words)
    word_frequency = []
    for elm in dico:
        word_frequency.append((dico[elm],elm))
    word_frequency.sort(reverse = True)
    freq = get_greatest_frequency(word_frequency,k)
    for i in word_frequency:
        if i[0] in freq:
            output.append(i)

    return output

    print(word_frequency)

def most_frequent_word(sorted_lst, k):
    most_frequent = []
    frequency = sorted_lst[0][0]
    
    if k == 0 :
        return
    for i in sorted_lst:
        
        most_frequent.append(i)

def get_greatest_frequency(list,k):
    fre_lst = []
    count = 1
    for elm in list:
        if count <= k:
            if elm[0] in fre_lst:
                pass
            else:
                fre_lst.append(elm[0])
                count += 1
        else:
            break
    return fre_lst
    
def create_dico(l):
    word_dic = {}
    for word in l:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic


l =["while", "the", "congress", "of", "the", "republic", "endlessly", "debates", "this", "alarming", "chain", "of", "events", "the", "supreme", "chancellor", "has", "secretly", "dispatched", "two", "jedi", "knights"]

print(topk_words(l,2))