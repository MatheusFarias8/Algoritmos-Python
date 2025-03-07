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
        self.length = 1
    
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

        self.length += 1
        return True
        
    def pop(self):
        temp = 0
        head = self.head
        tail = self.tail

        if not self.length:
            return None

        elif self.length == 1:
            temp = self.head
            self.head = None
            self.length -= 1
            return temp

        while head is not None:
            if head.next == tail:
                temp = tail
                self.tail = head
                head.next = None
                self.length -= 1
                break
            head = head.next

        return temp

    def pop_first(self):
        temp = self.head

        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None

        self.head = temp.next
        temp.next = None
        self.length -= 1

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

first_LL = LinkedList(4)
first_LL.append(3)
first_LL.append(2)
first_LL.append(1)

popped = first_LL.pop()


first_LL.prepend(5)
first_pop = first_LL.pop_first()


first_LL.print_list()
print(f"HEAD: {first_LL.head.value}")
print(f"TAIL: {first_LL.tail.value}")
print(f"LENGTH: {first_LL.length}")
print(f"POPPED: {popped.value}")
print(f"POPPED FIRST: {first_pop.value}")
print(f"GET: {first_LL.get(0).value}")