class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sol 1. Summation of series
        '''
        T: O(n) and S: O(1)
        '''
        n = len(nums)
        series_sum = n*(n+1) // 2
        nums_sum = sum(nums)
        return series_sum - nums_sum
    
        # Sol 2. Using hash map
        '''
        T: O(n) and S: O(n)
        '''
        # d = {}
        # for num in nums:
        #     d[num] = 1
        # for num in range(len(nums)+1):
        #     if num not in d:
        #         return num
        # return -1
