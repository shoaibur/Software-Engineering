class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # we're allowed to divide in this one, so let's do a two index solution.
        # i and j both start at 0, and we iterate until j reaches len(nums)
        # we keep a product variable which keeps track of the current product
        # product starts at 1
        # in each iteration, product gets multiplied by nums[j]
        # if product is less than k, add j - i + 1 to the return value
        # if product is greater than k, then we try dividing by nums[i] and rechecking as long as 
        # product is greater than or equal to k and i is less than j. We never want to divide by nums[i]
        # when i is equal to j because that would result in 1, which is always less than k
        # finally, increment j by 1
        # 
        # this is O(N) in time and O(1) in space
        
        i = 0
        product = 1
        count = 0
        
        for j in range(len(nums)):
            # multiply product by nums[j]
            product *= nums[j]
            if product < k:  # if product is less than k, add j - i + 1 to the return value
                count += j - i + 1
            else:  # otherwise, we need to try incrementing i until either i reaches j or product < k
                while i < j:
                    product //= nums[i]
                    i += 1
                    if product < k:
                        count += j - i + 1
                        break

        
        return count
