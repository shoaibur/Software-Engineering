class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> hashmap = new HashMap<>();
        
        for (int num : nums) {
            if (hashmap.containsKey(num)) {
                return true;
            } else {
                hashmap.put(num, true);
            }
        }
        return false;
    }
}
