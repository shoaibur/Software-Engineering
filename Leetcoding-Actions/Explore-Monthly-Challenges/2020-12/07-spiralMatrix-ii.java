class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int startRow = 0;
        int endRow = n - 1;
        int startCol = 0;
        int endCol = n - 1;
        
        int count = 1;
        
        while (startRow <= endRow && startCol <= endCol) {
            for (int col = startCol; col < endCol + 1; col++) {
                matrix[startRow][col] = count;
                count++;
            }
            for (int row = startRow + 1; row < endRow + 1; row++) {
                matrix[row][endCol] = count;
                count++;
            }
            for (int col = endCol - 1; col > startCol - 1; col--) {
                matrix[endRow][col] = count;
                count++;
            }
            for (int row = endRow - 1; row > startRow; row--) {
                matrix[row][startCol] = count;
                count++;
            }
            startRow++; endRow--;
            startCol++; endCol--;
        }
        return matrix;
    }
}
