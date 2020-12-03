class Solution {
    public void moveZeroes(int[] nums) {
        int i, j;
        for (i = 0; i < nums.length; i++) {
            if (nums[i] == 0) break;
        }
        j = i + 1;
        while (j < nums.length) {
            if(nums[j] != 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
            }
            j++;
        }
    }
}
