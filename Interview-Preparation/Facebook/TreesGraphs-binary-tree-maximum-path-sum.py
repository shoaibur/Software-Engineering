# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        maxSum = float('-inf')
        
        def gain(root):
            nonlocal maxSum
            if not root: return 0
            
            left = max(gain(root.left), 0)
            right = max(gain(root.right), 0)
            
            straightPath = root.val + max(left, right)
            newPath = root.val + left + right
            
            maxSum = max(maxSum, newPath)
            return straightPath
        
        gain(root)
        return maxSum
