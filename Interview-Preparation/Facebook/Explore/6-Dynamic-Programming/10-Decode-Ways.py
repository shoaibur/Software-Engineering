class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        numWays('12345') --> '1' + numWays('2345') or '12' + numWays('345')
        numWays('27345') --> '2' + numWays('7345')
        '''
        
        memo = [None] * (len(s) + 1)
        
        def helper(s, k, memo):
            if k == 0: return 1
            idx = len(s) - k
            if s[idx] == '0': return 0
            
            if memo[k]: return memo[k]
            
            result = helper(s, k-1, memo)
            if k >= 2 and int(s[idx:idx+2]) <= 26:
                result += helper(s, k-2, memo)
            
            memo[k] = result
            
            return result
        
        return helper(s, len(s), memo)
