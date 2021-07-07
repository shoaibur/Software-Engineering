from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nrow = len(grid)
        ncol = len(grid[0])
        if nrow == 0 or ncol == 0: return 0
        
        # Location of rotten oranges at time = 0
        coords = self.find_rot(grid)
        time = 0
        
        # Queue at time = 0
        q = deque()
        for coord in coords:
            q.append(coord)
        
        # Update all oranges
        while len(q) > 0:
            time, i, j = q.popleft()
            if i > 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                q.append((time+1, i-1, j))
            if i < nrow-1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                q.append((time+1, i+1, j))
            if j > 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                q.append((time+1, i, j-1))
            if j < ncol-1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                q.append((time+1, i, j+1))
                
        # Check if any orange is fresh
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    return -1
        return time
        
    
    def find_rot(self, grid):
        coords = []
        nrow = len(grid)
        ncol = len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    coords.append((0, i, j))
        return coords
