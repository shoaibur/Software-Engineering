class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxConsecutiveOnes = 0;
        int countOne = 0;
        for (int num : nums) {
            if (num == 1) {
                countOne++;
                maxConsecutiveOnes = Math.max(maxConsecutiveOnes, countOne);
            } else {
                countOne = 0;
            }
        }
        return maxConsecutiveOnes;
    }
}
