import sys
import search


b = {"l'éternel": {0: 1, 1: 1}, 'appela': {0: 1}, 'moïse': {0: 1}, 'de': {0: 1, 2: 2}, 'la': {0: 1, 2: 1}, 'tente': {0: 1, 2: 1}, "d'assignation": {0: 1, 2: 1}, 'il': {0: 1, 1: 1, 2: 2}, 'lui': {0: 1}, 'parla': {0: 1}, 'et': {0: 1, 1: 1}, 'dit': {0: 1}, 'parle': {1: 1}, 'aux': {1: 1}, 'enfants': {1: 1}, "d'israël": {1: 1}, 'dis-leur': {1: 1}, 'lorsque': {1: 1}, "quelqu'un": {1: 1}, "d'entre": {1: 1}, 'vous': {1: 1}, 'fera': {1: 1}, 'une': {1: 1}, 'offrande': {1: 1, 2: 1}, 'à': {1: 1, 2: 1}, 'offrira': {1: 1, 2: 1}, 'du': {1: 3}, 'bétail': {1: 2, 2: 1}, 'gros': {1: 1, 2: 1}, 'ou': {1: 1}, 'menu': {1: 1}, 'si': {2: 1}, 'son': {2: 1}, 'est': {2: 1}, 'un': {2: 2}, 'holocauste': {2: 1}, 'mâle': {2: 1}, 'sans': {2: 1}, 'défaut': {2: 1}, "l'offrira": {2: 1}, "l'entrée": {2: 1}, 'devant': {2: 1}, "l'éternel,pour": {2: 1}, 'obtenir': {2: 1}, 'sa': {2: 1}, 'faveur': {2: 1}}
a = ['ceci', 'est', 'un', 'test']
c = ["L'Éternel appela Moïse; de la tente d'assignation, il lui parla et dit:\n", "Parle aux enfants d'Israël, et dis-leur: Lorsque quelqu'un d'entre vous fera une offrande à l'Éternel, il offrira du bétail, du gros ou du menu bétail.\n", "Si son offrande est un holocaustede gros bétail, il offrira un mâle sans défaut; il l'offrira à l'entrée de la tente d'assignation, devant l'Éternel,pour obtenir sa faveur."]



def test(did_pass):
    """  Imprime le rÃ©sultat d'un teste.  """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_readfile():
    test(True)

def test_get_words():
    test(search.get_words("Ceci est un test.!!")==a)

def test_create_index():
    test(search.create_index("test_example_2.txt")==b)


test_create_index()
test_get_words()
test_readfile()