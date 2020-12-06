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
        T: O(n) and S: O(1) ignoring implicit q space
        '''
        if not root: return root
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            count = 0
            
            prevNode = None
            
            while count < size:
                currNode = q.popleft()
                
                if not prevNode:
                    prevNode = currNode
                else:
                    prevNode.next = currNode
                    prevNode = currNode
                
                if currNode.left: q.append(currNode.left)
                if currNode.right: q.append(currNode.right)
                count += 1
                
        return root
