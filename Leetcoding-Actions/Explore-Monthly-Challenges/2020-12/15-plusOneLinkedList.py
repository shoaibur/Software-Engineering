# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def reverse(head):
            prev = None
            tail = head
            while tail:
                temp = tail.next
                tail.next = prev
                prev = tail
                tail = temp
            return prev
        
        head = reverse(head)
        carry = 0
        tail = head
        while tail:
            if tail.val < 9:
                tail.val += 1
                carry = 0
                break
            else:
                tail.val = 0
                carry = 1
            tail = tail.next
        
        if carry:
            newHead = ListNode(1)
            newHead.next = reverse(head)
            return newHead
        return reverse(head)
