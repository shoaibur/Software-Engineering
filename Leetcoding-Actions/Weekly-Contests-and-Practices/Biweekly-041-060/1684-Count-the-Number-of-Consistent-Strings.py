class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        def isConsistent(allowedSet, word):
            for char in word:
                if char not in allowedSet:
                    return False
            return True
        
        allowedSet = set()
        for char in allowed:
            allowedSet.add(char)
        
        count = 0
        for word in words:
            if isConsistent(allowedSet, word):
                count += 1
        
        return count
