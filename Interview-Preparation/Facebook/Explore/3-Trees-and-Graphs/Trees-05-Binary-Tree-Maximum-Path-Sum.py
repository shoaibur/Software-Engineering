# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        maxPathSum = float('-inf')
        
        def gain(root):
            if not root: return 0
            nonlocal maxPathSum
            
            left = max(gain(root.left), 0)
            right = max(gain(root.right), 0)
            
            straightPathSum = root.val + max(left, right)
            newPathSum = root.val + left + right
            
            maxPathSum = max(maxPathSum, newPathSum)
            return straightPathSum
        
        gain(root)
        return maxPathSum
