class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        nrow, ncol = len(rooms), len(rooms[0])
        
        gates = []
        for i in range(nrow):
            for j in range(ncol):
                if rooms[i][j] == 0:
                    gates.append((i, j, 0))
        
        for gate in gates:
            visited = set()
            q = deque([gate])
            while q:
                i, j, dist = q.popleft()
                for (ni, nj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if ni >= 0 and ni < nrow and nj >= 0 and nj < ncol and (ni, nj) not in visited and rooms[ni][nj] != -1 and dist < rooms[ni][nj]:
                        rooms[ni][nj] = dist + 1
                        q.append((ni, nj, dist + 1))
        return
