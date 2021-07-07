# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        '''
        T: O(n) and S: O(1)
        '''
        i = 0
        tail = head
        from_start = None
        while i < k and tail:
            from_start = tail
            tail = tail.next
            i += 1

        from_end = head
        while tail:
            from_end = from_end.next
            tail = tail.next

        from_start.val, from_end.val = from_end.val, from_start.val

        return head
