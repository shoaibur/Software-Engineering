class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums, target, position):
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
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return indx
        
        first = binarySearch(nums, target, 'first')
        last = binarySearch(nums, target, 'last')
        return [first, last]
