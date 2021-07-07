# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        T: O(n) and S: O(n)
        '''        
        if not head or not head.next:
            return head
        
        firstNode = head
        secondNode = head.next
        
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode
        
        return secondNode
