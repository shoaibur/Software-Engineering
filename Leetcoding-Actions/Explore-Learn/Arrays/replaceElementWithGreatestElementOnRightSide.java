class Solution {
    public int[] replaceElements(int[] arr) {
        /**
        * T: O(n) and O(1)
        */
        int currMax = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            int currVal = arr[i];
            arr[i] = currMax;
            currMax = Math.max(currMax, currVal);
        }
        return arr;
    }
}
