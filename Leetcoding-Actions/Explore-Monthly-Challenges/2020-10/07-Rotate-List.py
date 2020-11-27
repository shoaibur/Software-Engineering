# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        T: O(2n) = O(n)
        S: O(1)
        '''
        if not head: return head
        
        def getLength(head):
            n = 0
            tail = head
            while tail:
                tail = tail.next
                n += 1
            return n
        
        n = getLength(head)
        k = k % n
        if k == 0: return head
        
        i = 0
        tail = head
        while tail.next:
            i += 1
            if i == n - k:
                temp = tail
            tail = tail.next
        newhead = temp.next
        temp.next = None
        tail.next = head
        return newhead
        
        
