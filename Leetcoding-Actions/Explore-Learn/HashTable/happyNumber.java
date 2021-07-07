class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        
        while (n > 1) {
            if (set.contains(n)) return false;
            set.add(n);
            int k = 0;
            while (n != 0) {
                int rem = n % 10;
                n = n / 10;
                k += rem * rem;
            }
            n = k;
        }
        return n == 1;
    }
}
