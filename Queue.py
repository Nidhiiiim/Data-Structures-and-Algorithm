### QUEUE IMPLEMENTATION USING LINKEDLIST ###
class QNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self,data):
        node = QNode(data)
        if self.isEmpty():
            self.front = node
            self.rear = node
            self.size += 1
        self.rear = node
        return node
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
            return None

