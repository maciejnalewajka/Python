class Node:
    """Klasa Node"""
    
    def __init__(self, key= None, left=None, right=None, parent =None):
        self.key = key
        self.left_n  = left
        self.right_n = right
        self.parent_n = parent

class binaryTree:
    """Klasa drzewo binarne"""
    
    def __init__(self):
        self.korzen = None

    def insert(self, key):
        z = Node(key)
        y = None
        x = self.korzen
        while (x is not None):
            y = x
            if (z.key < x.key):
                x = x.left_n
            else:
                x = x.right_n
        if (y is None):
            self.korzen = z
        elif (z.key < y.key):
            y.left_n = z
            z.parent_n = y
        else:
            y.right_n = z
            z.parent_n = y

    def preorder(self,drzewo):
        if drzewo != None:
            self.preorder(drzewo.left_n)
            self.preorder(drzewo.right_n)

    def inorder(self,drzewo):
        if drzewo != None:
            self.inorder(drzewo.left_n)
            self.inorder(drzewo.right_n)

    def postorder(self,drzewo):
        if drzewo != None:
            self.postorder(drzewo.left_n)
            self.postorder(drzewo.right_n)