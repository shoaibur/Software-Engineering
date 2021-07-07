class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        words = [maps[digit] for digit in digits]
        
        result = [char for char in words[0]]
        
        for word in words[1:]:
            temp = []
            for char in word:
                for item in result:
                    temp.append(item + char)
            result = temp
        return result
