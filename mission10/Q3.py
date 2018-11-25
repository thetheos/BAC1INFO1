class Figure:

    def __init__(self,x,y,visible=False):
        """
        @pre x, y sont des entiers représentant des positions sur l'écran
        @post Une figure a été créée avec centre de gravité aux coordonnées x,y.
              Cette figure n'est initialement pas visible
        """
        self.x = x
        self.y = y
        self.__visible = visible

    def estVisible(self):
        """
        @pre -
        @post a retourné la visibilité de cette figure
        """
        return self.__visible

    def surface(self):
        """
        @pre -
        @post la surface (un float) de la figure a été calculé et retournée
        """
        pass            # code non fourni

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
        return "({},{},{},{},{})".format(self.longeur,self.largeur,self.x,self.y,self.estVisible())

    def surface(self):
        return self.x * self.y


"""
- self.x,self.y; self.__visible, self.longeur, self.largeur
-Elle appelle la fonction init de figure puis assigne ses attributs d'instance
-Ca appelle init de figure
-Rien mais c'est pas bien


Surface doit être redéfini (tt dépend de comment a été définis surface dans figure eft)
estVisible ne doit pas l'être
"""
r = Rectangle(10,20,10,2)
print(r)
print(r.surface())
print(r.estVisible())

