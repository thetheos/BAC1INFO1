class Employe:
    def __init__(self, name, salaire):
        self.name = name
        self.salaire = salaire

    def augmente(self, pourcen_salaire):
        self.salaire = self.salaire + (self.salaire*pourcen_salaire)
        return True

    
    def __str__(self):
        return "Nom de l'emplye: {} , salaire: {}".format(self.name, self.salaire)

        