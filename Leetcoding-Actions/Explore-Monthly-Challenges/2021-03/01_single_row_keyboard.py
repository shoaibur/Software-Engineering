class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        d = {}
        for i, char in enumerate(keyboard):
            d[char] = i
        
        time = 0
        start = 0
        for char in word:
            time += abs(start - d[char])
            start = d[char]
        
        return time
