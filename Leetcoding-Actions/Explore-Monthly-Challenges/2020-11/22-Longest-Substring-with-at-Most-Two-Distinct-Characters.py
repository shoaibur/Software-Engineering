class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        charDict = {}
        start, end = 0, 0
        maxLen = 0
        while end < len(s):
            charDict[s[end]] = charDict.get(s[end], 0) + 1
            if len(charDict) <= 2:
                maxLen = max(maxLen, end - start + 1)
                end += 1
            else:
                charDict[s[start]] -= 1
                charDict[s[end]] -= 1
                if charDict[s[start]] == 0:
                    charDict.pop(s[start])
                start += 1
        
        return maxLen
