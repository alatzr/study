class BinaryTree:
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right = None

    def insertLeft(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t
    
    def insertRight(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left
    
    def setRootVal(self, val):
        self.val = val

    def getRootVal(self):
        return self.val


