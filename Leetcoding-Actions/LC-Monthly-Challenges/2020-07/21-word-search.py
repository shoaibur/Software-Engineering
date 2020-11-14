class Solution:
    
    def search(self, i, j, idx):
        if idx == len(self.word) - 1: return True
        self.board[i][j] = chr(ord(self.board[i][j])-65)
        if i > 0 and self.board[i-1][j] == self.word[idx+1] and self.search(i-1, j, idx+1): return True
        if i < len(self.board)-1 and self.board[i+1][j] == self.word[idx+1] and self.search(i+1, j, idx+1): return True
        if j > 0 and self.board[i][j-1] == self.word[idx+1] and self.search(i, j-1, idx+1): return True
        if j < len(self.board[0])-1 and self.board[i][j+1] == self.word[idx+1] and self.search(i, j+1, idx+1): return True
        self.board[i][j] = chr(ord(self.board[i][j])+65)
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and self.search(i, j, 0): return True
        return False
        
