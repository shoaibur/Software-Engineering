# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        head = ListNode(0)
        t = head
        t1, t2, carry = l1, l2, 0
        while t1 or t2 or carry:
            v1 = t1.val if t1 else 0
            v2 = t2.val if t2 else 0
            
            summ = v1 + v2 + carry
            carry, s = divmod(summ, 10)
            t.next = ListNode(s)
            
            t = t.next
            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None
            
        return head.next
