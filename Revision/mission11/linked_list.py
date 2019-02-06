class LinkedList:

    def __init__(self, lst=[]):
        self.__length = 0
        self.__head = None
        for elm in lst:
            node  = Node(elm, self.__head)
            self.__length += 1
            self.__head = node


    def add(self, cargo):
        new_node = Node(cargo,self.__head)
        self.__head = new_node
        self.__length += 1


    def insert(self, cargo):
        pass


    def __str__(self):
        local_head = self.__head
        lst_str = "["
        while local_head != None:
            lst_str += " " + str(local_head.cargo)
            local_head = local_head.next
        lst_str += " ]"
        return lst_str

    
    def get_length(self):
        return self.__length

            


class Node:
    def __init__(self, cargo, next = None):
        self.cargo = cargo
        self.next = next

    def get_next(self):
        return self.next
        

my_list = LinkedList([3,5,6])
print(my_list)
my_list.add(12)
print(my_list)
print(my_list.get_length())