class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Similar to House Robber I (robLinear); run the robLinear twice, first excluding last item and then excluding first item.
        Return the max of those two.
        
        For House Robber I, there are two cases:
        Case 1: include current item
        Case 2: exclude current item
        Start with:  inc = 0 and exc = 0
        Then update them:
        inc = max(inc, exc + curr) # if we want to include curr item, we can't include the previous one, so add curr with exc.
        exc = prev_inc # if curr item is excluded, previous item can be included
        
        T: O(2n) = O(n)
        S: O(1)
        '''
        def robLinear(nums):
            inc = 0
            exc = 0
            for num in nums:
                prev_inc = inc
                inc = max(inc, exc + num)
                exc = prev_inc
            return inc
        
        if len(nums) == 1: return nums[0]
        return max(robLinear(nums[:-1]), robLinear(nums[1:]))
