class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        /**
        * T: O(n) and S: O(k)
        */
        List<Integer> result = new ArrayList<>();
        ArrayDeque<Integer> q = new ArrayDeque<>();
        
        for (int i = 0; i < nums.length; i++) {
            while (!q.isEmpty() && (nums[q.getLast()] < nums[i])) {
                q.removeLast();
            }
            if (!q.isEmpty() && (i - q.getFirst() >= k)) {
                q.removeFirst();
            }
            q.add(i);
            result.add(nums[q.getFirst()]);
        }
        int[] res = new int[result.size() - k + 1];
        for (int i = k - 1; i < result.size(); i++) {
            res[i-k+1] = result.get(i);
        }
        return res;
    }
}
