class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    ## Adding Child
    def addChild(self, child):
        # That instance variable will be parent of child
        child.parent = self
        ## Every child will be of type TreeNode
        self.children.append(child)



