# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        levels = []
        q = collections.deque()
        q.append(root)
        
        while q:
            size = len(q)
            count = 0
            temp = []
            while count < size:
                p = q.popleft()
                temp.append(p.val)
                
                if p.left: q.append(p.left)
                if p.right: q.append(p.right)
                count += 1
            levels.append(temp)
        
        result = []
        for item in levels:
            result.append(item[-1])
        return result
