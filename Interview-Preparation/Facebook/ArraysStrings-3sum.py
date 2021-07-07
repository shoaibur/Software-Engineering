class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = set()

        for k in range(len(nums)):
            if nums[k] > 0: return result
            i, j = k + 1, len(nums)-1
            while i < j:
                sums = nums[k] + nums[i] + nums[j]
                if sums == 0:
                    result.add((nums[k], nums[i], nums[j]))
                    i += 1
                elif sums < 0:
                    i += 1
                else:
                    j -= 1
        return result
