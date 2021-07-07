class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        maxLen = 0
        d = {}
        i, j = 0, 0
        while j < len(s):
            d[s[j]] = d.get(s[j], 0) + 1
            if len(d) <= k:
                tempMax = 0
                for key, val in d.items():
                    tempMax += val
                maxLen = max(maxLen, tempMax)
                j += 1
            else:
                d[s[i]] -= 1
                d[s[j]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
        return maxLen
            
