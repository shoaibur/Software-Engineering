# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        res = []
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            size = len(q)
            count = 0
            temp = []
            while count < size:
                pop = q.popleft()
                temp.append(pop.val)
                count += 1
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            res.append(temp)
        return res
