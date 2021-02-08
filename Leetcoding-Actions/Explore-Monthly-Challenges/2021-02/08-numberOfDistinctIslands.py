class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        # dfs
        def exploreIsland(grid, i, j, starti, startj, shape):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == 0:
                return shape
            grid[i][j] = 0
            shape.append((i-starti, j-startj))
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                exploreIsland(grid, ni, nj, starti, startj, shape)
            return shape
        
        
        island_count = 0
        unique_shape = set()
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    shape = tuple(exploreIsland(grid, i, j, i, j, []))
                    if shape not in unique_shape:
                        unique_shape.add(shape)
                        island_count += 1
        return island_count
