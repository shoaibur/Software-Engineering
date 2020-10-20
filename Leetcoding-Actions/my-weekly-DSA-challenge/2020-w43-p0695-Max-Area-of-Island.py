class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        T: O(m * n) and S: O(1)
        '''
        if not grid: return 0
        nrow, ncol = len(grid), len(grid[0])
        
        # Calculate area of individual island
        def exploreIsland(grid, i, j):
            if i < 0 or i > nrow-1 or j < 0 or j > ncol-1 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            for (ni, nj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                area += exploreIsland(grid, ni, nj)
            return area
        
        # Traverse through grid and update maximum area.
        maxArea = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    area = exploreIsland(grid, i, j)
                    maxArea = max(maxArea, area)
        return maxArea
