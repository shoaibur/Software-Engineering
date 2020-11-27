class Solution {
    public void duplicateZeros(int[] arr) {
        /**
        * T: O(n) and S: O(n)
        */
        int i;
        for (i = 0; i < arr.length; i++) {
            if (arr[i] == 0) break;
        }
        Set<Integer> zerosPosition = new HashSet<>();
        ArrayDeque<Integer> nonZeroQ = new ArrayDeque<>();
        int zerosCount = 0;
        for (int j = i; j < arr.length; j++) {
            if (arr[j] == 0) {
                zerosPosition.add(j + zerosCount);
                zerosPosition.add(j + zerosCount + 1);
                zerosCount++;
            } else {
                nonZeroQ.add(arr[j]);
            }
        }
        for (int j = i; j < arr.length; j++) {
            if (zerosPosition.contains(j)) {
                arr[j] = 0;
            } else {
                arr[j] = nonZeroQ.removeFirst();
            }
        }
    }
}
