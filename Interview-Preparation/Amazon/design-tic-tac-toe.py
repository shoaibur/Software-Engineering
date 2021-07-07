class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.matrix = [[0]*n for _ in range(n)]
        self.matrixT = []
        self.win1 = tuple([1] * self.n)
        self.win2 = tuple([2] * self.n)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.matrix[row][col] = player
        self.matrixT = [*zip(*self.matrix)]       
        
        def find_winner(matrix):
            diag = []
            xdiag = []
            for i in range(self.n):
                if tuple(matrix[i]) == self.win1:
                    return 1
                elif tuple(matrix[i]) == self.win2:
                    return 2
                diag.append(matrix[i][i])
            if tuple(diag) == self.win1: return 1
            if tuple(diag) == self.win2: return 2
            
            i, j = 0, self.n - 1
            while i < self.n and j >= 0:
                xdiag.append(matrix[i][j])
                i, j = i+1, j-1
            if tuple(xdiag) == self.win1: return 1
            if tuple(xdiag) == self.win2: return 2
            return 0
        winner = find_winner(self.matrix)
        if winner: return winner
        
        winner = find_winner(self.matrixT)
        return winner


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
