class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        T: O(mn) and S: O(1)
        '''
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                summ = 0
                neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1), (i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)]
                for ni, nj in neighbors:
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and abs(board[ni][nj]) == 1:
                        summ += 1
                    
                if board[i][j] == 1:
                    if summ < 2 or summ > 3:
                        board[i][j] = -1 # live to dead
                else:
                    if summ == 3:
                        board[i][j] = 2 # dead to live
        
        for i in range(m):
            for j in range(n):
                board[i][j] = 0 if board[i][j] <= 0 else 1
