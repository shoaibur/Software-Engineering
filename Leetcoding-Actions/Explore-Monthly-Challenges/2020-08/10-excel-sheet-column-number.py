class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {}
        for i, char in enumerate(string.ascii_uppercase):
            d[char] = i + 1
        result = 0
        for i, char in enumerate(s[::-1]):
            result += d[char] * 26 ** i
        return result
    
