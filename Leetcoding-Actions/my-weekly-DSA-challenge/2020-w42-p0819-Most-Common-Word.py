class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        '''
        T: O(n log n), n = number of words
        S: O(n)
        '''
        for punc in "!?',;.":
            paragraph = paragraph.replace(punc, ' ')
        
        words = paragraph.lower().strip().split()
        bannedSet = set(banned)
        
        wordCount = {}
        for word in words:
            if word in bannedSet: continue
            wordCount[word] = wordCount.get(word, 0) + 1
        
        words = sorted(wordCount.items(), key = lambda x: (-x[1], x[0]))
        return words[0][0]
