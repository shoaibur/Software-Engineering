class Solution {
    public int removeDuplicates(int[] nums) {
        /**
        * T: O(n) and S: O(1)
        */
        int n = nums.length;
        if (n <= 1) return n;
        
        int i = 0;
        int currVal = nums[i];
        for (int j = 1; j < n; j++) {
            if (nums[j] != currVal) {
                nums[i+1] = nums[j];
                i++;
                currVal = nums[i];
            }
        }
        return i + 1;
    }
}
