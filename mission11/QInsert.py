def insert(self, s):
    node = self.__head
    next_node = None
    previous_node
    while node.next != None:
        if s > node.value():
            next_node = node
            break
        previous_node = node
        node = node.next
    self.length += 1
    new_node = Node(s,next_node)    
    previous_node.set_next(new_node)