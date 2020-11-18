class Solution {
    public int[][] merge(int[][] intervals) {
        /**
        * T: O(n log n) and S: O(1)
        */
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0],b[0]));
        
        List<int[]> result = new ArrayList<>();
        
        result.add(intervals[0]);
        
        for (int i = 1; i < intervals.length; i++) {
            int[] i1 = result.get(result.size() - 1);
            int[] i2 = intervals[i];
            
            if (i1[1] >= i2[0]) {
                int[] merged = {Math.min(i1[0], i2[0]), Math.max(i1[1], i2[1])};
                result.remove(result.size() - 1);
                result.add(merged);
            } else {
                result.add(i2);
            }
        }
        return result.toArray(new int[result.size()][2]);
    }    
}
