class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        def dfs(grid, i, j, starti, startj, shape):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == 0:
                return shape
            grid[i][j] = 0
            shape.append((i-starti, j-startj))
            dfs(grid, i-1, j, starti, startj, shape)
            dfs(grid, i+1, j, starti, startj, shape)
            dfs(grid, i, j-1, starti, startj, shape)
            dfs(grid, i, j+1, starti, startj, shape)
            return shape
        
        unique_shapes = set()
        num_islands = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    curr_shape = tuple(dfs(grid, i, j, i, j, []))
                    if curr_shape not in unique_shapes:
                        unique_shapes.add(curr_shape)
                        num_islands += 1
        return num_islands
