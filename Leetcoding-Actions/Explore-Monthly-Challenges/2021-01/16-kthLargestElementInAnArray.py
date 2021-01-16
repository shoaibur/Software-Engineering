class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        T: O(n log k) and S: O(k)
        '''
        if k > len(nums): return -1
        
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        
        return heap[0]
