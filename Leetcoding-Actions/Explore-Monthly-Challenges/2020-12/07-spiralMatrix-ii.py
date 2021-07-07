class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        startRow, endRow = 0, n - 1
        startCol, endCol = 0, n - 1
        
        count  = 1
        
        while startRow <= endRow and startCol <= endCol:
            
            for col in range(startCol, endRow + 1):
                matrix[startRow][col] = count
                count += 1
            
            for row in range(startRow + 1, endRow + 1):
                matrix[row][endCol] = count
                count += 1
            
            for col in range(endCol - 1, startCol - 1, -1):
                matrix[endRow][col] = count
                count += 1
            
            for row in range(endRow - 1, startRow, -1):
                matrix[row][startCol] = count
                count += 1
            
            startRow, endRow = startRow + 1, endRow - 1
            startCol, endCol = startCol + 1, endCol - 1
        
        return matrix
