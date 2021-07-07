class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int count = 0;
        boolean firstZero = false;
        for (int num : nums) {
            if (num == 1) {
                count++;
            }
            else if (num == 0 && !firstZero) {
                count++;
                firstZero = true;
            } else {
                count = 0;
                firstZero = false;
            }
            maxCount = Math.max(maxCount, count);
        }
        return maxCount;
    }
}
