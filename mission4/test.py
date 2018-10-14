import bioinfo

def test_is_adn():
    """
    pre: module bioinfo
    post: test la fonction is_adn()
    """
    test(bioinfo.is_adn('atx')==False)
    test(bioinfo.is_adn('atg')==True)
    test(bioinfo.is_adn('axg')==False)
    test(bioinfo.is_adn('ATG')==True)

def test(cdt):
    """
    pre: cdt: boolean value
    post: print if the test successful or not
    """
    if cdt == True:
        print("Succesfull test")
    elif cdt == False:
        print("Test failed")
    else:
        print("Invalid argument")
    return

def test_positions():
    """
    pre: module bioinfo
    post: teste la fonction position
    """
    test(bioinfo.positions("attggc","a")==[0])
    test(bioinfo.positions("attggcg","g")==[3,4,6])

def test_distanceH():
    return

test_is_adn()
test_positions()