class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        nrow = len(grid)
        ncol = len(grid[0])
        
        def exploreIsland(grid, i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                exploreIsland(grid, ni, nj)
        
        num_island = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1':
                    exploreIsland(grid, i, j)
                    num_island += 1
        return num_island
