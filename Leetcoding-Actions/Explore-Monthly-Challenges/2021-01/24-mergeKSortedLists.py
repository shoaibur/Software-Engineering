# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        tails = [tail for tail in lists if tail]
        if not tails: return None
        
        merged_head = ListNode(0)
        merged_tail = merged_head
        
        heap = []
        for i, tail in enumerate(tails):
            heapq.heappush(heap, (tail.val, i))
            
        while len(heap) > 0:
            val, idx = heapq.heappop(heap)
            
            tails[idx] = tails[idx].next
            if tails[idx]:
                heapq.heappush(heap, (tails[idx].val, idx))
                
            merged_tail.next = ListNode(val)
            merged_tail = merged_tail.next
        
        
        return merged_head.next
