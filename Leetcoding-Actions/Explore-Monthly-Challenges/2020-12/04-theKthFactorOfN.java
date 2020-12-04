class Solution {
    public int kthFactor(int n, int k) {
        /**
        * T: O(n) and S: O(1)
        */
        int factorCount = 0;
        int i = 1;
        while (i <= n) {
            if (n % i == 0) factorCount++;
            if (factorCount == k) break;
            i++;
        }
        return factorCount == k ? i : -1;
    }
}
