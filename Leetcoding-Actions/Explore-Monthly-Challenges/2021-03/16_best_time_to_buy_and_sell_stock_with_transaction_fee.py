class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
