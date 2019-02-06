class Ticket:
    __prochain_numero = 1

    def __init__(self):
        self.__numero = 0
        self.__numero = Ticket.__prochain_numero
        Ticket.__prochain_numero += 1

    def numero(self):
        return self.__numero


t1 = Ticket()
t2 = Ticket()
print(t1.numero())
print(t2.numero())