class Node:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, student_id):
        new_node = Node(name, student_id)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

# สร้าง linked list
linked_list = LinkedList()

# เพิ่มข้อมูลลงใน linked list
linked_list.append("นศ.อัญชิสา", 65030289)

# แสดงข้อมูลใน linked list
current_node = linked_list.head
while current_node:
    print("Name:", current_node.name)
    print("Student ID:", current_node.student_id)
    print("-----")
    current_node = current_node.next
