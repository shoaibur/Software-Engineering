class Solution {
    public int atMostNGivenDigitSet(String[] digits, int n) {
        char[] N = String.valueOf(n).toCharArray();
        int len = N.length;
        int res = 1, pres = 1, smaller = -1;
        
        for(int i = 1, m = 1; i <= len; i++, m *= digits.length) {
            pres = res;
            res = 0;
            int x = N[len-i] - '0';
            for(String d: digits) {
                if(Integer.valueOf(d) < x) res += m;
                else if(Integer.valueOf(d) == x) res += pres;
            }
            smaller += m;
        }
        
        return res + smaller;
    }
}
