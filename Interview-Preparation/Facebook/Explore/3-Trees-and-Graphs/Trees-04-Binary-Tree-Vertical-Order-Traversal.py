# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        q = deque()
        q.append((0, 0, root))
        
        data = {}
        
        while q:
            i, j, node = q.popleft()
            if i in data:
                data[i].append((j, node.val))
            else:
                data[i] = [(j, node.val)]
                
            if node.left: q.append((i-1, j+1, node.left))
            if node.right: q.append((i+1, j+1, node.right))
        
        minCol = min(list(data.keys()))
        maxCol = max(list(data.keys()))
        
        result = []
        for col in range(minCol, maxCol+1):
            temp = sorted(data[col], key = lambda x: x[0])
            temp = [item[1] for item in temp]
            result.append(temp)
        return result
