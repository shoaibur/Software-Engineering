def shortestDistance(self, grid: List[List[int]]) -> int:
    if not grid: return 0
    nrow, ncol = len(grid), len(grid[0])

    # Buildings coord
    buildings = []
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] == 1:
                buildings.append((i, j, 0))

    # Accumulate distances to 0 from buildings: bfs for each building
    distances = collections.defaultdict(list)
    for building in buildings:
        q = deque()
        q.append(building)
        visited = set()
        while q:
            i, j, distance = q.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < nrow and 0 <= nj < ncol \
                and grid[ni][nj] == 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    distances[(ni, nj)].append(distance+1)
                    q.append((ni, nj, distance+1))

    # Find the minimum distance
    minDistance = float('inf')
    for distance in distances.values():
        # Make sure all buildings are accessible
        if len(distance) == len(buildings):
            minDistance = min(minDistance, sum(distance))
    return -1 if minDistance == float('inf') else minDistance
