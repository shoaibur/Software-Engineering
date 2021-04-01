# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        T: O(n) and S: O(1)
        '''
        if not head: return True
        if head.next is None: return True
        if head.next.next is None:
            return head.val == head.next.val
        # split into two halves
        slow = head
        fast = head.next
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast.next is None:
                break
        right = slow.next
        slow.next = None
        left = head
        
        # Reverse second half
        prev = None
        tail = right
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp
        right = prev
        
        # compare first and second half
        left_tail = left
        right_tail = right
        while left_tail:
            if left_tail.val != right_tail.val:
                return False
            left_tail = left_tail.next
            right_tail = right_tail.next
        return True
