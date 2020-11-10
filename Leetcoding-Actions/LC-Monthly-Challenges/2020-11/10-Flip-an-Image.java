class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        /*
        T: O(m * n) and S: O(1)
        */
        int nrow = A.length;
        int ncol = A[0].length;
        
        for (int row = 0; row < nrow; row++) {
            int i = 0;
            int j = ncol - 1;
            while (i < j) {
                int temp = A[row][i];
                A[row][i] = A[row][j];
                A[row][j] = temp;
                i++; j--;
            }
        }
        
        for (int i = 0; i < nrow; i++) {
            for (int j = 0; j < ncol; j++) {
                A[i][j] = 1 - A[i][j];
            }
        }
        return A;
    }
}
