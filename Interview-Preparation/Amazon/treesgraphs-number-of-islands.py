class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        nrow = len(grid)
        ncol = len(grid[0])
        
        def dfs(grid, i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == '0':
                return 0
            grid[i][j] = '0'
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
            return 1
        
        num_islands = 0
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1':
                    num_islands += dfs(grid, i, j)
        return num_islands
