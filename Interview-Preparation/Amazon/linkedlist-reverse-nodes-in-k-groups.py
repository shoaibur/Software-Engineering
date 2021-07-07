# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def printLL(head):
            tail = head
            while tail:
                print(tail.val, end=' ')
                tail = tail.next
            return
        
        def partition(head, k):
            count = 0
            tail = head
            while tail:
                temp = tail.next
                count += 1
                if count == k:
                    tail.next = None
                    break
                tail = temp
            return head, temp, count

        def reverse(head):
            prev = None
            tail = head
            while tail:
                temp = tail.next
                tail.next = prev
                prev = tail
                tail = temp
            return prev
                
        tail = head
        newhead = ListNode()
        newtail = newhead
        
        while tail:
            temp_head, tail, count = partition(tail, k)
            
            if count == k:
                rev_temp_head = reverse(temp_head)
            else:
                rev_temp_head = temp_head
            
            while newtail.next:
                newtail = newtail.next
            newtail.next = rev_temp_head
        
        return newhead.next
