class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        /**
        * T: O(n) and S: O(1)
        */
        HashMap<Character, Integer> charDict = new HashMap<>();
        int start = 0;
        int end = 0;
        int maxLen = 0;
        
        while (end < s.length()) {
            
            if (charDict.containsKey(s.charAt(end))) {
                charDict.put(s.charAt(end), charDict.get(s.charAt(end))+1);
            } else {
                charDict.put(s.charAt(end), 1);
            }
            
            if (charDict.size() <= 2) {
                maxLen = Math.max(maxLen, end - start + 1);
                end++;
            } else {
                int startCharCount = charDict.get(s.charAt(start));
                charDict.put(s.charAt(start), startCharCount - 1);
                
                int endCharCount = charDict.get(s.charAt(end));
                charDict.put(s.charAt(end), endCharCount - 1);
                                
                if (charDict.get(s.charAt(start)) == 0) {
                    charDict.remove(s.charAt(start));
                }
                start++;
            }
        }
        return maxLen;
    }
}
