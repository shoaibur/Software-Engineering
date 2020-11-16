class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = -2**31
        maxx = -2**31
        for num in nums:
            summ = max( summ+num, num )
            maxx = max( maxx, summ )
        return maxx
