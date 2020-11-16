# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if not root: return 0
        
        summ = 0
        
        stack = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack: break
            curr = stack.pop()
            if curr.val >= L and curr.val <= R:
                summ += curr.val
            if curr.val > R: return summ
            curr = curr.right
        return summ
