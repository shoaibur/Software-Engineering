"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        
        # duplicates
        tail = head
        while tail:
            temp = tail.next
            tail.next = Node(tail.val)
            tail.next.next = temp
            tail = temp
        
        # copy random
        tail = head
        while tail:
            if tail.random:
                tail.next.random = tail.random.next
            tail = tail.next.next
        
        # separate
        tail = head
        clone = head.next
        clone_tail = clone
        
        while tail:
            tail = tail.next.next
            clone_tail.next = clone_tail.next.next if clone_tail.next else None
            clone_tail = clone_tail.next
        return clone
