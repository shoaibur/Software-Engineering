# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        LL = ListNode()
        carry = 0
        
        t1 = l1
        t2 = l2
        t = LL
        
        while t1 or t2 or carry:
            v1 = t1.val if t1 else 0
            v2 = t2.val if t2 else 0
            s = v1 + v2 + carry
            carry, s = divmod(s, 10)
            t.next = ListNode(s)
            
            if t1: t1 = t1.next
            if t2: t2 = t2.next
            t = t.next
        return LL.next
