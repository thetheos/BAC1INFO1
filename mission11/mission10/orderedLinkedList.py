"""
Code Réalisé par Théo Vanden Driessche dit Thetheos dit Blaster
"""

class OrderedLinkedList:
    
    def __init__(self):
        """
        Initialises a new linked list object.
        @pre:  -
        @post: A new empty linked list object has been initialised.
               It has 0 length, contains no nodes and the head points to None.
        """
        self.__length = 0
        self.__head = None

    def size(self):
        """
        Returns the number of nodes contained in this linked list
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list
        """
        return self.__length

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the front of this linked list.
        @pre: self is a (possibly empty) LinkedList
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented.
               The head of the list now points to this new node.
        """
        node = Node(cargo,self.__head)
        self.__head = node
        self.__length += 1

    def insert(self, cargo_to_insert):
        """
            Insert in the linkedList a value following certain conditions
        """
        local_head = self.__head
        node_to_insert = Node(cargo_to_insert)
        previous_node = None

        #Verifie que le cargo donnée est d'un type compatible
        """
        if isinstance(cargo_to_insert, int) != True and isinstance(cargo_to_insert, float) != True:
            return
        """
        #Si la liste est vide, on rajoute l'element.
        if local_head == None:
            self.add(cargo_to_insert)

        #Boucle principale
        while local_head != None:
            if local_head.value() >= cargo_to_insert:
                if previous_node == None:                   #Cas où il faudrait l'inserenr en tête de liste
                    node_to_insert.set_next(local_head)
                    self.__head = node_to_insert
                    self.__length += 1
                else:                                       #Cas où il faut inserer un nouveau noed ni en tête ni en queue de liste
                    previous_node.set_next(node_to_insert)
                    node_to_insert.set_next(local_head)
                    self.__length += 1
                break
            else:
                previous_node = local_head
                local_head = local_head.get_next()
                if local_head == None:                  #Cas s'il faut inserer un nouveau noed en queue de liste
                    node_to_insert.set_next(None)
                    self.__length += 1
                    previous_node.set_next(node_to_insert)


    def remove(self, cargo_to_remove):
        local_head = self.__head
        previous_node = None
        while local_head != None:
            if local_head.value().coureur() == cargo_to_remove:
                if previous_node == None:
                    self.__head = local_head.get_next()
                else:
                    previous_node.set_next(local_head.get_next())
                self.__length -= 1
                return
            else:
                previous_node = local_head
                local_head = local_head.get_next()
        return
    
    def get_first(self):
        """
            return the head ot the linked list
        """
        return self.__head


    def print(self):
        """
        Prints the contents of this linked list and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end="")
        if self.__head is not None:
            print(" ", end="")
            self.__head.print_list(" ")
        print(" ]")


    def print_avec_virgule(self):
        """
        Retoure un str des node séparées pr des virhules
        """
        print("[", end="")
        if self.__head is not None:
            print(" ", end="")
            self.__head.print_list(", ")
        print(" ]")

    def print_to_list(self):
        lst =[]

        return lst
    def print_backward(self):
        """
        Prints the contents of this linked list and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")



class Node:

    def __init__(self, cargo=None, next=None):
        """
        Initialises a new Node object.
        @pre:  -
        @post: A new Node object has been initialised.
               A node can contain a cargo and a reference to another node.
               If none of these are given, a node with empty cargo (None) and no reference (None) is created.
        """
        self.__cargo = cargo
        self.__next  = next

    def value(self):
        """
        Returns the value of the cargo contained in this node.
        @pre:  -
        @post: Returns the value of the cargo contained in this node, or None if no cargo  was put there.

        """
        return self.__cargo

    def __str__(self):
        """
        Returns a string representation of the cargo of this node.
        @pre:  self is possibly empty Node object
        @post: returns a print representation of the cargo contained in this Node
        """
        return str(self.value())

    def print_list(self,sep):
        """
        Prints the cargo of this node and then recursively of each node connected to this one.
        @pre:  self is a node (possibly connected to a next node)
        @post: Has printed a space-separated list of the form "a b c ... ",
               where "a" is the string-representation of this node,
               "b" is the string-representation of my next node, and so on.
               A space is printed in-between the printed value.
        """
        head = self
        tail = self.__next      # go to my next node
        print(head, end="")  # print my head
        if tail is not None : # as long as the end of the list has not been reached
            print(sep, end="")
            tail.print_list(sep) # recursively print remainder of the list

    def print_backward(self):
        """
        Recursively prints the cargo of each node connected to this node (in opposite order), and then prints the cargo of this node as last value.
        @pre:  self is a node (possibly connected to a next node)
        @post: Has printed a space-separated list of the form "... c b a",
               where a is my cargo (self), b is the cargo of the next node, and so on.
               The nodes are printed in opposite order: the last nodes' value is printed first.
        """
        head = self
        tail = self.__next                # go to my next node
        if tail is not None :           # as long as the end of the list has not been reached
            tail.print_backward() # recursively print remainder of the list backwards
        print(head, end = " ")          # print my head


    def get_next(self):
        """
        Return the next node
        """
        return self.__next


    def set_next(self,next_node):
        """
        Set the next node
        """
        self.__next = next_node

""" 
l = OrderedLinkedList()

#l.add(5)
l.insert(3)
l.insert(7)
l.insert(5)
l.insert(12)
l.insert(2.3)
l.insert(2.42)
l.print()
l.remove(7)
l.print()
l.insert(7)
l.print()
"""