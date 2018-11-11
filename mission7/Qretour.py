def topk_words(words, k):
    l = []
    index = index_count_words(words)

    if k >= len(words):
        return (index[elm],elm) for elm in index
    
    for elm in index:
        if index[elm] >= k:
            l.append((index[elm],elm))
    
    sorted(l)
    return l

def index_count_words(l):
    index = {}
    for word in l:
        if word in index:
            index[word] += 1
        else:
            index[word] = 1
    return index


print(topk_words(words,3))
