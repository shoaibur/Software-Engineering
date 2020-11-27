class Solution {
    public int mirrorReflection(int p, int q) {
        /**
        * T: O(log p) and S: O(1)
        */
        if (q == 0) return 0;
        
        int m = 1;
        int n = 1;
        while (m*p != n*q) {
            n += 1;
            m = (n * q) / p;
        }
        if (n % 2 == 0) {
            return 2;
        } else if (m % 2 != 0) {
            return 1;
        }
        return 0;
    }
}
