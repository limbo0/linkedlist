# A perfect binary tree is a type of binary tree in which every internal/parent node has ecactly  two child nodes and all the leaf nodes are in the same level.

class newNode:
    def __init__(self, k):
        self.key = k
        self.right = None
        self.left = None

# The depth of a node is the number of edges from the root to the node.
def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d

def is_perfect(root, d, level=0):

    # check if the tree is empty
    if (root is None):
        return True

    # check the presence of trees
    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False
    
    return (is_perfect(root.left, d, level + 1) and 
            is_perfect(root.right, d, level + 1))

root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

# remove the below to prove it's not
root.right.left = newNode(6)
root.right.right = newNode(7)



if (is_perfect(root, calculateDepth(root))):
    print("it's a perfect binary tree")

else:
    print("it's not a perfect binary tree")