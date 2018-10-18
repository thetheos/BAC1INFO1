def extract(code):
    output = ""
    for c in code:
        if c in "CBDFGHJKLMNPQRSTVWXZ":
            code += "consonant-up "
        elif c in "CBDFGHJKLMNPQRSTVWXZ".lower():
            code += "consonant-low "
        elif c in "AEIOUY":
            code += "vowel-up "
        elif c in "aeiouy":
            code += "vowel-low "
        elif c in "0123456789":
            code += "number "    
    
    return code

print(extract("A12t"))