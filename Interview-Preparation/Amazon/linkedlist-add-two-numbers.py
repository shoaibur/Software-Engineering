# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None: return l1
        if l1 is not None and l2 is None: return l1
        if l1 is None and l2 is not None: return l2
        
        l = ListNode(0)
        t1, t2, t = l1, l2, l
        
        carry = 0
        
        while t1 or t2 or carry:
            val1 = (t1.val if t1 else 0)
            val2 = (t2.val if t2 else 0)
            t1 = (t1.next if t1 else None)
            t2 = (t2.next if t2 else None)
            
            summ = val1 + val2 + carry            
            carry, s = divmod(summ, 10) # summ//10, summ%10
            
            t.next = ListNode(s)
            t = t.next
            
        return l.next
