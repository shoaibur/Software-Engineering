# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        out = []
        q = collections.deque()
        q.append((root, 0, 0))
        
        while q:
            temp, i, j = q.popleft()
            out.append((temp.val, i, j))
            
            if temp.left:
                q.append((temp.left, i-1, j-1))
            if temp.right:
                q.append((temp.right, i+1, j-1))
                
        out.sort(key = lambda x: (x[1]))
        
        val, previ, prevj = out[0]
        result = [[val]]
        
        for item in out[1:]:
            currVal, curri, currj = item
            if curri == previ:
                result[-1].append(currVal)
            else:
                result.append([currVal])
            previ, prevj = curri, currj
            
        return result
