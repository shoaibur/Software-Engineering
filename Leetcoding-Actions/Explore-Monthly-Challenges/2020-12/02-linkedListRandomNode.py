# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.n = 0
        self.head = head
        
        tail = head
        while tail:
            self.n += 1
            tail = tail.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        tail = self.head
        k = random.randint(1, self.n)
        for i in range(k - 1):
            tail = tail.next
        return tail.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
