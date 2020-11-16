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
        n = getLength(head)
        if n <= 2: return
        
        def partition(head, k):
            count = 1
            tail = head
            while tail:
                tail = tail.next
                count += 1
                if count == k:
                    newhead = tail.next
                    tail.next = None
                    break
            return head, newhead
        k = n // 2 + 1 if n%2 else n // 2  # 6//2 = 3, 5//2 = 2
        head, newhead = partition(head, k)
        
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
            temp = tail.next # 2
            newtemp = newtail.next # 5
            
            tail.next = newtail # 4
            tail.next.next = temp
            
            tail = temp
            newtail = newtemp
        return
