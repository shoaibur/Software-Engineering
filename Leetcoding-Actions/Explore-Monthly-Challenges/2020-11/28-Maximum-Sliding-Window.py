class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        T: O(n log k) and S: O(k)
        
        result = []
        for i in range(len(nums) - k + 1):
            numsK = nums[i: i + k]
            heapq._heapify_max(numsK)
            result.append(numsK[0])
        return result
        
        T: O(n) and S: O(k)
        '''
        result = []
        q = deque()
        
        for i in range(len(nums)):            
            while q and (nums[q[-1]] < nums[i]):
                q.pop()
            if q and (i - q[0] >= k):
                q.popleft()
            q.append(i)
            result.append(nums[q[0]])
            
        return result[k-1:]
        
