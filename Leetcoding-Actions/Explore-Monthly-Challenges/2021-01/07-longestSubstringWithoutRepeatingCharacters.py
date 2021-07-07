class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        d = {}
        maxLen = 0
        start, end = 0, 0
        while start <= end and end < len(s):
            if s[end] not in d:
                d[s[end]] = 1
                end += 1
                maxLen = max(maxLen, len(d))
            else:
                d.pop(s[start])
                start += 1
        
        return maxLen
