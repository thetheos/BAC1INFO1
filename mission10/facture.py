"""
    Une facture, sous forme d'une liste d'articles.
   
    @author Kim Mens
    @version 18 novembre 2018
    (code adaptÃ© du code java de Charles Pecheur)
"""


class Facture :

    __facture_count = 0

    def __init__(self, description, articles):
        """
        CrÃ©e une facture avec une description (titre) et un liste d'articles.
        """
        self.__reference = description
        self.__articles = articles
        Facture.__facture_count += 1

    def description(self):
        """
        Retourne la description de cette facture.
        """
        return self.__reference

    def articles(self):
        """
        Retourne la liste des articles de cette facture.
        """
        return self.__articles
        
    def __str__(self):
        """
        Retourne la reprÃ©sentation string d'une facture, Ã  imprimer avec la mÃ©thode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles() :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        Imprime l'entÃªte de la facture, comprenant le descriptif et les tÃªtes de colonnes.
        """
        e = "Facture " + str(Facture.__facture_count) + " " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC")
        e += self.barre_str()
        return e

    def entete_livraison_str(self):
        """
        Imprime l'entÃªte de la livraison, comprenant le descriptif et les tÃªtes de colonnes.
        """
        e = "Livraison - Facture No " + str(Facture.__facture_count) + " : " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string reprÃ©sentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
        Retourne un string correspondant Ã  une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())
    

    def piece_livraison_str(self, art):
        """
        Retourne un string correspondant Ã  une ligne de facture pour l'article art
        """
        if art.fragile() == True:
            return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description() + " (!)", art.poids() , self.nombre(art), art.poids() * self.nombre(art))
    
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.poids(), self.nombre(art), art.poids() * self.nombre(art))
    

    def totaux_str(self, prix, tva):
        """
        Retourne un string reprÃ©sentant une ligne de facture avec les totaux prix et tva, Ã  imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva)
        b += self.barre_str()
        return b

    def totaux_livraison_str(self, count, n, poids):
        """
        Retourne un string reprÃ©sentant une ligne de facture avec les totaux prix et tva, Ã  imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10} | {2:10.2f} | {3:10.2f} |\n".format(str(count) + " Articles", "", n, poids)
        b += self.barre_str()
        return b
        
    # This method needs to be added during Etape 4 of the mission
    def nombre(self, pce) :
        """
        Retourne le nombre d'exemplaires de la piÃ¨ce pce dans la facture, en totalisant sur tous les articles qui concernent cette piÃ¨ce.
        """
        total_count = 0
        for item in self.__articles:
            try:
                if item.item() == pce:
                    total_count += item.item_count()
            except:
                pass
        return total_count


    def printLivraison(self):
        """
        Retourne la reprÃ©sentation string d'une facture, Ã  imprimer avec la mÃ©thode print().
        """
        s = self.entete_livraison_str()
        totalArticle = 0
        totalPoids = 0.0
        count = 0
        fragile = False
        for art in self.articles() :
            try:
                s += self.piece_livraison_str(art.item())
                if art.item().fragile() == True:
                    fragile = True
                count += 1
                totalArticle += self.nombre(art.item())
                totalPoids += art.poids()
            except:
                pass
        s += self.totaux_livraison_str(count,totalArticle, totalPoids)
        if fragile == True:
            s += "(!) ***Attention livraison fragile***"
        return s

    # This method needs to be added during Etape 5 of the mission
    def livraison_str(self):
        """
        Cette mÃ©thode est une mÃ©thode auxiliaire pour la mÃ©thode printLivraison
        """
        pass
