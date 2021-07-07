class Solution {
    public int removeElement(int[] nums, int val) {
        /**
        * T: O(n) and S: O(1)
        */
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}
