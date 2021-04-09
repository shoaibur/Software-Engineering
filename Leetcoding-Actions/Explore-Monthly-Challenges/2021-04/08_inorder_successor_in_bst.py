# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return None
        
        stack = []
        curr = root
        
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack: break
            curr = stack.pop()
            
            if curr.val > p.val:
                return curr
            curr = curr.right
            
        return None
