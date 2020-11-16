class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        nrow = len(grid)
        ncol = len(grid[0])
        
        def getArea(grid, i, j):
            area = 1
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                area += getArea(grid, ni, nj)
            return area
        
        maxArea = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    area = getArea(grid, i, j)
                    maxArea = max(maxArea, area)
        return maxArea
    
