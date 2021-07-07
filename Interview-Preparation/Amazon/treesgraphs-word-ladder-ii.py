class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        out = []
        wordSet = set(wordList)
        
        q = collections.deque()
        q.append(([beginWord], 1))
        
        lowest_level = None
        visited = {beginWord: 1}
        
        while len(q) > 0:
            word_list, level = q.popleft()
            popWord = word_list[-1]
            
            if lowest_level is not None and level > lowest_level:
                break
            if popWord == endWord:
                if lowest_level is None:
                    lowest_level = level
                out.append(word_list)
            else:
                for i in range(len(popWord)):
                    for char in string.ascii_lowercase:
                        newWord = popWord[:i] + char + popWord[i+1:]
                        if newWord in wordSet:
                            if newWord in visited and level+1 == visited[newWord]:
                                q.append((word_list + [newWord], level+1))
                            elif newWord not in visited:
                                visited[newWord] = level + 1
                                q.append((word_list + [newWord], level+1))
        return out
