class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        T: O(log n) and S: O(1)
        '''
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[lo]
