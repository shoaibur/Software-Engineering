class Solution {
    public int findNumbers(int[] nums) {
        int evenDigits = 0;
        
        for (int num : nums) {
            int digitInCurrNum = 0;
            while (num > 0) {
                num = num / 10;
                digitInCurrNum++;
            }
            if (digitInCurrNum % 2 == 0) {
                evenDigits++;
            }
        }
        return evenDigits;
    }
}
