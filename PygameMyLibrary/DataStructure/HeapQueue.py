

class Node:
    def __init__(self, left, right, data):
        self.right = right
        self.left = left
        self.data = data

class HeapQueue:
    def __init__(self, root = None):
        self.root = root

    def pop(self):
        if self.root == None: return None
        return self.reconstruction(self.root)
    def reconstruction(self, node : Node):

        right = node.right.data
        left = node.left.data

        self.reconstruction(node.right if right < left else node.left)

    def __str__(self):
        return self.pr(self.root)

    def pr(self, node : Node):
        left = node.left
        right = node.right

        res : str = ""
        if left != None: res += self.pr(left)+" "
        if right != None: res += self.pr(right)+" "
        res+=str(node.data)
        return res

root = Node(None, None, 5)
root.right = Node(None, None, 3)
root.left = Node(None, None, 2)
root.right.right = Node(None, None, 0)
Heap = HeapQueue(root)
print(Heap)




