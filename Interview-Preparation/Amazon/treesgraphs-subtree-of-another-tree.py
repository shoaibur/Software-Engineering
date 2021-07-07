# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def preorder(root):
            if root is None:
                return '#None'
            return '#'+str(root.val) + ' ' + preorder(root.left) + ' ' + preorder(root.right)
                
        S = preorder(s)
        T = preorder(t)
        return (T in S)
