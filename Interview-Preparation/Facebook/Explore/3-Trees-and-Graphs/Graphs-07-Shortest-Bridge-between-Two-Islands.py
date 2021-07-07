class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A: return 0
        
        nrow = len(A)
        ncol = len(A[0])
        
        q = deque()
        
        def dfs(A, i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or A[i][j] != 1:
                return
            q.append((i, j, 0))
            A[i][j] = 2
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(A, ni, nj)
            
        # First island coordiantes
        def getIslandCoord(A):
            for i in range(nrow):
                for j in range(ncol):
                    if A[i][j] == 1:
                        dfs(A, i, j)
                        return
            return
        getIslandCoord(A)
        
        while q:
            i, j, currStep = q.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if ni >= 0 and ni < nrow and nj >= 0 and nj < ncol and A[ni][nj] != 2:
                    if A[ni][nj] == 0:
                        A[ni][nj] = 2
                        q.append((ni, nj, currStep+1))
                    elif A[ni][nj] == 1:
                        return currStep
