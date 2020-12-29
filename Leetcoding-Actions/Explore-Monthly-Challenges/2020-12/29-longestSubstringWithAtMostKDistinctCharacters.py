class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k == 0: return 0
        n = len(s)
        
        d = {}
        i, j, maxLen = 0, 0, 0
        while j < n:
            d[s[j]] = d.get(s[j], 0) + 1
            if len(d) <= k:
                maxLen = max(maxLen, j-i+1)
                j += 1
            else:
                d[s[i]] -= 1
                d[s[j]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
        return maxLen
