# Node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList constructor
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

first_LL = LinkedList(4)

print(first_LL.head.value)