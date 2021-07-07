# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        visited = set()
        duplicates = set()
        tail = head
        while tail:
            if tail.val in visited:
                duplicates.add(tail.val)
            visited.add(tail.val)
            tail = tail.next
        
        newHead = ListNode(-101)
        newTail = newHead
        
        tail = head
        while tail:
            if tail.val not in duplicates:
                newTail.next = ListNode(tail.val)
                newTail = newTail.next
            tail = tail.next
            
        return newHead.next
