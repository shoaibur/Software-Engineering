"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        T: O(n) and S: O(2^(H-1)); H = height of tree
        '''
        if not root: return None
        
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            count = 0
            temp = []
            
            while count < size:
                currNode = q.popleft()
                temp.append(currNode)
                if currNode.left: q.append(currNode.left)
                if currNode.right: q.append(currNode.right)
                count += 1
                
            for i in range(len(temp)-1):
                temp[i].next = temp[i+1]
            temp[-1].next = None
            
        return root
