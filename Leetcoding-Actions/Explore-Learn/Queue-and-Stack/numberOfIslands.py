class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        nrow, ncol = len(grid), len(grid[0])
        
        def exploreIslands(grid, i, j):
            if i < 0 or i > nrow-1 or j < 0 or j > ncol-1 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for (ni, nj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                exploreIslands(grid, ni, nj)
        
        countIslands = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "1":
                    exploreIslands(grid, i, j)
                    countIslands += 1
        return countIslands
