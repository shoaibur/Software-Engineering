"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head: self.flatten_rec(head)
        return head
        
    def flatten_rec(self, head):
        curr = head
        child = curr.child
        next = curr.next
        if child:
            level = self.flatten_rec(child)
            level.next = next
            
            curr.child = None
            curr.next = child
            child.prev = curr
            
            next.prev = level
        curr = next
        
        return head
        
