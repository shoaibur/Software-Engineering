# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    if not board: return board
    nrow = len(board)
    ncol = len(board[0])
    if nrow <= 2 or ncol <= 2: return board
    for i in range(nrow):
        for j in range(ncol):
            if (i == 0 or i == nrow-1 or j == 0 or j == ncol-1) and board[i][j] == 'O':
                dfs(board, i, j)
    for i in range(nrow):
        for j in range(ncol):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'o':
                board[i][j] = 'O'
    return board

def dfs(self, board, i, j):
    nrow = len(board)
    ncol = len(board[0])
    if i >= 0 and i < nrow and j >= 0 and j < ncol and board[i][j] == 'O':
        board[i][j] = 'o'
        dfs(board, i-1, j)
        dfs(board, i+1, j)
        dfs(board, i, j-1)
        dfs(board, i, j+1)
    return
