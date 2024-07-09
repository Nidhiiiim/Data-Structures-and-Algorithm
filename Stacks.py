### IMPLEMENTING STACK USING ARRAYS
class stack:
    def __init__(self):
        # Need empty list called stack
        # self method initialioses variable for the instance with all structure attributes
        self.stack = []
        self.size = 0
        self.top = None

    ## PUSHING
    def push(self, value):
        self.stack.append(value)
        self.size += 1
        self.top = self.stack[-1]
    def pop(self):
        if self.size == 0:
            print("Stack is empty")
            return None
        return self.stack.pop()

    def peek(self):
        if self.size == 0:
            print("Stack is empty")
            return None
        return self.stack[-1]

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    s = stack()
    s.push(5)
    s.push(6)
    s.push(7)
    print(s.top)
    s.pop()
