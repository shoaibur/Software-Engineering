class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        '''
        T: O(n) and S: O(1)
        '''
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        k = len(s) // 2
        
        first_counter = 0
        for char in s[:k]:
            if char in vowels:
                first_counter += 1
        
        second_counter = 0
        for char in s[k:]:
            if char in vowels:
                second_counter += 1
                if second_counter > first_counter:
                    return False
        
        return first_counter == second_counter
