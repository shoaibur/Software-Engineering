class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        /**
        * T: O(n) and S: O(n)
        */
        int[] extNums = new int[nums.length + 2];
        extNums[0] = lower - 1;
        extNums[extNums.length - 1] = upper + 1;
        for (int i = 1; i < extNums.length - 1; i++) {
            extNums[i] = nums[i-1];
        }
        
        List<String> result = new ArrayList<>();
        
        for (int i = 0; i < extNums.length - 1; i++) {
            int diff = extNums[i+1] - extNums[i];
            if (diff == 1) continue;
            int lo = Math.max(extNums[i] + 1, lower);
            int hi = Math.min(extNums[i+1] - 1, upper);
            if (lo == hi) 
                result.add(String.valueOf(lo));
            else
                result.add(lo + "->" + hi);
        }
        return result;
    }
}
