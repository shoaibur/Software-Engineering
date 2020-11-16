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
        if not head: return None
        
        def printLL(head):
            tail = head
            while tail:
                print(tail.val, end=' ')
                tail = tail.next
            print()
            return
        
        def partition(head):
            n = 0
            tail = head
            while tail:
                n += 1
                tail = tail.next
            if n % 2 == 0:
                n = n // 2
            else:
                n = n // 2 + 1
            
            tail = head
            for i in range(n-1):
                tail = tail.next
            newhead = tail.next
            tail.next = None
            return head, newhead
        head, newhead = partition(head)
        
        def reverse(head):
            prev = None
            tail = head
            while tail:
                temp = tail.next
                tail.next = prev
                prev = tail
                tail = temp
            return prev
        newhead = reverse(newhead)   
        
        tail = head
        newtail = newhead
        while tail and newtail:
            temp = tail.next
            newtemp = newtail.next
            tail.next = newtail
            tail.next.next = temp
            tail = temp
            newtail = newtemp
        printLL(head)
