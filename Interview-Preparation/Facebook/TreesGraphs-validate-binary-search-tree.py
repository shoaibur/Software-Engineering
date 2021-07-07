# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        data = []
        def inorder(root):
            if root:
                inorder(root.left)
                data.append(root.val)
                inorder(root.right)
            return data
        inorder(root)
        for i in range(len(data)-1):
            if data[i] >= data[i+1]:
                return False
        return True
