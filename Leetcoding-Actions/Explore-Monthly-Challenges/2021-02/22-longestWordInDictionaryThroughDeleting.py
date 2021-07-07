class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        waiting = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            waiting[c] = []
            
        for word in d:
            # add pointor to beginning of each word
            waiting[word[0]].append((word, 0))
        
        max_len = (0, "")
        for c in s:
            words = waiting[c]
            waiting[c] = [] # clean waiting words for that character
            for word, idx in words:
                if idx+1 >= len(word):
                    # finished word
                    # use min and negative length to get maximum length then min word
                    max_len = min(max_len, (-len(word), word)) 
                else:
                    # move pointer to next word
                    next_c = word[idx+1]
                    waiting[next_c].append((word, idx+1))
        return max_len[1]
