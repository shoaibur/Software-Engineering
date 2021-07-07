# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        if not root: return 0
        
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            count = 0
            summ = 0
            while count < size:
                curr = q.popleft()
                summ += curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
                count += 1
        
        return summ
