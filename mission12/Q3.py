class Counters:
    def __init__ ( self, number ):
        self.__counter_list = []
        for i in range(number):
            self.__counter_list.append(-1)

    def next(self, number):
        try:
            self.__counter_list[number-1] += 1
            return self.__counter_list[number-1]
        except:
            raise


cln = Counters(10)
print(cln.next(10))
print(cln.next(10))