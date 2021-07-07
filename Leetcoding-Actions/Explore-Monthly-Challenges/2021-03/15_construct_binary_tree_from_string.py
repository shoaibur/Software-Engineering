# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        '''
        T: O(n) and S: O(n)
        '''
        if not s: return
        
        def q2tree(q):
            if not q: return
            
            digits = ''
            q.popleft() # Remove (
            while q and q[0] != '(' and q[0] != ')':
                digits += q[0]
                q.popleft() # Remove digit
            root = TreeNode(int(digits))
            
            if q[0] == '(':
                root.left = q2tree(q) # If ( exists, construct left tree
                if q[0] == '(':
                    root.right = q2tree(q) # If still ( exists, construct right tree
            
            q.popleft() # Remove )
            return root
        
        q = deque(list('('+s+')'))
        return q2tree(q)
