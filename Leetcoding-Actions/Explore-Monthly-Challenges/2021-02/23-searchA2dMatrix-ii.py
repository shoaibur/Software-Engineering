class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        i, j = 0, ncol-1
        while i < nrow and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        
        return False
