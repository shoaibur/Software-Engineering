def invert_binary_tree(root):
    if root is None: return None
    new_left = self.invertTree(root.right)
    new_right = self.invertTree(root.left)
    root.left = new_left
    root.right = new_right
    return root
    
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
