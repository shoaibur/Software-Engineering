# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        head = ListNode(0)
        tail = head
        
        t1, t2 = l1, l2
        while t1 or t2:
            v1 = t1.val if t1 else float('inf')
            v2 = t2.val if t2 else float('inf')
            
            if v1 <= v2:
                tail.next = ListNode(v1)
                t1 = t1.next if t1 else None
            else:
                tail.next = ListNode(v2)
                t2 = t2.next if t2 else None
            tail = tail.next
        return head.next
