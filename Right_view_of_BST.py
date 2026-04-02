class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self,x):
        if(self.front == -1):
            self.front = 0
        self.q.append(x)

    def pop(self):
        if(len(self.q)==0):
            return None
        x = self.q[self.front]
        self.front+=1
        if(self.front == len(self.q)):
            self.front = -1
            self.q = []
        return x

    def getFront(self):
        if(len(self.q)==0):
            return None
        else:
            return self.q[self.front]

    def size(self):
        if(self.front == -1):
            return 0
        return len(self.q)-self.front 
        
           
class Solution:
    def levelOrder(self, root):
        ans = []
        if(root is None):
            return ans

        queue = Queue()
        queue.push(root)
        ans.append(root.data)

        while queue.size()>0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                if(front.left!=None):
                    queue.push(front.left)
                    level.append(front.left.data)
                if(front.right!=None):
                    queue.push(front.right)
                    level.append(front.right.data)

            if(len(level)>0):
                ans.append(level[-1])
                 
        print(ans)
    
root = Node(5)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(2)
root.right.right = Node(6)
soln=Solution()
soln.levelOrder(root)
        