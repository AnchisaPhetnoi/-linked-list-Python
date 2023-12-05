class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Corrected the attribute name from 'pext' to 'next'

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):  # Corrected the method name from 'insext_at_tail' to 'insert_at_tail'
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                # Do something when the data is found
                return True
            current_node = current_node.next
        return False  # Return False if the data is not found

# สร้าง linked list
linked_list = LinkedList()
linked_list = LinkedList()
linked_list.insert_at_head(10)
linked_list.insert_at_head(20)
linked_list.insert_at_tail(30)


print("Anchisa Phetnoi")
linked_list.print_list()
print(linked_list.search(20))
print(linked_list.search(40))

linked_list.insert_at_head(20)
linked_list.print_list()

    
