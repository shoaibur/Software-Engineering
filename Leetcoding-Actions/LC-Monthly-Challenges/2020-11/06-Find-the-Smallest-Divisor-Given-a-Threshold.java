class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        /**
        T: O(n + log N_max) and S: O(1)
        T: O(n) for finding max (i.e., N_max) and O(log N_max) for binary search.
        */
        
        int lo = 1;
        int hi = getMax(nums);
        
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (satisfyCondition(nums, mid, threshold))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
    
    public static boolean satisfyCondition(int[] nums, int divisor, int threshold) {
        /**
        Rounding a number to its closest integer
        5 / 3 = 2 = (5 - 1) // 3 + 1
        6 / 3 = 2 = (6 - 1) // 3 + 1
        */
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += (nums[i] - 1) / divisor + 1;
        }
        return sum <= threshold;
    }
    
    public static int getMax(int[] nums) {
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            max = Math.max(max, nums[i]);
        }
        return max;
    }
}
