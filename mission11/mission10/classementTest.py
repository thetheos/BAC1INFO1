import unittest
from coureur    import Coureur
from classement import Classement
from temps      import Temps
from resultat   import Resultat

class ClassementTest(unittest.TestCase):
    """
    Cette classe de test traite les différents cas suivants:
    -Un coureur réalise le même temps qu'un autre
    -Lorsqu'il n'y a qu'un seul coureur et que celui ci bat son propre record
    -Un coureur réalise un meilleur temps qu'un autre
    -Un coureur réalise un moin bon temps que sont temps précedent
    -un coureur bat son propre record
    -un coureur réalise le pire temps parmi un groupe de coureur
    -Position d'un coureur
    -Enlever un coureur
    -Methode "get" qui retourne le résultat d'un coureur
    -Methode "add" qui ajoute un element à la linked list (soit un joueur bat son record soit un nouveau coureur arrive)
    
    Tout ces test fonctionnnes mais je n'arrive pas à implement unittest
    
    
    def __init__(self):
        self.
        c = self.coureurs[0]
        t = Temps()
        t.add_secondes(3000)
        self.r = Resultat(c,t)
        self.cl = Classement()

    def add_is_working(self):
        self.assertEqual(cl.add(self.r), True)
        print(self.cl)

    def get_is_working(self):
        coureurs = [ Coureur("Alfred", 24), \
                    Coureur("Bernard", 27), \
                    Coureur("Claude", 19), \
                    Coureur("Daniel", 31),  \
                    Coureur("Emile", 25),  \
                    Coureur("Fred", 28),  \
                    Coureur("Gerard", 25) ]
        c = self.coureurs[0]
        t = Temps()
        t.add_secondes(3000)
        r = Resultat(c,t)
        cl.add(r)
        self.assertEqual(self.cl.get(c),r)








if __name__ == '__main__':
    unittest.main()
    """