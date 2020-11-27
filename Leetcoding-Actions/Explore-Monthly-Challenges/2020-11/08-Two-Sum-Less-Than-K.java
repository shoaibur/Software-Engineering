class Solution {
    public int twoSumLessThanK(int[] A, int K) {
        /*
        T: O(n) and S: O(1)
        */
        Arrays.sort(A);
        int i = 0;
        int j = A.length - 1;
        int maxSum = -1;
        while (i < j) {
            int sum = A[i] + A[j];
            if (sum < K) {
                maxSum = Math.max(maxSum, sum);
                i++;
            } else {
                j--;
            }
        }
        return maxSum;
    }
}
