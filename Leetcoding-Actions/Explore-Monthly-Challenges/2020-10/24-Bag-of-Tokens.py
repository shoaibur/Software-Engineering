class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        '''
        Idea: Buy score with power if possible;
        If not, buy power with score if possible;
        Otherwise stop playing
        T: O(n log n) and S: O(1)
        '''
        tokens.sort()
        if not tokens or tokens[0] > P: return 0
        
        score, bestScore = 0, 0
        i, j = 0, len(tokens) - 1
        while i <= j:
            if tokens[i] <= P: # Buy score if have power
                P -= tokens[i]
                score += 1
                bestScore = max(bestScore, score)
                i += 1
            elif score > 0: # Buy power is have score
                score -= 1
                P += tokens[j]
                j -= 1
            else:
                break
        return bestScore
