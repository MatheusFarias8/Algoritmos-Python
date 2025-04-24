class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lengh = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp =  temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.lengh += 1
        return True

doublyLL = DoublyLinkedList(7)
doublyLL.append(5)
doublyLL.print_list()
print(F"HEAD = {doublyLL.head.value}")
print(F"TAIL = {doublyLL.tail.value}")
print(F"LENGHT = {doublyLL.lengh}")