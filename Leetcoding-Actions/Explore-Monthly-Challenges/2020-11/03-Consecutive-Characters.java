class Solution {
    public int maxPower(String s) {
        // T: O(n) and S: O(1)
        
        int n = s.length();
        if (n == 1) return 1;
        
        int power = 0;
        int i = 0;
        int j = 0;
        while (j < n) {
            if (s.charAt(i) == s.charAt(j)) {
                j++;
            } else {
                i++;
            }
            power = Math.max(power, j - i);
        }
        return power;
    }
}
