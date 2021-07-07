class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        T: O(n log n) and S: O(1)
        '''
        n = len(nums)
        
        sorted_nums = sorted(nums)
        
        start, end = n + 1, -1
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        diff = end - start
        
        return diff + 1 if diff > 0 else 0
