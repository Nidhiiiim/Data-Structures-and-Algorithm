class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

   def __init__(self):
       self.root = None

    def preorder(self):
        return self._preorder(self.root, [])

    def _preorder(self, node, res):
        if node:
            res.append(node.val)
            self._preorder(node.left, res)
            self._preorder(node.right, res)
        return res

    def insert(self, value):
        if self.root is None:
            return Node(value)
        else:
            if self.root.value == value:
                return self.root
            elif value < self.root.value:
                self.root.left = self.insert(self.root.left, value)
            else:
                self.root.right = self.insert(self.root.right, value)
        return self.root


    def dfs(self, value):
        if self.root is None:
            return False
        if self.root.value == value:
            return True
        elif value < self.root.value:
            return self.dfs(self.root.left, value)
        else:
            return self.dfs(self.root.right, value)


def print_tree(root):
    if root is None:
        return None
    print_tree(root.left)


if __name__ == '__main__':
    bst = BinarySearchTree(5)
    bst.insert(r, 3)
    r = insert(r, 5)
    r = insert(r, 6)
    r = insert(r, 2)
    print(inorder(r))
    print(preorder(r))
    print(postorder(r))
    print(dfs(r, 3))
