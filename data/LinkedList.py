class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def pop(self):
        if self.length == 0:
            return None
        temp_node = self.head
        prev_node = self.head
        while temp_node.next is not None:
            prev_node = temp_node
            temp_node = temp_node.next
        self.tail = prev_node
        prev_node.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp_node.value

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.pop_first()
my_linked_list.pop_first()
print(my_linked_list.print_list())
