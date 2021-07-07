# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None: return 0
        
        max_sum = -float('inf')
        
        def gain(root):
            nonlocal max_sum
            if root is None: return 0
            
            left = max(gain(root.left), 0)
            right = max(gain(root.right), 0)
            
            straight_path = root.val + max(left, right)
            new_path = root.val + left + right
            
            max_sum = max(max_sum, new_path)
            return straight_path
        
        gain(root)
        return max_sum
