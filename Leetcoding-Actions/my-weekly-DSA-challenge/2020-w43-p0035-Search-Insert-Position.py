class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        T: O(log n) and S: O(1)
        '''
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo
