class Node:
    #Initializing a node object with data, previous pointer and next pointer set to None by default
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Node has list of elements
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Declaring new node to append with all node class attributes
        new_node = Node(data)

        # If Node list is empty, means no LL exists yet
        if self.head is None:
            # Assigning head to itself
            self.head = new_node
            return

        # If its not empty, we declare last element to get last attribute
        last_node = self.head
        # Finding last element parsing thru all list
        while last_node.next:
            last_node = last_node.next
        # Once we reach last element, it comes out of loop and assigns new node value to its pointer
        last_node.next = new_node
        last_node.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        # If the node is empty, it will point to itself
        if self.head is None:
            self.head = new_node
        # Else it will look for first element it has to point
        next_node = self.head
        new_node.next = next_node
        next_node.prev = new_node
        # Head is first element it counts for LL
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            if current.next:
                print("->", end=" ")
            current = current.next
        print("None")


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.display()  # Output: 2 -> 3 -> 4 None

    dll.prepend(1)
    dll.display()  # Output: 1 -> 2 -> 3 -> 4 None
