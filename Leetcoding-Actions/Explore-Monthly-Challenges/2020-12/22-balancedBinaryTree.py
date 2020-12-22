# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        
        def height(root):
            if not root: return 0
            if not root.left:
                return height(root.right) + 1
            if not root.right:
                return height(root.left) + 1
            return max(height(root.left), height(root.right)) + 1
        
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
