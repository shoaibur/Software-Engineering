class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        '''
        T: O(m * n) and S: O(1)
        '''
        if not A: return A
        
        nrow, ncol = len(A), len(A[0])
        
        for row in range(nrow):
            i, j = 0, ncol - 1
            while i < j:
                A[row][i], A[row][j] = A[row][j], A[row][i]
                i, j = i + 1, j - 1
        
        for i in range(nrow):
            for j in range(ncol):
                A[i][j] = 1 - A[i][j]
                
        return A
