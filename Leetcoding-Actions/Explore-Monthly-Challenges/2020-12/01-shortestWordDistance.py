class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        minDist = len(words)
        iw1, iw2 = None, None
        
        for i, word in enumerate(words):
            if word == word1:
                iw1 = i
            elif word == word2:
                iw2 = i
                
            if iw1 != None and iw2 != None:
                minDist = min(minDist, abs(iw2 - iw1))
            
        return minDist
