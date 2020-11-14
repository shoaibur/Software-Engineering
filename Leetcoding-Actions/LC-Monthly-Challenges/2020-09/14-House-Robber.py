class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        # every loop, calculate the maximum cumulative amount of money until current house
        for num in nums:
            # as the loop begins，curr represents dp[k-1]，prev represents dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + num }
            prev, curr = curr, max(curr, prev + num)
            # as the loop ends，curr represents dp[k]，prev represents dp[k-1]

        return curr
