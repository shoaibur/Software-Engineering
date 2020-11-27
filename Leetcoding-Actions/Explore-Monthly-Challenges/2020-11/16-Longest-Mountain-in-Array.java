class Solution {
    public int longestMountain(int[] A) {
        /**
        * T: O(n) and S: O(1)
        */
        int n = A.length;
        if (n < 3) return 0;
        
        int maxLen = 0;
        for (int i = 1; i < n-1; i++) {
            int left = i - 1;
            int right = i + 1;
            if ((A[left] < A[i]) && (A[i] > A[right])) {
                while (left > 0 && A[left-1] < A[left]) {
                    left--;
                }
                while (right < n-1 && A[right] > A[right+1]) {
                    right ++;
                }
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }
        return maxLen;
    }
}
