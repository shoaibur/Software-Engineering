# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        if not root: return 0
        if not root.left and not root.right: return 1
        
        if not root.left:
            return self.maxDepth(root.right) + 1
        if not root.right:
            return self.maxDepth(root.left) + 1
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
