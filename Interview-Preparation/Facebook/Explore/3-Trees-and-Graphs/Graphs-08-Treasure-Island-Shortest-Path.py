def minimumSteps(grid, startX, startY, target='X', obstackle='D'):
    nrow, ncol = len(grid), len(grid[0])
    visited = [[False] * ncol for row in range(nrow)]

    q = collections.deque()
    q.append((startX,startY,0)) # i, j, distance
    
    while q:
        i, j, step = q.popleft()
        if grid[i][j] == target:
            return step
        visited[i][j] = True
        grid[i][j] = 'U'
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < nrow and 0 <= nj < ncol \
            and grid[ni][nj] != 'D' and not visited[ni][nj]:
                q.append((ni, nj, step+1))
    return -1
