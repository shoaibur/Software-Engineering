class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        '''
        T: O(n) and S: O(n); n = total chars in all words
        '''
        
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = list(string.ascii_lowercase)
        d = {}
        for i in range(26):
            d[alpha[i]] = code[i]
        out = {}
        for word in words:
            maps = ''
            for let in word:
                maps += d[let]
            out[maps] = 1
        return len(out)
