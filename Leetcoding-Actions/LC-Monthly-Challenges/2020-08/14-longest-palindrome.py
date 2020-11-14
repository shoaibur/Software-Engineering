class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        
        for char in s:
            d[char] = d.get(char, 0) + 1
            
        maxLen = 0
        odd = False
        for char in d:
            if d[char] % 2:
                odd = True
            maxLen += 2 * (d[char] // 2)
        if odd:
            maxLen += 1
            
        return maxLen
