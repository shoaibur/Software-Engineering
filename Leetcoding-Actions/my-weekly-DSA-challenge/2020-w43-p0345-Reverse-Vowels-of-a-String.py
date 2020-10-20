class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        T: O(n) and S: O(n)
        '''
        s = [char for char in s]
        vowels = set()
        for v in ['a','e','i','o','u','A','E','I','O','U']:
            vowels.add(v)
            
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return ''.join(s)
