"""
Un ticket de parking
"""
class Ticket :

    __prochain_numero = 1  # variable de classe pour générer le numéro du ticket

    def __init__(self) :
        """
        @pre  -
        @post Crée un ticket avec un nouveau numéro.
              Les numéros sont attribués séquentiellement à partir de 1.
        """
        Ticket.__prochain_numero += 1
        self.__numero = Ticket.__prochain_numero

    

    def numero(self):
        """
        @pre  -
        @post retourne le numero de billet
        """
        return self.__numero


class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    def RobotInstances(self):
        return Robot.__counter
        

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())

x = Ticket()
y = Ticket()
z = Ticket()
y = Ticket()
print(y.numero())