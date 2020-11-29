class Solution {
    public boolean canReach(int[] arr, int start) {
        /**
        * T: O(n) and S: O(n)
        */
        Set<Integer> visited = new HashSet<>();
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.push(start);
        
        while (!q.isEmpty()) {
            int currIndex = q.removeFirst();
            if (arr[currIndex] == 0) {
                return true;
            }
            int leftIndex = currIndex - arr[currIndex];
            int rightIndex = currIndex + arr[currIndex];
            
            if (leftIndex >= 0 && !visited.contains(leftIndex)) {
                visited.add(leftIndex);
                q.push(leftIndex);
            }
            if (rightIndex < arr.length && !visited.contains(rightIndex)) {
                visited.add(rightIndex);
                q.push(rightIndex);
            }
        }
        return false;
    }
}
