class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        T: O(n * m) and S: O(m)
        n = coins counts; m = amount
        '''
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
