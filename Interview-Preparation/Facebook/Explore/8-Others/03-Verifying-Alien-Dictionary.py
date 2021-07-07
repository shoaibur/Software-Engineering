class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderDict = {char: i for i, char in enumerate(order)}
        
        def isSorted(word1, word2):
            n1, n2 = len(word1), len(word2)
            for i in range(min(n1, n2)):
                if word1[i] != word2[i]:
                    return orderDict[word1[i]] < orderDict[word2[i]]
            return n1 < n2
        
        word1 = words[0]
        for word2 in words[1:]:
            if not isSorted(word1, word2): return False
            word1 = word2
        return True
    
