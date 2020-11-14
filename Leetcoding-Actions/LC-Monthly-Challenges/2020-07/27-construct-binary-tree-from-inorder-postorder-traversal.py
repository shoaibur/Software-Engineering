# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        # inorderMap = {num: i for i,num in enumerate(inorder)}
        
        if not inorder: return None
        
        root_val = postorder.pop()
        root_idx = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.right = self.buildTree(inorder[root_idx+1:], postorder)
        root.left = self.buildTree(inorder[:root_idx], postorder)
        
        return root
