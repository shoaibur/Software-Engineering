# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        out = []
        
        def inorder(root):
            if root:
                inorder(root.left)
                out.append(root.val)
                inorder(root.right)
        inorder(root)
        
        for i in range(1,len(out)):
            if out[i-1] >= out[i]:
                return False
        return True
