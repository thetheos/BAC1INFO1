class LinkedList:
    class Node:
        def __init__(self,cargo):
            self.__cargo = cargo
            self.__next = None
            self.__previous = None

        def set_next(self, nxt_node):
            if isinstance(nxt_node, LinkedList.Node):
                self.__next = nxt_node
                return True
            else:
                return False

        def set_previous(self, prvs_node):
            self.__previous = prvs_node

        def set_cargo(self, cargo):
            if isinstance(cargo, string):
                self.__cargo = cargo
                return True
            else:
                return False

        def get_cargo(self):
            return self.__cargo

        def get_next(self):
            return self.__next

        def get_previous(self):
            return self.__previous     

        def __str__(self):
            if self.__next == None and self.__previous == None:
                return "cargo: {0:<10}, next: {1:<10}, previous: {2:<10}".format(self.__cargo, str(None), None)
            elif self.__next == None:
                return "cargo: {0:<10}, next: {1:<10}, previous: {2:<10}".format(self.__cargo, str(None), self.__previous.get_cargo())
            elif self.__previous == None:
                return "cargo: {0:<10}, next: {1:<10}, previous: {2:<10}".format(self.__cargo, self.__next.get_cargo(), str(None))
            else:
                return "cargo: {0:<10}, next: {1:<10}, previous: {2:<10}".format(self.__cargo, self.__next.get_cargo(), self.__previous.get_cargo())
                
                
                   

    def __init__(self):
        self.__head = None
        self.__length = 0

    def add(self, cargo):
        new_node = LinkedList.Node(cargo)
        new_node.set_next(self.__head)
        if isinstance(self.__head, LinkedList.Node):
            self.__head.set_previous(new_node)
        self.__head = new_node
        self.__length += 1

    def insert(self, cargo):
        local_head = self.__head
        if local_head == None:
            self.add(cargo)
            return
        else:
            new_node = LinkedList.Node(cargo)
        self.__length += 1
        while local_head != None:
            if local_head.get_cargo() > new_node.get_cargo():
                #Check si local_head et en tete de liste
                if local_head.get_previous() != None:
                    local_head.get_previous().set_next(new_node)
                    new_node.set_previous(local_head.get_previous())
                else:
                    self.__head = new_node

                local_head.set_previous(new_node)
                new_node.set_next(local_head)
                break
            
            if local_head.get_next() == None:
                local_head.set_next(new_node)
                new_node.set_previous(local_head)
                break

            local_head = local_head.get_next()

    def remove(self, cargo):
        local_head = self.__head
        while local_head != None:
            if local_head.get_cargo() == cargo:
                if local_head.get_next() != None:
                    local_head.get_next().set_previous(local_head.get_previous())
                if local_head.get_previous() != None:
                    previous = local_head.get_previous()
                    previous.set_next(local_head.get_next())
                else:
                    self.__head = local_head.get_next()
                self.__length -= 1
                break
            else:
                local_head = local_head.get_next()

        

    
    def get_lenght(self):
        return self.__length

    
    def __str__(self):
        outpu_str = ""
        local_head = self.__head
        while local_head != None:
            outpu_str += str(local_head) + "\n"
            local_head = local_head.get_next()
        return outpu_str

    def simple_print(self):
        outpu_str = "["
        local_head = self.__head
        while local_head != None:
            outpu_str += str(local_head.get_cargo()) + " "
            local_head = local_head.get_next()
        return outpu_str + "]"
        


mylst = LinkedList()

mylst.add("salut")
mylst.add("comment")
mylst.add("va")
mylst.remove("va")
mylst.insert("fafa")
mylst.insert("ecole")
mylst.insert("aba")
mylst.insert("tot")
mylst.insert("zingzang")
mylst.insert("dora")
mylst.remove("dora")
print(mylst)
print(mylst.simple_print())


