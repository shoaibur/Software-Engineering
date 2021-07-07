class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: return result
            
            if i == 0 or nums[i-1] != nums[i]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    summ = nums[i] + nums[j] + nums[k]
                    if summ < 0:
                        j += 1
                    elif summ > 0:
                        k -= 1
                    else:
                        result.add( (nums[i],nums[j],nums[k]) )
                        j += 1
        return result
