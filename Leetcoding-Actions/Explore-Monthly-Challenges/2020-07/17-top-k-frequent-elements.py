class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        pairs = [(val, key) for key, val in d.items()]
        
        heap = pairs[:k]
        heapq.heapify(heap)
        
        for pair in pairs[k:]:
            if pair > heap[0]:
                heapq.heappushpop(heap, pair)
            
        return [key for _, key in heap]
