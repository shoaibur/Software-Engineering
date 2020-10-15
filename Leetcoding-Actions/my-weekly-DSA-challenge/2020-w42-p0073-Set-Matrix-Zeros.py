class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        T: O(m * n)
        S: (m + n)
        '''
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        rows, cols = set(), set()
        
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(nrow):
            for j in range(ncol):
                if i in rows or j in cols:
                    matrix[i][j] = 0
