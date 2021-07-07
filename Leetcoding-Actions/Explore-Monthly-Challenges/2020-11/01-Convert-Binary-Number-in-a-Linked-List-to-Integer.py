# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        def reverseLinkedList(head):
            prev = None
            tail = head
            while tail:
                temp = tail.next
                tail.next = prev
                prev = tail
                tail = temp
            return prev
        
        head = reverseLinkedList(head)
        i, decimal = 0, 0
        tail = head
        while tail:
            if tail.val:
                decimal += tail.val * 2 ** i
            tail = tail.next
            i += 1
            
        return decimal
