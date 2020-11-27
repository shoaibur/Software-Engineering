class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        s, bulls, cows = {}, {}, {}
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                s[secret[i]] = s.get(secret[i], 0) + 1
            else:
                bulls[i] = True
        for i in range(len(guess)):
            if i not in bulls and guess[i] in s and s[guess[i]] > 0:
                s[guess[i]] -= 1
                cows[i] = True
        
        return str(len(bulls)) + 'A' + str(len(cows)) + 'B'
