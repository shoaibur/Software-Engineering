# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        totalTilt = 0
        def tiltSum(root):
            nonlocal totalTilt
            if not root: return 0
            
            leftSum = tiltSum(root.left)
            rightSum = tiltSum(root.right)
            tilt = abs(leftSum - rightSum)
            totalTilt += tilt
            
            return leftSum + rightSum + root.val
        
        tiltSum(root)
        return totalTilt
