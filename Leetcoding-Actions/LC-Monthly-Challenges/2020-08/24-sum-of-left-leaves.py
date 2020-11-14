# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        
        q = deque()
        q.append((root, False))
        
        summ = 0
        while q:
            node, left = q.popleft()
            if left and not node.left and not node.right:
                summ += node.val
            if node.left: q.append((node.left, True))
            if node.right: q.append((node.right, False))
        return summ
