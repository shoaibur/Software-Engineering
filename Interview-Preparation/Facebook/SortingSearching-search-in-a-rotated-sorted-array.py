class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]: # left is sorted
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else: # right is sorted
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
