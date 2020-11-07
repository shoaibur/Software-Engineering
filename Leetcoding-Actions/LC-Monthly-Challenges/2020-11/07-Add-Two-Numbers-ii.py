# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        T: O(max(n1, n2)); n1 and n2 are lengths of l1 and l2.
        and S: O(1) ignore space required for storing results.
        '''
        if not l1: return l2
        if not l2: return l1
        
        def reverse(head):
            prev = None
            tail = head
            while tail:
                temp = tail.next
                tail.next = prev
                prev = tail
                tail = temp
            return prev
        
        def add(l1, l2):
            l = ListNode(0)
            t1, t2, t = l1, l2, l
            carry = 0
            while l1 or l2 or carry:
                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0
                
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
                
                s = v1 + v2 + carry
                carry, s = divmod(s, 10)
                t.next = ListNode(s)
                t = t.next
            return l.next
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        l = add(l1, l2)
        return reverse(l)
