# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
        for i in range(len(res)):
            if i%2:
                res[i] = res[i][::-1]
        return res
