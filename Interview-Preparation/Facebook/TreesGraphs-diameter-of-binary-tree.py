# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diameter = 0
        
        def depth(root):
            nonlocal diameter
            
            if not root: return 0
            
            left = depth(root.left)
            right = depth(root.right)
            
            diameter = max(diameter, left+right)
            
            return max(left, right) + 1
        
        depth(root)
        return diameter
