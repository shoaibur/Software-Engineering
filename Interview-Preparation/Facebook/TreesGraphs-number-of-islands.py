class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        nrow = len(grid)
        ncol = len(grid[0])
        if nrow == 0 or ncol == 0: return 0
        
        def dfs(grid, i, j):
            grid[i][j] = '0'
            if i-1 >= 0 and grid[i-1][j] == '1': dfs(grid, i-1, j)
            if i+1 < nrow and grid[i+1][j] == '1': dfs(grid, i+1, j)
            if j-1 >= 0 and grid[i][j-1] == '1': dfs(grid, i, j-1)
            if j+1 < ncol and grid[i][j+1] == '1': dfs(grid, i, j+1)
            return
        
        islandCount = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    islandCount += 1
        return islandCount
