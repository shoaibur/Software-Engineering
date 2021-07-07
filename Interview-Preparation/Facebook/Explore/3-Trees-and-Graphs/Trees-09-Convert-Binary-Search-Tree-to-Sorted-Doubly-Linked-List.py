"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        nodes = []
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root)
                inorder(root.right)
        inorder(root)
        
        for i in range(len(nodes)-1):
            nodes[i].right = nodes[i+1]
            nodes[i+1].left = nodes[i]
        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]
        
        return nodes[0]
