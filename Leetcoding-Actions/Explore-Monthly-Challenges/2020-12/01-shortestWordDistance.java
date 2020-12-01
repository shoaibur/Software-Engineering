class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        /**
        * T: O(n) and S: O(1)
        */
        int iw1 = -1;
        int iw2 = -1;
        int minDist = words.length;
        
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                iw1 = i;
            } else if (words[i].equals(word2)) {
                iw2 = i;
            }
            if (iw1 != -1 && iw2 != -1)
                minDist = Math.min(minDist, Math.abs(iw2 - iw1));
        }
        return minDist;
    }
}
