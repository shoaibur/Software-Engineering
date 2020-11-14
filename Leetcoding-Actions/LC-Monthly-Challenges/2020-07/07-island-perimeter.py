def islandPerimeter(grid):
    if len(grid) == 0: return 0
    nrow = len(grid)
    ncol = len(grid[0])

    perimeter = 0

    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] == 1:
                if i-1 < 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i+1 >= nrow or grid[i+1][j] == 0:
                    perimeter += 1
                if j-1 < 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j+1 >= ncol or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
