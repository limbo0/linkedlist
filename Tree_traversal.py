class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        #traverse root
        print(str(root.val) + "->", end="")
        inorder(root.right)