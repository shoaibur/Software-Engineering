# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        nodes = []
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root.val)
                inorder(root.right)
        inorder(root)
        
        for i in range(len(nodes)-1):
            if nodes[i] >= nodes[i+1]:
                return False
        return True

    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = float('-inf')
        stack = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack: break
            
            curr = stack.pop()
            if prev >= curr.val:
                return False
            prev = curr.val
            curr = curr.right
        return True
