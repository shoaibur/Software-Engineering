class Solution {
    public int singleNumber(int[] nums) {
        // Using bit manipulation - T: O(n) and S: O(1)
        int a = 0;
        for (int num : nums) {
            a ^= num;
        }
        return a;
        
        
        /** // Using HashMap - T: O(n) and S: O(n)
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num : nums) {
            int count = map.getOrDefault(num, 0);
            map.put(num, count+1);
        }
        for (int key : map.keySet()) {
            if (map.get(key) == 1)
                return key;
        }
        return -1;
        */
    }
}
