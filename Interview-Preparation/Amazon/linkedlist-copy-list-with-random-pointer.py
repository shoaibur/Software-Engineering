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
        if head is None: return head
        
        def printLL(head):
            tail = head
            while tail:
                print(tail.val, end=' ')
                tail = tail.next
            return
        
        # make duplicates
        tail = head
        while tail:
            temp = tail.next
            tail.next = Node(tail.val)
            tail.next.next = temp
            tail = temp
                
        # copy random to duplicates
        tail = head
        while tail:
            if tail.random:
                tail.next.random = tail.random.next
            tail = tail.next.next
        
        # separate two lists
        tail = head
        clone = head.next
        clonetail = clone
        
        while tail:
            tail = tail.next.next
            clonetail.next = (clonetail.next.next if clonetail.next else None)
            clonetail = clonetail.next
        return clone
