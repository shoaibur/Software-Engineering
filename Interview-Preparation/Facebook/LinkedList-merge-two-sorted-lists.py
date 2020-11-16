# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None: return l1
        if l1 is None and l2: return l2
        if l1 and l2 is None: return l1
        
        l = ListNode(0)
        t1, t2, t = l1, l2, l
        
        while t1 or t2:
            val1 = (t1.val if t1 else float('inf'))
            val2 = (t2.val if t2 else float('inf'))
            
            if val1 <= val2:
                t.next = ListNode(val1)
                t1 = (t1.next if t1 else None)
            else:
                t.next = ListNode(val2)
                t2 = (t2.next if t2 else None)
            t = t.next
        
        return l.next
