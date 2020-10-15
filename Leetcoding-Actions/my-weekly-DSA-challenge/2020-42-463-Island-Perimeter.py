class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        T: O(m * n)
        S: O(1)
        '''
        if not grid: return 0
        nrow = len(grid)
        ncol = len(grid[0])
        
        perimeter = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] != 1: continue
                for (ni, nj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if ni < 0 or ni >= nrow or nj < 0 or nj >= ncol or grid[ni][nj] == 0:
                        perimeter += 1
        return perimeter
