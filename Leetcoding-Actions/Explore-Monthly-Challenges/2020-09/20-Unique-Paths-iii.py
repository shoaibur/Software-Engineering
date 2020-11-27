class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        
        # Yields sanity-checked steps
        def next_step(row, col):
            for (r, c) in ((row-1,col), (row+1,col), (row,col-1), (row,col+1)):
                if 0 <= r < nrows and 0 <= c < ncols and grid[r][c] % 2 == 0:
                    yield r, c
        
        # Calculates number of required steps, 
        # & source/destination square locations
        required_steps = 0
        for r_idx, row in enumerate(grid):
            for c_idx, val in enumerate(row):
                if val != -1: required_steps += 1
                if val == 1: src_r, src_c = (r_idx, c_idx)
                if val == 2: dest_r, dest_c = (r_idx, c_idx)
        
        # Solution
        self.ans = 0
        def dfs(row, col, required_steps):
            required_steps -= 1
            if required_steps < 0: return
            if (row, col) == (dest_r, dest_c):
                if required_steps == 0:
                    self.ans += 1
                return
            grid[row][col] = -1
            for (r, c) in next_step(row, col):
                dfs(r, c, required_steps)
            # Enable square for other paths
            grid[row][col] = 0
        
        dfs(src_r, src_c, required_steps)
        return self.ans
    
#         nrow, ncol = len(grid), len(grid[0])
        
#         def findStartPoint(grid):
#             for i in range(nrow):
#                 for j in range(ncol):
#                     if grid[i][j] == 1:
#                         return (i, j)
#         starti, startj = findStartPoint(grid)
        
#         numPaths = 0
        
#         q = deque()
#         q.append((starti, startj))
        
#         visited = set()
#         visited.add((starti, startj))
        
#         while q:
#             i, j = q.popleft()
#             print(i, j, end='----')
#             for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
#                 # print('here', ni, nj)
#                 if ni >= 0 and ni < nrow and nj >= 0 and nj < ncol and (ni,nj) not in visited:
#                     print(ni, nj, grid[ni][nj])
#                     if grid[ni][nj] == 0:
#                         visited.add((ni, nj))
#                         q.append((ni, nj))
#                     elif grid[ni][nj] == 2:
#                         numPaths += 1
#         return numPaths
