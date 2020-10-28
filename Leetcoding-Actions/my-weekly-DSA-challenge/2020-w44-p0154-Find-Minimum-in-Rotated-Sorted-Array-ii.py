class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        T: O(n) and S: O(1)
        Worst case: all elements are same, then T: O(n); average T: O(log n)
        '''
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi = hi - 1
        
        return nums[lo]
