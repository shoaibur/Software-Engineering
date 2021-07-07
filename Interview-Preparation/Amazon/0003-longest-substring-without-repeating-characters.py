class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        maxx = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
                j += 1
                maxx = max(maxx, j-i)
            else:
                d.pop(s[i])
                i += 1
        return maxx
