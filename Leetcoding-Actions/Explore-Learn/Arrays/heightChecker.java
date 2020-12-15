class Solution {
    public int heightChecker(int[] heights) {
        /**
        * T: O(n log n) and S: O(1)
        */
        int[] s = new int[heights.length];
        for (int i = 0; i < heights.length; i ++) {
            s[i] = heights[i];
        }
        Arrays.sort(heights);
        int count = 0;
        for (int i = 0; i < s.length; i++) {
            if (s[i] != heights[i]) {
                count++;
            }
        }
        return count;
    }
}
