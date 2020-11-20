class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        T: O(n) worst; O(log n) best and S: O(1)
        '''
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return True
            
            elif nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
                
            elif nums[lo] <= nums[mid]: # Left is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
                    
            else: # right is sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
