class Solution {
    public int smallestRepunitDivByK(int K) {
        /*
        * T: O(K) and S: O(1)
        */
        int remainder = 0;
        
        for (int lengthN = 1; lengthN < K + 1; lengthN++) {
            remainder = (remainder * 10 + 1) % K;
            
            if (remainder == 0) {
                return lengthN;
            }
        }
        return -1;
    }
}
