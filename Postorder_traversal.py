class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printPostorder(root):
    if(root is None):
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.data,end=" ")

root = Node(5)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(2)
root.right.right = Node(6)

printPostorder(root)