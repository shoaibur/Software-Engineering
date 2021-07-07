class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        def dfs(matrix, i, j):
            if i < 0 or i > nrow-1 or j < 0 or j > ncol-1 or matrix[i][j] == '0':
                return
            matrix[i][j] = '0'
            dfs(matrix, i-1, j)
            dfs(matrix, i+1, j)
            dfs(matrix, i, j-1)
            dfs(matrix, i, j+1)
        
        count = 0
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == '1':
                    dfs(matrix, i, j)
                    count += 1
        return count
