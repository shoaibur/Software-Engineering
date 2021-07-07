class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        T: O(n + log N_max) and S: O(1)
        T: O(n) for finding max (i.e., N_max) and O(log N_max) for binary search.
        '''
        def roundNum(num, divisor):
            '''
            Rounding a number to its closest integer
            5 / 3 = 2 = (5 - 1) // 3 + 1
            6 / 3 = 2 = (6 - 1) // 3 + 1
            '''
            return (num - 1) // divisor + 1
        
        def satisfyCondition(divisor):
            return sum([roundNum(num, divisor) for num in nums]) <= threshold
        
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if satisfyCondition(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
