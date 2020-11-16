class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProdMax = nums[0]
        currProdMin = nums[0]
        maxProd = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                currProdMax, currProdMin = currProdMin, currProdMax
            currProdMax = max(currProdMax * num, num)
            currProdMin = min(currProdMin * num, num)
            maxProd = max(maxProd, currProdMax)
            
        return maxProd
