class Solution:
    def countVowelStrings(self, n: int) -> int:
        '''
        T: O(1) and S: O(1)
        '''
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
