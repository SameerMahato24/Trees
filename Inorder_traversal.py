class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printInorder(root):
    if(root is None):
        return
    printInorder(root.left)
    print(root.data,end=" ")
    printInorder(root.right)

root = Node(5)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(2)
root.right.right = Node(6)

printInorder(root)