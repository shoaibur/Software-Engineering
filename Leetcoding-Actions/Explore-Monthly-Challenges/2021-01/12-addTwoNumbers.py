# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l = ListNode(0)
        t1, t2, t = l1, l2, l
        while t1 or t2:
            if t1:
                v1 = t1.val
                t1 = t1.next
            else:
                v1 = 0
            if t2:
                v2 = t2.val
                t2 = t2.next
            else:
                v2 = 0
            
            s = v1 + v2 + carry
            carry, s = divmod(s, 10)
            t.next = ListNode(s)
            t = t.next
        if carry:
            t.next = ListNode(carry)
        
        return l.next
