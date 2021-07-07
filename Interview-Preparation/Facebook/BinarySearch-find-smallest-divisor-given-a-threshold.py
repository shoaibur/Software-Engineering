class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def condition(divisor) -> bool:
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold

        lo, hi = 1, max(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if condition(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
