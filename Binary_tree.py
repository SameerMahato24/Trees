class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)

print(root.right.data)
print(root.left.right.data)