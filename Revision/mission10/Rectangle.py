class Figure:
    def __init(self, x, y , visible = False):
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
        super().__init__(x,y)
        self.longeur = lo
        self.largeur = la

    def __str__(self) :
        return "({},{},{},{},{})".format(self.longeur,self.largeur,self.x,self.y,self.estVisible())