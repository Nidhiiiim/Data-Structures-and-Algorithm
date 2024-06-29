class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.top = None

    def push(self, value):
        self.stack.append(value)
        self.size += 1
        self.top = self
        return self

    def pop(self):
        if self.size == 0:
            self.top = None
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.size == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return self.size == 0

    def display(self):
        print(self.stack)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    # Pops  last element that was added
    s.peek()
