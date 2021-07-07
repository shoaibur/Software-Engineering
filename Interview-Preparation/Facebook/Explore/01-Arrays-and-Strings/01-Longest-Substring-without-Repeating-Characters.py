class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        
        d = {}
        i, j = 0, 0
        maxLen = 0
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
                j += 1
                maxLen = max(maxLen, len(d))
            else:
                d.pop(s[i])
                i += 1
        return maxLen
