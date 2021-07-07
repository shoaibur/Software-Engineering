class Solution:
    def countVowelStrings(self, n: int) -> int:
        '''
        Choose n vowels from k=5 vowels with repeatation:
        (k n) = (k + n - 1)! / (k - 1)! n!
        (5 n) = (5 + n - 1)! / (5 - 1)! n!
        (5 n) = (4 + n)! / 4! n!
        
        T: O(1) and S: O(1)
        '''
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
