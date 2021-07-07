class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Apply two binary search: binary search at last column to select 
        which row to search for and then binary search in that row.
        
        T: O(log m + log n)
        S: (m + n)
        '''
        if not matrix: return False
        nrow, ncol = len(matrix), len(matrix[0])
        if nrow < 1 or ncol < 1: return False
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        
        lastCol = [matrix[i][-1] for i in range(nrow)]
        
        def binarySearch(nums, target, lo, hi):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        row = binarySearch(lastCol, target, lo = 0, hi = len(lastCol))
        if row == nrow: return False
        
        rowNums = matrix[row]
        col = binarySearch(rowNums, target, lo = 0, hi = len(rowNums)-1)
        
        return rowNums[col] == target
