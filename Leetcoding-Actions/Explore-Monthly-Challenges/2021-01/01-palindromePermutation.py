class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        
        oddCount = 0
        for char in d:
            oddCount += d[char] % 2
            if oddCount > 1:
                return False
            
        return True
