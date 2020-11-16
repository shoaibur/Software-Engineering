def wallsAndGates(self, rooms: List[List[int]]) -> None:
    # Using BFS
    if not rooms: return
    nrow, ncol = len(rooms), len(rooms[0])
    gates = []
    for i in range(nrow):
        for j in range(ncol):
            if rooms[i][j] == 0:
                gates.append((i,j,0))
                
    for gate in gates:
        q = deque([gate])
        while q:
            i, j, dist = q.popleft()
            for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= ni < nrow and 0 <= nj < ncol \
                and rooms[ni][nj] > dist and rooms[ni][nj] != -1:
                    rooms[ni][nj] = dist+1
                    q.append((ni, nj, dist+1))
    # Using DFS
    if not rooms: return
    nrow, ncol = len(rooms), len(rooms[0])

    def dfs(rooms, i, j, distance):
        if i < 0 or i >= nrow or j < 0 or j >= ncol or rooms[i][j] < distance:
            return
        rooms[i][j] = distance
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            dfs(rooms, ni, nj, distance+1)

    for i in range(nrow):
        for j in range(ncol):
            if rooms[i][j] == 0:
                dfs(rooms, i, j, 0)
    return
