# Check all four sides when 1 is found
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
    
# Solution 2: Check left and up when 1 is found
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
                perimeter += 4
                for (ni, nj) in [(i-1, j), (i, j-1)]:
                    if ni >= 0 and nj >= 0 and grid[ni][nj] == 1:
                        perimeter -= 2
        return perimeter
