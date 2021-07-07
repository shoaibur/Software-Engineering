class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        nrow = len(grid)
        ncol = len(grid[0])
        
        def dfs(grid, i, j):
            area = 1
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area += dfs(grid, i-1, j)
            area += dfs(grid, i+1, j)
            area += dfs(grid, i, j-1)
            area += dfs(grid, i, j+1)
            return area
        
        max_area = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(grid, i, j))
        return max_area
