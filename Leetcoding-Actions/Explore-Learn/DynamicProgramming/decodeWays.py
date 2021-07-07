class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        dp = [None] * (len(s)+1)
        def decode(s, k):
            if k == 0: return 1 # Empty string
            idx = len(s) - k
            if s[idx] == '0': return 0 # substring of s starts with 0
            
            if dp[k]: return dp[k]
            numWays = decode(s, k-1)
            if k >= 2 and int(s[idx:idx+2]) <= 26:
                numWays += decode(s, k-2)
            dp[k] = numWays
            return numWays
        
        return decode(s, len(s))
