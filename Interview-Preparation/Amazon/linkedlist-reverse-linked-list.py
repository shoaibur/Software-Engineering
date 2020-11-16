# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        tail = head
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp
        return prev
    
