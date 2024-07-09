class TreeNode:
    # Constructor for treenode class, initializes node with value key
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val

        # Takes root of tree as parameter


def inorder(root):
    # For storing values inorder
    res = []
    # If there is value in root
    if root:
        # Recursively go to left
        res = inorder(root.left)

        # Store all left node values
        res.append(root.val)
        res = res + inorder(root.right)

    # Gives the binary tree in order
    return res


def preorder(root):
    # To Store pre order array
    res = []
    if root:
        res.append(root.val)
        res = res + preorder(root.left)
        res = res + preorder(root.right)
    return res


def postorder(root):
    res = []
    if root:
        res = postorder(root.left)
        res = res + postorder(root.right)
        res = res + [root.val]
    return res


# All are recursive function, where function calls itself
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left is not None:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- " + "None")
            if root.right is not None:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- " + "None")


class Search:
    def depthfirstsearch(self, root: TreeNode):
        if root is None:
            return 0
        return 1 + max(self.depthfirstsearch(root.left), self.depthfirstsearch(root.right))

    def breadthfirstSearch(self, root: TreeNode):
        if root is None:
            return 0
        
## Solving Puzzles.


if __name__ == "__main__":
    root = TreeNode(5)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 9)
    root = insert(root, 2)
    root = insert(root, 4)
    print(inorder(root))
    print(preorder(root))
    print(postorder(root))
    print_tree(root)
    print(Search().depthfirstsearch(root))
