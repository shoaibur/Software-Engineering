# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None: return result
        cache = {}
        self.minC, self.maxC = 0, 0
        
        def dfs(node, r, c):
            if node == None: return
            if c in cache: cache[c].append([r, node.val])
            else: cache[c] = [[r, node.val]]
            self.minC = min(self.minC, c)
            self.maxC = max(self.maxC, c)
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
            
        dfs(root, 0, 0)
        for c in range(self.minC, self.maxC+1):
            col = sorted(cache[c], key=lambda x: (x[0], x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            result.append(col_sorted)
        return result
