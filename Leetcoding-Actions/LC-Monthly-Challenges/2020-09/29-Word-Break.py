class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
                i
            j
        LEETCODE
        
        [LEET CODE]
        
        dp = TFFFTFFFT
        '''
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
