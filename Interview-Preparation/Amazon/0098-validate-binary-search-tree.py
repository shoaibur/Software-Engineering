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
            return out
        out = inorder(root)
        print(out)
        if len(out) <= 1: return True
        
        for i in range(len(out)-1):
            if out[i+1] <= out[i]:
                return False
        return True
    
