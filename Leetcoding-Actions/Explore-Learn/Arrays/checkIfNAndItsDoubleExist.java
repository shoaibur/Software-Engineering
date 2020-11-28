class Solution {
    public boolean checkIfExist(int[] arr) {
        /**
        * T: O(n) and S: O(n)
        */
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < arr.length; i++) {
            if (set.contains(2 * arr[i])) {
                return true;
            } else {
                set.add(arr[i]);
            }
        }
        Set<Integer> revSet = new HashSet<>();
        for (int i = arr.length - 1; i >= 0; i--) {
            if (revSet.contains(2 * arr[i])) {
                return true;
            } else {
                revSet.add(arr[i]);
            }
        }
        return false;
    }
}
