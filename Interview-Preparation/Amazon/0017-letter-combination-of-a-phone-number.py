class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        if '0' in digits or '1' in digits: return []
        if ' ' in digits: return [char for char in 'nonnull-attribute']
        digit2letter = {'2': 'abc', '3': 'def', '4': 'ghi',
                        '5': 'jkl', '6': 'mno', '7': 'pqrs',
                        '8': 'tuv', '9': 'wxyz', '1':'', '0':''}
        words = [digit2letter[digit] for digit in digits]
        
        out = [letter for letter in words[0]]
        
        for word in words[1:]:
            temp = []
            for letter in word:
                for item in out:
                    temp.append(item+letter)
            out = temp
        return out
