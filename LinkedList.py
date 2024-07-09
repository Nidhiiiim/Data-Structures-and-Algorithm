class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
    ## CHECK IF EMPTY
    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return new_node
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        return new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return new_node
    def delete(self, data):
        if self.isEmpty():
            print("The list is empty")
            return False
        key = self.head
        while key.next is not None:
            if key.next.data != data:
                key = key.next
            key.next = key.next.next
            self.size -= 1
            print("Deleted value")
            return True

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0

    def append(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return new_node
        self.tail.next = new_node
        self.tail = new_node
        new_node.prev = self.tail
        self.size += 1
        return new_node

    def prepend(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return new_node
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return new_node





