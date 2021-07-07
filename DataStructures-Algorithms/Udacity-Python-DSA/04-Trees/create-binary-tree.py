class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
