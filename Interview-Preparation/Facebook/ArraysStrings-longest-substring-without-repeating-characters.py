class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        maxLen = 0
        
        start, end = 0, 0
        while end < len(s):
            if s[end] in d:
                maxLen = max(maxLen, len(d))
                d.pop(s[start])
                start += 1
            else:
                d[s[end]] = True
                end += 1
        maxLen = max(maxLen, len(d))
        return maxLen
