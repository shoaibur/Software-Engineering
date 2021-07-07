# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True
        
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node is None:
                return not any(q)
            q.append(node.left)
            q.append(node.right)
        return True
