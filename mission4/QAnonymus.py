def extract(code):
    output = ""
    for c in code:
        if c in "CBDFGHJKLMNPQRSTVWXZ":
            output += "consonant-up "
        elif c in "CBDFGHJKLMNPQRSTVWXZ".lower():
            output += "consonant-low "
        elif c in "AEIOUY":
            output += "vowel-up "
        elif c in "aeiouy":
            output += "vowel-low "
        elif c in "0123456789":
            output += "number "    
    
    return output

print(extract("A12t"))