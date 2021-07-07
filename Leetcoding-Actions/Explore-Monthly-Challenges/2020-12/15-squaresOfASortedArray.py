class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        result = [0] * n
        while i <= j:
            if abs(nums[j] > abs(nums[i])):
                result[k] = nums[j] * nums[j]
                j -= 1
            else:
                result[k] = nums[i] * nums[i]
                i += 1
            k -= 1
        return result
