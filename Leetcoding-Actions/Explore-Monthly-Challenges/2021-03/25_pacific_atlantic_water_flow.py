class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        T: O(mn) and S: O(mn)
        '''
        def bfs(q, directions):
            can_flow = set()
            while q:
                row, col = q.popleft()
                can_flow.add((row, col))
                for dx, dy in directions:
                    x, y = row + dx, col + dy
                    if x < 0 or x >= nrow or y < 0 or y >= ncol or (x, y) in can_flow or matrix[x][y] < matrix[row][col]:
                        continue
                    q.append((x, y))
            return can_flow
        
        
        if not matrix or not matrix[0]:
            return []
        
        nrow, ncol = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        pacific_q = deque()
        atlantic_q = deque()
        
        for i in range(nrow):
            pacific_q.append((i, 0))
            atlantic_q.append((i, ncol - 1))
        
        for j in range(ncol):
            pacific_q.append((0, j))
            atlantic_q.append((nrow - 1, j))
        
        can_flow_to_pacific = bfs(pacific_q, directions)
        can_flow_to_atlantic = bfs(atlantic_q, directions)
        
        return list(can_flow_to_pacific & can_flow_to_atlantic)
