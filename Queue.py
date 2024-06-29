class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        return True

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            if current.next:
                print("<-", end=" ")
            current = current.next
        print("None")

    def dequeue(self):
        if self.front is None:
            return None
        self.front = self.front.next
        self.front.prev = None
        return self.front

    def peek(self):
        if self.front is None:
            return None
        print(self.front.data)
        return self.front


if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)

    q.display()

    q.dequeue()
    q.display()

    q.peek()
