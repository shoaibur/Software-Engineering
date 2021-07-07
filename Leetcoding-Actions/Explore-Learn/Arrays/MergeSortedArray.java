class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        /**
        * T: O(m + n) and S: O(1)
        */
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while (i >= 0 || j >= 0) {
            int v1 = i >= 0 ? nums1[i] : Integer.MIN_VALUE;
            int v2 = j >= 0 ? nums2[j] : Integer.MIN_VALUE;
            if (v1 > v2) {
                nums1[k] = v1;
                i--;
            } else {
                nums1[k] = v2;
                j--;
            }
            k--;
        }
    }
}
