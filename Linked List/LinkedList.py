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
        
    def pop(self):
        temp = 0
        head = self.head
        tail = self.tail
        
        if not self.lenght:
            return None

        elif self.lenght == 1:
            temp = self.head
            self.head = None
            self.lenght -= 1
            return temp

        while head is not None:
            if head.next == tail:
                temp = tail
                self.tail = head
                head.next = None
                self.lenght -= 1
                break
            head = head.next

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.lenght += 1
        return True


first_LL = LinkedList(4)
first_LL.append(3)
first_LL.append(2)
first_LL.append(1)

popped = first_LL.pop()

first_LL.prepend(5)

first_LL.print_list()
print(f"HEAD: {first_LL.head.value}")
print(f"TAIL: {first_LL.tail.value}")
print(f"LENGHT: {first_LL.lenght}")
print(f"POPPED: {popped.value}")