class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary search
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
                
        # Return lo if target exists, else return -1
        if nums[lo] == target:
            return lo
        return -1
