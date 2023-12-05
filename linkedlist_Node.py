Class Node:
    def _init_(self, data):
        self.data = data
        self.pext = None
        
Class LinkedList:
    def _init_(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insext_at_tail(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self)
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:        
