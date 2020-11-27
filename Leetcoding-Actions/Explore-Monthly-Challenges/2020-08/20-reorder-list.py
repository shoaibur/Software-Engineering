# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        def getLength(head):
            n = 0
            tail = head
            while tail:
                tail = tail.next
                n += 1
            return n
        
        def partition(head, k):
            tail = head
            i = 0
            while i < k-1: # 1,2,3,4,5
                tail = tail.next
                i += 1
            newhead = tail.next
            tail.next = None
            return head, newhead
        
        def reverse(head):
            prev = None
            tail = head
            while tail:
                temp = tail.next
                tail.next = prev
                prev = tail
                tail = temp
            return prev
        
        
        n = getLength(head)
        k = (n+1) // 2
        head, newhead = partition(head, k)
        newhead = reverse(newhead)
        
        tail = head
        newtail = newhead
        while tail and newtail:
            temp = tail.next
            newtemp = newtail.next
            
            tail.next = newtail
            tail.next.next = temp
            newtail = newtemp
            tail = temp
