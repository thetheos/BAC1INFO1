from article import Article
from mission10 import Facture
from mission10 import ArticleReparation
from mission10 import ArticlePiece
from mission10 import Piece

"""
   Classe de test initiale pour la classe Facture.
   @author Kim Mens
   @version 18 novembre 2018
   (code adaptÃ© du code java de Charles Pecheur)
"""

class TestFactureInitial :

    articles = [ Article("laptop 15\" 8GB RAM", 743.79),
                 Article("installation windows", 66.11),
                 Article("installation wifi", 45.22),
                 Article("carte graphique", 119.49),
                 ArticleReparation(0.75),
                 ArticlePiece(10,Piece("Livre: Ubuntu pour les nuls",6.60,0.33,tva = True)),
                 ArticlePiece(10,Piece("Souris Bluetooth",4.29,0.122,True))
                 ]
    
    @classmethod
    def run(cls) :
        fac = Facture("PC Store - 22 novembre", cls.articles)
        print(fac)
        print(fac.nombre(Piece("Livre: Ubuntu pour les nuls",6.60,tva = True)))
        print(fac.printLivraison())

if __name__ == "__main__":
    TestFactureInitial.run()
