class Figure:

    def __init__(self,x,y,visible=False):
        """
        @pre x, y sont des entiers représentant des positions sur l'écran
        @post Une figure a été créée avec centre de gravité aux coordonnées x,y.
              Cette figure n'est initialement pas visible
        """
        self.__x = x
        self.__y = y
        self.__visible = visible

    def surface(self):
        """
        @pre -
        @post la surface (un float) de la figure a été calculé et retournée
        """
        pass            # code non fourni

    def estVisible(self):
        """
        @pre -
        @post a retourné la visibilité de cette figure
        """
        return self.__visible

"""
LEs variable d'instance x et y sont devenus privé du coup on ne peut plus les imprimer
"""

class Rectangle(Figure):

    def __init__(self,lo,la,x,y):
        """
        @pre longeur,largeur sont des entiers positifs
        @post un rectangle dont le centre de gravite est en x,y
              et ayant longueur et largeur a été créé
        """
        
        self.longeur = lo
        self.largeur = la
        super().__init__(x,y)

    def __str__(self) :
        return "({},{},{},{},{})".format(self.longeur,self.largeur,super().__x,super.__y,self.estVisible())

    def surface(self):
        return super().__x * super().__y

"""
POur que le code refonctionne il faudrait creer des méthode dans la classe figure qui retournerai les attributs locaux de cette classe.
"""
r = Rectangle(10,20,10,2)
print(r)
print(r.surface())
print(r.estVisible())
