class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        maxLen = 0
        d = {}
        i, j = 0, 0
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            if len(d) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
            j += 1
            maxLen = max(maxLen, sum([val for _, val in d.items()]))
        return maxLen
