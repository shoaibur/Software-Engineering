class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, position):
            indx = -1
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] == target:
                    indx = mid
                    if position == 'first':
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return indx
        
        
        first = binary_search(nums, target, position='first')
        last = binary_search(nums, target, position='last')
        return [first, last]
