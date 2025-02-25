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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True
        
first_LL = LinkedList(4)
first_LL.append(3)
first_LL.append(2)
first_LL.append(1)
first_LL.append(0)

first_LL.print_list()
print(f"HEAD: {first_LL.head.value}")
print(f"TAIL: {first_LL.tail.value}")
print(f"LENGHT: {first_LL.lenght}")