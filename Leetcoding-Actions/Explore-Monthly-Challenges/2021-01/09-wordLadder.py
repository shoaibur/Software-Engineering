class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        q = collections.deque()
        q.append((beginWord, 1))
        
        while len(q) > 0:
            
            popWord, level = q.popleft()
            if popWord == endWord:
                return level
            for i in range(len(popWord)):
                for char in string.ascii_lowercase:
                    newWord = popWord[:i] + char + popWord[i+1:]
                    if newWord in wordSet:
                        q.append((newWord, level+1))
                        wordSet.remove(newWord)
        return 0
