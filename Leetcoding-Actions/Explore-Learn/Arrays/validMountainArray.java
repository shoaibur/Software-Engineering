class Solution {
    public boolean validMountainArray(int[] arr) {
        /**
        * T: O(log n + n) and S: O(1)
        */
        int i = binarySearch(arr);
        if (i == 0 || i == arr.length - 1) {
            return false;
        }
        for (int j = i+1; j < arr.length; j++) {
            if (arr[j-1] <= arr[j]) {
                return false;
            }
        }
        for (int j = i - 1; j >= 0; j--) {
            if (arr[j+1] <= arr[j]) {
                return false;
            }
        }
        return true;
    }
    
    public int binarySearch(int[] arr) {
        int lo = 0;
        int hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] > arr[mid+1]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
