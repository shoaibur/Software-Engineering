# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        T: O(n) and S: O(1)
        '''        
        def findIntersection(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        
        if not head: return None
        intersect = findIntersection(head)
        if not intersect: return None
        
        i, j = head, intersect
        while i != j:
            i = i.next
            j = j.next
        
        return i



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        T: O(n) and S: O(n)
        '''
        if not head: return None
        
        visited = set()
        tail = head
        while tail:
            if tail in visited:
                return tail
            visited.add(tail)
            tail = tail.next
        
        return None
