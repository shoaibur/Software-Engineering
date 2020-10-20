class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        '''
        T: O(log n) and S: O(1)
        '''
        def binarySearch(nums, target, side):
            index = -1
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] == target:
                    index = mid
                    if side == 'left':
                        hi = mid - 1
                    elif side == 'right':
                        lo = mid + 1
                    else:
                        raise ValueError('Give correct side name: "left" or "right"')
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
                
            return index
        
        left = binarySearch(nums, target, side='left')
        right = binarySearch(nums, target, side='right')
        
        if left == -1 or right == -1:
            return False
        return (right - left + 1) > len(nums) // 2
