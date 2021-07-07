class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        '''
        T: O(row*col*log(col)) and S: O(row)
        '''
        def binary_search(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return nums[lo] == target
        
        if len(mat) == 1:
            return min(mat[0])
        
        # A possible set of targets is mat[0].
        # Check if any target exists in all rows.
        # Since mat[0] is sorted, as soon as we
        # find a target in all other rows, that
        # will be the minimum common element in
        # all rows, so return that target.
        for target in mat[0]:
            exist = [False] * (len(mat) - 1)
            
            for i in range(1, len(mat)):
                row = mat[i]
                if not binary_search(row, target):
                    break
                else:
                    exist[i-1] = True
                    
            if all(exist):
                return target
            
        return -1
